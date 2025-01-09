# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Salinity_LonLat_ButtonslLcoHP.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QThread)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)
import resources_rc
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from datetime import datetime
import time
import os


class AnimationWorker(QThread):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def run(self):
        self.page.play_animation()


class Ui_WindButton_LonLatProfile(object):
    def setupUi(self, page, WindButton_LonLatProfile, dataset):
        if not WindButton_LonLatProfile.objectName():
            WindButton_LonLatProfile.setObjectName(u"WindButton_LonLatProfile")
        WindButton_LonLatProfile.resize(546, 436)

        self.mainpage = page
        self.dataset = dataset

        self.horizontalLayout = QHBoxLayout(WindButton_LonLatProfile)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(WindButton_LonLatProfile)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(WindButton_LonLatProfile)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(320, 0))
        self.frame_2.setMaximumSize(QSize(320, 16777215))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_34 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_34)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.TimeFilterLabel = QLabel(self.frame_2)
        self.TimeFilterLabel.setObjectName(u"TimeFilterLabel")
        self.TimeFilterLabel.setMinimumSize(QSize(180, 22))
        self.TimeFilterLabel.setMaximumSize(QSize(180, 22))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.TimeFilterLabel.setFont(font)

        self.verticalLayout_13.addWidget(self.TimeFilterLabel)

        self.frame_buttons_animation_time = QFrame(self.frame_2)
        self.frame_buttons_animation_time.setObjectName(u"frame_buttons_animation_time")
        self.frame_buttons_animation_time.setMinimumSize(QSize(180, 50))
        self.frame_buttons_animation_time.setMaximumSize(QSize(180, 50))
        self.frame_buttons_animation_time.setStyleSheet(u"QPushButton {\n"
                                                        "    background-color: transparent;\n"
                                                        "    border: none;\n"
                                                        "    padding: 10px; /* Adicione um padding maior para ajustar o tamanho do fundo */\n"
                                                        "}\n"
                                                        "\n"
                                                        "QPushButton:hover {\n"
                                                        "    background-color: rgba(255, 165, 0, 0.2); /* Cor de fundo no hover */\n"
                                                        "    border-radius: 5px; /* Bordas arredondadas */\n"
                                                        "}\n"
                                                        "\n"
                                                        "QPushButton:pressed {\n"
                                                        "    background-color: rgba(255, 165, 0, 0.5); /* Cor de fundo ao pressionar */\n"
                                                        "}")
        self.frame_buttons_animation_time.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_buttons_animation_time.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_buttons_animation_time)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.start_button_time = QPushButton(self.frame_buttons_animation_time)
        self.start_button_time.setObjectName(u"start_button_time")
        icon = QIcon()
        icon.addFile(u":/icons/icons/backward - laranja.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start_button_time.setIcon(icon)
        self.start_button_time.setIconSize(QSize(20, 20))
        self.start_button_time.clicked.connect(self.firts_in_time)

        self.gridLayout_7.addWidget(self.start_button_time, 0, 0, 1, 1)

        self.backward_button_time = QPushButton(self.frame_buttons_animation_time)
        self.backward_button_time.setObjectName(u"backward_button_time")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/arrow-left - laranja.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backward_button_time.setIcon(icon1)
        self.backward_button_time.setIconSize(QSize(20, 20))
        self.backward_button_time.clicked.connect(self.back_in_time)

        self.gridLayout_7.addWidget(self.backward_button_time, 0, 1, 1, 1)

        self.pause_button_time = QPushButton(self.frame_buttons_animation_time)
        self.pause_button_time.setObjectName(u"pause_button_time")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/pause - laranja.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pause_button_time.setIcon(icon2)
        self.pause_button_time.setIconSize(QSize(20, 20))
        self.pause_button_time.setCheckable(True)
        self.pause_button_time.setChecked(False)

        self.gridLayout_7.addWidget(self.pause_button_time, 0, 2, 1, 1)

        self.play_button_time = QPushButton(self.frame_buttons_animation_time)
        self.play_button_time.setObjectName(u"play_button_time")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/play - laranja.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.play_button_time.setIcon(icon3)
        self.play_button_time.setIconSize(QSize(20, 20))
        self.play_button_time.setCheckable(False)
        self.play_button_time.clicked.connect(self.play_temp_animation)

        self.gridLayout_7.addWidget(self.play_button_time, 0, 3, 1, 1)

        self.forward_button_time = QPushButton(self.frame_buttons_animation_time)
        self.forward_button_time.setObjectName(u"forward_button_time")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/arrow-right - laranja.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.forward_button_time.setIcon(icon4)
        self.forward_button_time.setIconSize(QSize(20, 20))
        self.forward_button_time.clicked.connect(self.forward_in_time)

        self.gridLayout_7.addWidget(self.forward_button_time, 0, 4, 1, 1)

        self.finish_button_time = QPushButton(self.frame_buttons_animation_time)
        self.finish_button_time.setObjectName(u"finish_button_time")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/forward - laranja.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.finish_button_time.setIcon(icon5)
        self.finish_button_time.setIconSize(QSize(20, 20))
        self.finish_button_time.clicked.connect(self.last_in_time)

        self.gridLayout_7.addWidget(self.finish_button_time, 0, 5, 1, 1)

        self.verticalLayout_13.addWidget(self.frame_buttons_animation_time)

        self.TimeValueLabel = QLabel(self.frame_2)
        self.TimeValueLabel.setObjectName(u"TimeValueLabel")
        self.TimeValueLabel.setMinimumSize(QSize(180, 22))
        self.TimeValueLabel.setMaximumSize(QSize(180, 22))
        self.TimeValueLabel.setStyleSheet(u"border: 2px solid #212b33")
        self.TimeValueLabel.setText(u"Aqui vai o valor de tempo")
        self.TimeValueLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.TimeValueLabel)

        self.horizontalLayout_7.addLayout(self.verticalLayout_13)

        self.horizontalSpacer_35 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_35)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_36 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_36)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.DepthFilterLabel = QLabel(self.frame_2)
        self.DepthFilterLabel.setObjectName(u"DepthFilterLabel")
        self.DepthFilterLabel.setMinimumSize(QSize(180, 22))
        self.DepthFilterLabel.setMaximumSize(QSize(180, 22))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.DepthFilterLabel.setFont(font1)

        self.verticalLayout_14.addWidget(self.DepthFilterLabel)

        self.frame_buttons_animation_2_depth = QFrame(self.frame_2)
        self.frame_buttons_animation_2_depth.setObjectName(u"frame_buttons_animation_2_depth")
        self.frame_buttons_animation_2_depth.setMinimumSize(QSize(180, 50))
        self.frame_buttons_animation_2_depth.setMaximumSize(QSize(180, 50))
        self.frame_buttons_animation_2_depth.setStyleSheet(u"QPushButton {\n"
                                                           "    background-color: transparent;\n"
                                                           "    border: none;\n"
                                                           "    padding: 10px; /* Adicione um padding maior para ajustar o tamanho do fundo */\n"
                                                           "}\n"
                                                           "\n"
                                                           "QPushButton:hover {\n"
                                                           "    background-color: rgba(255, 165, 0, 0.2); /* Cor de fundo no hover */\n"
                                                           "    border-radius: 5px; /* Bordas arredondadas */\n"
                                                           "}\n"
                                                           "\n"
                                                           "QPushButton:pressed {\n"
                                                           "    background-color: rgba(255, 165, 0, 0.5); /* Cor de fundo ao pressionar */\n"
                                                           "}")
        self.frame_buttons_animation_2_depth.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_buttons_animation_2_depth.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_buttons_animation_2_depth)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.start_button_depth = QPushButton(self.frame_buttons_animation_2_depth)
        self.start_button_depth.setObjectName(u"start_button_depth")
        self.start_button_depth.setIcon(icon)
        self.start_button_depth.setIconSize(QSize(20, 20))
        self.start_button_depth.clicked.connect(self.start_in_depth)

        self.gridLayout_8.addWidget(self.start_button_depth, 0, 0, 1, 1)

        self.backward_button_depth = QPushButton(self.frame_buttons_animation_2_depth)
        self.backward_button_depth.setObjectName(u"backward_button_depth")
        self.backward_button_depth.setIcon(icon1)
        self.backward_button_depth.setIconSize(QSize(20, 20))
        self.backward_button_depth.clicked.connect(self.back_in_depth)

        self.gridLayout_8.addWidget(self.backward_button_depth, 0, 1, 1, 1)

        self.pause_button_depth = QPushButton(self.frame_buttons_animation_2_depth)
        self.pause_button_depth.setObjectName(u"pause_button_depth")
        self.pause_button_depth.setIcon(icon2)
        self.pause_button_depth.setIconSize(QSize(20, 20))
        self.pause_button_depth.setCheckable(True)
        self.pause_button_depth.setChecked(False)

        self.gridLayout_8.addWidget(self.pause_button_depth, 0, 2, 1, 1)

        self.play_button_depth = QPushButton(self.frame_buttons_animation_2_depth)
        self.play_button_depth.setObjectName(u"play_button_depth")
        self.play_button_depth.setIcon(icon3)
        self.play_button_depth.setIconSize(QSize(20, 20))
        self.play_button_depth.setCheckable(False)
        self.play_button_depth.clicked.connect(self.play_depth_animation)

        self.gridLayout_8.addWidget(self.play_button_depth, 0, 3, 1, 1)

        self.forward_button_depth = QPushButton(self.frame_buttons_animation_2_depth)
        self.forward_button_depth.setObjectName(u"forward_button_depth")
        self.forward_button_depth.setIcon(icon4)
        self.forward_button_depth.setIconSize(QSize(20, 20))
        self.forward_button_depth.clicked.connect(self.forward_in_depth)

        self.gridLayout_8.addWidget(self.forward_button_depth, 0, 4, 1, 1)

        self.finish_button_depth = QPushButton(self.frame_buttons_animation_2_depth)
        self.finish_button_depth.setObjectName(u"finish_button_depth")
        self.finish_button_depth.setIcon(icon5)
        self.finish_button_depth.setIconSize(QSize(20, 20))
        self.finish_button_depth.clicked.connect(self.last_in_depth)

        self.gridLayout_8.addWidget(self.finish_button_depth, 0, 5, 1, 1)

        self.verticalLayout_14.addWidget(self.frame_buttons_animation_2_depth)

        self.DepthValueLabel = QLabel(self.frame_2)
        self.DepthValueLabel.setObjectName(u"DepthValueLabel")
        self.DepthValueLabel.setMinimumSize(QSize(180, 22))
        self.DepthValueLabel.setMaximumSize(QSize(180, 22))
        self.DepthValueLabel.setStyleSheet(u"border: 2px solid #212b33")
        self.DepthValueLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.DepthValueLabel.setWordWrap(False)

        self.verticalLayout_14.addWidget(self.DepthValueLabel)

        self.horizontalLayout_8.addLayout(self.verticalLayout_14)

        self.horizontalSpacer_37 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_37)

        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_40 = QSpacerItem(18, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_40)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.SaveFigButton = QPushButton(self.frame_2)
        self.SaveFigButton.setObjectName(u"SaveFigButton")
        self.SaveFigButton.setMinimumSize(QSize(120, 30))
        self.SaveFigButton.setMaximumSize(QSize(120, 30))
        self.SaveFigButton.setStyleSheet(u"QPushButton{\n"
                                         "	background-color: rgb(61, 80, 95);\n"
                                         "	border-radius: 15px;\n"
                                         "	border: 2px solid #F98600;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "	color: #F98600;\n"
                                         "	font-size: 14px;\n"
                                         "}")
        self.SaveFigButton.clicked.connect(self.save_fig)

        self.horizontalLayout_6.addWidget(self.SaveFigButton)

        self.SaveAnimationButton = QPushButton(self.frame_2)
        self.SaveAnimationButton.setObjectName(u"SaveAnimationButton")
        self.SaveAnimationButton.setMinimumSize(QSize(120, 30))
        self.SaveAnimationButton.setMaximumSize(QSize(120, 30))
        self.SaveAnimationButton.setStyleSheet(u"QPushButton{\n"
                                               "	background-color: rgb(61, 80, 95);\n"
                                               "	border-radius: 15px;\n"
                                               "	border: 2px solid #F98600;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover{\n"
                                               "	color: #F98600;\n"
                                               "	font-size: 14px;\n"
                                               "}")
        self.SaveAnimationButton.clicked.connect(self.save_anim)

        self.horizontalLayout_6.addWidget(self.SaveAnimationButton)

        self.horizontalLayout_15.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer_41 = QSpacerItem(18, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_41)

        self.verticalLayout.addLayout(self.horizontalLayout_15)

        self.horizontalLayout.addWidget(self.frame_2)

        self.retranslateUi(WindButton_LonLatProfile)

        QMetaObject.connectSlotsByName(WindButton_LonLatProfile)

        self.graph_layout = QVBoxLayout()
        self.figure = Figure(figsize=(6, 6))
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.frame)
        # self.toolbar = CustomNavigationToolbar(self.canvas, self.frame)  # Use the custom toolbar
        self.graph_layout.addWidget(self.toolbar)
        self.graph_layout.addWidget(self.canvas)

        self.frame.setLayout(self.graph_layout)

        try:
            self.lat = [lat_value for lat_value in self.dataset['lat'].values]
            self.lon = [lon_value for lon_value in self.dataset['lon'].values]
            self.time = self.dataset['time'].values
            self.time_selected = self.time[0]
            self.depth = self.dataset['depth'].values
            self.depth_selected = self.depth[0]
            self.var_selected = None
            self.sel_time(self.time_selected)
            self.sel_depth()
            self.first_profile()
        except Exception as e:
            raise e

    def sel_time(self, value_time):
        time_to_format = str(value_time).split('.')[0]
        t_formated = datetime.strptime(time_to_format, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d-%Hh')
        self.TimeValueLabel.setText(f'{t_formated}')

    def sel_depth(self):
        self.DepthValueLabel.setText(f'{self.depth_selected} metros')

    def firts_in_time(self):
        if self.time_selected == self.time[0]:
            return
        else:
            self.time_selected = self.time[0]
            self.sel_time(self.time_selected)
            self.plot_profile()

    def last_in_time(self):
        if self.time_selected == self.time[-1]:
            return
        else:
            self.time_selected = self.time[-1]
            self.sel_time(self.time_selected)
            self.plot_profile()

    def forward_in_time(self):
        if self.time_selected == self.time[-1]:
            return
        else:
            index = np.where(self.time == self.time_selected)[0][0]
            self.time_selected = self.time[index + 1]
            self.sel_time(self.time_selected)
            self.plot_profile()

    def back_in_time(self):
        if self.time_selected == self.time[0]:
            return
        else:
            index = np.where(self.time == self.time_selected)[0][0]
            self.time_selected = self.time[index - 1]
            self.sel_time(self.time_selected)
            self.plot_profile()

    def last_in_depth(self):
        if self.depth_selected == self.depth[-1]:
            return
        else:
            self.depth_selected = self.depth[-1]
            self.sel_depth()
            self.plot_profile()

    def forward_in_depth(self):
        if self.depth_selected == self.depth[-1]:
            return
        else:
            index = np.where(self.depth == self.depth_selected)[0][0]
            self.depth_selected = self.depth[index + 1]
            self.sel_depth()
            self.plot_profile()

    def back_in_depth(self):
        if self.depth_selected == self.depth[0]:
            return
        else:
            index = np.where(self.depth == self.depth_selected)[0][0]
            self.depth_selected = self.depth[index - 1]
            self.sel_depth()
            self.plot_profile()

    def start_in_depth(self):
        if self.depth_selected == self.depth[0]:
            return
        else:
            self.depth_selected = self.depth[0]
            self.sel_depth()
            self.plot_profile()

    def play_temp_animation(self):
        self.var_selected = 'time'
        self.start_animation()

    def play_depth_animation(self):
        self.var_selected = 'depth'
        self.start_animation()

    def cls_components(self):
        self.pause_button_time.setChecked(False)
        self.pause_button_depth.setChecked(False)
        self.backward_button_time.setDisabled(True)
        self.start_button_time.setDisabled(True)
        self.play_button_time.setDisabled(True)
        self.forward_button_time.setDisabled(True)
        self.finish_button_time.setDisabled(True)
        self.start_button_depth.setDisabled(True)
        self.backward_button_depth.setDisabled(True)
        self.play_button_depth.setDisabled(True)
        self.forward_button_depth.setDisabled(True)
        self.finish_button_depth.setDisabled(True)
        self.SaveAnimationButton.setDisabled(True)
        self.SaveFigButton.setDisabled(True)
        self.frame.setDisabled(True)
        self.mainpage.frame.setDisabled(True)

    def opn_components(self):
        self.frame_buttons_animation_2_depth.setDisabled(False)
        self.frame_buttons_animation_time.setDisabled(False)
        self.backward_button_time.setDisabled(False)
        self.start_button_time.setDisabled(False)
        self.play_button_time.setDisabled(False)
        self.forward_button_time.setDisabled(False)
        self.finish_button_time.setDisabled(False)
        self.start_button_depth.setDisabled(False)
        self.backward_button_depth.setDisabled(False)
        self.play_button_depth.setDisabled(False)
        self.forward_button_depth.setDisabled(False)
        self.finish_button_depth.setDisabled(False)
        self.SaveAnimationButton.setDisabled(False)
        self.SaveFigButton.setDisabled(False)
        self.frame.setDisabled(False)
        self.mainpage.frame.setDisabled(False)

    def play_animation(self):
        if (self.var_selected == 'time' and self.time_selected == self.time[-1]) or (
                self.var_selected == 'depth' and self.depth_selected == self.time[-1]):
            return
        else:
            self.cls_components()

            if self.var_selected == 'time':
                self.frame_buttons_animation_2_depth.setDisabled(True)

                while True:
                    index = np.where(self.time == self.time_selected)[0][0]
                    self.time_selected = self.time[index + 1]
                    self.sel_time(self.time_selected)

                    self.plot_profile()

                    if self.pause_button_time.isChecked():
                        break
                    if self.time_selected >= self.time[-1]:
                        break

                    time.sleep(.2)
                    QApplication.processEvents()
            else:
                self.frame_buttons_animation_time.setDisabled(True)

                while True:
                    index = np.where(self.depth == self.depth_selected)[0][0]
                    self.depth_selected = self.depth[index + 1]
                    self.sel_depth()

                    self.plot_profile()

                    if self.pause_button_depth.isChecked():
                        break
                    if self.depth_selected >= self.depth[-1]:
                        break

                    time.sleep(.2)
                    QApplication.processEvents()

            self.opn_components()

    def plot_profile(self):
        dataset_filtered = self.dataset.sel(time=self.time_selected, depth=self.depth_selected)
        water_temp_filtered = dataset_filtered['salinity'].values
        self.im.set_data(water_temp_filtered)
        self.canvas.draw()

    def first_profile(self):
        self.figure.clear()
        self.canvas.draw()

        dataset_filtered = self.dataset.sel(time=self.time_selected, depth=self.depth_selected)
        lon, lat = self.dataset['lon'].values, self.dataset['lat'].values
        water_temp, water_temp_filtered = self.dataset['salinity'].values, dataset_filtered['salinity'].values

        min_value, max_value = np.nanmin(water_temp), np.nanmax(water_temp)
        cmap = cm.get_cmap('RdYlGn_r')
        norm = plt.Normalize(vmin=min_value, vmax=max_value)

        self.ax = self.figure.add_subplot(111)

        mp = Basemap(projection='merc',
                     llcrnrlon=min(lon),
                     llcrnrlat=min(lat),
                     urcrnrlon=max(lon),
                     urcrnrlat=max(lat),
                     resolution='i',
                     ax=self.ax)

        self.im = mp.imshow(water_temp_filtered, cmap=cmap, norm=norm)
        cbar = plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=self.ax, orientation='vertical', pad=0.05)
        cbar.set_label(f'{self.dataset['salinity'].units}', fontsize=6, color="white")
        cbar.ax.tick_params(labelsize=8)
        cbar.ax.yaxis.set_tick_params(color='white')
        plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='white')

        mp.drawcoastlines()
        mp.drawstates()
        mp.drawcountries()
        mp.fillcontinents(color='lightgreen', lake_color='lightblue')

        parallels = mp.drawparallels(np.arange(min(lat), max(lat), 3), labels=[1, 0, 0, 0], fontsize=6)
        meridians = mp.drawmeridians(np.arange(min(lon), max(lon), 3), labels=[0, 0, 0, 1], fontsize=6)

        for lat, text_objects in parallels.items():
            for text in text_objects[1]:
                text.set_color("white")

        for lon, text_objects in meridians.items():
            for text in text_objects[1]:
                text.set_color("white")

        self.ax.set_xlabel('Longitude', labelpad=15, fontsize=8)
        self.ax.set_ylabel('Latitude', labelpad=30, fontsize=8)
        self.ax.xaxis.label.set_color('white')
        self.ax.yaxis.label.set_color('white')
        self.ax.set_aspect('equal')

        self.canvas.draw()
        self.canvas.figure.subplots_adjust(
            top=0.975,
            bottom=0.116,
            left=0.124,
            right=0.97,
            hspace=0.2,
            wspace=0.2
        )
        self.canvas.figure.set_facecolor("#3d505f")

    def save_fig(self):
        dataset_filtered = self.dataset.sel(time=self.time_selected, depth=self.depth_selected)
        lon, lat = self.dataset['lon'].values, self.dataset['lat'].values
        salinity, salinity_filtered = self.dataset['salinity'].values, dataset_filtered['salinity'].values

        min_value, max_value = np.nanmin(salinity), np.nanmax(salinity)
        cmap = cm.get_cmap('RdYlGn_r')
        norm = plt.Normalize(vmin=min_value, vmax=max_value)

        fig, ax = plt.subplots(figsize=(14, 14), constrained_layout=True, facecolor=None)

        mp = Basemap(projection='merc',
                     llcrnrlon=min(lon),
                     llcrnrlat=min(lat),
                     urcrnrlon=max(lon),
                     urcrnrlat=max(lat),
                     resolution='i')

        mp.imshow(salinity_filtered, cmap=cmap, norm=norm)
        cbar = plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, orientation='vertical', pad=0.05)
        cbar.set_label(f'{self.dataset['salinity'].units}', fontsize=18)
        cbar.ax.tick_params(labelsize=16)

        mp.drawcoastlines()
        mp.drawstates()
        mp.drawcountries()
        mp.fillcontinents(color='lightgreen', lake_color='lightblue')

        mp.drawparallels(np.arange(min(lat), max(lat), 3), labels=[1, 0, 0, 0], fontsize=17)
        mp.drawmeridians(np.arange(min(lon), max(lon), 3), labels=[0, 0, 0, 1], fontsize=17)

        ax.set_xlabel('Longitude', labelpad=40, fontsize=18)
        ax.set_ylabel('Latitude', labelpad=55, fontsize=18)

        ax.set_aspect('equal')

        path_to_save = f'{self.mainpage.project.caminho}\\figs'
        os.makedirs(path_to_save, exist_ok=True)

        time_to_format = str(self.time_selected).split('.')[0]
        t_formated = datetime.strptime(time_to_format, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d-%Hh')

        plt.savefig(f'{path_to_save}\\SalinityMap_{t_formated}_{self.depth_selected}m.png', transparent=True)
        plt.close()

    def save_anim(self):
        self.mainpage.centralwidget.setDisabled(True)
        QApplication.processEvents()

        salinity = self.dataset['salinity'].values
        min_value, max_value = np.nanmin(salinity), np.nanmax(salinity)
        cmap = cm.get_cmap('RdYlGn_r')
        norm = plt.Normalize(vmin=min_value, vmax=max_value)

        lon, lat = self.dataset['lon'].values, self.dataset['lat'].values

        time = list(self.dataset.time.values)

        def update(frame):
            if frame == 0:
                return

            data = self.dataset.salinity.sel(time=time[frame], depth=self.depth_selected)

            axs.cla()

            mp = Basemap(projection='merc',
                         llcrnrlon=min(lon),
                         llcrnrlat=min(lat),
                         urcrnrlon=max(lon),
                         urcrnrlat=max(lat),
                         resolution='i')

            mp.imshow(data, cmap=cmap, norm=norm)

            mp.drawcoastlines()
            mp.drawstates()
            mp.drawcountries()
            mp.fillcontinents(color='lightgreen', lake_color='lightblue')

            mp.drawparallels(np.arange(min(lat), max(lat), 3), labels=[1, 0, 0, 0], fontsize=17)
            mp.drawmeridians(np.arange(min(lon), max(lon), 3), labels=[0, 0, 0, 1], fontsize=17)

            axs.set_xlabel('Longitude', labelpad=40, fontsize=18)
            axs.set_ylabel('Latitude', labelpad=55, fontsize=18)

            axs.set_aspect('equal')

        fig = plt.figure(figsize=(12, 12))
        subfigs = fig.subfigures(1, 1)
        axs = subfigs.subplots(1, 1)

        cbar = fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=axs, orientation='vertical', pad=0.05)
        cbar.set_label(f'{self.dataset['salinity'].units}', fontsize=18)
        cbar.ax.tick_params(labelsize=16)

        ani = FuncAnimation(fig, update, frames=len(time) - 1, interval=1000)

        path_to_save = f'{self.mainpage.project.caminho}\\figs'
        os.makedirs(path_to_save, exist_ok=True)

        ani.save(f'{path_to_save}\\animacao_salinitymap_{self.var_selected}.gif', writer='pillow', fps=3)
        plt.close()
        print('Finish')

    def start_animation(self):
        self.worker = AnimationWorker(page=self)
        self.worker.start()

    def retranslateUi(self, WindButton_LonLatProfile):
        WindButton_LonLatProfile.setWindowTitle(QCoreApplication.translate("WindButton_LonLatProfile", u"Form", None))
        self.TimeFilterLabel.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"Time Filter", None))
        self.start_button_time.setText("")
        self.backward_button_time.setText("")
        self.pause_button_time.setText("")
        self.play_button_time.setText("")
        self.forward_button_time.setText("")
        self.finish_button_time.setText("")
        self.DepthFilterLabel.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"Depth Filter", None))
        self.start_button_depth.setText("")
        self.backward_button_depth.setText("")
        self.pause_button_depth.setText("")
        self.play_button_depth.setText("")
        self.forward_button_depth.setText("")
        self.finish_button_depth.setText("")
        self.SaveFigButton.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"SAVE FIGURE", None))
        self.SaveAnimationButton.setText(
            QCoreApplication.translate("WindButton_LonLatProfile", u"SAVE ANIMATION", None))
    # retranslateUi
