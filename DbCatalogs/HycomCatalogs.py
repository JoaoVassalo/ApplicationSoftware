from datetime import datetime, date


class Catalogs:
    def __init__(self, url: str, initial: datetime.date, final: datetime.date or str, type_: str, region: str,
                 variables: list[str]):
        self.url = url
        self.i_date = initial
        self.f_date = final
        self.type = type_
        self.region = region
        self.variables = variables


hycom_catalogs = {
    'ESPC-D-V02': Catalogs(
        url=f'https://tds.hycom.org/thredds/catalog/datasets/ESPC-D-V02/data/archive/',
        initial=date(year=2024, month=8, day=10), final=date(year=2024, month=8, day=10),
        type_='Global 1/12° Analysis', region='Global',
        variables=['ice', 'steric ssh', 'surf el', 'salinity',
                   'water_temp', 'water_u', 'water_v']
    ),

    'GLBy0.08 - expt_93.0': Catalogs(
        url=f'https://tds.hycom.org/thredds/catalog/datasets/GLBy0.08/expt_93.0/data/hindcasts/',
        initial=datetime(year=2018, month=12, day=4), final=datetime(year=2024, month=9, day=4),
        type_='HYCOM + NCODA Global 1/12° Analysis (NRL)', region='Global',
        variables=['ssh', 'water_temp', 'salinity', 'water_u',
                   'water_v']
    ),

    'GLBv0.08 - expt_53.X': Catalogs(
        url=f'https://tds.hycom.org/thredds/catalog/datasets/GLBv0.08/expt_53.X/data/',
        initial=datetime(year=1994, month=1, day=1), final=datetime(year=2015, month=12, day=31),
        type_='HYCOM + NCODA Global 1/12° Reanalysis (NRL)', region='Global',
        variables=['ssh', 'water_temp', 'salinity', 'water_u',
                   'water_v']
    ),

    'GOMb0.01 - reanalysis': Catalogs(
        url=f'https://tds.hycom.org/thredds/catalog/datasets/GOMb0.01/reanalysis/data/',
        initial=datetime(year=2001, month=1, day=1), final=datetime(year=2024, month=12, day=31),
        type_='HYCOM-TSIS 1/100º Gulf of Mexico Reanalysis', region='Golf Mexico',
        variables=['water_temp', 'salinity', 'water_u',
                   'water_v', 'water_w', '10u', '10v']
    ),

    'GOMb0.04 - reanalysis': Catalogs(
        url=f'https://tds.hycom.org/thredds/catalog/datasets/GOMb0.04/reanalysis/data/',
        initial=datetime(year=2001, month=1, day=1), final=datetime(year=2024, month=12, day=31),
        type_='HYCOM-TSIS 1/25º Gulf of Mexico Reanalysis', region='Golf Mexico',
        variables=['water_temp', 'salinity', 'water_u',
                   'water_v', 'water_w', '10u', '10v']
    ),

    'GOMu0.04 - expt_90.1m000': Catalogs(
        url=f'https://tds.hycom.org/thredds/catalog/datasets/GOMu0.04/expt_90.1m000/data/hindcasts/',
        initial=datetime(year=2019, month=1, day=1), final=datetime(year=2015, month=1, day=15),
        type_='HYCOM + NCODA Gulf of Mexico 1/25° Analysis (NRL)', region='Golf Mexico',
        variables=['ssh', 'water_temp', 'salinity',
                   'water_u', 'water_v']
    ),

    'GOMu0.04 - expt_50.1': Catalogs(
        url=f'https://tds.hycom.org/thredds/catalog/datasets/GOMu0.04/expt_50.1/data/netcdf/',
        initial=datetime(year=1993, month=1, day=1), final=datetime(year=2012, month=12, day=31),
        type_='HYCOM + NCODA Gulf of Mexico 1/25° Reanalysis (NRL)', region='Golf Mexico',
        variables=['ssh', 'water_temp', 'salinity',
                   'water_u', 'water_v']
    ),

    'GOMl0.04 - expt_32.5': Catalogs(
        url=f'https://tds.hycom.org/thredds/catalog/datasets/GOMl0.04/expt_32.5/data/',
        initial=datetime(year=2014, month=1, day=1), final=datetime(year=2019, month=12, day=31),
        type_='HYCOM + NCODA Southeast United States 1/25 Degree Analysis', region='Southeast EUA',
        variables=['water_temp', 'salinity',
                   'water_u', 'water_v', 'water_w']
    ),

    'GOMl0.04 - expt_31.0': Catalogs(
        url=f'https://tds.hycom.org/thredds/catalog/datasets/GOMl0.04/expt_31.0/data/',
        initial=datetime(year=2009, month=1, day=1), final=datetime(year=2014, month=12, day=31),
        type_='HYCOM + NCODA Southeast United States 1/25 Degree Analysis', region='Southeast EUA',
        variables=['water_temp', 'salinity',
                   'water_u', 'water_v', 'water_w']
    ),

    'GLBu0.08 - expt_19.0': Catalogs(
        url=f'https://tds.hycom.org/thredds/catalog/datasets/GLBu0.08/expt_19.0/data/',
        initial=datetime(year=1992, month=1, day=1), final=datetime(year=1995, month=12, day=31),
        type_='GOFS 3.0: HYCOM + NCODA Global 1/12° Reanalysis', region='Global',
        variables=['ssh', 'water_temp', 'salinity',
                   'water_u', 'water_v']
    ),

    'GLBu0.08 - expt_19.1': Catalogs(
        url=f'https://tds.hycom.org/thredds/catalog/datasets/GLBu0.08/expt_19.1/data/',
        initial=datetime(year=1995, month=1, day=1), final=datetime(year=2012, month=12, day=31),
        type_='GOFS 3.0: HYCOM + NCODA Global 1/12° Reanalysis', region='Global',
        variables=['ssh', 'water_temp', 'salinity',
                   'water_u', 'water_v']
    ),
}
