import os
import shutil
import xarray as xr
import cdsapi
from datetime import datetime, timedelta
from multiprocessing import Process, Manager
from collections import defaultdict


class CopernicusDownloader:
    def __init__(self, initial_date: datetime.date, final_date: datetime.date, variables: list,
                 coordenates: dict, catalog: object, file_name: str, project_path: str):
        self.start = initial_date
        self.finish = final_date
        self.var_ = variables
        self.coords = coordenates
        self.catalog_ = catalog
        self.file = file_name
        self.projectpath = project_path
        self.processing_ = True
        self.client = None
        self.func = None
        self.dict_to_request, self.coordinates = self.set_list_to_package()

    def set_list_to_package(self):
        dias_por_mes = defaultdict(list)
        data_atual = self.start

        while data_atual <= self.finish:
            chave = f"{data_atual.year}-{data_atual.month:02}"
            dias_por_mes[chave].append(data_atual.day)
            data_atual += timedelta(days=1)

        dias_por_mes = dict(dias_por_mes)

        requests_list = []
        for chave, dias in dias_por_mes.items():
            year, month = chave.split('-')
            request = {
                'product_type': [f'{self.catalog_.type}'],
                'year': [int(year)],
                'month': [int(month)],
                'day': dias,
                'time': ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00',
                         '06:00', '07:00', '08:00', '09:00', '10:00', '11:00',
                         '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
                         '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'],
                'data_format': 'netcdf',
                'download_format': 'unarchived',
                'variable': self.var_,
                'area': [self.coords['N'], self.coords['W'], self.coords['S'], self.coords['E']]
            }
            requests_list.append(request)

        return requests_list, [self.coords['N'], self.coords['W'], self.coords['S'], self.coords['E']]

    @staticmethod
    def get_dim_name(dset):
        var_name = None
        variable_mame_map = ['valid_time', 'Valid_time', 'time', 'Time']

        for var in dset.variables:
            if dset.variables[var].ndim > 1:
                attrs = dset[var].attrs
                standard_name = attrs.get('standard_name', None)
                long_name = attrs.get('long_name', None)

                if standard_name in variable_mame_map:
                    var_name = var
                    break
                elif long_name in variable_mame_map:
                    var_name = var
                    break
            else:
                pass

        del dset
        return var_name

    def stop(self):
        if hasattr(self, 'func') and self.func.is_alive():
            self.func.terminate()
            self.func.join()
        if os.path.isdir(f'{self.projectpath}\\Temp\\Copernicus'):
            shutil.rmtree(f'{self.projectpath}\\Temp\\Copernicus')
        self.processing_ = False

    def process(self, dataset, request, shared_dict):
        try:
            temp_path = f'{self.projectpath}\\Temp\\Copernicus'
            os.makedirs(temp_path, exist_ok=True)

            self.client = cdsapi.Client()

            if len(request) == 1:
                self.client.retrieve(dataset, request[0]).download(f'{self.projectpath}\\{self.file}')
            else:
                dict_files = []
                for idx in range(len(request)):
                    self.client.retrieve(dataset, request[idx]).download(f'{temp_path}\\_{idx}_.nc')
                    dict_files.append(xr.open_dataset(f'{temp_path}\\_{idx}_.nc'))

                dim_name = self.get_dim_name(dict_files[0])
                f_file = xr.concat(dict_files, dim=f'{dim_name}')
                f_file.to_netcdf(f'{self.projectpath}\\{self.file}', format='NETCDF4')
                del f_file
                del dict_files
                if os.path.isdir(f'{self.projectpath}\\Temp\\Copernicus'):
                    shutil.rmtree(f'{self.projectpath}\\Temp\\Copernicus')

            shared_dict['processing'] = True
        except Exception as e:
            shared_dict['processing'] = str(e)

    def download(self):
        dataset = f"{self.catalog_.nome}"
        if self.processing_:
            with Manager() as manager:
                shared_dict = manager.dict()
                shared_dict['processing'] = self.processing_

                self.func = Process(target=self.process, args=(dataset, self.dict_to_request, shared_dict))
                self.func.start()
                self.func.join()

                self.processing_ = shared_dict.get('processing', "Unknown error")
        return self.processing_

