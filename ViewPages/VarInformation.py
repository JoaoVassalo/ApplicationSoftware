# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VarInformationDiVStp.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, )
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
                               QHBoxLayout, QHeaderView, QLabel, QPushButton,
                               QSizePolicy, QSpacerItem, QTreeWidget, QTreeWidgetItem,
                               QWidget)
import resources_rc
import numpy as np
from datetime import datetime


class Ui_Form(object):
    def setupUi(self, Form, file_name, file):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(16777215, 250)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QSize(16777215, 250))
        # Form.setMaximumSize(QSize(610, 250))

        self.file_name = file_name
        self.file = file

        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(390, 30))
        self.label.setMaximumSize(QSize(390, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setText(QCoreApplication.translate("Form", f"File: {self.file_name}", None))

        self.horizontalLayout.addWidget(self.label)
        self.horizontalSpacer_lay = QSpacerItem(10, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer_lay)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 30))
        self.frame.setMaximumSize(QSize(200, 30))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 0, 191, 32))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(18, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(20, 20))
        self.checkBox.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.checkBox)

        self.horizontalSpacer_2 = QSpacerItem(5, 17, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(25, 25))
        self.pushButton.setMaximumSize(QSize(25, 25))
        self.pushButton.setStyleSheet(u"QPushButton:hover{\n"
                                      "	border: 1px solid black;\n"
                                      "	border-radius: 10px;\n"
                                      "}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/cruz - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(15, 15))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer_3 = QSpacerItem(5, 17, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.horizontalLayout.addWidget(self.frame)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.variables = list(self.file.variables)
        self.variables = [value for value in self.variables if value != 'number' and value != 'expver']
        self.header = ["Variables", "Dimension", "Values Qtd", "M\u00edm", "M\u00e1x", "Unit"]

        self.treeWidget = QTreeWidget(Form)
        font1 = QFont()
        font1.setBold(True)
        __qtreewidgetitem = QTreeWidgetItem()
        for header in range(len(self.header)):
            __qtreewidgetitem.setFont(header, font1)

        self.treeWidget.setHeaderItem(__qtreewidgetitem)

        for var in range(len(self.variables)):
            new = QTreeWidgetItem(self.treeWidget)

            for header_idx in range(len(self.header)):

                if self.header[header_idx] == 'Variables':
                    new.setText(header_idx, QCoreApplication.translate("Form", self.variables[var], None))

                elif self.header[header_idx] == 'Unit':
                    try:
                        unit = self.file[self.variables[var]].units
                        new.setText(header_idx, QCoreApplication.translate("Form", f'{unit}', None))
                    except:
                        new.setText(header_idx, QCoreApplication.translate("Form", '-', None))

                elif self.header[header_idx] == 'Dimension':
                    dimension = self.file[self.variables[var]].ndim
                    new.setText(header_idx, QCoreApplication.translate("Form", f'{dimension}', None))

                elif self.header[header_idx] == 'Values Qtd':
                    size = self.file[self.variables[var]].size
                    new.setText(header_idx, QCoreApplication.translate("Form", f'{size}', None))

                elif self.header[header_idx] == "M\u00edm":
                    if self.variables[var] == 'time' or self.variables[var] == 'valid_time':
                        min_value = self.sel_time(min(self.file[self.variables[var]].values))
                    elif self.variables[var] == 'lon' or self.variables[var] == 'longitude':
                        min_value = np.nanmin(self.file[self.variables[var]].values)
                        if min_value > 180:
                            min_value = round(np.nanmin(self.file[self.variables[var]].values) - 360, ndigits=2)
                    else:
                        min_value = round(np.nanmin(self.file[self.variables[var]].values), ndigits=3)
                    new.setText(header_idx, QCoreApplication.translate("Form", f'{min_value}', None))

                elif self.header[header_idx] == 'M\u00e1x':
                    if self.variables[var] == 'time' or self.variables[var] == 'valid_time':
                        min_value = self.sel_time(max(self.file[self.variables[var]].values))
                    elif self.variables[var] == 'lon' or self.variables[var] == 'longitude':
                        min_value = np.nanmax(self.file[self.variables[var]].values)
                        if min_value > 180:
                            min_value = round(np.nanmax(self.file[self.variables[var]].values) - 360, ndigits=2)
                    else:
                        min_value = round(np.nanmax(self.file[self.variables[var]].values), ndigits=3)
                    new.setText(header_idx, QCoreApplication.translate("Form", f'{min_value}', None))

        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMinimumSize(QSize(16777215, 200))

        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    @staticmethod
    def sel_time(value_time):
        time_to_format = str(value_time).split('.')[0]
        t_formated = datetime.strptime(time_to_format, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d-%Hh')
        return t_formated

    def setstylesheet(self):
        self.treeWidget.setStyleSheet("""
                    QTreeWidget {
                        background-color: #C3C3C3;
                        color: black;
                        border: 2px solid #2C423F;
                        border-radius: 5px;
                    }
                    QTreeWidget::item {
                        height: 30px;
                        padding: 5px;
                    }
                    QTreeWidget::item:selected {
                        background-color: #596869;
                        color: white;
                    }
                    QTreeWidget::item:hover {
                        background-color: #6F1A07;
                    }
                    QHeaderView::section {
                        background-color: #2C423F;
                        padding: 5px;
                        border: 1px solid #3B4252;
                        font-weight: bold;
                        color: white;
                    }
                """)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.checkBox.setText("")
        self.pushButton.setText("")

        ___qtreewidgetitem = self.treeWidget.headerItem()
        for idx in range(len(self.header)):
            ___qtreewidgetitem.setText(idx, QCoreApplication.translate("Form", self.header[idx], None))

        del self.file
        self.setstylesheet()
