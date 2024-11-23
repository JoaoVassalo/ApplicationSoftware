# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DownloadPageaencYW.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QTimeEdit,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_PageDownload(object):
    def setupUi(self, PageDownload):
        if not PageDownload.objectName():
            PageDownload.setObjectName(u"PageDownload")
        PageDownload.resize(875, 626)
        PageDownload.setMinimumSize(QSize(875, 626))
        PageDownload.setBaseSize(QSize(875, 626))
        self.Header = QWidget(PageDownload)
        self.Header.setObjectName(u"Header")
        self.Header.setGeometry(QRect(0, 0, 875, 121))
        self.Header.setMinimumSize(QSize(875, 121))
        self.Header.setMaximumSize(QSize(16777215, 121))
        self.Header.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLabel{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QFrame{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(0, 170, 127);\n"
"}\n"
"\n"
"QPushButton{\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(0, 170, 127);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.layoutWidget = QWidget(self.Header)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 0, 262, 121))
        self.DatabaseButtons = QVBoxLayout(self.layoutWidget)
        self.DatabaseButtons.setSpacing(0)
        self.DatabaseButtons.setObjectName(u"DatabaseButtons")
        self.DatabaseButtons.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.DatabaseButtons.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(135, 25))
        self.label.setMaximumSize(QSize(135, 25))
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")

        self.DatabaseButtons.addWidget(self.label)

        self.frame = QFrame(self.layoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(260, 50))
        self.frame.setMaximumSize(QSize(260, 50))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 0, 130, 50))
        self.pushButton.setMinimumSize(QSize(130, 50))
        self.pushButton.setMaximumSize(QSize(130, 50))
        self.pushButton.setCheckable(True)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(130, 0, 130, 50))
        self.pushButton_2.setMinimumSize(QSize(130, 50))
        self.pushButton_2.setMaximumSize(QSize(130, 50))
        self.pushButton_2.setCheckable(True)

        self.DatabaseButtons.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.DatabaseButtons.addItem(self.verticalSpacer)

        self.layoutWidget1 = QWidget(self.Header)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(506, 2, 352, 121))
        self.CatalogArea = QVBoxLayout(self.layoutWidget1)
        self.CatalogArea.setSpacing(0)
        self.CatalogArea.setObjectName(u"CatalogArea")
        self.CatalogArea.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.CatalogArea.addItem(self.verticalSpacer_4)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(135, 25))
        self.label_2.setMaximumSize(QSize(135, 25))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")

        self.CatalogArea.addWidget(self.label_2)

        self.comboBox = QComboBox(self.layoutWidget1)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(350, 35))
        self.comboBox.setMaximumSize(QSize(350, 35))
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.CatalogArea.addWidget(self.comboBox)

        self.verticalSpacer_3 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.CatalogArea.addItem(self.verticalSpacer_3)

        self.PageFunc = QWidget(PageDownload)
        self.PageFunc.setObjectName(u"PageFunc")
        self.PageFunc.setGeometry(QRect(0, 121, 875, 505))
        self.PageFunc.setMinimumSize(QSize(875, 505))
        self.PageFunc.setMaximumSize(QSize(16777215, 505))
        self.PageFunc.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(118, 118, 118);\n"
"}\n"
"\n"
"QDateEdit, QTimeEdit, QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.VariablesArea = QWidget(self.PageFunc)
        self.VariablesArea.setObjectName(u"VariablesArea")
        self.VariablesArea.setGeometry(QRect(50, 160, 751, 111))
        self.VariablesArea.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.DownloadButton = QPushButton(self.PageFunc)
        self.DownloadButton.setObjectName(u"DownloadButton")
        self.DownloadButton.setGeometry(QRect(510, 350, 141, 31))
        self.DownloadButton.setStyleSheet(u"")
        self.DownloadButton.setCheckable(True)
        self.progressBar = QProgressBar(self.PageFunc)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(670, 350, 141, 31))
        self.progressBar.setValue(24)
        self.progressBar.setHidden(True)
        self.Icon = QPushButton(self.PageFunc)
        self.Icon.setObjectName(u"Icon")
        self.Icon.setGeometry(QRect(800, 450, 40, 40))
        self.Icon.setMinimumSize(QSize(40, 40))
        self.Icon.setMaximumSize(QSize(40, 40))
        self.Icon.setStyleSheet(u"background-color: rgb(118, 118, 118);\n"
"border: none;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/informacion_verde.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Icon.setIcon(icon)
        self.Icon.setIconSize(QSize(40, 40))
        self.StopButton = QPushButton(self.PageFunc)
        self.StopButton.setObjectName(u"StopButton")
        self.StopButton.setGeometry(QRect(510, 400, 141, 31))
        self.StopButton.setStyleSheet(u"")
        self.StopButton.setHidden(True)
        self.DateArea = QWidget(self.PageFunc)
        self.DateArea.setObjectName(u"DateArea")
        self.DateArea.setGeometry(QRect(50, 30, 751, 80))
        self.DateArea.setStyleSheet(u"QDateEdit, QTimeEdit, QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.widget = QWidget(self.DateArea)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 10, 751, 71))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 6, -1, 6)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_3.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_3)

        self.dateEdit = QDateEdit(self.widget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(141, 31))
        self.dateEdit.setMaximumSize(QSize(141, 31))

        self.verticalLayout_3.addWidget(self.dateEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 6, -1, 6)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.timeEdit = QTimeEdit(self.widget)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setMinimumSize(QSize(141, 31))
        self.timeEdit.setMaximumSize(QSize(141, 31))

        self.verticalLayout_4.addWidget(self.timeEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 6, -1, 6)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_4)

        self.dateEdit_2 = QDateEdit(self.widget)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setMinimumSize(QSize(141, 31))
        self.dateEdit_2.setMaximumSize(QSize(141, 31))

        self.verticalLayout_5.addWidget(self.dateEdit_2)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 6, -1, 6)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_6)

        self.timeEdit_2 = QTimeEdit(self.widget)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        self.timeEdit_2.setMinimumSize(QSize(141, 31))
        self.timeEdit_2.setMaximumSize(QSize(141, 31))

        self.verticalLayout_6.addWidget(self.timeEdit_2)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.widget1 = QWidget(self.PageFunc)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(140, 300, 136, 148))
        self.NorthSouth = QVBoxLayout(self.widget1)
        self.NorthSouth.setObjectName(u"NorthSouth")
        self.NorthSouth.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_7 = QLabel(self.widget1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_10.addWidget(self.label_7)

        self.lineEdit = QLineEdit(self.widget1)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_10.addWidget(self.lineEdit)


        self.NorthSouth.addLayout(self.verticalLayout_10)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.NorthSouth.addItem(self.verticalSpacer_5)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_10 = QLabel(self.widget1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_10)

        self.lineEdit_4 = QLineEdit(self.widget1)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_9.addWidget(self.lineEdit_4)


        self.NorthSouth.addLayout(self.verticalLayout_9)

        self.widget2 = QWidget(self.PageFunc)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(50, 350, 322, 49))
        self.WestEast = QHBoxLayout(self.widget2)
        self.WestEast.setObjectName(u"WestEast")
        self.WestEast.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_9 = QLabel(self.widget2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_9)

        self.lineEdit_2 = QLineEdit(self.widget2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_7.addWidget(self.lineEdit_2)


        self.WestEast.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.WestEast.addItem(self.horizontalSpacer_4)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.widget2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_8)

        self.lineEdit_3 = QLineEdit(self.widget2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_8.addWidget(self.lineEdit_3)


        self.WestEast.addLayout(self.verticalLayout_8)


        self.retranslateUi(PageDownload)
        self.DownloadButton.toggled.connect(self.StopButton.setVisible)
        self.DownloadButton.toggled.connect(self.progressBar.setVisible)
        self.StopButton.clicked["bool"].connect(self.DownloadButton.setChecked)
        self.DownloadButton.toggled.connect(self.lineEdit_3.setDisabled)
        self.DownloadButton.toggled.connect(self.lineEdit_4.setDisabled)
        self.DownloadButton.toggled.connect(self.lineEdit_2.setDisabled)
        self.DownloadButton.toggled.connect(self.lineEdit.setDisabled)
        self.DownloadButton.toggled.connect(self.DateArea.setDisabled)
        self.DownloadButton.toggled.connect(self.VariablesArea.setDisabled)

        QMetaObject.connectSlotsByName(PageDownload)
    # setupUi

    def retranslateUi(self, PageDownload):
        PageDownload.setWindowTitle(QCoreApplication.translate("PageDownload", u"Form", None))
        self.label.setText(QCoreApplication.translate("PageDownload", u"Select one database", None))
        self.pushButton.setText(QCoreApplication.translate("PageDownload", u"HYCOM", None))
        self.pushButton_2.setText(QCoreApplication.translate("PageDownload", u"COPERNICUS", None))
        self.label_2.setText(QCoreApplication.translate("PageDownload", u"Select one catalog", None))
        self.comboBox.setPlaceholderText(QCoreApplication.translate("PageDownload", u"Searh for a catalog here...", None))
        self.DownloadButton.setText(QCoreApplication.translate("PageDownload", u"Download", None))
        self.Icon.setText("")
        self.StopButton.setText(QCoreApplication.translate("PageDownload", u"STOP", None))
        self.label_3.setText(QCoreApplication.translate("PageDownload", u"Initial Date", None))
        self.label_5.setText(QCoreApplication.translate("PageDownload", u"Starting time", None))
        self.label_4.setText(QCoreApplication.translate("PageDownload", u"Final Date", None))
        self.label_6.setText(QCoreApplication.translate("PageDownload", u"Ending Time", None))
        self.label_7.setText(QCoreApplication.translate("PageDownload", u"North", None))
        self.label_10.setText(QCoreApplication.translate("PageDownload", u"South", None))
        self.label_9.setText(QCoreApplication.translate("PageDownload", u"West", None))
        self.label_8.setText(QCoreApplication.translate("PageDownload", u"East", None))
    # retranslateUi

