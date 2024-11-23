# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'indexTMkGwi.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc
from DownloadPage import Ui_PageDownload


class UiDownloadPage(QWidget):
        def __init__(self):
                super().__init__()
                self.new_download_page = Ui_PageDownload()
                self.new_download_page.setupUi(self)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1220, 735)
        MainWindow.setMinimumSize(QSize(1220, 735))
        MainWindow.setBaseSize(QSize(1220, 735))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(70, 0))
        self.icon_only_widget.setMaximumSize(QSize(70, 16777215))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius: 10px\n"
"}")
        self.icon_only_widget.setHidden(True)
        self.verticalLayout_5 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 20, -1, -1)
        self.logo_icon_only = QHBoxLayout()
        self.logo_icon_only.setObjectName(u"logo_icon_only")
        self.horizontalSpacer_4 = QSpacerItem(10, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.logo_icon_only.addItem(self.horizontalSpacer_4)

        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/icons/icons/hogar.png"))
        self.label.setScaledContents(True)

        self.logo_icon_only.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(10, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.logo_icon_only.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addLayout(self.logo_icon_only)

        self.icons_up_only = QVBoxLayout()
        self.icons_up_only.setSpacing(20)
        self.icons_up_only.setObjectName(u"icons_up_only")
        self.icons_up_only.setContentsMargins(-1, 20, -1, -1)
        self.DB_1 = QPushButton(self.icon_only_widget)
        self.DB_1.setObjectName(u"DB_1")
        self.DB_1.setMinimumSize(QSize(0, 30))
        self.DB_1.setMaximumSize(QSize(16777215, 30))
        self.DB_1.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 70, 0);\n"
"	font-size: 13px;\n"
"}")
        self.DB_1.clicked.connect(self.build_download_page)
        icon = QIcon()
        icon.addFile(u":/icons/icons/descargar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.DB_1.setIcon(icon)
        self.DB_1.setIconSize(QSize(100, 20))
        self.DB_1.setCheckable(False)

        self.icons_up_only.addWidget(self.DB_1)

        self.VB_1 = QPushButton(self.icon_only_widget)
        self.VB_1.setObjectName(u"VB_1")
        self.VB_1.setMinimumSize(QSize(0, 30))
        self.VB_1.setMaximumSize(QSize(16777215, 30))
        self.VB_1.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 70, 0);\n"
"	font-size: 13px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/ojo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.VB_1.setIcon(icon1)
        self.VB_1.setIconSize(QSize(100, 20))
        self.VB_1.setCheckable(False)

        self.icons_up_only.addWidget(self.VB_1)

        self.CB_1 = QPushButton(self.icon_only_widget)
        self.CB_1.setObjectName(u"CB_1")
        self.CB_1.setMinimumSize(QSize(0, 30))
        self.CB_1.setMaximumSize(QSize(16777215, 30))
        self.CB_1.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 70, 0);\n"
"	font-size: 13px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/agregar-documento.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.CB_1.setIcon(icon2)
        self.CB_1.setIconSize(QSize(100, 20))
        self.CB_1.setCheckable(False)

        self.icons_up_only.addWidget(self.CB_1)

        self.SB_1 = QPushButton(self.icon_only_widget)
        self.SB_1.setObjectName(u"SB_1")
        self.SB_1.setMinimumSize(QSize(0, 30))
        self.SB_1.setMaximumSize(QSize(16777215, 30))
        self.SB_1.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 70, 0);\n"
"	font-size: 13px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/grafico-histograma.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SB_1.setIcon(icon3)
        self.SB_1.setIconSize(QSize(100, 20))
        self.SB_1.setCheckable(False)

        self.icons_up_only.addWidget(self.SB_1)


        self.verticalLayout_5.addLayout(self.icons_up_only)

        self.verticalSpacer = QSpacerItem(20, 343, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.icons_down_only = QVBoxLayout()
        self.icons_down_only.setSpacing(20)
        self.icons_down_only.setObjectName(u"icons_down_only")
        self.ConfigB_1 = QPushButton(self.icon_only_widget)
        self.ConfigB_1.setObjectName(u"ConfigB_1")
        self.ConfigB_1.setMinimumSize(QSize(0, 30))
        self.ConfigB_1.setMaximumSize(QSize(16777215, 30))
        self.ConfigB_1.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 70, 0);\n"
"	font-size: 13px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/ajustes.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ConfigB_1.setIcon(icon4)
        self.ConfigB_1.setIconSize(QSize(100, 20))
        self.ConfigB_1.setCheckable(False)

        self.icons_down_only.addWidget(self.ConfigB_1)

        self.LogoutB_1 = QPushButton(self.icon_only_widget)
        self.LogoutB_1.setObjectName(u"LogoutB_1")
        self.LogoutB_1.setMinimumSize(QSize(0, 30))
        self.LogoutB_1.setMaximumSize(QSize(16777215, 30))
        self.LogoutB_1.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 70, 0);\n"
"	font-size: 13px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/salida.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.LogoutB_1.setIcon(icon5)
        self.LogoutB_1.setIconSize(QSize(100, 20))
        self.LogoutB_1.setCheckable(False)

        self.icons_down_only.addWidget(self.LogoutB_1)


        self.verticalLayout_5.addLayout(self.icons_down_only)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 2, 1)

        self.icon_text_widget = QWidget(self.centralwidget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setMinimumSize(QSize(241, 0))
        self.icon_text_widget.setMaximumSize(QSize(241, 16777215))
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"	color:white;\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 20, -1, -1)
        self.logo_name = QHBoxLayout()
        self.logo_name.setObjectName(u"logo_name")
        self.horizontalSpacer_2 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.logo_name.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.logo_name.addItem(self.horizontalSpacer_5)

        self.logoicon_with_name = QHBoxLayout()
        self.logoicon_with_name.setSpacing(20)
        self.logoicon_with_name.setObjectName(u"logoicon_with_name")
        self.label_2 = QLabel(self.icon_text_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/icons/icons/hogar.png"))
        self.label_2.setScaledContents(True)

        self.logoicon_with_name.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_text_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)

        self.logoicon_with_name.addWidget(self.label_3)


        self.logo_name.addLayout(self.logoicon_with_name)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.logo_name.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addLayout(self.logo_name)

        self.icons_up_name = QVBoxLayout()
        self.icons_up_name.setSpacing(20)
        self.icons_up_name.setObjectName(u"icons_up_name")
        self.icons_up_name.setContentsMargins(-1, 20, -1, -1)
        self.DB_2 = QPushButton(self.icon_text_widget)
        self.DB_2.setObjectName(u"DB_2")
        self.DB_2.setMinimumSize(QSize(0, 30))
        self.DB_2.setMaximumSize(QSize(16777215, 30))
        self.DB_2.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 70, 0);\n"
"	font-size: 13px;\n"
"}")
        self.DB_2.clicked.connect(self.build_download_page)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/descargar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/icons/icons/descargar.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.DB_2.setIcon(icon6)
        self.DB_2.setIconSize(QSize(100, 20))
        self.DB_2.setCheckable(False)

        self.icons_up_name.addWidget(self.DB_2)

        self.VB_2 = QPushButton(self.icon_text_widget)
        self.VB_2.setObjectName(u"VB_2")
        self.VB_2.setMinimumSize(QSize(0, 30))
        self.VB_2.setMaximumSize(QSize(16777215, 30))
        self.VB_2.setStyleSheet(u"QPushButton{\n"
"	padding-left: -20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 70, 0);\n"
"	font-size: 13px;\n"
"}")
        self.VB_2.setIcon(icon1)
        self.VB_2.setIconSize(QSize(100, 20))
        self.VB_2.setCheckable(False)

        self.icons_up_name.addWidget(self.VB_2)

        self.CB_2 = QPushButton(self.icon_text_widget)
        self.CB_2.setObjectName(u"CB_2")
        self.CB_2.setMinimumSize(QSize(0, 30))
        self.CB_2.setMaximumSize(QSize(16777215, 30))
        self.CB_2.setStyleSheet(u"QPushButton{\n"
"	padding-left: -50px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 70, 0);\n"
"	font-size: 13px;\n"
"}")
        self.CB_2.setIcon(icon2)
        self.CB_2.setIconSize(QSize(100, 20))
        self.CB_2.setCheckable(False)

        self.icons_up_name.addWidget(self.CB_2)

        self.SB_2 = QPushButton(self.icon_text_widget)
        self.SB_2.setObjectName(u"SB_2")
        self.SB_2.setMinimumSize(QSize(0, 30))
        self.SB_2.setMaximumSize(QSize(16777215, 30))
        self.SB_2.setStyleSheet(u"QPushButton{\n"
"	padding-left: -14px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 70, 0);\n"
"	font-size: 13px;\n"
"}")
        self.SB_2.setIcon(icon3)
        self.SB_2.setIconSize(QSize(100, 20))
        self.SB_2.setCheckable(False)

        self.icons_up_name.addWidget(self.SB_2)


        self.verticalLayout_6.addLayout(self.icons_up_name)

        self.verticalSpacer_2 = QSpacerItem(20, 341, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.icons_down_name = QVBoxLayout()
        self.icons_down_name.setSpacing(20)
        self.icons_down_name.setObjectName(u"icons_down_name")
        self.ConfigB_2 = QPushButton(self.icon_text_widget)
        self.ConfigB_2.setObjectName(u"ConfigB_2")
        self.ConfigB_2.setMinimumSize(QSize(0, 30))
        self.ConfigB_2.setMaximumSize(QSize(16777215, 30))
        self.ConfigB_2.setStyleSheet(u"QPushButton{\n"
"	padding-left: -70px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 70, 0);\n"
"	font-size: 13px;\n"
"}")
        self.ConfigB_2.setIcon(icon4)
        self.ConfigB_2.setIconSize(QSize(100, 20))
        self.ConfigB_2.setCheckable(False)

        self.icons_down_name.addWidget(self.ConfigB_2)

        self.LogoutB_2 = QPushButton(self.icon_text_widget)
        self.LogoutB_2.setObjectName(u"LogoutB_2")
        self.LogoutB_2.setMinimumSize(QSize(0, 30))
        self.LogoutB_2.setMaximumSize(QSize(16777215, 30))
        self.LogoutB_2.setStyleSheet(u"QPushButton{\n"
"	padding-left: -70px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 70, 0);\n"
"	font-size: 13px;\n"
"}")
        self.LogoutB_2.setIcon(icon5)
        self.LogoutB_2.setIconSize(QSize(100, 20))
        self.LogoutB_2.setCheckable(False)

        self.icons_down_name.addWidget(self.LogoutB_2)


        self.verticalLayout_6.addLayout(self.icons_down_name)


        self.gridLayout.addWidget(self.icon_text_widget, 0, 1, 2, 1)

        self.header_widget = QWidget(self.centralwidget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMinimumSize(QSize(861, 80))
        self.header_widget.setMaximumSize(QSize(16777215, 80))
        self.header_widget.setStyleSheet(u"background-color: rgb(23, 132, 65);\n"
"border-radius: 10px;")
        self.horizontalLayout_5 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.header_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(30, 35))
        self.pushButton.setMaximumSize(QSize(30, 35))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/menu_preto.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/icons/icons/menu-hamburguesa.png", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.pushButton.setIcon(icon7)
        self.pushButton.setIconSize(QSize(30, 35))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 5, -1, 5)
        self.label_4 = QLabel(self.header_widget)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_4.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_4)

        self.label_5 = QLabel(self.header_widget)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_5.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_6 = QSpacerItem(682, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.gridLayout.addWidget(self.header_widget, 0, 2, 1, 1)

        self.main_screen_widget = QWidget(self.centralwidget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(48, 48, 48);\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.main_grid_widget = QGridLayout(self.main_screen_widget)

        self.gridLayout.addWidget(self.main_screen_widget, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.LogoutB_1.clicked.connect(MainWindow.close)
        self.LogoutB_2.clicked.connect(MainWindow.close)
        self.pushButton.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton.toggled.connect(self.icon_only_widget.setVisible)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.DB_1.setText("")
        self.VB_1.setText("")
        self.CB_1.setText("")
        self.SB_1.setText("")
        self.ConfigB_1.setText("")
        self.LogoutB_1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"GeoEnergia Lab", None))
        self.DB_2.setText(QCoreApplication.translate("MainWindow", u"  Search and Download", None))
        self.VB_2.setText(QCoreApplication.translate("MainWindow", u"  Data Visualization", None))
        self.CB_2.setText(QCoreApplication.translate("MainWindow", u"  File Creation", None))
        self.SB_2.setText(QCoreApplication.translate("MainWindow", u"  Simulation Results", None))
        self.ConfigB_2.setText(QCoreApplication.translate("MainWindow", u"  Settings", None))
        self.LogoutB_2.setText(QCoreApplication.translate("MainWindow", u"  Log out", None))
        self.pushButton.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Hello,", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Welcome to your page", None))
    # retranslateUi

    def build_download_page(self):
        self.download_page = UiDownloadPage()
        self.main_grid_widget.addWidget(self.download_page)
        print('Construiu página!')

