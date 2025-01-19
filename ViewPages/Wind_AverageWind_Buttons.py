from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout)
from ViewPages import ColorEscale as Cs
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib import colors
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame as Df
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
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.StepFilterLabel.setFont(font)

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
        icon = QIcon()
        icon.addFile(u":/icons/icons/arrow-left - laranja.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backward_button_step.setIcon(icon)
        self.backward_button_step.setIconSize(QSize(20, 20))
        self.backward_button_step.clicked.connect(self.back_in_year)

        self.gridLayout_9.addWidget(self.backward_button_step, 0, 0, 1, 1)

        self.forward_button_step = QPushButton(self.frame_buttons_animation_step)
        self.forward_button_step.setObjectName(u"forward_button_step")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/arrow-right - laranja.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.forward_button_step.setIcon(icon1)
        self.forward_button_step.setIconSize(QSize(20, 20))
        self.forward_button_step.clicked.connect(self.forward_in_year)

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

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_42 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_42)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.StepFilterLabel_2 = QLabel(self.frame_2)
        self.StepFilterLabel_2.setObjectName(u"StepFilterLabel_2")
        self.StepFilterLabel_2.setMinimumSize(QSize(180, 22))
        self.StepFilterLabel_2.setMaximumSize(QSize(180, 22))
        self.StepFilterLabel_2.setFont(font)

        self.verticalLayout_16.addWidget(self.StepFilterLabel_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_34 = QSpacerItem(18, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_34)

        self.frame_buttons_animation_step_2 = QFrame(self.frame_2)
        self.frame_buttons_animation_step_2.setObjectName(u"frame_buttons_animation_step_2")
        self.frame_buttons_animation_step_2.setMinimumSize(QSize(80, 50))
        self.frame_buttons_animation_step_2.setMaximumSize(QSize(80, 50))
        self.frame_buttons_animation_step_2.setStyleSheet(u"QPushButton {\n"
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
        self.frame_buttons_animation_step_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_buttons_animation_step_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_buttons_animation_step_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.backward_button_step_2 = QPushButton(self.frame_buttons_animation_step_2)
        self.backward_button_step_2.setObjectName(u"backward_button_step_2")
        self.backward_button_step_2.setIcon(icon)
        self.backward_button_step_2.setIconSize(QSize(20, 20))
        self.backward_button_step_2.clicked.connect(self.back_in_month)

        self.gridLayout_10.addWidget(self.backward_button_step_2, 0, 0, 1, 1)

        self.forward_button_step_2 = QPushButton(self.frame_buttons_animation_step_2)
        self.forward_button_step_2.setObjectName(u"forward_button_step_2")
        self.forward_button_step_2.setIcon(icon1)
        self.forward_button_step_2.setIconSize(QSize(20, 20))
        self.forward_button_step_2.clicked.connect(self.forward_in_month)

        self.gridLayout_10.addWidget(self.forward_button_step_2, 0, 1, 1, 1)

        self.horizontalLayout_3.addWidget(self.frame_buttons_animation_step_2)

        self.horizontalSpacer_35 = QSpacerItem(18, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_35)

        self.verticalLayout_16.addLayout(self.horizontalLayout_3)

        self.StepValueLabel_2 = QLabel(self.frame_2)
        self.StepValueLabel_2.setObjectName(u"StepValueLabel_2")
        self.StepValueLabel_2.setMinimumSize(QSize(180, 22))
        self.StepValueLabel_2.setMaximumSize(QSize(180, 22))
        self.StepValueLabel_2.setStyleSheet(u"border: 2px solid #212b33")
        self.StepValueLabel_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.StepValueLabel_2)

        self.horizontalLayout_16.addLayout(self.verticalLayout_16)

        self.horizontalSpacer_43 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_43)

        self.verticalLayout.addLayout(self.horizontalLayout_16)

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
        self.SaveFigButton.clicked.connect(self.save_gif)

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

        self.hori_frame.addLayout(self.graph_layout)

        self.frame.setLayout(self.hori_frame)

        try:
            self.f_magnitude = lambda x_, y_: np.sqrt(x_ ** 2 + y_ ** 2)
            self.lat = [lat_value for lat_value in self.dataset[self.lat_name].values]
            self.lon = [lon_value for lon_value in self.dataset[self.lon_name].values]
            self.ucomponent = self.dataset[self.u_name].values
            self.vcomponent = self.dataset[self.v_name].values
            self.time = self.dataset[self.time_name].values
            self.year = list(np.unique(self.dataset[self.time_name].dt.year.values))
            self.year_selected = self.year[0]
            self.month = self.get_months_for_year()
            self.month_selected = self.month[0]
            self.sel_year()
            self.sel_month()
            self.color_scale_widget = None
            self.current_min, self.current_max = self.set_magvector()
            self.current_scale = "RdYlGn_r"
            self.plot_average_wind()
        except Exception as e:
            raise e

    def sel_month(self):
        self.StepValueLabel_2.setText(f'{self.month_selected}')

    def sel_year(self):
        self.StepValueLabel.setText(f'{self.year_selected}')

    def forward_in_month(self):
        if self.month_selected == self.month[-1]:
            return
        else:
            index = self.month.index(self.month_selected)
            self.month_selected = self.month[index + 1]
            self.sel_month()
            self.plot_average_wind()

    def back_in_month(self):
        if self.month_selected == self.month[0]:
            return
        else:
            index = self.month.index(self.month_selected)
            self.month_selected = self.month[index - 1]
            self.sel_month()
            self.plot_average_wind()

    def forward_in_year(self):
        if self.year_selected == self.year[-1]:
            return
        else:
            index = self.year.index(self.year_selected)
            self.year_selected = self.year[index + 1]
            self.month = self.get_months_for_year()
            self.month_selected = self.month[0]
            self.sel_year()
            self.sel_month()
            self.plot_average_wind()

    def back_in_year(self):
        if self.year_selected == self.year[0]:
            return
        else:
            index = self.year.index(self.year_selected)
            self.year_selected = self.year[index - 1]
            self.month = self.get_months_for_year()
            self.month_selected = self.month[0]
            self.sel_year()
            self.sel_month()
            self.plot_average_wind()

    def get_months_for_year(self):
        time_coords = self.dataset[self.time_name]
        months = time_coords.where(time_coords.dt.year == self.year_selected, drop=True).dt.month.values
        return list(sorted(set(months)))

    def set_magvector(self):
        u_mag = self.dataset[self.u_name].values[:, :, :]
        v_mag = self.dataset[self.v_name].values[:, :, :]
        mag = [self.f_magnitude(u_mag[t, :, :], v_mag[t, :, :]) for t in range(len(self.dataset[self.time_name]))]
        magnitude_min = np.nanmin(mag)
        magnitude_max = np.nanmax(mag)
        if magnitude_max == magnitude_min:
            magnitude_max += 1e-6
        return magnitude_min, magnitude_max

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
        self.plot_average_wind()
        self.color_scale_widget.close()

    def filter_data(self):
        """

        """
        date_times = [pd.to_datetime(value).to_pydatetime() for value in self.dataset[self.time_name].values]
        list_months = []
        list_year = []

        for date in date_times:
            if date.month not in list_months:
                list_months.append(date.month)

            if date.year not in list_year:
                list_year.append(date.year)

        return list_year, list_months

    def mag_all(self):
        u_mag = self.dataset[self.u_name].values[:, :, :]
        v_mag = self.dataset[self.v_name].values[:, :, :]
        mag = [self.f_magnitude(u_mag[t, :, :], v_mag[t, :, :]) for t in range(len(self.dataset[self.time_name]))]
        magnitude_min = np.nanmin(mag)
        magnitude_max = np.nanmax(mag)
        if magnitude_max == magnitude_min:
            magnitude_max += 1e-6
        return magnitude_min, magnitude_max

    def save_gif(self):
        wind = self.dataset

        time_index = pd.to_datetime(wind[self.time_name].values)
        mask = (time_index.year == self.year_selected) & (time_index.month == self.month_selected)
        dataset_filtrado = wind.sel(valid_time=wind[self.time_name][mask])
        time_index_filter = pd.to_datetime(dataset_filtrado[self.time_name].values)
        dias_unicos = time_index_filter.day.unique().to_list()
        horas_unicas = time_index_filter.hour.unique().to_list()

        f = lambda x, y: np.sqrt(x ** 2 + y ** 2)

        vec_u = []
        vec_v = []
        list_days = []
        list_horas = []
        dict_average_data = {i: [] for i in range(1, dias_unicos[-1] + 1)}

        for time in dataset_filtrado[self.time_name].values:
            t_formated = datetime.strptime(time.astype(str).split('.')[0], '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d-%H')
            t_formated = datetime.strptime(t_formated, '%Y-%m-%d-%H')

            list_days.append(t_formated.day)
            list_horas.append(t_formated.hour)

            dict_to_sel = {
                self.time_name: time
            }

            u = dataset_filtrado[self.u_name].sel(dict_to_sel)[:, :].values
            v = dataset_filtrado[self.v_name].sel(dict_to_sel)[:, :].values

            vec_u.append(np.mean(u))
            vec_v.append(np.mean(v))
            media_u = np.mean(u)
            media_v = np.mean(v)
            media_mag = f(media_u, media_v)
            dict_average_data[int(t_formated.day)].append(media_mag)

        list_hour = list(set(list_horas))
        list_day = list(set(list_days))
        X, Y = np.meshgrid(list_hour, list_day)
        data_average = Df.from_dict(dict_average_data, orient='index')

        fig, ax = plt.subplots(figsize=(14, 14), constrained_layout=True, facecolor=None)
        cmap = plt.get_cmap(self.current_scale)
        norm = colors.Normalize(vmin=self.current_min, vmax=self.current_max)

        im = ax.imshow(data_average, aspect='auto', cmap=cmap, norm=norm,
                       interpolation='bicubic', origin='lower',
                       extent=[0, horas_unicas[-1], 1, dias_unicos[-1]])
        ax.set_xticks(np.arange(horas_unicas[0], horas_unicas[-1] + 1, 1))
        ax.set_yticks(np.arange(dias_unicos[0], dias_unicos[-1] + 1, 1))
        ax.set_xlabel('Hour', fontsize=18)
        ax.set_ylabel('Days', fontsize=18)

        cb = fig.colorbar(im, ax=ax, orientation='vertical')
        cb.set_label(f'Wind velocity {self.dataset[self.u_name].attrs['units']}', fontsize=18)
        cb.set_ticks(np.arange(self.current_min, self.current_max, 2))
        cb.ax.set_yticklabels([f'{i:.2f}' for i in np.arange(self.current_min, self.current_max, 2)])

        ax.margins(x=0.01, y=0.01)
        ax.set_xlim(horas_unicas[0] - 0.5, horas_unicas[-1] + .5)
        ax.set_ylim(dias_unicos[0] - 0.5, dias_unicos[-1] + .5)
        ax.tick_params(axis='both', which='major', labelsize=12)

        ax.quiver(X, Y, vec_u, vec_v, scale=250, color='black', headwidth=3, headlength=5, width=0.001,
                  headaxislength=4.5)

        path_to_save = f'{self.mainpage.project.caminho}\\figs'
        os.makedirs(path_to_save, exist_ok=True)

        plt.savefig(f'{path_to_save}\\{self.year_selected}_{self.month_selected}.png', transparent=True)
        plt.close()

    def plot_average_wind(self):  # .data, year, month
        self.figure.clear()
        self.canvas.draw()

        wind = self.dataset

        time_index = pd.to_datetime(wind[self.time_name].values)
        mask = (time_index.year == self.year_selected) & (time_index.month == self.month_selected)
        dataset_filtrado = wind.sel(valid_time=wind[self.time_name][mask])
        time_index_filter = pd.to_datetime(dataset_filtrado[self.time_name].values)
        dias_unicos = time_index_filter.day.unique().to_list()
        horas_unicas = time_index_filter.hour.unique().to_list()

        f = lambda x, y: np.sqrt(x ** 2 + y ** 2)

        vec_u = []
        vec_v = []
        list_days = []
        list_horas = []
        dict_average_data = {i: [] for i in range(1, dias_unicos[-1] + 1)}

        for time in dataset_filtrado[self.time_name].values:
            t_formated = datetime.strptime(time.astype(str).split('.')[0], '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d-%H')
            t_formated = datetime.strptime(t_formated, '%Y-%m-%d-%H')

            list_days.append(t_formated.day)
            list_horas.append(t_formated.hour)

            dict_to_sel = {
                self.time_name: time
            }

            u = dataset_filtrado[self.u_name].sel(dict_to_sel)[:, :].values
            v = dataset_filtrado[self.v_name].sel(dict_to_sel)[:, :].values

            vec_u.append(np.mean(u))
            vec_v.append(np.mean(v))
            media_u = np.mean(u)
            media_v = np.mean(v)
            media_mag = f(media_u, media_v)
            dict_average_data[int(t_formated.day)].append(media_mag)

        list_hour = list(set(list_horas))
        list_day = list(set(list_days))
        X, Y = np.meshgrid(list_hour, list_day)
        data_average = Df.from_dict(dict_average_data, orient='index')

        ax = self.figure.add_subplot(111)
        cmap = plt.get_cmap(self.current_scale)
        norm = colors.Normalize(vmin=self.current_min, vmax=self.current_max)

        im = ax.imshow(data_average, aspect='auto', cmap=cmap, norm=norm,
                       interpolation='bicubic', origin='lower',
                       extent=[0, horas_unicas[-1], 1, dias_unicos[-1]])
        ax.set_xticks(np.arange(horas_unicas[0], horas_unicas[-1] + 1, 1))
        ax.set_yticks(np.arange(dias_unicos[0], dias_unicos[-1] + 1, 1))
        ax.set_xlabel('Hour', fontsize=8, color='white')
        ax.set_ylabel('Days', fontsize=8, color='white')

        cb = self.figure.colorbar(im, ax=ax, orientation='vertical')
        cb.set_label(f'Wind velocity {self.dataset[self.u_name].attrs['units']}', fontsize=6, color="white")
        cb.set_ticks(np.arange(self.current_min, self.current_max, 2))
        cb.ax.set_yticklabels([f'{i:.2f}' for i in np.arange(self.current_min, self.current_max, 2)])
        cb.ax.tick_params(labelsize=8)
        cb.ax.yaxis.set_tick_params(color='white')
        plt.setp(plt.getp(cb.ax.axes, 'yticklabels'), color='white')

        ax.margins(x=0.01, y=0.01)
        ax.set_xlim(horas_unicas[0] - 0.5, horas_unicas[-1] + .5)
        ax.set_ylim(dias_unicos[0] - 0.5, dias_unicos[-1] + .5)
        ax.tick_params(axis='both', which='major', labelsize=7, color='white', labelcolor='white')

        ax.quiver(X, Y, vec_u, vec_v, scale=250, color='black', headwidth=3, headlength=5, width=0.001,
                  headaxislength=4.5)

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

    def retranslateUi(self, WindButton_LonLatProfile):
        WindButton_LonLatProfile.setWindowTitle(QCoreApplication.translate("WindButton_LonLatProfile", u"Form", None))
        self.StepFilterLabel.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"Year", None))
        self.backward_button_step.setText("")
        self.forward_button_step.setText("")
        self.StepFilterLabel_2.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"Month", None))
        self.backward_button_step_2.setText("")
        self.forward_button_step_2.setText("")
        self.SaveFigButton.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"SAVE FIGURE", None))
        self.ColorScaleButton.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"Set Color Scale", None))
