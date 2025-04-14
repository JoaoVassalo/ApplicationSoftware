# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImpDatasetFormsjVZiF.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)
import xarray as xr
import os

class Ui_Form(object):
    def setupUi(self, page, Form, file):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(240, 200)
        Form.setMinimumSize(QSize(200, 200))
        Form.setMaximumSize(QSize(240, 200))

        self.form_main_page = Form

        self.main_page = page
        self.filelist = file
        file_path = os.path.join(self.main_page.project.caminho, self.filelist[0])
        self.file = xr.open_dataset(file_path)
        self.variables = [f'{var}' for var in list(self.file.variables) if self.file[var].ndim > 1]

        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(120, 30))
        self.label_5.setMaximumSize(QSize(200, 30))

        self.verticalLayout.addWidget(self.label_5)

        self.comboBox_4 = QComboBox(Form)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setProperty('CommomComboBoxFilterPage', True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setMinimumSize(QSize(0, 30))
        self.comboBox_4.setMaximumSize(QSize(16777215, 30))
        # self.comboBox_4.setStyleSheet(u"QComboBox{\n"
        #                             "	background-color: white;\n"
        #                             "	border-radius: 12px;\n"
        #                             "	border: 2px solid #F98600;\n"
        #                             "	color: black;\n"
        #                             "	padding-left: 15px;\n"
        #                             "    padding-right: 10px;\n"
        #                             "}\n"
        #                             "\n"
        #                             "QComboBox::drop-down {\n"
        #                             "    border: none;\n"
        #                             "    width: 20px;  /*tamanho da seta*/\n"
        #                             "    background-color: #F98600;\n"
        #                             "    border-top-right-radius: 10px;\n"
        #                             "    border-bottom-right-radius: 10px;\n"
        #                             "}\n"
        #                             "\n"
        #                             "QComboBox::down-arrow {\n"
        #                             "    width: 10px;\n"
        #                             "    height: 10px;\n"
        #                             "}\n"
        #                             "\n"
        #                             "QComboBox QAbstractItemView {\n"
        #                             "    border: 1px solid #F98600;\n"
        #                             "    background-color: white;\n"
        #                             "    color: black;\n"
        #                             "    selection-background-color: orange;\n"
        #                             "    selection-color: black;\n"
        #                             "    padding: 5px;\n"
        #                             "    border-radius: 5px;\n"
        #                             "}")
        self.comboBox_4.addItems(['Wind', 'Current'])
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_4.currentIndexChanged.connect(self.set_combos_values)

        self.verticalLayout.addWidget(self.comboBox_4)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.label_2)

        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setProperty('CommomComboBoxFilterPage', True)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setMinimumSize(QSize(0, 30))
        self.comboBox_2.setMaximumSize(QSize(16777215, 30))
        # self.comboBox_2.setStyleSheet(u"QComboBox{\n"
        #                               "	background-color: white;\n"
        #                               "	border-radius: 12px;\n"
        #                               "	border: 2px solid #F98600;\n"
        #                               "	color: black;\n"
        #                               "	padding-left: 15px;\n"
        #                               "    padding-right: 10px;\n"
        #                               "}\n"
        #                               "\n"
        #                               "QComboBox::drop-down {\n"
        #                               "    border: none;\n"
        #                               "    width: 20px;  /*tamanho da seta*/\n"
        #                               "    background-color: #F98600;\n"
        #                               "    border-top-right-radius: 10px;\n"
        #                               "    border-bottom-right-radius: 10px;\n"
        #                               "}\n"
        #                               "\n"
        #                               "QComboBox::down-arrow {\n"
        #                               "    width: 10px;\n"
        #                               "    height: 10px;\n"
        #                               "}\n"
        #                               "\n"
        #                               "QComboBox QAbstractItemView {\n"
        #                               "    border: 1px solid #F98600;\n"
        #                               "    background-color: white;\n"
        #                               "    color: black;\n"
        #                               "    selection-background-color: orange;\n"
        #                               "    selection-color: black;\n"
        #                               "    padding: 5px;\n"
        #                               "    border-radius: 5px;\n"
        #                               "}")

        self.verticalLayout_2.addWidget(self.comboBox_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_3.addWidget(self.label_3)

        self.comboBox_3 = QComboBox(Form)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setProperty('CommomComboBoxFilterPage', True)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setMinimumSize(QSize(0, 30))
        self.comboBox_3.setMaximumSize(QSize(16777215, 30))
        # self.comboBox_3.setStyleSheet(u"QComboBox{\n"
        #                               "	background-color: white;\n"
        #                               "	border-radius: 12px;\n"
        #                               "	border: 2px solid #F98600;\n"
        #                               "	color: black;\n"
        #                               "	padding-left: 15px;\n"
        #                               "    padding-right: 10px;\n"
        #                               "}\n"
        #                               "\n"
        #                               "QComboBox::drop-down {\n"
        #                               "    border: none;\n"
        #                               "    width: 20px;  /*tamanho da seta*/\n"
        #                               "    background-color: #F98600;\n"
        #                               "    border-top-right-radius: 10px;\n"
        #                               "    border-bottom-right-radius: 10px;\n"
        #                               "}\n"
        #                               "\n"
        #                               "QComboBox::down-arrow {\n"
        #                               "    width: 10px;\n"
        #                               "    height: 10px;\n"
        #                               "}\n"
        #                               "\n"
        #                               "QComboBox QAbstractItemView {\n"
        #                               "    border: 1px solid #F98600;\n"
        #                               "    background-color: white;\n"
        #                               "    color: black;\n"
        #                               "    selection-background-color: orange;\n"
        #                               "    selection-color: black;\n"
        #                               "    padding: 5px;\n"
        #                               "    border-radius: 5px;\n"
        #                               "}")

        self.verticalLayout_3.addWidget(self.comboBox_3)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

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
        self.lineEdit.setProperty('commonLineEditDownloadPage', True)
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_4.addWidget(self.lineEdit)


        self.gridLayout.addLayout(self.verticalLayout_4, 2, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
        self.setstylesheet()

    def setstylesheet(self):
        self.form_main_page.setStyleSheet("""
            [CommomComboBoxFilterPage='true'] {
                background-color: #C3C3C3; /*829191*/
                border-radius: 15px;
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
                border-top-right-radius: 10px;
                border-bottom-right-radius: 10px;
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

    def set_combos_values(self):
        if self.comboBox_4.currentText() == 'Wind':
            self.comboBox_2.clear()
            self.comboBox_3.clear()
        else:
            self.comboBox_2.addItems(self.variables)
            self.comboBox_3.addItems(self.variables)
            self.comboBox_3.setCurrentIndex(1)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Type of IMP file", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"U component", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"V component", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Final File Name", None))
    # retranslateUi

