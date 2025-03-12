# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConcatDatasetFormeCkPNd.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget, QLineEdit)
import xarray as xr

class Ui_Form(object):
    def setupUi(self, page, Form, filelist):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(240, 200)
        Form.setMinimumSize(QSize(200, 200))
        Form.setMaximumSize(QSize(240, 200))

        self.main_page = page
        self.filelist_to = filelist

        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 20))
        self.label.setMaximumSize(QSize(200, 20))

        self.verticalLayout.addWidget(self.label)

        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setProperty('CommomComboBox', True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QSize(0, 20))
        self.comboBox.setMaximumSize(QSize(16777215, 20))

        self.set_list_combobox()

        self.verticalLayout.addWidget(self.comboBox)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 20))
        self.label_2.setMaximumSize(QSize(200, 20))

        self.verticalLayout.addWidget(self.label_2)

        self.file_name = QLineEdit(Form)
        self.file_name.setObjectName(u"file_name")
        self.file_name.setProperty('commonLineEditDownloadPage', True)
        self.file_name.setMinimumSize(QSize(0, 30))
        self.file_name.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.file_name)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def set_list_combobox(self):
        f = xr.open_dataset(f'{self.main_page.project.caminho}\\{self.filelist_to[0]}')
        var = list(f.variables)
        self.comboBox.addItems([f'{var_item}' for var_item in var if f[var_item].ndim == 1])

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Dimension to Concatenate", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Final File Name", None))
    # retranslateUi

