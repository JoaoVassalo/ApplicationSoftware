from abc import ABC
import xarray as xr


class CheckVariables(ABC):
    def __init__(self):
        super().__init__()
        self.message = False

    def check_variables(self, var_n, ds):
        var_list = set()

        for var in ds.variables:
            attrs = ds[var].attrs
            standard_name = attrs.get('standard_name', None)
            long_name = attrs.get('long_name', None)

            if standard_name in var_n:
                var_list.add(var_n[standard_name])
            elif long_name in var_n:
                var_list.add(var_n[long_name])

        var_list = list(var_list)

        var_name_values = list(set(var_n.values()))
        missing_values = [value for value in var_name_values if value not in var_list]

        if len(missing_values) > 0:
            if len(missing_values) == 1:
                self.message = (
                    'The selected dataset appears to be missing the following variables that are necessary '
                    f'to plot the data: {missing_values[0]}.'
                )
            elif len(missing_values) == 2:
                self.message = (
                    'The selected dataset appears to be missing the following variables that are necessary '
                    f'to plot the data: {missing_values[0]} and {missing_values[1]}.'
                )
            else:
                self.message = (
                    'The selected dataset appears to be missing the following variables that are necessary '
                    f'to plot the data: {", ".join(missing_values[:-1])} e {missing_values[-1]}.'
                )

        return self.message

    @staticmethod
    def get_variables(varmap, dataset):
        names = {}
        for chave, valores in varmap.items():
            for var in dataset.variables:
                attrs = dataset[var].attrs
                if any(valor in attrs.get('standard_name', '') or valor in attrs.get('long_name', '') for valor in
                       valores):
                    names[chave] = var
                    break
        del dataset
        return names


class CurrentVar(CheckVariables):
    def __init__(self):
        super().__init__()
        self.variables = None
        self.var_names = {
            'eastward_sea_water_velocity': 'U component of current',
            'northward_sea_water_velocity': 'V component of current',
            'latitude': 'latitude coordinate',
            'longitude': 'longitude coordinate',
            'depth': 'depth variable',
            'Valid Time': 'time variable',
            'Valid time': 'time variable',
            'time': 'time variable',
            'Time': 'time variable'
        }
        self.varname_map = {
            'u': ['eastward_sea_water_velocity'],
            'v': ['northward_sea_water_velocity'],
            'depth': ['depth'],
            'time': ['Valid time', 'time', 'Valid Time', 'Valid time'],
            'longitude': ['longitude', 'Longitude'],
            'latitude': ['latitude', 'Latitude']
        }

    def check(self, path):
        dataset = xr.open_dataset(path)
        response = self.check_variables(self.var_names, dataset)
        del dataset
        return response

    def get_var_names(self, path):
        dataset = xr.open_dataset(path)
        self.variables = self.get_variables(self.varname_map, dataset)
        del dataset
        return self.variables


class WindVar(CheckVariables):
    def __init__(self):
        super().__init__()
        self.variables = None
        self.var_names = {
            '10 metre U wind component': 'U component of wind',
            '10-meter_eastward_wind': 'U component of wind',
            '10 metre V wind component': 'V component of wind',
            '10-meter_northward_wind': 'V component of wind',
            'latitude': 'latitude coordinate',
            'longitude': 'longitude coordinate',
            'Valid Time': 'time variable',
            'Valid time': 'time variable',
            'time': 'time variable'
        }
        self.varname_map = {
            'u': ['10 metre U wind component', 'U component of wind', 'eastward_wind',
                  '10-metre_eastward_wind', '10-metre_northward_wind'],
            'v': ['10 metre V wind component', 'V component of wind', 'northward_wind'],
            'time': ['Valid time', 'time', 'Valid Time', 'Valid time'],
            'longitude': ['longitude', 'Longitude'],
            'latitude': ['latitude', 'Latitude']
        }

    def check(self, path):
        dataset = xr.open_dataset(path)
        response = self.check_variables(self.var_names, dataset)
        del dataset
        return response

    def get_var_names(self, path):
        dataset = xr.open_dataset(path)
        self.variables = self.get_variables(self.varname_map, dataset)
        del dataset
        return self.variables


class TemperatureVar(CheckVariables):
    def __init__(self):
        super().__init__()
        self.variables = None
        self.var_names = {
            'sea_water_temperature': 'Temperature',
            'latitude': 'latitude coordinate',
            'longitude': 'longitude coordinate',
            'depth': 'depth variable',
            'Valid Time': 'time variable',
            'Valid time': 'time variable'
        }
        self.varname_map = {
            'temperature': ['sea_water_temperature'],
            'depth': ['depth'],
            'time': ['Valid time', 'time', 'Valid Time', 'Valid time'],
            'longitude': ['longitude', 'Longitude'],
            'latitude': ['latitude', 'Latitude']
        }

    def check(self, path):
        dataset = xr.open_dataset(path)
        response = self.check_variables(self.var_names, dataset)
        del dataset
        return response

    def get_var_names(self, path):
        dataset = xr.open_dataset(path)
        self.variables = self.get_variables(self.varname_map, dataset)
        del dataset
        return self.variables


class SalinityVar(CheckVariables):
    def __init__(self):
        super().__init__()
        self.variables = None
        self.var_names = {
            'sea_water_salinity': 'Salinity',
            'latitude': 'latitude coordinate',
            'longitude': 'longitude coordinate',
            'depth': 'depth variable',
            'Valid Time': 'time variable',
            'Valid time': 'time variable'
        }
        self.varname_map = {
            'salinity': ['sea_water_salinity'],
            'depth': ['depth'],
            'time': ['Valid time', 'time', 'Valid Time', 'Valid time'],
            'longitude': ['longitude', 'Longitude'],
            'latitude': ['latitude', 'Latitude']
        }

    def check(self, path):
        dataset = xr.open_dataset(path)
        response = self.check_variables(self.var_names, dataset)
        del dataset
        return response

    def get_var_names(self, path):
        dataset = xr.open_dataset(path)
        self.variables = self.get_variables(self.varname_map, dataset)
        del dataset
        return self.variables
