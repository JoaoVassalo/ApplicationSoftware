import logging
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import xarray as xr
import lxml


class HycomDownloader:
    def __init__(self, initial_date: datetime.date, final_date: datetime.date, variables: list,
                 coordenates: dict, catalog: str, file_name: str, project_path: str):
        self.start = initial_date
        self.finish = final_date
        self.var_ = variables
        self.coords = coordenates
        self.catalog_ = catalog
        self.file = file_name
        self.projectpath = project_path
        self._stop = False

    def catalog_url(self, year: int) -> str:
        """
        Get the catalog url for a given year

        Args:
            year (int): required calendar year

        Returns:
            str: url
        """
        return f'{self.catalog_}{int(year)}/catalog.xml'

    @staticmethod
    def download_catalog(catalog_url: str) -> str:
        """
        Download the content of the catalog web page.

        Args:
            catalog_url (str): url of the catalog

        Returns:
            str: the catalog as plain text
        """
        return requests.get(catalog_url).text

    @staticmethod
    def parse_catalog(catalog: str):
        """
        Parse the catalog using BeautifulSoup's xml parser.

        Args:
            catalog (str): the catalog content
        """
        return BeautifulSoup(catalog, 'xml')

    @staticmethod
    def extract_urls(parsed_catalogs) -> list:
        """
        Get the list of the url of the ncdf file from the parsed catalog.

        Args:
            parsed_catalogs: the parsed catalog

        Returns:
            list: list of all the urls of the netcdf files
        """
        urls = []
        datasets = parsed_catalogs.find_all('dataset')
        for dataset in datasets:
            url = dataset.get('urlPath')
            if url:
                # if 'ts3z' in url:
                urls.append(url)
        return urls

    def download_data(self, path):
        """

        """
        try:
            dataset = xr.open_dataset(path, decode_cf=False, decode_times=False)
            var = list(dataset.variables)

            # Selecionar variáveis que existem no dataset
            vars_in_dataset = [v for v in self.var_ if v in var]

            if vars_in_dataset:

                print(f'Downloading file {path}')
                data_filtered = dataset[vars_in_dataset].sel(lat=slice(self.coords['S'], self.coords['N']),
                                                       lon=slice(self.coords['W'], self.coords['E']))

                if len(data_filtered.lon.values) > 0:
                    return data_filtered

                else:
                    data_filtered = dataset[vars_in_dataset].sel(lat=slice(self.coords['S'], self.coords['N']),
                                                           lon=slice(360 + self.coords['W'], 360 + self.coords['E']))
                    return data_filtered

            else:
                return

        except Exception as e:
            logging.warning(f"File {path} skipped (error {e}, {e.__doc__}")
            return

    def get_url_list(self, from_date: datetime.date, to_date: datetime.date) -> list:
        """
        Get the list of the netcdf url between the two input dates.

        Args:
            from_date (datetime): lower limit of the desired time range
            to_date (datetime): upper limit of the desired time range

        Returns:
            url_list (list): list of the needed urls
        """
        print('Getting url list from HYCOM catalog')
        from_year = from_date.year
        to_year = to_date.year

        all_urls = []

        for year in range(from_year, to_year + 1):
            catalog_url_for_year = self.catalog_url(year)
            catalog_content = self.download_catalog(catalog_url_for_year)
            parsed_catalog = self.parse_catalog(catalog_content)
            urls_for_year = self.extract_urls(parsed_catalog)
            all_urls.extend(urls_for_year)

        return all_urls

    def stop(self):
        self._stop = True

    def download(self):
        """

        """
        partial_urls = self.get_url_list(self.start, self.finish)

        full_urls = []
        for url in partial_urls:
            full_urls.append('https://tds.hycom.org/thredds/dodsC/' + url)

        daterange = []
        for date in pd.date_range(self.start, self.finish, freq='D'):
            formatted_date = str(10000 * date.year + 100 * date.month + date.day)
            daterange.append(formatted_date)

        to_be_downloaded = []
        for data in daterange:

            urls_for_data = []
            for url in full_urls:

                if data in url:
                    urls_for_data.append(url)

            to_be_downloaded.extend(urls_for_data)

        count = 1
        final_old = None
        final_file = None
        processing_ = True
        for dire in to_be_downloaded:
            if self._stop:
                processing_ = False
                break
            else:
                fi_ = self.download_data(path=dire)
                if fi_:
                    if count == 1:
                        final_file = fi_
                        count += 1
                    else:
                        final_file = xr.merge([final_old, fi_])
                    final_old = final_file

        if processing_:
            final_file.to_netcdf(f'{self.projectpath}\\{self.file}', format='NETCDF4')

        if final_file:
            del final_file

        return processing_
