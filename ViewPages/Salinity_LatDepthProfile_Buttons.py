from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QComboBox, QFrame, QGridLayout,
                               QHBoxLayout, QLabel, QPushButton, QSizePolicy,
                               QSpacerItem, QVBoxLayout)
from PySide6.QtGui import QColor
from PySide6 import QtWidgets
from ViewPages import ColorEscale as Cs
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from datetime import datetime
import os


class Ui_WindButton_LonLatProfile(object):
    def setupUi(self, page, WindButton_LonLatProfile, dataset, variables):
        if not WindButton_LonLatProfile.objectName():
            WindButton_LonLatProfile.setObjectName(u"WindButton_LonLatProfile")
        WindButton_LonLatProfile.resize(546, 436)

        self.mainpage = page
        self.dataset = dataset
        self.sali_name = variables['salinity']
        self.time_name = variables['time']
        self.depth_name = variables['depth']
        self.lon_name, self.lat_name = variables['longitude'], variables['latitude']

        self.horizontalLayout = QHBoxLayout(WindButton_LonLatProfile)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(WindButton_LonLatProfile)
        self.frame.setObjectName(u"frame")
        self.frame.setProperty('ViewCommomFrame', True)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.hori_frame = QHBoxLayout(self.frame)

        self.verticalLayout_ScaleButton = QVBoxLayout()
        self.verticalLayout_ScaleButton.setAlignment(Qt.AlignmentFlag.AlignBottom)

        self.ColorScaleButton = QPushButton()
        self.ColorScaleButton.setObjectName(u"ColorScale")
        self.ColorScaleButton.setProperty('CommomButtonViewPageFunc', True)
        self.ColorScaleButton.setMinimumSize(QSize(100, 30))
        self.ColorScaleButton.setMaximumSize(QSize(100, 30))

        self.ColorScaleButton.clicked.connect(self.open_color_scale_widget)

        self.verticalLayout_ScaleButton.addWidget(self.ColorScaleButton)
        self.hori_frame.addLayout(self.verticalLayout_ScaleButton)

        self.color_scale_widget = None
        self.current_min = np.nanmin(self.dataset[self.sali_name].values)
        self.current_max = np.nanmax(self.dataset[self.sali_name].values)
        self.current_scale = "RdYlGn_r"

        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(WindButton_LonLatProfile)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setProperty('ViewCommomFrame', True)
        self.frame_2.setMinimumSize(QSize(320, 0))
        self.frame_2.setMaximumSize(QSize(320, 16777215))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_34 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_34)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(3)
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
        self.frame_buttons_animation_time.setProperty('ViewCommomFrame_Animations', True)
        self.frame_buttons_animation_time.setMinimumSize(QSize(180, 50))
        self.frame_buttons_animation_time.setMaximumSize(QSize(180, 50))

        self.frame_buttons_animation_time.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_buttons_animation_time.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_buttons_animation_time)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.start_button_time = QPushButton(self.frame_buttons_animation_time)
        self.start_button_time.setObjectName(u"start_button_time")
        self.start_button_time.setProperty('CommomButton_Animations', True)
        icon = QIcon()
        icon.addFile(u":/icons/icons/backward - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start_button_time.setIcon(icon)
        self.start_button_time.setIconSize(QSize(20, 20))
        self.start_button_time.clicked.connect(self.start_in_time)

        self.gridLayout_7.addWidget(self.start_button_time, 0, 0, 1, 1)

        self.backward_button_time = QPushButton(self.frame_buttons_animation_time)
        self.backward_button_time.setObjectName(u"backward_button_time")
        self.backward_button_time.setProperty('CommomButton_Animations', True)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/arrow-left - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backward_button_time.setIcon(icon1)
        self.backward_button_time.setIconSize(QSize(20, 20))
        self.backward_button_time.clicked.connect(self.back_in_time)

        self.gridLayout_7.addWidget(self.backward_button_time, 0, 1, 1, 1)

        self.forward_button_time = QPushButton(self.frame_buttons_animation_time)
        self.forward_button_time.setObjectName(u"forward_button_time")
        self.forward_button_time.setProperty('CommomButton_Animations', True)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/arrow-right - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.forward_button_time.setIcon(icon4)
        self.forward_button_time.setIconSize(QSize(20, 20))
        self.forward_button_time.clicked.connect(self.forward_in_time)

        self.gridLayout_7.addWidget(self.forward_button_time, 0, 4, 1, 1)

        self.finish_button_time = QPushButton(self.frame_buttons_animation_time)
        self.finish_button_time.setObjectName(u"finish_button_time")
        self.finish_button_time.setProperty('CommomButton_Animations', True)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/forward - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.finish_button_time.setIcon(icon5)
        self.finish_button_time.setIconSize(QSize(20, 20))
        self.finish_button_time.clicked.connect(self.last_in_time)

        self.gridLayout_7.addWidget(self.finish_button_time, 0, 5, 1, 1)

        self.verticalLayout_13.addWidget(self.frame_buttons_animation_time)

        self.TimeValueLabel = QLabel(self.frame_2)
        self.TimeValueLabel.setObjectName(u"TimeValueLabel")
        self.TimeValueLabel.setProperty('ValueLabel_ViewPages', True)
        self.TimeValueLabel.setMinimumSize(QSize(180, 22))
        self.TimeValueLabel.setMaximumSize(QSize(180, 22))
        self.TimeValueLabel.setText(u"Aqui vai o valor de tempo")
        self.TimeValueLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.TimeValueLabel)

        self.horizontalLayout_7.addLayout(self.verticalLayout_13)

        self.horizontalSpacer_35 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_35)

        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_37 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_37)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TimeFilterLabel_2 = QLabel(self.frame_2)
        self.TimeFilterLabel_2.setObjectName(u"TimeFilterLabel_2")
        self.TimeFilterLabel_2.setMinimumSize(QSize(180, 22))
        self.TimeFilterLabel_2.setMaximumSize(QSize(180, 22))
        self.TimeFilterLabel_2.setFont(font)

        self.verticalLayout.addWidget(self.TimeFilterLabel_2)

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(180, 50))
        self.comboBox.setMaximumSize(QSize(180, 50))

        self.verticalLayout.addWidget(self.comboBox)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer_36 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_36)

        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_40 = QSpacerItem(18, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_40)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.SaveFigButton = QPushButton(self.frame_2)
        self.SaveFigButton.setObjectName(u"SaveFigButton")
        self.SaveFigButton.setProperty('CommomButtonViewPageFunc', True)
        self.SaveFigButton.setMinimumSize(QSize(120, 30))
        self.SaveFigButton.setMaximumSize(QSize(120, 30))

        self.SaveFigButton.clicked.connect(self.save_fig)

        self.horizontalLayout_6.addWidget(self.SaveFigButton)

        self.horizontalLayout_15.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer_41 = QSpacerItem(18, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_41)

        self.gridLayout.addLayout(self.horizontalLayout_15, 2, 0, 1, 1)

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

        shadow_elements = {
            'frame',
            'frame_2',
            'frame_buttons_animation_time',
            'comboBox',
            'SaveFigButton',
            'ColorScaleButton'
        }

        try:
            for x in shadow_elements:
                effect = QtWidgets.QGraphicsDropShadowEffect(WindButton_LonLatProfile)
                effect.setBlurRadius(18)
                effect.setXOffset(0)
                effect.setYOffset(0)
                effect.setColor(QColor(0, 0, 0, 255))
                getattr(self, x).setGraphicsEffect(effect)

            self.lat = [lat_value for lat_value in self.dataset[self.lat_name].values]
            self.lon = [lon_value for lon_value in self.dataset[self.lon_name].values]
            self.time = self.dataset[self.time_name].values
            self.time_selected = self.time[0]
            self.sel_time(self.time_selected)
            for value in self.lon:
                self.comboBox.addItem(f'{value}')
            self.comboBox.setCurrentIndex(0)
            self.comboBox.currentIndexChanged.connect(self.plot_var_profile_withdepth)
            self.plot_var_profile_withdepth()
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
            self.plot_var_profile_withdepth()

    def start_in_time(self):
        if self.time_selected == self.time[0]:
            return
        else:
            self.time_selected = self.time[0]
            self.sel_time(self.time_selected)
            self.plot_var_profile_withdepth()

    def forward_in_time(self):
        if self.time_selected == self.time[-1]:
            return
        else:
            index = np.where(self.time == self.time_selected)[0][0]
            self.time_selected = self.time[index + 1]
            self.sel_time(self.time_selected)
            self.plot_var_profile_withdepth()

    def back_in_time(self):
        if self.time_selected == self.time[0]:
            return
        else:
            index = np.where(self.time == self.time_selected)[0][0]
            self.time_selected = self.time[index - 1]
            self.sel_time(self.time_selected)
            self.plot_var_profile_withdepth()

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
        self.plot_var_profile_withdepth()
        self.color_scale_widget.close()

    def set_normvalues(self) -> tuple:
        vmax = np.nanmax(self.dataset[self.sali_name][:, :, :, :])
        vmin = np.nanmin(self.dataset[self.sali_name][:, :, :, :])
        return vmin, vmax

    def plot_var_profile_withdepth(self):
        self.figure.clear()
        self.canvas.draw()

        cmap = cm.get_cmap(self.current_scale)
        norm = plt.Normalize(vmin=self.current_min, vmax=self.current_max)

        dataset_to_plot = self.dataset.sel({self.lon_name: float(self.comboBox.currentText()), self.time_name: self.time_selected})

        var_value = dataset_to_plot[self.sali_name].values
        depth = dataset_to_plot[self.depth_name].values
        x_axis = dataset_to_plot[self.lat_name].values

        linhas_validas = ~np.isnan(var_value).all(axis=1)
        ulcd = np.where(linhas_validas)
        colunas_validas = ~np.isnan(var_value).all(axis=0)
        uccd = np.where(colunas_validas)

        matriz_filtrada = var_value[np.ix_(linhas_validas, colunas_validas)]

        depth_filtered = depth[ulcd]
        x_axis_filtered = x_axis[uccd]

        ax = self.figure.add_subplot(111)

        ax.imshow(matriz_filtrada, cmap=cmap, norm=norm,
                  extent=(min(x_axis_filtered), max(x_axis_filtered), max(depth_filtered), min(depth_filtered)),
                  interpolation='bicubic', aspect='auto')  # , vmin=vmin, vmax=vmax

        cbar = self.figure.figure.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, orientation='vertical',
                                           pad=0.05)
        cbar.set_label(f'{self.dataset[self.sali_name].units}', fontsize=6, color="black")
        cbar.ax.tick_params(labelsize=8)
        cbar.ax.yaxis.set_tick_params(color='black')
        plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='black')

        ax.set_xlabel(f'Latitude [{self.dataset[self.lat_name].attrs['units']}]', labelpad=5, fontsize=8, color='black')
        ax.set_ylabel('Depth [m]', labelpad=5, fontsize=8, color='black')
        ax.tick_params(axis='both', which='major', labelsize=7, color='black', labelcolor='black')

        self.canvas.draw()
        self.canvas.figure.subplots_adjust(
            top=0.975,
            bottom=0.116,
            left=0.124,
            right=0.97,
            hspace=0.2,
            wspace=0.2
        )
        self.canvas.figure.set_facecolor("#C3C3C3")

    def save_fig(self):
        cmap = cm.get_cmap(self.current_scale)
        norm = plt.Normalize(vmin=self.current_min, vmax=self.current_max)

        dataset_to_plot = self.dataset.sel({self.lon_name: float(self.comboBox.currentText()), self.time_name: self.time_selected})

        var_value = dataset_to_plot[self.sali_name].values
        depth = dataset_to_plot[self.depth_name].values
        x_axis = dataset_to_plot[self.lat_name].values

        linhas_validas = ~np.isnan(var_value).all(axis=1)
        ulcd = np.where(linhas_validas)
        colunas_validas = ~np.isnan(var_value).all(axis=0)
        uccd = np.where(colunas_validas)

        matriz_filtrada = var_value[np.ix_(linhas_validas, colunas_validas)]

        depth_filtered = depth[ulcd]
        x_axis_filtered = x_axis[uccd]

        fig, ax = plt.subplots(figsize=(14, 14), constrained_layout=True, facecolor=None)

        plt.imshow(matriz_filtrada, cmap=cmap, norm=norm,
                   extent=(min(x_axis_filtered), max(x_axis_filtered), max(depth_filtered), min(depth_filtered)),
                   interpolation='bicubic', aspect='auto')  # , vmin=vmin, vmax=vmax

        cbar = plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, orientation='vertical', pad=0.05)
        cbar.set_label(f'{self.dataset[self.sali_name].units}', fontsize=18)
        cbar.ax.tick_params(labelsize=16)

        ax.set_xlabel(f'Latitude [{self.dataset[self.lat_name].attrs['units']}]', labelpad=20, fontsize=18)
        ax.set_ylabel('Depth [m]', labelpad=20, fontsize=18)
        plt.tick_params(axis='both', which='major', labelsize=16)

        path_to_save = f'{self.mainpage.project.caminho}\\figs'
        os.makedirs(path_to_save, exist_ok=True)

        time_to_format = str(self.time_selected).split('.')[0]
        t_formated = datetime.strptime(time_to_format, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d-%Hh')

        plt.savefig(f'{path_to_save}\\DEPTHvsLAT_SALINITY_{t_formated}_LONcoord{self.comboBox.currentText()}.png',
                    transparent=True)
        plt.close()

    def retranslateUi(self, WindButton_LonLatProfile):
        WindButton_LonLatProfile.setWindowTitle(QCoreApplication.translate("WindButton_LonLatProfile", u"Form", None))
        self.TimeFilterLabel.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"Time Filter", None))
        self.start_button_time.setText("")
        self.backward_button_time.setText("")
        self.forward_button_time.setText("")
        self.finish_button_time.setText("")
        self.TimeFilterLabel_2.setText(
            QCoreApplication.translate("WindButton_LonLatProfile", u"Longitude coordinate", None))
        self.SaveFigButton.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"SAVE FIGURE", None))
        self.ColorScaleButton.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"Set Color Scale", None))
