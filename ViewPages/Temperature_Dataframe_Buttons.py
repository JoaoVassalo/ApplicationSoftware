from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt, QAbstractTableModel)
from PySide6.QtWidgets import (QLabel, QFrame, QHBoxLayout, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QTableView)
from PySide6.QtGui import QColor
from PySide6 import QtWidgets
from datetime import datetime
from pandas import DataFrame as Df
import numpy as np
import os


class DataFrameModel(QAbstractTableModel):
    def __init__(self, dataframe):
        super().__init__()
        self._dataframe = dataframe

    def rowCount(self, index=None):
        return self._dataframe.shape[0]

    def columnCount(self, index=None):
        return self._dataframe.shape[1]

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._dataframe.iloc[index.row(), index.column()]
            return str(value)
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._dataframe.columns[section])
            elif orientation == Qt.Orientation.Vertical:
                return str(self._dataframe.index[section])
        return None


class Ui_WindButton_LonLatProfile(object):
    def setupUi(self, page, WindButton_LonLatProfile, dataset, variables):
        if not WindButton_LonLatProfile.objectName():
            WindButton_LonLatProfile.setObjectName(u"WindButton_LonLatProfile")
        WindButton_LonLatProfile.resize(546, 436)

        self.mainpage = page
        self.dataset = dataset
        self.temp_name = variables['temperature']
        self.time_name = variables['time']
        self.depth_name = variables['depth']
        self.lon_name, self.lat_name = variables['longitude'], variables['latitude']

        self.verticalLayout_2 = QVBoxLayout(WindButton_LonLatProfile)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(WindButton_LonLatProfile)
        self.frame.setObjectName(u"frame")
        self.frame.setProperty('ViewCommomFrame', True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(WindButton_LonLatProfile)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setProperty('ViewCommomFrame', True)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 60))
        self.frame_2.setMaximumSize(QSize(16777215, 60))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, -1, 0, -1)

        self.horizontalSpacer_39 = QSpacerItem(2, 17, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_15.addItem(self.horizontalSpacer_39)

        self.tablename = QLabel(self.frame_2)
        self.tablename.setObjectName(u"TableName")
        self.tablename.setProperty('TableLabel_ViewPages', True)
        self.tablename.setText("Average temperature table for the entire domain")
        self.tablename.setStyleSheet(
            u"font-size: 16px;\n"
            u"font-style: italic;\n"
            u"font-weight: bold;\n"
            u"color: #4C5B61;\n"
        )
        self.layoutTable = QHBoxLayout()
        self.layoutTable.addWidget(self.tablename)
        self.horizontalLayout_15.addLayout(self.layoutTable)

        self.horizontalSpacer_40 = QSpacerItem(18, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_40)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.SaveDataframe = QPushButton(self.frame_2)
        self.SaveDataframe.setObjectName(u"SaveDataframe")
        self.SaveDataframe.setProperty('CommomButtonViewPageFunc', True)
        self.SaveDataframe.setMinimumSize(QSize(120, 30))
        self.SaveDataframe.setMaximumSize(QSize(120, 30))

        self.SaveDataframe.clicked.connect(self.save_df)

        self.horizontalLayout_6.addWidget(self.SaveDataframe)

        self.horizontalLayout_15.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer_41 = QSpacerItem(2, 17, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_41)

        self.horizontalLayout.addLayout(self.horizontalLayout_15)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.retranslateUi(WindButton_LonLatProfile)

        QMetaObject.connectSlotsByName(WindButton_LonLatProfile)

        shadow_elements = {
            'frame',
            'frame_2'
        }

        try:
            for x in shadow_elements:
                effect = QtWidgets.QGraphicsDropShadowEffect(WindButton_LonLatProfile)
                effect.setBlurRadius(18)
                effect.setXOffset(0)
                effect.setYOffset(0)
                effect.setColor(QColor(0, 0, 0, 255))
                getattr(self, x).setGraphicsEffect(effect)

            self.dataframe = self.average_temp_df()
            self.tablemodel = DataFrameModel(self.dataframe)
            self.tableview = QTableView()
            self.tableview.setModel(self.tablemodel)
            self.layouttable = QVBoxLayout()
            self.layouttable.addWidget(self.tableview)
            self.frame.setLayout(self.layouttable)

            self.tableview.setStyleSheet("""
                            QTableView {
                                background-color: #C3C3C3;
                                gridline-color: #C0C0C0;
                                font-size: 14px;
                                border: 1px solid #C0C0C0;
                            }
                            QHeaderView::section {
                                background-color: #2C423F;
                                color: white;
                                font-weight: bold;
                                padding: 5px;
                                border: 1px solid #C0C0C0;
                                border-radius: 3px;
                            }
                            QTableView::item {
                                padding: 5px;
                            }
                            QTableView::item:selected {
                                background-color: #515751;
                                color: white;
                            }
                            QTableCornerButton::section {
                                background-color: #C3C3C3;
                                border: 1px solid #C0C0C0;
                            }
                        """)
        except KeyError as e:
            raise e

    def save_df(self):
        path_to_save = f'{self.mainpage.project.caminho}\\figs'
        os.makedirs(path_to_save, exist_ok=True)
        self.dataframe.to_excel(f'{path_to_save}\\AverageTemperatureDF_.xlsx')

    def average_temp_df(self):
        df_temp = {
            'Depth [m]': [round(dpt, ndigits=2) for dpt in self.dataset[self.depth_name].values]
        }
        for t in range(len(self.dataset[self.time_name].values)):
            t_ = str(self.dataset[self.time_name].values[t]).split('.')[0]
            t_formated = datetime.strptime(t_, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d-%H')

            df_temp[f'{t_formated}'] = [np.nanmean(self.dataset[self.temp_name][t, dpt, :, :]) for dpt in
                                        range(len(self.dataset[self.temp_name][self.depth_name].values))]

        df_temp = Df(df_temp)
        df_temp['Média'] = df_temp.iloc[:, 1:].mean(axis=1)
        return df_temp

    def retranslateUi(self, WindButton_LonLatProfile):
        WindButton_LonLatProfile.setWindowTitle(QCoreApplication.translate("WindButton_LonLatProfile", u"Form", None))
        self.SaveDataframe.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"Save Dataframe", None))
