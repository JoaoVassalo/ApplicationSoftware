# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DatDatasetFormdxDnou.ui'
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
    QLineEdit, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)
import xarray as xr

class Ui_Form(object):
    def setupUi(self, page, Form, filelist):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(240, 200)
        Form.setMinimumSize(QSize(200, 200))
        Form.setMaximumSize(QSize(240, 200))

        self.main_page = page
        self.filelist = filelist

        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setMinimumSize(QSize(0, 30))
        self.comboBox_2.setMaximumSize(QSize(16777215, 30))
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
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setMinimumSize(QSize(0, 30))
        self.comboBox_3.setMaximumSize(QSize(16777215, 30))
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


        self.verticalLayout_5.addLayout(self.horizontalLayout)

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
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setMaximumSize(QSize(16777215, 30))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
                                                   "	border-radius: 15px;\n"
                                                   "	border: 2px solid #F98600;\n"
                                                   "	color: white;\n"
                                                   "}\n"
                                                   "\n"
                                                   "\n"
                                                   "\n"
                                                   "")

        self.verticalLayout_4.addWidget(self.lineEdit)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 60))
        self.textEdit.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_5.addWidget(self.textEdit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
        self.set_combobox_values()
    # setupUi

    def set_combobox_values(self):
        self.f = xr.open_dataset(f'{self.main_page.project.caminho}\\{self.filelist[0]}')
        self.variables = [f'{var}' for var in list(self.f.variables) if self.f[var].ndim > 1]
        self.comboBox_2.addItems(self.variables)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_3.addItems(self.variables)
        self.comboBox_3.setCurrentIndex(1)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"U component", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"V component", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Final File Name", None))
    # retranslateUi

