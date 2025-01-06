# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Salinity_Dataframe_ButtonsWOkNuq.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QAbstractTableModel)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget, QMainWindow, QTableView)
import resources_rc
import sys
import pandas as pd
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

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            value = self._dataframe.iloc[index.row(), index.column()]
            return str(value)
        return None


class Ui_WindButton_LonLatProfile(object):
    def setupUi(self, page, WindButton_LonLatProfile, dataset):
        if not WindButton_LonLatProfile.objectName():
            WindButton_LonLatProfile.setObjectName(u"WindButton_LonLatProfile")
        WindButton_LonLatProfile.resize(546, 436)

        self.mainpage = page
        self.dataset = dataset

        self.verticalLayout_2 = QVBoxLayout(WindButton_LonLatProfile)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(WindButton_LonLatProfile)
        self.frame.setObjectName(u"frame")
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
        self.horizontalSpacer_40 = QSpacerItem(18, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_40)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.SaveDataframe = QPushButton(self.frame_2)
        self.SaveDataframe.setObjectName(u"SaveDataframe")
        self.SaveDataframe.setMinimumSize(QSize(120, 30))
        self.SaveDataframe.setMaximumSize(QSize(120, 30))
        self.SaveDataframe.setStyleSheet(u"QPushButton{\n"
                                         "	background-color: rgb(61, 80, 95);\n"
                                         "	border-radius: 15px;\n"
                                         "	border: 2px solid #F98600;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "	color: #F98600;\n"
                                         "	font-size: 14px;\n"
                                         "}")
        self.SaveDataframe.clicked.connect(self.save_df)

        self.horizontalLayout_6.addWidget(self.SaveDataframe)

        self.horizontalLayout_15.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer_41 = QSpacerItem(2, 17, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_41)

        self.horizontalLayout.addLayout(self.horizontalLayout_15)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.retranslateUi(WindButton_LonLatProfile)

        QMetaObject.connectSlotsByName(WindButton_LonLatProfile)

        try:
            self.dataframe = self.average_sali_df()
            self.tablemodel = DataFrameModel(self.dataframe)
            self.tableview = QTableView()
            self.tableview.setModel(self.tablemodel)
            self.layouttable = QVBoxLayout()
            self.layouttable.addWidget(self.tableview)
            self.frame.setLayout(self.layouttable)
        except KeyError as e:
            raise e

    def save_df(self):
        path_to_save = f'{self.mainpage.project.caminho}\\figs'
        os.makedirs(path_to_save, exist_ok=True)
        self.dataframe.to_excel(f'{path_to_save}\\AverageSalinidadeDF_.xlsx')

    def average_sali_df(self):
        df_sali = {
            'Depth [m]': [round(dpt, ndigits=2) for dpt in self.dataset['depth'].values]
        }
        for t in range(len(self.dataset['time'].values)):
            t_ = str(self.dataset['time'].values[t]).split('.')[0]
            t_formated = datetime.strptime(t_, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d-%H')

            df_sali[f'{t_formated}'] = [np.nanmean(self.dataset.salinity[t, dpt, :, :]) for dpt in
                                        range(len(self.dataset.salinity['depth'].values))]

        df_sali = Df(df_sali)
        df_sali['Média'] = df_sali.iloc[:, 1:].mean(axis=1)
        return df_sali

    def retranslateUi(self, WindButton_LonLatProfile):
        WindButton_LonLatProfile.setWindowTitle(QCoreApplication.translate("WindButton_LonLatProfile", u"Form", None))
        self.SaveDataframe.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"Save Dataframe", None))
