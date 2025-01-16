import xarray as xr
from abc import ABC
from datetime import datetime
from pandas import DataFrame as Df
import os
import re
import numpy as np


class FilesExtension(ABC):
    def __init__(self):
        pass

    def set_kargs(self):
        return

    def run(self):
        return


class Concat(FilesExtension):
    def __init__(self, filelist, path, filename):
        self.filelist = filelist
        self.path = path
        self.filename = filename if '.nc' in filename else filename + '.nc'
        self.dim_to_concat = None
        super().__init__()

    def set_kargs(self, **kargs):
        self.dim_to_concat = kargs['dim']

    def run(self):
        datasets = []
        for file in self.filelist:
            datasets.append(xr.open_dataset(f'{self.path}\\{file}'))
        final_ds = xr.concat(datasets, dim=self.dim_to_concat)
        final_ds.to_netcdf(f'{self.path}\\{self.filename}', format='NETCDF4')
        del datasets


class Merge(FilesExtension):
    def __init__(self, filelist, path, filename):
        self.filelist = filelist
        self.path = path
        self.filename = filename if '.nc' in filename else filename + '.nc'
        self.dim_to_concat = None
        super().__init__()

    def run(self):
        datasets = []
        for file in self.filelist:
            datasets.append(xr.open_dataset(f'{self.path}\\{file}'))
        final_ds = xr.merge(datasets)
        final_ds.to_netcdf(f'{self.path}\\{self.filename}', format='NETCDF4')
        del datasets


class Filter(FilesExtension):
    def __init__(self, filelist, path, filename):
        self.filelist = filelist
        self.path = path
        self.filename = filename if '.nc' in filename else filename + '.nc'
        self.var_to_filter = None
        self.dim_to_filter = None
        self.start = None
        self.finish = None
        super().__init__()

    def set_kargs(self, **kargs):
        self.var_to_filter = kargs['var']
        self.dim_to_filter = kargs['dim']
        self.start = kargs['start']
        self.finish = kargs['stop']

    @staticmethod
    def adjust_format(data_string):
        return re.sub(r'-\d{2}h$', lambda x: 'T' + x.group(0)[1:-1] + ':00', data_string)

    def str2time(self, value_str):
        time = self.adjust_format(value_str)
        datetime64_value = np.datetime64(time)
        return datetime64_value

    def run(self):
        dataset = xr.open_dataset(f'{self.path}\\{self.filelist[0]}')

        if self.dim_to_filter == 'time' or self.dim_to_filter == 'valid_time':
            start, finish = self.str2time(self.start), self.str2time(self.finish)
        elif self.dim_to_filter == ' - ':
            start, finish = self.start, self.finish
        else:
            start, finish = float(self.start), float(self.finish)

        if start == finish:
            dict_key = {
                f'{self.dim_to_filter}': start
            }
        else:
            dict_key = {
                f'{self.dim_to_filter}': slice(start, finish)
            }

        if self.var_to_filter == 'All variables':
            list_var = [f'{var}' for var in list(dataset.variables) if dataset[var].ndim > 1]
            dataset_filtered = dataset[list_var].sortby(self.dim_to_filter).sel(dict_key)
        else:
            if self.dim_to_filter == ' - ':
                dataset_filtered = dataset[self.var_to_filter]
            else:
                dataset_filtered = dataset[self.var_to_filter].sel(dict_key)

        dataset_filtered.to_netcdf(f'{self.path}\\{self.filename}', format='NETCDF4')
        del dataset, dataset_filtered


class Dat(FilesExtension):
    def __init__(self, filelist, path, filename):
        self.filelist = filelist
        self.path = path
        self.filename = filename if '.dat' in filename else filename + '.dat'
        self.u_component = None
        self.v_component = None
        super().__init__()

    def set_kargs(self, **kargs):
        self.u_component = kargs['u_component']
        self.v_component = kargs['v_component']

    def run(self):
        os.makedirs(f'{self.path}\\DatFiles', exist_ok=True)
        if self.u_component != self.v_component:
            dataset = xr.open_dataset(f'{self.path}\\{self.filelist[0]}')

            lon, lat = dataset['longitude'].values, dataset['latitude'].values
            times_ = dataset['valid_time'].values

            # Variávies a serem escritas nos arquivos ----------------------------------------------------------------------
            x, y = len(lon), len(lat)
            missing_values = dataset[self.u_component].attrs['GRIB_missingValue']
            reflon = min(lon)
            reflat = min(lat)
            dlon = (dataset['longitude'].values.max() - dataset['longitude'].values.min()) / dataset[
                'longitude'].values.size
            dlat = (dataset['latitude'].values.max() - dataset['latitude'].values.min()) / dataset[
                'latitude'].values.size

            # Criação de arquivo .dat com base nos dados do arquivo netcdf -------------------------------------------------
            with open(f'{self.path}\\DatFiles\\{self.filename}', 'w') as w_file:
                w_file.write(
                    f"""xy  {x}  {y}
            projection  lonlat
            missing {missing_values}
            proj-reflon {reflon}
            proj-reflat {reflat}
            proj-dlon {dlon}
            proj-dlat {dlat}
            # time series starts here
            """)
                for t in times_:
                    t_ = str(t).split('.')[0]
                    t_formated = datetime.strptime(t_, '%Y-%m-%dT%H:%M:%S').strftime('%Y %m %d %H %M')

                    wind_u = Df(dataset[self.u_component].sel(valid_time=t).values).to_string(index=False, header=False)
                    wind_v = Df(dataset[self.v_component].sel(valid_time=t).values).to_string(index=False, header=False)

                    w_file.write(f'time {t_formated}\n')
                    w_file.write('wind_u\n')
                    w_file.write(f'{wind_u}\n')
                    w_file.write('wind_v\n')
                    w_file.write(f'{wind_v}\n')

            del dataset
        else:
            raise Exception('u and v components must be different')


class Imp(FilesExtension):
    def __init__(self, filelist, path, filename):
        self.filelist = filelist
        self.path = path
        self.filename = filename if '.imp' in filename else filename + '.imp'
        self.type = None
        self.u_component = None
        self.v_component = None
        super().__init__()

    def set_kargs(self, **kargs):
        self.type = kargs['type']
        self.u_component = kargs['u_component']
        self.v_component = kargs['v_component']

    def run(self):
        os.makedirs(f'{self.path}\\ImpFiles', exist_ok=True)
        dataset = xr.open_dataset(f'{self.path}\\{self.filelist[0]}')

        if self.type == 'Wind':
            with open(f'{self.path}\\ImpFiles\\{self.filename}', 'w') as w_imp:
                w_imp.write(
                    f"FORMAT	ASCII_3D\n"
                    f"FILE  ***path_to_file***.dat\n"
                    f"INCLUDE-WIND	1\n"
                    f"INCLUDE-CURRENT	0\n"
                    f""
                )
            del dataset
        else:
            if self.u_component != self.v_component:
                with open(f'{self.path}\\ImpFiles\\{self.filename}', 'w') as w_imp:
                    w_imp.write(
                        f"FORMAT	NetCDF\n"
                        f"PROJECTION	LONLAT\n"
                        f"FILE	***path_to_file***.nc\n"
                        f"FILE_OUTPUT	***path_to_file***.hyd\n"
                        f"NAME-TIME	time\n"
                        f"DIMNAME-TIME	time\n"
                        f"TYPE-VECTOR	uv\n"
                        f"TYPE-DATA	current\n"
                        f"LIMIT-DEPTH	>{dataset.depth.values.max()}\n"
                        f"NAME-UVECTOR	water_u\n"
                        f"NAME-VVECTOR	water_v\n"
                        f"NAME_LON	lon\n"
                        f"DIMNAME-X	lon\n"
                        f"NAME-LAT	lat\n"
                        f"DIMNAME-Y	lat\n"
                        f"Compression	1"
                    )
                del dataset
            else:
                raise Exception('u and v components must be different')


class Delete(FilesExtension):
    def __init__(self, filelist, path, filename):
        self.filelist = filelist
        self.path = path
        self.filename = filename
        super().__init__()

    def run(self):
        for file in self.filelist:
            os.remove(f'{self.path}\\{file}')
