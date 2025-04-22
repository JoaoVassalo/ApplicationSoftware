# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RenameDatasetFormyXZBuv.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtWidgets import (QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QRadioButton, QSizePolicy, QVBoxLayout)
import xarray as xr
import os


class Ui_Form(object):
    def setupUi(self, page, Form, filelist):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(240, 200)
        Form.setMinimumSize(QSize(200, 200))
        Form.setMaximumSize(QSize(240, 200))

        self.main_page = page
        self.filelist = filelist
        self.form_main_page = Form

        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
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
        self.comboBox_5.setProperty('CommomComboBoxFilterPage', True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy1)
        self.comboBox_5.setMinimumSize(QSize(0, 25))
        self.comboBox_5.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_6.addWidget(self.comboBox_5)


        self.verticalLayout_3.addLayout(self.verticalLayout_6)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 30))
        self.label.setMaximumSize(QSize(200, 30))

        self.verticalLayout.addWidget(self.label)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setProperty('commonLineEditDownloadPage', True)
        self.lineEdit_2.setMinimumSize(QSize(0, 25))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout.addWidget(self.lineEdit_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(120, 30))
        self.label_4.setMaximumSize(QSize(200, 30))

        self.horizontalLayout.addWidget(self.label_4)

        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.clicked.connect(self.newfile_field)

        self.horizontalLayout.addWidget(self.radioButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setProperty('commonLineEditDownloadPage', True)
        self.lineEdit.setMinimumSize(QSize(0, 25))
        self.lineEdit.setMaximumSize(QSize(16777215, 25))
        self.lineEdit.setDisabled(True)

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

        self.set_variable_list()
        self.setstylesheet()

    def setstylesheet(self):
        self.form_main_page.setStyleSheet("""
            [CommomComboBoxFilterPage='true'] {
                background-color: #C3C3C3; /*829191*/
                border-radius: 10px;
                border: 2px solid #2C423F;
                color: black;
                padding-left: 15px;
                padding-right: 10px;
            }

            [CommomComboBoxFilterPage='true']::down-arrow {
                width: 15px;
                height: 15px;
                image: url(':/icons/icons/seta_baixo - branca.png');
            }

            [CommomComboBoxFilterPage='true']::drop-down {
                border: none;
                width: 15px;  /*tamanho da seta*/
                background-color: #2C423F;
                border-top-right-radius: 8px;
                border-bottom-right-radius: 8px;
            }

            QComboBox QAbstractiItemView {
                border: 1px solid #2C423F;
                background-color: white;
                color: black;
                selection-background-color: orange;
                selection-color: black;
                padding: 5px;
                border-radius: 5px;
            }
        """)

    def newfile_field(self):
        if self.radioButton.isChecked():
            self.lineEdit.setDisabled(False)
        else:
            self.lineEdit.setDisabled(True)

    def set_variable_list(self):
        file_path = os.path.join(self.main_page.project.caminho, self.filelist[0])
        with xr.open_dataset(file_path) as self.f:
            self.var = list(self.f.variables)

        self.comboBox_5.addItems([f'{var_item}' for var_item in self.var])
        self.comboBox_5.setCurrentIndex(0)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Variable to Change", None))
        self.label.setText(QCoreApplication.translate("Form", u"New name", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Final File Name", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"New File", None))
