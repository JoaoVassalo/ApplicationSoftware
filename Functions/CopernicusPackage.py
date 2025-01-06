import cdsapi
from datetime import datetime


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
        self.set_list_to_package()

    def set_list_to_package(self):
        self.days = [f'{day}' for day in
                     range(self.start.day,
                           self.finish.day + 1)] if (self.start.month == self.finish.month and self.start.year ==
                                                     self.finish.year) \
            else [f'{day}' for day in range(1, 32)]

        self.months = [month for month in range(self.start.month, self.finish.month + 1)] if (self.start.month !=
                                                                                              self.finish.month) else [self.start.month]

        self.years = [year for year in range(self.start.year, self.finish.year + 1)] if (
                self.start.year != self.finish.year) else [self.start.year]

        self.coordinates = [self.coords['N'], self.coords['W'], self.coords['S'], self.coords['E']]

    def download(self):
        dataset = f"{self.catalog_.nome}"
        request = {
            'product_type': [f'{self.catalog_.type}'],
            'year': self.years,
            'month': self.months,
            'day': self.days,
            'time': ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00',
                     '06:00', '07:00', '08:00', '09:00', '10:00', '11:00',
                     '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
                     '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'],
            'data_format': 'netcdf',
            'download_format': 'unarchived',
            'variable': ['10m_u_component_of_wind', '10m_v_component_of_wind'],
            'area': self.coordinates
        }

        client = cdsapi.Client()
        client.retrieve(dataset, request).download(f'{self.projectpath}\\{self.file}')
