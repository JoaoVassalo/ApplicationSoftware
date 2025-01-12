# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FilterDatasetFormzicaNz.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)
import xarray as xr
from datetime import datetime
import re
import numpy as np


class Ui_Form(object):
    def setupUi(self, page, Form, filelist):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(240, 200)
        Form.setMinimumSize(QSize(200, 200))
        Form.setMaximumSize(QSize(240, 200))

        self.main_page = page
        self.filelist = filelist

        self.verticalLayout_7 = QVBoxLayout(Form)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(0, 30))
        self.label_6.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_6.addWidget(self.label_6)

        self.comboBox_5 = QComboBox(Form)
        self.comboBox_5.setObjectName(u"comboBox_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy1)
        self.comboBox_5.setMinimumSize(QSize(0, 25))
        self.comboBox_5.setMaximumSize(QSize(16777215, 25))
        self.comboBox_5.setStyleSheet(u"QComboBox{\n"
                                    "	background-color: white;\n"
                                    "	border-radius: 12px;\n"
                                    "	border: 2px solid #F98600;\n"
                                    "	color: black;\n"
                                    "	padding-left: 15px;\n"
                                    "    padding-right: 10px;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox::drop-down {\n"
                                    "    border: none;\n"
                                    "    width: 20px;  /*tamanho da seta*/\n"
                                    "    background-color: #F98600;\n"
                                    "    border-top-right-radius: 10px;\n"
                                    "    border-bottom-right-radius: 10px;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox::down-arrow {\n"
                                    "    width: 10px;\n"
                                    "    height: 10px;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox QAbstractItemView {\n"
                                    "    border: 1px solid #F98600;\n"
                                    "    background-color: white;\n"
                                    "    color: black;\n"
                                    "    selection-background-color: orange;\n"
                                    "    selection-color: black;\n"
                                    "    padding: 5px;\n"
                                    "    border-radius: 5px;\n"
                                    "}")
        self.set_variable_list()
        self.comboBox_5.currentIndexChanged.connect(self.set_list_combobox)

        self.verticalLayout_6.addWidget(self.comboBox_5)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 30))
        self.label.setMaximumSize(QSize(200, 30))

        self.verticalLayout.addWidget(self.label)

        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 25))
        self.comboBox.setMaximumSize(QSize(16777215, 25))
        self.comboBox.setStyleSheet(u"QComboBox{\n"
                                    "	background-color: white;\n"
                                    "	border-radius: 12px;\n"
                                    "	border: 2px solid #F98600;\n"
                                    "	color: black;\n"
                                    "	padding-left: 15px;\n"
                                    "    padding-right: 10px;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox::drop-down {\n"
                                    "    border: none;\n"
                                    "    width: 20px;  /*tamanho da seta*/\n"
                                    "    background-color: #F98600;\n"
                                    "    border-top-right-radius: 10px;\n"
                                    "    border-bottom-right-radius: 10px;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox::down-arrow {\n"
                                    "    width: 10px;\n"
                                    "    height: 10px;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox QAbstractItemView {\n"
                                    "    border: 1px solid #F98600;\n"
                                    "    background-color: white;\n"
                                    "    color: black;\n"
                                    "    selection-background-color: orange;\n"
                                    "    selection-color: black;\n"
                                    "    padding: 5px;\n"
                                    "    border-radius: 5px;\n"
                                    "}")
        self.comboBox.currentIndexChanged.connect(self.set_list_combobox_2)

        self.verticalLayout.addWidget(self.comboBox)


        self.verticalLayout_7.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 30))
        self.label_2.setMaximumSize(QSize(60, 30))

        self.verticalLayout_2.addWidget(self.label_2)

        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy1.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy1)
        self.comboBox_2.setMinimumSize(QSize(0, 25))
        self.comboBox_2.setMaximumSize(QSize(16777215, 25))
        self.comboBox_2.setStyleSheet(u"QComboBox{\n"
                                      "	background-color: white;\n"
                                      "	border-radius: 12px;\n"
                                      "	border: 2px solid #F98600;\n"
                                      "	color: black;\n"
                                      "	padding-left: 15px;\n"
                                      "    padding-right: 10px;\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox::drop-down {\n"
                                      "    border: none;\n"
                                      "    width: 20px;  /*tamanho da seta*/\n"
                                      "    background-color: #F98600;\n"
                                      "    border-top-right-radius: 10px;\n"
                                      "    border-bottom-right-radius: 10px;\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox::down-arrow {\n"
                                      "    width: 10px;\n"
                                      "    height: 10px;\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox QAbstractItemView {\n"
                                      "    border: 1px solid #F98600;\n"
                                      "    background-color: white;\n"
                                      "    color: black;\n"
                                      "    selection-background-color: orange;\n"
                                      "    selection-color: black;\n"
                                      "    padding: 5px;\n"
                                      "    border-radius: 5px;\n"
                                      "}")
        self.comboBox_2.currentIndexChanged.connect(self.set_list_combobox_3)

        self.verticalLayout_2.addWidget(self.comboBox_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(50, 30))
        self.label_3.setMaximumSize(QSize(60, 30))

        self.verticalLayout_3.addWidget(self.label_3)

        self.comboBox_3 = QComboBox(Form)
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy1.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy1)
        self.comboBox_3.setMinimumSize(QSize(0, 25))
        self.comboBox_3.setMaximumSize(QSize(16777215, 25))
        self.comboBox_3.setStyleSheet(u"QComboBox{\n"
                                      "	background-color: white;\n"
                                      "	border-radius: 12px;\n"
                                      "	border: 2px solid #F98600;\n"
                                      "	color: black;\n"
                                      "	padding-left: 15px;\n"
                                      "    padding-right: 10px;\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox::drop-down {\n"
                                      "    border: none;\n"
                                      "    width: 20px;  /*tamanho da seta*/\n"
                                      "    background-color: #F98600;\n"
                                      "    border-top-right-radius: 10px;\n"
                                      "    border-bottom-right-radius: 10px;\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox::down-arrow {\n"
                                      "    width: 10px;\n"
                                      "    height: 10px;\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox QAbstractItemView {\n"
                                      "    border: 1px solid #F98600;\n"
                                      "    background-color: white;\n"
                                      "    color: black;\n"
                                      "    selection-background-color: orange;\n"
                                      "    selection-color: black;\n"
                                      "    padding: 5px;\n"
                                      "    border-radius: 5px;\n"
                                      "}")

        self.verticalLayout_3.addWidget(self.comboBox_3)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(120, 30))
        self.label_4.setMaximumSize(QSize(200, 30))

        self.verticalLayout_4.addWidget(self.label_4)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 25))
        self.lineEdit.setMaximumSize(QSize(16777215, 25))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
                                    "	border-radius: 10px;\n"
                                    "	border: 2px solid #F98600;\n"
                                    "	color: white;\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "")

        self.verticalLayout_4.addWidget(self.lineEdit)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

        self.set_list_combobox()

    @staticmethod
    def adjust_format(data_string):
        return re.sub(r'-\d{2}h$', lambda x: 'T' + x.group(0)[1:-1] + ':00', data_string)

    @staticmethod
    def time2str(value_time):
        time_to_format = str(value_time).split('.')[0]
        t_formated = datetime.strptime(time_to_format, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d-%Hh')
        return t_formated

    def str2time(self, value_str):
        time = self.adjust_format(value_str)
        datetime64_value = np.datetime64(time)
        return datetime64_value

    def clear_combobox(self, box):
        if box == 2:
            self.comboBox_2.clear()
        elif box == 1:
            self.comboBox.clear()
        else:
            self.comboBox_3.clear()

    def set_list_combobox_3(self):
        if self.comboBox_2.count() == 0:
            self.clear_combobox(3)
        else:
            self.clear_combobox(3)
            max_values_var = self.f[self.comboBox.currentText()].values
            if self.comboBox.currentText() == 'time' or self.comboBox.currentText() == 'valid_time':
                self.comboBox_3.addItems([f'{self.time2str(value)}' for value in max_values_var if
                                          value >= self.str2time(self.comboBox_2.currentText())])
            else:
                self.comboBox_3.addItems(
                    [f'{value}' for value in max_values_var if value >= float(self.comboBox_2.currentText())])
            self.comboBox_3.setCurrentIndex(1)

    def set_list_combobox_2(self):
        if self.comboBox.currentText() == ' - ' or self.comboBox.currentText() == '':
            self.clear_combobox(2)
        else:
            self.clear_combobox(2)
            if self.comboBox.currentText() == 'time' or self.comboBox.currentText() == 'valid_time':
                min_values_var = [f'{self.time2str(v)}' for v in self.f[self.comboBox.currentText()].values]
            else:
                min_values_var = [f'{v}' for v in self.f[self.comboBox.currentText()].values]
            self.comboBox_2.addItems(min_values_var)
            self.comboBox_2.setCurrentIndex(0)
        self.set_list_combobox_3()

    def set_list_combobox(self):
        self.clear_combobox(1)

        if self.comboBox_5.currentIndex() != 0:
            self.comboBox.addItem(' - ')

        self.comboBox.addItems([f'{var_item}' for var_item in self.var if self.f[var_item].ndim == 1])
        self.comboBox.setCurrentIndex(0)

        self.set_list_combobox_2()

    def set_variable_list(self):
        self.f = xr.open_dataset(f'{self.main_page.project.caminho}\\{self.filelist[0]}')
        self.var = list(self.f.variables)
        self.comboBox_5.addItem('All variables')
        self.comboBox_5.addItems([f'{var_item}' for var_item in self.var if self.f[var_item].ndim > 1])
        self.comboBox_5.setCurrentIndex(0)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Variable to Filter", None))
        self.label.setText(QCoreApplication.translate("Form", u"Dimension to Filter", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"From", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"To", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Final File Name", None))
