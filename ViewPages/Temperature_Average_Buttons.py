from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import os


class Ui_WindButton_LonLatProfile(object):
    def setupUi(self, page, WindButton_LonLatProfile, dataset, variables):
        if not WindButton_LonLatProfile.objectName():
            WindButton_LonLatProfile.setObjectName(u"WindButton_LonLatProfile")
        WindButton_LonLatProfile.resize(546, 436)

        self.mainpage = page
        self.dataset = dataset
        self.temp_name = variables['temperature']
        self.time_name = variables['time']
        self.depth_name = variables['depth']
        self.lon_name, self.lat_name = variables['longitude'], variables['latitude']

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
        self.start_button_time.clicked.connect(self.start_in_time)

        self.gridLayout_7.addWidget(self.start_button_time, 0, 0, 1, 1)

        self.backward_button_time = QPushButton(self.frame_buttons_animation_time)
        self.backward_button_time.setObjectName(u"backward_button_time")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/arrow-left - laranja.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backward_button_time.setIcon(icon1)
        self.backward_button_time.setIconSize(QSize(20, 20))
        self.backward_button_time.clicked.connect(self.back_in_time)

        self.gridLayout_7.addWidget(self.backward_button_time, 0, 1, 1, 1)

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
            self.lat = [lat_value for lat_value in self.dataset[self.lat_name].values]
            self.lon = [lon_value for lon_value in self.dataset[self.lon_name].values]
            self.time = self.dataset[self.time_name].values
            self.time_selected = self.time[0]
            self.sel_time(self.time_selected)
            self.plot_graph()
        except Exception as e:
            raise e

    def sel_time(self, value_time):
        time_to_format = str(value_time).split('.')[0]
        t_formated = datetime.strptime(time_to_format, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d-%Hh')
        self.TimeValueLabel.setText(f'{t_formated}')

    def last_in_time(self):
        if self.time_selected == self.time[-1]:
            return
        else:
            self.time_selected = self.time[-1]
            self.sel_time(self.time_selected)
            self.plot_graph()

    def start_in_time(self):
        if self.time_selected == self.time[0]:
            return
        else:
            self.time_selected = self.time[0]
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

    def plot_graph(self):
        self.figure.clear()
        self.canvas.draw()

        dict_to_sel_ds = {
            self.time_name: self.time_selected
        }

        dataset = self.dataset[self.temp_name].sel(dict_to_sel_ds)

        ax = self.figure.add_subplot(111)

        depth = [dpt for dpt in dataset[self.depth_name].values][::-1]
        variable_x = [np.nanmean(dataset.sel({self.depth_name: d}).values) for d in depth]

        x_values = np.arange(min(variable_x), max(variable_x), 0.5) if max(variable_x) - min(variable_x) <= 10 \
            else np.arange(min(variable_x), max(variable_x), 2)

        ax.plot(variable_x, depth)
        ax.set_xticks(x_values)
        ax.set_xlabel(f'Temperatura [{dataset.units}]', labelpad=5, fontsize=8, color='white')

        ax.set_ylabel(f'Depth [{dataset[self.depth_name].units}]', labelpad=5, fontsize=8, color='white')
        ax.grid()
        ax.tick_params(axis='both', which='major', labelsize=7, color='white', labelcolor='white')
        self.figure.figure.gca().invert_yaxis()

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
        dataset = self.dataset[self.temp_name].sel({self.time_name: self.time_selected})
        fig, ax = plt.subplots(figsize=(14, 14), constrained_layout=True, facecolor=None)

        depth = [dpt for dpt in dataset[self.depth_name].values][::-1]
        variable_x = [np.nanmean(dataset.sel({self.depth_name: d}).values) for d in depth]

        x_values = np.arange(min(variable_x), max(variable_x), 0.5) if max(variable_x) - min(variable_x) <= 10 \
            else np.arange(min(variable_x), max(variable_x), 2)

        ax.plot(variable_x, depth)
        ax.set_xticks(x_values)
        ax.set_xlabel(f'Temperatura [{dataset.units}]', labelpad=20, fontsize=18)

        ax.set_ylabel(f'Depth [{dataset[self.depth_name].units}]', labelpad=20, fontsize=18)
        plt.grid()
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.gca().invert_yaxis()

        path_to_save = f'{self.mainpage.project.caminho}\\figs'
        os.makedirs(path_to_save, exist_ok=True)

        time_to_format = str(self.time_selected).split('.')[0]
        t_formated = datetime.strptime(time_to_format, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d-%Hh')

        plt.savefig(f'{path_to_save}\\AverageTemperature_{t_formated}.png', transparent=True)
        plt.close()

    def retranslateUi(self, WindButton_LonLatProfile):
        WindButton_LonLatProfile.setWindowTitle(QCoreApplication.translate("WindButton_LonLatProfile", u"Form", None))
        self.TimeFilterLabel.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"Time Filter", None))
        self.start_button_time.setText("")
        self.backward_button_time.setText("")
        self.forward_button_time.setText("")
        self.finish_button_time.setText("")
        self.SaveFigButton.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"SAVE FIGURE", None))
