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
                    f'to plot the data: {', '.join(missing_values[:-1])} e {missing_values[-1]}.'
                )

        return self.message


class CurrentVar(CheckVariables):
    def __init__(self):
        super().__init__()
        self.var_names = {
            'eastward_sea_water_velocity': 'U component of current',
            'northward_sea_water_velocity': 'V component of current',
            'latitude': 'latitude coordinate',
            'longitude': 'longitude coordinate',
            'depth': 'depth variable',
            'Valid Time': 'time variable'
        }

    def check(self, path):
        dataset = xr.open_dataset(path)
        response = self.check_variables(self.var_names, dataset)
        del dataset
        return response


class WindVar(CheckVariables):
    def __init__(self):
        super().__init__()
        self.var_names = {
            '10 metre U wind component': 'U component of wind',
            '10 metre V wind component': 'V component of wind',
            'latitude': 'latitude coordinate',
            'longitude': 'longitude coordinate',
            'Valid Time': 'time variable',
            'time': 'time variable'
        }

    def check(self, path):
        dataset = xr.open_dataset(path)
        response = self.check_variables(self.var_names, dataset)
        del dataset
        return response


class TemperatureVar(CheckVariables):
    def __init__(self):
        super().__init__()
        self.var_names = {
            'sea_water_temperature': 'Temperature',
            'latitude': 'latitude coordinate',
            'longitude': 'longitude coordinate',
            'depth': 'depth variable',
            'Valid Time': 'time variable'
        }

    def check(self, path):
        dataset = xr.open_dataset(path)
        response = self.check_variables(self.var_names, dataset)
        del dataset
        return response


class SalinityVar(CheckVariables):
    def __init__(self):
        super().__init__()
        self.var_names = {
            'sea_water_salinity': 'Salinity',
            'latitude': 'latitude coordinate',
            'longitude': 'longitude coordinate',
            'depth': 'depth variable',
            'Valid Time': 'time variable'
        }

    def check(self, path):
        dataset = xr.open_dataset(path)
        response = self.check_variables(self.var_names, dataset)
        del dataset
        return response
