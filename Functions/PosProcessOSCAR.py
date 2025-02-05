import pandas as pd
import re
from abc import ABC
from pandas import DataFrame as Df
import random as rm


class PosProcessOSCAR(ABC):
    def __init__(self):
        self.time = None
        self.polluting = None
        self.polluted = None
        self.impacted = None
        self.total_value = None
        self.correct_file = True

    def set_dataframe(self):
        return

    def extract_data(self, data):
        time_days = []
        polluting = []
        polluted = []
        impacted = []

        with open(data.pathfile, "r") as file:
            lines = file.readlines()
            extracting = False
            total_value = None

            if any(data.total_value_name in l for l in lines):
                pass
            else:
                self.correct_file = False
                return

            # FAZER MELHORIAS PARA LEITURA DINÂMICA ------------------------
            # lines_read = 0
            # while True:
            #     line = file.readline()
            #     if line.startswith(f"{data.total_value_name}:"):

            for line in lines:
                line = line.strip()

                if line.startswith(f"{data.total_value_name}:"):
                    match = re.search(f"{data.total_value_name}:\\s+([\\d\\.e\\+]+) {data.unit}", line)
                    if match:
                        total_value = float(match.group(1))

                if line.startswith("Time"):
                    extracting = True
                    continue

                if extracting:
                    values = line.split()
                    if len(values) == 4:
                        try:
                            time_days.append(float(values[0]))
                            polluting.append(float(values[1]))
                            polluted.append(float(values[2]))
                            impacted.append(float(values[3]))
                        except ValueError:
                            pass

            self.time = time_days
            self.polluting = polluting
            self.polluted = polluted
            self.impacted = impacted
            self.total_value = total_value

        self.set_dataframe()


class OilThick(PosProcessOSCAR):
    def __init__(self, path):
        super().__init__()
        self.pathfile = path
        self.total_value_name = 'OilThck'
        self.unit = 'km2'
        self.dataframe = None
        self.extract_data(self)

    def set_dataframe(self):
        if self.correct_file:
            df = pd.DataFrame({
                "Time days": self.time,
                "Polluting Mass [ton]": self.polluting,
                "Polluted Area [km²]": self.polluted,
                "Impacted Area [km²]": self.impacted
            })

            self.dataframe = df
        else:
            self.dataframe = False


class TotalConc(PosProcessOSCAR):
    def __init__(self, path):
        super().__init__()
        self.pathfile = path
        self.total_value_name = 'Tot.Conc'
        self.unit = 'km3'
        self.dataframe = None
        self.extract_data(self)

    @staticmethod
    def set_color(list_color: list):
        while True:
            a = rm.randint(0, 9)
            if f'C{a}' not in list_color:
                break
        return f'C{a}'

    def set_dataframe(self):
        if self.correct_file:
            df = pd.DataFrame({
                "Time days": self.time,
                "Polluting Mass [ton]": self.polluting,
                "Polluted Vol [km³]": self.polluted,
                "Impacted Vol [km³]": self.impacted
            })

            self.dataframe = df
        else:
            self.dataframe = None


class MassBalance:
    def __init__(self, path):
        self.pathfile = path
        self.extract_data()

    @staticmethod
    def set_color(list_color: list):
        while True:
            a = rm.randint(0, 9)
            if f'C{a}' not in list_color:
                break
        return f'C{a}'

    def extract_data(self):
        file = pd.read_csv(self.pathfile, sep=',')


class ChemicComposi:
    def __init__(self, path):
        self.pathfile = path
        self.extract_data()

    def extract_data(self):
        with open(self.pathfile, 'r', encoding='utf-8', errors='ignore') as f:
            _ = f.readline().split()
            n_composition = int(f.readline().split()[0])

            name_composition = []
            composition = {}
            for l in range(n_composition):
                c_ = f.readline().split(',')
                composition[c_[0].replace('\x00', '').strip()] = float(c_[1].strip())
                name_composition.append(c_[0].split('(')[0].replace('\x00', '').strip())

            name_composition.insert(0, 'Total')

            dict_time_tables = {}
            lines = f.readlines()

            step = 0
            table = False
            while True:
                if step == len(lines):
                    dict_time_tables[time] = Df(dict_table)
                    dict_time_tables[time].index = name_composition
                    break

                line = lines[step]

                if 'metric tons' in line:
                    if table:
                        dict_time_tables[time] = Df(dict_table)
                        dict_time_tables[time].index = name_composition

                    dict_table = {}
                    table = True
                    time = float(line.split(',')[0].replace('\x00', '').strip())
                    dict_time_tables[time] = None
                    step += 1
                else:
                    data = [value.replace('\x00', '').strip() for value in line.split(',')]
                    data.remove(data[0])
                    data = [float(value) for value in data]
                    dict_table[line.split(',')[0].replace('\x00', '').strip()] = data
                    step += 1


# file_path = r"C:\Users\UDESC\Documents\PosProcessamento - OSCAR\BMS40_mGS_TCC.impact.summary.oilthck.log"
# OilThick(file_path)
file_path = r"C:\Users\UDESC\Documents\PosProcessamento - OSCAR\BMS40_mGS_TCC.impact.summary.totconc.log"
TotalConc(file_path)
# file_path = r"C:\Users\UDESC\Documents\PosProcessamento - OSCAR\BMS40_mGS_TCC.masbal.log"
# MassBalance(file_path)
# file_path = r"C:\Users\UDESC\Documents\PosProcessamento - OSCAR\BMS40_mGS_TCC_chemcomp.txt"
# ChemicComposi(file_path)
