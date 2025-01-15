from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt, QThread)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout)
from ViewPages import ColorEscale as Cs
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import time
from datetime import datetime
import os


class AnimationWorker(QThread):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def run(self):
        self.page.play_animation()


class CustomNavigationToolbar(NavigationToolbar):
    def __init__(self, canvas, parent=None):
        super().__init__(canvas, parent)

        # Set transparent background
        self.setStyleSheet("QToolBar { background: transparent; }")

        # Replace default black icons with white versions
        self.update_icons()

    def update_icons(self):
        # White versions of icons (you need to have these available or generate them)
        icon_paths = {
            'home': 'icons/home_white.png',
            'back': 'icons/back_white.png',
            'forward': 'icons/forward_white.png',
            'pan': 'icons/pan_white.png',
            'zoom': 'icons/zoom_white.png',
            'save': 'icons/save_white.png'
        }

        # Update icons
        actions = self.actions()
        for action in actions:
            text = action.text().lower()
            for key, path in icon_paths.items():
                if key in text and path:  # Match action name to icon
                    action.setIcon(QIcon(path))


class Ui_WindButton_LonLatProfile(object):
    def setupUi(self, page, WindButton_LonLatProfile, dataset, variables):  # , page
        if not WindButton_LonLatProfile.objectName():
            WindButton_LonLatProfile.setObjectName(u"WindButton_LonLatProfile")
        WindButton_LonLatProfile.resize(546, 436)

        self.mainpage = page
        self.dataset = dataset
        self.u_name, self.v_name = variables['u'], variables['v']
        self.time_name = variables['time']
        self.lon_name, self.lat_name = variables['longitude'], variables['latitude']

        self.horizontalLayout = QHBoxLayout(WindButton_LonLatProfile)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(WindButton_LonLatProfile)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.hori_frame = QHBoxLayout(self.frame)

        self.verticalLayout_ScaleButton = QVBoxLayout()
        self.verticalLayout_ScaleButton.setAlignment(Qt.AlignmentFlag.AlignBottom)

        self.ColorScaleButton = QPushButton()
        self.ColorScaleButton.setObjectName(u"ColorScale")
        self.ColorScaleButton.setMinimumSize(QSize(100, 30))
        self.ColorScaleButton.setMaximumSize(QSize(100, 30))
        self.ColorScaleButton.setStyleSheet(u"QPushButton{\n"
                                            "	background-color: rgb(61, 80, 95);\n"
                                            "	border-radius: 15px;\n"
                                            "	border: 2px solid #F98600;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "	color: #F98600;\n"
                                            "	font-size: 14px;\n"
                                            "}")
        self.ColorScaleButton.clicked.connect(self.open_color_scale_widget)

        self.verticalLayout_ScaleButton.addWidget(self.ColorScaleButton)
        self.hori_frame.addLayout(self.verticalLayout_ScaleButton)

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
        self.play_button_time.clicked.connect(self.start_animation)

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
        self.TimeValueLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.TimeValueLabel)

        self.horizontalLayout_7.addLayout(self.verticalLayout_13)

        self.horizontalSpacer_35 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_35)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_38 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_38)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.StepFilterLabel = QLabel(self.frame_2)
        self.StepFilterLabel.setObjectName(u"StepFilterLabel")
        self.StepFilterLabel.setMinimumSize(QSize(180, 22))
        self.StepFilterLabel.setMaximumSize(QSize(180, 22))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.StepFilterLabel.setFont(font1)

        self.verticalLayout_15.addWidget(self.StepFilterLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_32 = QSpacerItem(18, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_32)

        self.frame_buttons_animation_step = QFrame(self.frame_2)
        self.frame_buttons_animation_step.setObjectName(u"frame_buttons_animation_step")
        self.frame_buttons_animation_step.setMinimumSize(QSize(80, 50))
        self.frame_buttons_animation_step.setMaximumSize(QSize(80, 50))
        self.frame_buttons_animation_step.setStyleSheet(u"QPushButton {\n"
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
        self.frame_buttons_animation_step.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_buttons_animation_step.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_buttons_animation_step)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.backward_button_step = QPushButton(self.frame_buttons_animation_step)
        self.backward_button_step.setObjectName(u"backward_button_step")
        self.backward_button_step.setIcon(icon1)
        self.backward_button_step.setIconSize(QSize(20, 20))
        self.backward_button_step.clicked.connect(self.back_in_step)

        self.gridLayout_9.addWidget(self.backward_button_step, 0, 0, 1, 1)

        self.forward_button_step = QPushButton(self.frame_buttons_animation_step)
        self.forward_button_step.setObjectName(u"forward_button_step")
        self.forward_button_step.setIcon(icon4)
        self.forward_button_step.setIconSize(QSize(20, 20))
        self.forward_button_step.clicked.connect(self.forward_in_step)

        self.gridLayout_9.addWidget(self.forward_button_step, 0, 1, 1, 1)

        self.horizontalLayout_2.addWidget(self.frame_buttons_animation_step)

        self.horizontalSpacer_33 = QSpacerItem(18, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_33)

        self.verticalLayout_15.addLayout(self.horizontalLayout_2)

        self.StepValueLabel = QLabel(self.frame_2)
        self.StepValueLabel.setObjectName(u"StepValueLabel")
        self.StepValueLabel.setMinimumSize(QSize(180, 22))
        self.StepValueLabel.setMaximumSize(QSize(180, 22))
        self.StepValueLabel.setStyleSheet(u"border: 2px solid #212b33")
        self.StepValueLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.StepValueLabel)

        self.horizontalLayout_14.addLayout(self.verticalLayout_15)

        self.horizontalSpacer_39 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_39)

        self.verticalLayout.addLayout(self.horizontalLayout_14)

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
        self.SaveFigButton.clicked.connect(self.save_figure)

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
        self.SaveAnimationButton.clicked.connect(self.save_animation)

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

        self.graph_num = QVBoxLayout()
        self.graph_num.setSpacing(5)
        self.graph_num.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vecmean = Figure(figsize=(2, 2))
        self.canvasmean = FigureCanvas(self.vecmean)
        self.graph_num.addWidget(self.canvasmean, alignment=Qt.AlignmentFlag.AlignCenter)

        self.meanvectorlabel = QLabel(self.frame)
        self.meanvectorlabel.setObjectName(u"AverageWindDirection")
        self.meanvectorlabel.setMinimumSize(QSize(180, 22))
        self.meanvectorlabel.setMaximumSize(QSize(180, 22))
        self.meanvectorlabel.setStyleSheet(u"border: 2px solid #212b33")
        self.meanvectorlabel.setText(u"Average Wind Direction")
        self.meanvectorlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.graph_num.addWidget(self.meanvectorlabel, alignment=Qt.AlignmentFlag.AlignCenter)

        # Adicionar os dois layouts verticais ao layout horizontal principal
        self.hori_frame.addLayout(self.graph_layout)
        self.hori_frame.addLayout(self.graph_num)

        self.frame.setLayout(self.hori_frame)

        try:
            self.f_magnitude = lambda x_, y_: np.sqrt(x_ ** 2 + y_ ** 2)
            self.lat = [lat_value for lat_value in self.dataset[self.lat_name].values]
            self.lon = [lon_value for lon_value in self.dataset[self.lon_name].values]
            self.time = self.dataset[self.time_name].values
            self.time_selected = self.time[0]
            self.sel_time(self.time_selected)
            self.step = 1
            self.last_step = self.step
            self.sel_step(self.step)
            self.color_scale_widget = None
            self.current_min, self.current_max = self.set_magvector()
            self.current_scale = "RdYlGn_r"
            self.plot_first_graph()
            self.plot_first_average()
        except Exception as e:
            raise e

    def sel_time(self, value_time):
        time_to_format = str(value_time).split('.')[0]
        t_formated = datetime.strptime(time_to_format, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d-%Hh')
        self.TimeValueLabel.setText(f'{t_formated}')

    def sel_step(self, value_step):
        self.StepValueLabel.setText(f'{value_step}')

    def plot_graph(self):
        self.plot_vec_wind()
        self.plot_average_vec_wind()

    def cls_components(self):
        self.pause_button_time.setChecked(False)
        self.frame_buttons_animation_step.setDisabled(True)
        self.start_button_time.setDisabled(True)
        self.backward_button_time.setDisabled(True)
        self.play_button_time.setDisabled(True)
        self.forward_button_time.setDisabled(True)
        self.finish_button_time.setDisabled(True)
        self.SaveAnimationButton.setDisabled(True)
        self.SaveFigButton.setDisabled(True)
        self.frame.setDisabled(True)
        self.mainpage.frame.setDisabled(True)

    def opn_components(self):
        self.frame_buttons_animation_step.setDisabled(False)
        self.start_button_time.setDisabled(False)
        self.backward_button_time.setDisabled(False)
        self.play_button_time.setDisabled(False)
        self.forward_button_time.setDisabled(False)
        self.finish_button_time.setDisabled(False)
        self.SaveAnimationButton.setDisabled(False)
        self.SaveFigButton.setDisabled(False)
        self.frame.setDisabled(False)
        self.mainpage.frame.setDisabled(False)

    def play_animation(self):
        if self.time_selected == self.time[-1]:
            return
        else:
            self.cls_components()

            while True:
                index = np.where(self.time == self.time_selected)[0][0]
                self.time_selected = self.time[index + 1]
                self.sel_time(self.time_selected)

                self.plot_graph()

                if self.pause_button_time.isChecked():
                    break
                if self.time_selected >= self.time[-1]:
                    break

                time.sleep(.2)
                QApplication.processEvents()

            self.opn_components()

    def forward_in_step(self):
        max_step = min(len(self.lat), len(self.lon)) - 1
        if self.step == max_step:
            return
        else:
            self.step += 1
            self.sel_step(self.step)
            self.plot_graph()

    def back_in_step(self):
        if self.step == 1:
            return
        else:
            self.step -= 1
            self.sel_step(self.step)
            self.plot_graph()

    def firts_in_time(self):
        if self.time_selected == self.time[0]:
            return
        else:
            self.time_selected = self.time[0]
            self.sel_time(self.time_selected)
            self.plot_graph()

    def last_in_time(self):
        if self.time_selected == self.time[-1]:
            return
        else:
            self.time_selected = self.time[-1]
            self.sel_time(self.time_selected)
            self.plot_graph()

    def forward_in_time(self):
        if self.time_selected == self.time[-1]:
            return
        else:
            index = np.where(self.time == self.time_selected)[0][0]
            self.time_selected = self.time[index + 1]
            self.sel_time(self.time_selected)
            self.plot_graph()

    def back_in_time(self):
        if self.time_selected == self.time[0]:
            return
        else:
            index = np.where(self.time == self.time_selected)[0][0]
            self.time_selected = self.time[index - 1]
            self.sel_time(self.time_selected)
            self.plot_graph()

    def open_color_scale_widget(self):
        if self.color_scale_widget is None:
            self.color_scale_widget = Cs.ColorScaleWidget(self.current_scale)

        self.color_scale_widget.scale_updated.connect(self.update_color_scale)
        self.color_scale_widget.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.color_scale_widget.setWindowFlag(Qt.WindowType.Window)
        self.color_scale_widget.show()

    def update_color_scale(self, min_value, max_value, scale):
        self.current_min = min_value
        self.current_max = max_value
        self.current_scale = scale
        self.plot_first_graph()
        self.plot_average_vec_wind()
        self.color_scale_widget.close()

    def set_magvector(self):
        u_mag = self.dataset[self.u_name].values[:, ::self.step, ::self.step]
        v_mag = self.dataset[self.v_name].values[:, ::self.step, ::self.step]
        mag = [self.f_magnitude(u_mag[t, :, :], v_mag[t, :, :]) for t in range(len(self.dataset[self.time_name]))]
        magnitude_min = np.nanmin(mag)
        magnitude_max = np.nanmax(mag)
        if magnitude_max == magnitude_min:
            magnitude_max += 1e-6
        return magnitude_min, magnitude_max

    def plot_average_vec_wind(self):
        dict_to_sel = {
            self.time_name: self.time_selected
        }
        u = self.dataset[self.u_name].sel(dict_to_sel).values
        v = self.dataset[self.v_name].sel(dict_to_sel).values

        u_mean = np.nanmean(u)
        v_mean = np.nanmean(v)

        mag = np.sqrt(u_mean ** 2 + v_mean ** 2)
        desired_mag = 4
        if mag != 0:
            scale = desired_mag / mag
            u_mean *= scale
            v_mean *= scale

        self.arrow.remove()
        self.arrow = self.ax_aver.arrow(0, 0, u_mean, v_mean, head_width=0.5, head_length=0.5, fc='white', ec='white')
        self.canvasmean.draw()

    def plot_first_average(self):
        self.vecmean.clear()
        self.canvasmean.draw()

        dict_to_sel = {
            self.time_name: self.time_selected
        }
        u = self.dataset[self.u_name].sel(dict_to_sel).values
        v = self.dataset[self.v_name].sel(dict_to_sel).values

        u_mean = np.nanmean(u)
        v_mean = np.nanmean(v)

        mag = np.sqrt(u_mean ** 2 + v_mean ** 2)
        desired_mag = 4
        if mag != 0:
            scale = desired_mag / mag
            u_mean *= scale
            v_mean *= scale

        self.ax_aver = self.vecmean.add_subplot(111)

        self.arrow = self.ax_aver.arrow(0, 0, u_mean, v_mean, head_width=0.5, head_length=0.5, fc='white', ec='white')

        self.ax_aver.text(0, 5.2, "N", fontsize=12, ha='center', color='white')
        self.ax_aver.text(5.2, 0, "E", fontsize=12, va='center', color='white')
        self.ax_aver.text(0, -6, "S", fontsize=12, ha='center', color='white')
        self.ax_aver.text(-6.2, 0, "W", fontsize=12, va='center', color='white')

        self.ax_aver.set_xlim(-5, 5)
        self.ax_aver.set_ylim(-5, 5)
        self.ax_aver.axhline(0, color='white', lw=0.5)
        self.ax_aver.axvline(0, color='white', lw=0.5)
        self.ax_aver.set_aspect('equal', adjustable='box')

        self.ax_aver.axis('off')

        self.canvasmean.draw()
        self.canvasmean.figure.set_facecolor("#3d505f")


    def plot_vec_wind(self):
        if self.last_step != self.step:
            self.plot_first_graph()
        else:
            dict_to_sel = {
                self.time_name: self.time_selected
            }
            u_plot = self.dataset[self.u_name].sel(dict_to_sel).values[::self.step, ::self.step]
            v_plot = self.dataset[self.v_name].sel(dict_to_sel).values[::self.step, ::self.step]

            lon_plot, lat_plot = self.lons[::self.step, ::self.step], self.lats[::self.step, ::self.step]
            x, y = self.mp(lon_plot, lat_plot)

            xx = x.flatten()
            yy = y.flatten()
            new_position = list(zip(xx, yy))

            self.quiver.X = xx
            self.quiver.Y = yy
            self.quiver.XY = new_position
            self.quiver.N = len(xx)

            vec_mag = self.f_magnitude(u_plot, v_plot)
            u_norm = u_plot / vec_mag
            v_norm = v_plot / vec_mag

            cmap = cm.get_cmap(self.current_scale)
            norm = plt.Normalize(vmin=self.current_min, vmax=self.current_max)
            colors_ = cmap(norm(vec_mag))
            colors_ = colors_.reshape(-1, 4)

            self.quiver.set_UVC(u_norm, v_norm)
            self.quiver.set_color(colors_)

            self.canvas.draw()

    def plot_first_graph(self):
        self.figure.clear()
        self.canvas.draw()

        lon = self.dataset[self.lon_name].values
        lat = self.dataset[self.lat_name].values

        self.ax_vec = self.figure.add_subplot(111)

        dict_to_sel = {
            self.time_name: self.time_selected
        }

        u_plot = self.dataset[self.u_name].sel(dict_to_sel).values[::self.step, ::self.step]
        v_plot = self.dataset[self.v_name].sel(dict_to_sel).values[::self.step, ::self.step]

        self.lons, self.lats = np.meshgrid(lon, lat)
        lon_plot, lat_plot = self.lons[::self.step, ::self.step], self.lats[::self.step, ::self.step]

        self.mp = Basemap(projection='merc',
                     llcrnrlon=min(lon),
                     llcrnrlat=min(lat),
                     urcrnrlon=max(lon),
                     urcrnrlat=max(lat),
                     resolution='i',
                     ax=self.ax_vec)

        x, y = self.mp(lon_plot, lat_plot)

        vec_mag = self.f_magnitude(u_plot, v_plot)
        u_norm = u_plot / vec_mag
        v_norm = v_plot / vec_mag

        cmap = cm.get_cmap(self.current_scale)
        norm = plt.Normalize(vmin=self.current_min, vmax=self.current_max)
        colors = cmap(norm(vec_mag))
        colors = colors.reshape(-1, 4)

        self.quiver = self.mp.quiver(x, y, u_norm[::-1], v_norm[::-1], color=colors, scale=30)
        cbar = plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=self.ax_vec, orientation='vertical', pad=0.05)
        cbar.set_label(f'Magnitude dos Vetores [{self.dataset[self.u_name].attrs['units']}]', fontsize=6, color="white")
        cbar.ax.tick_params(labelsize=8)
        cbar.ax.yaxis.set_tick_params(color='white')
        plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='white')

        self.mp.drawcoastlines()
        self.mp.drawstates()
        self.mp.drawcountries()

        lat_label_step = (max(lat) - min(lat)) // 3 if (max(lat) - min(lat)) > 3 else 3
        lon_label_step = (max(lon) - min(lon)) // 3 if (max(lon) - min(lon)) > 3 else 3

        parallels = self.mp.drawparallels(np.arange(min(lat), max(lat), lat_label_step), labels=[1, 0, 0, 0], fontsize=6)
        meridians = self.mp.drawmeridians(np.arange(min(lon), max(lon), lon_label_step), labels=[0, 0, 0, 1], fontsize=6)

        for lat, text_objects in parallels.items():
            for text in text_objects[1]:
                text.set_color("white")

        for lon, text_objects in meridians.items():
            for text in text_objects[1]:
                text.set_color("white")

        self.ax_vec.set_xlabel('Longitude', labelpad=15, fontsize=8)
        self.ax_vec.set_ylabel('Latitude', labelpad=30, fontsize=8)
        self.ax_vec.set_aspect('equal', adjustable='box')
        self.ax_vec.xaxis.label.set_color('white')
        self.ax_vec.yaxis.label.set_color('white')

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
        self.last_step = self.step

    def save_figure(self):
        lon = self.dataset[self.lon_name].values
        lat = self.dataset[self.lat_name].values

        fig, ax = plt.subplots(figsize=(14, 14), constrained_layout=True, facecolor=None)

        dict_to_sel = {
            self.time_name: self.time_selected
        }

        u_plot = self.dataset[self.u_name].sel(dict_to_sel).values[::self.step, ::self.step]
        v_plot = self.dataset[self.v_name].sel(dict_to_sel).values[::self.step, ::self.step]

        lons, lats = np.meshgrid(lon, lat)
        lon_plot, lat_plot = lons[::self.step, ::self.step], lats[::self.step, ::self.step]

        mp = Basemap(projection='merc',
                     llcrnrlon=min(lon),
                     llcrnrlat=min(lat),
                     urcrnrlon=max(lon),
                     urcrnrlat=max(lat),
                     resolution='i')

        x, y = mp(lon_plot, lat_plot)

        vec_mag = self.f_magnitude(u_plot, v_plot)
        u_norm = u_plot / vec_mag
        v_norm = v_plot / vec_mag

        cmap = cm.get_cmap(self.current_scale)
        norm = plt.Normalize(vmin=self.current_min, vmax=self.current_max)
        colors = cmap(norm(vec_mag))
        colors = colors.reshape(-1, 4)

        mp.quiver(x, y, u_norm[::-1], v_norm[::-1], color=colors, scale=30)
        cbar = plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, orientation='vertical', pad=0.05)
        cbar.set_label(f'Magnitude dos Vetores [{self.dataset[self.u_name].attrs['units']}]', fontsize=18)
        cbar.ax.tick_params(labelsize=16)

        mp.drawcoastlines()
        mp.drawstates()
        mp.drawcountries()

        mp.drawparallels(np.arange(min(lat), max(lat), 3), labels=[1, 0, 0, 0], fontsize=17)
        mp.drawmeridians(np.arange(min(lon), max(lon), 3), labels=[0, 0, 0, 1], fontsize=17)

        plt.title(f'Wind data - {str(self.time_selected)[:-16]}')
        ax.set_xlabel('Longitude', labelpad=40, fontsize=18)
        ax.set_ylabel('Latitude', labelpad=55, fontsize=18)

        path_to_save = f'{self.mainpage.project.caminho}\\figs'
        os.makedirs(path_to_save, exist_ok=True)

        time_to_format = str(self.time_selected).split('.')[0]
        t_formated = datetime.strptime(time_to_format, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d-%Hh')

        plt.savefig(f'{path_to_save}\\{t_formated}.png', transparent=True)

    def save_animation(self):
        self.mainpage.centralwidget.setDisabled(True)
        QApplication.processEvents()

        time = list(self.dataset[self.time_name].values)

        def update(frame):
            if frame == 0:
                return

            dict_to_sel = {
                self.time_name: time[frame]
            }

            data_wind = self.dataset.sel(dict_to_sel)

            axs.cla()

            lon = data_wind[self.lon_name].values
            lat = data_wind[self.lat_name].values

            u_plot = data_wind[self.u_name].values[::self.step, ::self.step]
            v_plot = data_wind[self.v_name].values[::self.step, ::self.step]

            lons, lats = np.meshgrid(lon, lat)
            lon_plot, lat_plot = lons[::self.step, ::self.step], lats[::self.step, ::self.step]

            mp = Basemap(projection='merc',
                         llcrnrlon=min(lon),
                         llcrnrlat=min(lat),
                         urcrnrlon=max(lon),
                         urcrnrlat=max(lat),
                         resolution='i',
                         ax=axs)

            x, y = mp(lon_plot, lat_plot)

            vec_mag = self.f_magnitude(u_plot, v_plot)
            u_norm = u_plot / vec_mag
            v_norm = v_plot / vec_mag

            colors = cmap(norm(vec_mag))
            colors = colors.reshape(-1, 4)

            mp.quiver(x, y, u_norm[::-1], v_norm[::-1], color=colors, scale=30)

            mp.drawcoastlines()
            mp.drawstates()
            mp.drawcountries()

            mp.drawparallels(np.arange(min(lat), max(lat), 3), labels=[1, 0, 0, 0], fontsize=17)
            mp.drawmeridians(np.arange(min(lon), max(lon), 3), labels=[0, 0, 0, 1], fontsize=17)

            axs.set_xlabel('Longitude', labelpad=40, fontsize=18)
            axs.set_ylabel('Latitude', labelpad=55, fontsize=18)

        fig = plt.figure(figsize=(12, 12))
        subfigs = fig.subfigures(1, 1)
        axs = subfigs.subplots(1, 1)

        cmap = cm.get_cmap(self.current_scale)
        norm = plt.Normalize(vmin=self.current_min, vmax=self.current_max)

        cbar = fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=axs, orientation='vertical', pad=0.05)
        cbar.set_label(f'Magnitude dos Vetores [{self.dataset[self.u_name].attrs['units']}]', fontsize=18)
        cbar.ax.tick_params(labelsize=16)

        ani = FuncAnimation(fig, update, frames=len(time) - 1, interval=1000)

        path_to_save = f'{self.mainpage.project.caminho}\\figs'
        os.makedirs(path_to_save, exist_ok=True)

        ani.save(f'{path_to_save}\\animacao_dataframe.gif', writer='pillow', fps=3)
        plt.close()

        self.mainpage.centralwidget.setDisabled(False)

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
        self.StepFilterLabel.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"Step Filter", None))
        self.backward_button_step.setText("")
        self.forward_button_step.setText("")
        self.SaveFigButton.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"Save Figure", None))
        self.SaveAnimationButton.setText(
            QCoreApplication.translate("WindButton_LonLatProfile", u"Save Animation", None))
        self.ColorScaleButton.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"Set Color Scale", None))

