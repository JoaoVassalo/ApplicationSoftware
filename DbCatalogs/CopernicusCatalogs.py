from datetime import date, datetime


class Catalogs:
    def __init__(self, typeproduct: str, initial: datetime.date, final: datetime.date or str, variables: list[str]):
        self.type = typeproduct
        self.i_date = initial
        self.f_date = final
        self.variables = variables


copernicus_catalogs = {
    'reanalysis-era5-single-levels': Catalogs(
        typeproduct='reanalysis',
        initial=date(year=1940, month=1, day=1), final=date(year=2024, month=1, day=11),
        variables=['10m_u_component_of_wind', '10m_v_component_of_wind']
    )
}