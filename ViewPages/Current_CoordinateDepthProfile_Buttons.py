# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Current_CoordinateDepthProfile_ButtonslwXMpM.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
                               QHBoxLayout, QLabel, QPushButton, QRadioButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

import resources_rc
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
from matplotlib import colors
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from datetime import datetime
import os


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
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
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
        self.forward_button_time = QPushButton(self.frame_buttons_animation_time)
        self.forward_button_time.setObjectName(u"forward_button_time")
        icon = QIcon()
        icon.addFile(u":/icons/icons/arrow-right - laranja.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.forward_button_time.setIcon(icon)
        self.forward_button_time.setIconSize(QSize(20, 20))

        self.gridLayout_7.addWidget(self.forward_button_time, 0, 2, 1, 1)

        self.finish_button_time = QPushButton(self.frame_buttons_animation_time)
        self.finish_button_time.setObjectName(u"finish_button_time")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/forward - laranja.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.finish_button_time.setIcon(icon1)
        self.finish_button_time.setIconSize(QSize(20, 20))

        self.gridLayout_7.addWidget(self.finish_button_time, 0, 3, 1, 1)

        self.backward_button_time = QPushButton(self.frame_buttons_animation_time)
        self.backward_button_time.setObjectName(u"backward_button_time")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/arrow-left - laranja.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backward_button_time.setIcon(icon2)
        self.backward_button_time.setIconSize(QSize(20, 20))

        self.gridLayout_7.addWidget(self.backward_button_time, 0, 1, 1, 1)

        self.start_button_time = QPushButton(self.frame_buttons_animation_time)
        self.start_button_time.setObjectName(u"start_button_time")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/backward - laranja.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start_button_time.setIcon(icon3)
        self.start_button_time.setIconSize(QSize(20, 20))

        self.gridLayout_7.addWidget(self.start_button_time, 0, 0, 1, 1)

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

        self.frame.setLayout(self.graph_layout)

        try:
            self.lat = [f'{lat_value}' for lat_value in self.dataset['lat'].values]
            self.lon = [f'{lon_value}' for lon_value in self.dataset['lon'].values]
            self.LatRadioButton.setChecked(True)

            self.time = self.dataset['time'].values
            self.time_selected = self.time[0]
            self.sel_time(self.time_selected)

            self.depth = [f'{depth_value}' for depth_value in self.dataset.depth.values]
            self.depthComboBox.addItems(self.depth)
            self.depthComboBox.setCurrentIndex(25)
            self.depthComboBox.currentIndexChanged.connect(self.plot_graph)

            self.updateLat()

        except Exception as e:
            raise e

    def sel_time(self, value_time):
        time_to_format = str(value_time).split('.')[0]
        t_formated = datetime.strptime(time_to_format, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d-%Hh')
        self.TimeValueLabel.setText(f'{t_formated}')

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
        return vmin, vmax

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

        all_depth = self.dataset.depth.values
        index = self.depth.index(self.depthComboBox.currentText())
        depth = all_depth[:index + 1]

        if self.LatRadioButton.isChecked():
            var = 'Latitude'
            componente = 'water_u'
            dados_filtrados = self.dataset[componente].sel(time=self.time_selected, lat=float(self.coordComboBox.currentText()), depth=depth)[:, :].values
            eixo_x = self.dataset.lon.values
        else:
            var = 'Longitude'
            componente = 'water_v'
            dados_filtrados = self.dataset[componente].sel(time=self.time_selected, lon=float(self.coordComboBox.currentText()), depth=depth)[:, :].values
            eixo_x = self.dataset.lat.values

        min_value, max_value = self.set_normvalues(self.dataset[componente])

        linhas_validas = ~np.isnan(dados_filtrados).all(axis=1)
        ulcd = np.where(linhas_validas)
        colunas_validas = ~np.isnan(dados_filtrados).all(axis=0)
        uccd = np.where(colunas_validas)

        matriz_filtrada = dados_filtrados[np.ix_(linhas_validas, colunas_validas)]

        cmap = cm.get_cmap('RdYlGn_r')
        norm = plt.Normalize(vmin=min_value, vmax=max_value)

        colors_ = cmap(norm(matriz_filtrada))
        colors_ = colors_.reshape(-1, 4)

        depth_filtered = depth[ulcd]
        x_axis_filtered = eixo_x[uccd]

        x, y = np.meshgrid(x_axis_filtered, depth_filtered)

        # fig, ax = plt.subplots(figsize=(14, 14), constrained_layout=True, facecolor=None)
        ax = self.figure.add_subplot(111)

        ax.quiver(
            x, y,
            np.sign(matriz_filtrada), 0, color=colors_, cmap=cmap,
            # Apenas a componente selecionada, com vetor vertical = 0
            scale=50
        )

        cbar = plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, orientation='vertical', pad=0.05)
        cbar.set_label(f'Magnitude dos Vetores [{self.dataset[componente].attrs['units']}]', fontsize=6, color="white")
        cbar.ax.tick_params(labelsize=8)
        cbar.ax.yaxis.set_tick_params(color='white')
        plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='white')

        ax.set_ylim(max(depth_filtered), 0)
        ax.set_xlabel('Latitude', fontsize=8, color='white') if var == 'longitude' \
            else ax.set_xlabel('Longitude', fontsize=8, color='white')
        ax.set_ylabel('Depth [m]', fontsize=8, color='white')
        ax.tick_params(axis='both', which='major', labelsize=7, color='white', labelcolor='white')

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
