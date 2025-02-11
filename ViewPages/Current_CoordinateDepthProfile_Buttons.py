from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QComboBox, QFrame, QGridLayout,
                               QHBoxLayout, QLabel, QPushButton, QRadioButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout)
from PySide6 import QtWidgets
from PySide6.QtGui import QColor
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
        self.u_name, self.v_name = variables['u'], variables['v']
        self.time_name = variables['time']
        self.depth_name = variables['depth']
        self.lon_name, self.lat_name = variables['longitude'], variables['latitude']

        self.horizontalLayout = QHBoxLayout(WindButton_LonLatProfile)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(WindButton_LonLatProfile)
        self.frame.setObjectName(u"frame")
        self.frame.setProperty(u"ViewCommomFrame", True)
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
        # self.ColorScaleButton.setStyleSheet(u"QPushButton{\n"
        #                                     "	background-color: rgb(61, 80, 95);\n"
        #                                     "	border-radius: 15px;\n"
        #                                     "	border: 2px solid #F98600;\n"
        #                                     "}\n"
        #                                     "\n"
        #                                     "QPushButton:hover{\n"
        #                                     "	color: #F98600;\n"
        #                                     "	font-size: 14px;\n"
        #                                     "}")
        self.ColorScaleButton.clicked.connect(self.open_color_scale_widget)

        self.verticalLayout_ScaleButton.addWidget(self.ColorScaleButton)
        self.hori_frame.addLayout(self.verticalLayout_ScaleButton)

        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(WindButton_LonLatProfile)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setProperty(u"ViewCommomFrame", True)
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
        # self.frame_buttons_animation_time.setStyleSheet(u"QPushButton {\n"
        #                                                 "    background-color: transparent;\n"
        #                                                 "    border: none;\n"
        #                                                 "    padding: 10px; /* Adicione um padding maior para ajustar o tamanho do fundo */\n"
        #                                                 "}\n"
        #                                                 "\n"
        #                                                 "QPushButton:hover {\n"
        #                                                 "    background-color: rgba(255, 165, 0, 0.2); /* Cor de fundo no hover */\n"
        #                                                 "    border-radius: 5px; /* Bordas arredondadas */\n"
        #                                                 "}\n"
        #                                                 "\n"
        #                                                 "QPushButton:pressed {\n"
        #                                                 "    background-color: rgba(255, 165, 0, 0.5); /* Cor de fundo ao pressionar */\n"
        #                                                 "}")
        self.frame_buttons_animation_time.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_buttons_animation_time.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_buttons_animation_time)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.forward_button_time = QPushButton(self.frame_buttons_animation_time)
        self.forward_button_time.setObjectName(u"forward_button_time")
        self.forward_button_time.setProperty('CommomButton_Animations', True)
        icon = QIcon()
        icon.addFile(u":/icons/icons/arrow-right - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.forward_button_time.setIcon(icon)
        self.forward_button_time.setIconSize(QSize(20, 20))
        self.forward_button_time.clicked.connect(self.forward_in_time)

        self.gridLayout_7.addWidget(self.forward_button_time, 0, 2, 1, 1)

        self.finish_button_time = QPushButton(self.frame_buttons_animation_time)
        self.finish_button_time.setObjectName(u"finish_button_time")
        self.finish_button_time.setProperty('CommomButton_Animations', True)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/forward - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.finish_button_time.setIcon(icon1)
        self.finish_button_time.setIconSize(QSize(20, 20))
        self.finish_button_time.clicked.connect(self.last_in_time)

        self.gridLayout_7.addWidget(self.finish_button_time, 0, 3, 1, 1)

        self.backward_button_time = QPushButton(self.frame_buttons_animation_time)
        self.backward_button_time.setObjectName(u"backward_button_time")
        self.backward_button_time.setProperty('CommomButton_Animations', True)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/arrow-left - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backward_button_time.setIcon(icon2)
        self.backward_button_time.setIconSize(QSize(20, 20))
        self.backward_button_time.clicked.connect(self.back_in_time)

        self.gridLayout_7.addWidget(self.backward_button_time, 0, 1, 1, 1)

        self.start_button_time = QPushButton(self.frame_buttons_animation_time)
        self.start_button_time.setObjectName(u"start_button_time")
        self.start_button_time.setProperty('CommomButton_Animations', True)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/backward - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start_button_time.setIcon(icon3)
        self.start_button_time.setIconSize(QSize(20, 20))
        self.start_button_time.clicked.connect(self.first_in_time)

        self.gridLayout_7.addWidget(self.start_button_time, 0, 0, 1, 1)

        self.verticalLayout_13.addWidget(self.frame_buttons_animation_time)

        self.TimeValueLabel = QLabel(self.frame_2)
        self.TimeValueLabel.setObjectName(u"TimeValueLabel")
        self.TimeValueLabel.setProperty('ValueLabel_ViewPages', True)
        self.TimeValueLabel.setMinimumSize(QSize(180, 22))
        self.TimeValueLabel.setMaximumSize(QSize(180, 22))
        # self.TimeValueLabel.setStyleSheet(u"border: 2px solid #212b33")
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

        self.depthComboBox = QComboBox(self.frame_2)
        self.depthComboBox.setObjectName(u"depthComboBox")
        self.depthComboBox.setProperty(u"CommomComboboxView", True)
        self.depthComboBox.setMinimumSize(QSize(180, 50))
        self.depthComboBox.setMaximumSize(QSize(180, 50))

        self.verticalLayout.addWidget(self.depthComboBox)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer_36 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_36)

        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_38 = QSpacerItem(17, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_38)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.LatRadioButton = QRadioButton(self.frame_2)
        self.LatRadioButton.setObjectName(u"LatRadioButton")
        self.LatRadioButton.clicked.connect(self.updateLat)

        self.verticalLayout_3.addWidget(self.LatRadioButton)

        self.LonRadioButton = QRadioButton(self.frame_2)
        self.LonRadioButton.setObjectName(u"LonRadioButton")
        self.LonRadioButton.clicked.connect(self.updateLon)

        self.verticalLayout_3.addWidget(self.LonRadioButton)

        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.TimeFilterLabel_3 = QLabel(self.frame_2)
        self.TimeFilterLabel_3.setObjectName(u"TimeFilterLabel_3")
        self.TimeFilterLabel_3.setMinimumSize(QSize(180, 22))
        self.TimeFilterLabel_3.setMaximumSize(QSize(180, 22))
        self.TimeFilterLabel_3.setFont(font)

        self.verticalLayout_2.addWidget(self.TimeFilterLabel_3)

        self.coordComboBox = QComboBox(self.frame_2)
        self.coordComboBox.setObjectName(u"coordComboBox")
        self.coordComboBox.setProperty(u"CommomComboboxView", True)
        self.coordComboBox.setMinimumSize(QSize(180, 50))
        self.coordComboBox.setMaximumSize(QSize(180, 50))

        self.verticalLayout_2.addWidget(self.coordComboBox)

        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_39 = QSpacerItem(17, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_39)

        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

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
        # self.SaveFigButton.setStyleSheet(u"QPushButton{\n"
        #                                  "	background-color: rgb(61, 80, 95);\n"
        #                                  "	border-radius: 15px;\n"
        #                                  "	border: 2px solid #F98600;\n"
        #                                  "}\n"
        #                                  "\n"
        #                                  "QPushButton:hover{\n"
        #                                  "	color: #F98600;\n"
        #                                  "	font-size: 14px;\n"
        #                                  "}")
        self.SaveFigButton.clicked.connect(self.save_fig)

        self.horizontalLayout_6.addWidget(self.SaveFigButton)

        self.horizontalLayout_15.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer_41 = QSpacerItem(18, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_41)

        self.gridLayout.addLayout(self.horizontalLayout_15, 3, 0, 1, 1)

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
            'depthComboBox',
            'coordComboBox',
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

            self.lat = [f'{lat_value}' for lat_value in self.dataset[self.lat_name].values]
            self.lon = [f'{lon_value}' for lon_value in self.dataset[self.lon_name].values]
            self.LatRadioButton.setChecked(True)

            self.time = self.dataset[self.time_name].values
            self.time_selected = self.time[0]
            self.sel_time(self.time_selected)

            self.depth = [f'{depth_value}' for depth_value in self.dataset[self.depth_name].values]
            self.depthComboBox.addItems(self.depth)
            self.depthComboBox.setCurrentIndex(25)
            self.depthComboBox.currentIndexChanged.connect(self.plot_graph)

            self.color_scale_widget = None
            self.current_min, self.current_max = self.set_normvalues(self.dataset[self.u_name])
            self.current_scale = "RdYlGn_r"

            self.updateLat()

        except Exception as e:
            raise e

    def sel_time(self, value_time):
        time_to_format = str(value_time).split('.')[0]
        self.t_formated = datetime.strptime(time_to_format, '%Y-%m-%dT%H:%M:%S').strftime('%m-%d-%Y-%Hh')
        self.TimeValueLabel.setText(f'{self.t_formated}')

    def forward_in_time(self):
        if self.time_selected == self.time[-1]:
            return
        else:
            index = np.where(self.time == self.time_selected)[0][0]
            self.time_selected = self.time[index + 1]
            self.sel_time(self.time_selected)
            self.plot_graph()

    def last_in_time(self):
        if self.time_selected == self.time[-1]:
            return
        else:
            self.time_selected = self.time[-1]
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

    def first_in_time(self):
        if self.time_selected == self.time[0]:
            return
        else:
            self.time_selected = self.time[0]
            self.sel_time(self.time_selected)
            self.plot_graph()

    def updateLon(self):
        self.coordComboBox.blockSignals(True)
        self.coordComboBox.clear()
        self.coordComboBox.addItems(self.lon)
        self.updateComboBox()

    def updateLat(self):
        self.coordComboBox.blockSignals(True)
        self.coordComboBox.clear()
        self.coordComboBox.addItems(self.lat)
        self.updateComboBox()

    def updateComboBox(self):
        self.coordComboBox.setCurrentIndex(0)
        self.coordComboBox.blockSignals(False)
        self.coordComboBox.currentIndexChanged.connect(self.plot_graph)
        self.plot_graph()

    def set_normvalues(self, dset) -> tuple:
        vmax = np.nanmax(dset[:, :, :, :])
        vmin = np.nanmin(dset[:, :, :, :])
        del dset
        return vmin, vmax

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
        self.plot_graph()
        self.color_scale_widget.close()

    def plot_graph(self):
        """
        Plota o perfil de corrente em função da profundidade e da coordenada selecionada.

        Parâmetros:
        - ds: xarray.Dataset com componentes 'water_u' e 'water_v'.
        - tempo: Índice do tempo a ser filtrado.
        - variavel: 'latitude' ou 'longitude' para indicar qual variável será filtrada.
        - coord: Coordenada específica (latitude ou longitude) a ser utilizada no filtro.
        """
        # Seleciona a componente e define as coordenadas do gráfico

        self.figure.clear()
        self.canvas.draw()

        all_depth = self.dataset[self.depth_name].values
        index = self.depth.index(self.depthComboBox.currentText())
        depth = all_depth[:index + 1]

        if self.LatRadioButton.isChecked():
            var = 'Latitude'
            componente = self.u_name
            dict_to_sel = {
                self.time_name: self.time_selected,
                self.lat_name: float(self.coordComboBox.currentText()),
                self.depth_name: depth
            }
            dados_filtrados = self.dataset[componente].sel(dict_to_sel)[:, :].values
            eixo_x = self.dataset[self.lon_name].values
        else:
            var = 'Longitude'
            componente = self.v_name
            dict_to_sel = {
                self.time_name: self.time_selected,
                self.lon_name: float(self.coordComboBox.currentText()),
                self.depth_name: depth
            }
            dados_filtrados = self.dataset[componente].sel(dict_to_sel)[:, :].values
            eixo_x = self.dataset[self.lat_name].values

        # min_value, max_value = self.set_normvalues(self.dataset[componente])

        linhas_validas = ~np.isnan(dados_filtrados).all(axis=1)
        ulcd = np.where(linhas_validas)
        colunas_validas = ~np.isnan(dados_filtrados).all(axis=0)
        uccd = np.where(colunas_validas)

        matriz_filtrada = dados_filtrados[np.ix_(linhas_validas, colunas_validas)]

        cmap = cm.get_cmap(self.current_scale)
        norm = plt.Normalize(vmin=self.current_min, vmax=self.current_max)

        colors_ = cmap(norm(matriz_filtrada))
        colors_ = colors_.reshape(-1, 4)

        depth_filtered = depth[ulcd]
        x_axis_filtered = eixo_x[uccd]

        x, y = np.meshgrid(x_axis_filtered, depth_filtered)

        ax = self.figure.add_subplot(111)

        ax.quiver(
            x, y,
            np.sign(matriz_filtrada), 0, color=colors_, cmap=cmap,
            # Apenas a componente selecionada, com vetor vertical = 0
            scale=50
        )

        cbar = plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, orientation='vertical', pad=0.05)
        cbar.set_label(f'Vector Magnitude [{self.dataset[componente].attrs['units']}]', fontsize=6, color="black")
        cbar.ax.tick_params(labelsize=8)
        cbar.ax.yaxis.set_tick_params(color='black')
        plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='black')

        ax.set_ylim(max(depth_filtered), 0)
        ax.set_xlabel('Latitude', fontsize=8, color='black') if var == 'Longitude' \
            else ax.set_xlabel('Longitude', fontsize=8, color='black')
        ax.set_ylabel('Depth [m]', fontsize=8, color='black')
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
        all_depth = self.dataset[self.depth_name].values
        index = self.depth.index(self.depthComboBox.currentText())
        depth = all_depth[:index + 1]

        if self.LatRadioButton.isChecked():
            var = 'Latitude'
            componente = self.u_name
            dict_to_sel = {
                self.time_name: self.time_selected,
                self.lat_name: float(self.coordComboBox.currentText()),
                self.depth_name: depth
            }
            dados_filtrados = self.dataset[componente].sel(dict_to_sel)[:, :].values
            eixo_x = self.dataset[self.lon_name].values
        else:
            var = 'Longitude'
            componente = self.v_name
            dict_to_sel = {
                self.time_name: self.time_selected,
                self.lon_name: float(self.coordComboBox.currentText()),
                self.depth_name: depth
            }
            dados_filtrados = self.dataset[componente].sel(dict_to_sel)[:, :].values
            eixo_x = self.dataset[self.lat_name].values

        linhas_validas = ~np.isnan(dados_filtrados).all(axis=1)
        ulcd = np.where(linhas_validas)
        colunas_validas = ~np.isnan(dados_filtrados).all(axis=0)
        uccd = np.where(colunas_validas)

        matriz_filtrada = dados_filtrados[np.ix_(linhas_validas, colunas_validas)]

        cmap = cm.get_cmap(self.current_scale)
        norm = plt.Normalize(vmin=self.current_min, vmax=self.current_max)

        colors_ = cmap(norm(matriz_filtrada))
        colors_ = colors_.reshape(-1, 4)

        depth_filtered = depth[ulcd]
        x_axis_filtered = eixo_x[uccd]

        x, y = np.meshgrid(x_axis_filtered, depth_filtered)

        fig, axs = plt.subplots(figsize=(14, 14), constrained_layout=True, facecolor=None)

        axs.quiver(
            x, y,
            np.sign(matriz_filtrada), 0, color=colors_, cmap=cmap,
            # Apenas a componente selecionada, com vetor vertical = 0
            scale=50
        )

        cbar = plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=axs, orientation='vertical', pad=0.05)
        cbar.set_label(f'Vector Magnitude [{self.dataset[componente].attrs['units']}]', fontsize=18, color="black")
        cbar.ax.tick_params(labelsize=16)
        cbar.ax.yaxis.set_tick_params(color='black')
        plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='black')

        axs.set_ylim(max(depth_filtered), 0)
        axs.set_xlabel('Latitude', fontsize=18, color='black') if var == 'Longitude' \
            else axs.set_xlabel('Longitude', fontsize=18, color='black')
        axs.set_ylabel('Depth [m]', fontsize=18, color='black')
        axs.tick_params(axis='both', which='major', labelsize=16, color='black', labelcolor='black')

        path_to_save = f'{self.mainpage.project.caminho}\\figs'
        os.makedirs(path_to_save, exist_ok=True)

        section = 'Eastward' if var == 'Latitude' else 'Northward'

        plt.savefig(f'{path_to_save}\\{section} SeawaterVelocity for {var} '
                    f'{round(float(self.coordComboBox.currentText()), ndigits=2)} at {self.t_formated} '
                    f'for {self.mainpage.comboBox.currentText()[:-3]}.png', transparent=True)
        plt.close()

    def retranslateUi(self, WindButton_LonLatProfile):
        WindButton_LonLatProfile.setWindowTitle(QCoreApplication.translate("WindButton_LonLatProfile", u"Form", None))
        self.TimeFilterLabel.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"Time Filter", None))
        self.forward_button_time.setText("")
        self.finish_button_time.setText("")
        self.backward_button_time.setText("")
        self.start_button_time.setText("")
        self.TimeFilterLabel_2.setText(
            QCoreApplication.translate("WindButton_LonLatProfile", u"Choose a deep release", None))
        self.LatRadioButton.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"Latitude", None))
        self.LonRadioButton.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"Longitude", None))
        self.TimeFilterLabel_3.setText(
            QCoreApplication.translate("WindButton_LonLatProfile", u"Select a coordinate", None))
        self.SaveFigButton.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"SAVE FIGURE", None))
        self.ColorScaleButton.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"Set Color Scale", None))
