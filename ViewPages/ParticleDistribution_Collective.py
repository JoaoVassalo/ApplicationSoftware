# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'AreaImpactQBfdTs.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QSize)
from PySide6.QtWidgets import (QFrame, QGridLayout, QGroupBox,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QSpacerItem, QStackedLayout)
from PySide6.QtWidgets import (QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QFileDialog, QAbstractItemView, QAbstractScrollArea, QRadioButton, QButtonGroup, QScrollArea
)
from PySide6.QtGui import (QIcon)
from PySide6.QtCore import Qt, QThread
import os
import pandas as pd
from pandas import DataFrame as Df
from PySide6.QtGui import QColor
from PySide6 import QtWidgets
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from Functions import ColorReference as Cr
import random
from Functions import PosProcessOSCAR as Ppo
import time
import seaborn as sns


class AnimationWorker(QThread):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def run(self):
        self.page.play_animation()


class Ui_Form:
    def setupUi(self, frame):
        self.main_frame_PD = frame

        self.main_frame_PD.setObjectName(u"main_frame_PD")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame_PD.sizePolicy().hasHeightForWidth())
        self.main_frame_PD.setSizePolicy(sizePolicy)
        self.main_frame_PD.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame_PD.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.main_frame_PD)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.VLayout_VarButton_PD = QVBoxLayout()
        self.VLayout_VarButton_PD.setSpacing(0)
        self.VLayout_VarButton_PD.setObjectName(u"VLayout_VarButton_PD")

        self.frame_variables_PD = QFrame(self.main_frame_PD)
        self.frame_variables_PD.setObjectName(u"frame_variables_PD")
        self.frame_variables_PD.setProperty("commomFrame", True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_variables_PD.sizePolicy().hasHeightForWidth())
        self.frame_variables_PD.setSizePolicy(sizePolicy1)
        self.frame_variables_PD.setMinimumSize(QSize(300, 0))
        self.frame_variables_PD.setMaximumSize(QSize(300, 16777215))
        self.frame_variables_PD.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_variables_PD.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_variables_PD)
        self.gridLayout_6.setObjectName(u"gridLayout_6")

        self.vertical_layout_table = QVBoxLayout()
        self.HLayout_file_table = QHBoxLayout()
        self.HLayout_file_table.setObjectName("HLayout_file_table")
        self.horizontalSpacer_left = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.HLayout_file_table.addItem(self.horizontalSpacer_left)
        self.file_table = QTableWidget(3, 2)
        self.file_table.setMinimumSize(QSize(0, 130))
        self.file_table.setMaximumSize(QSize(16777215, 130))
        self.file_table.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.file_table.setHorizontalHeaderLabels(["Files", "Description"])
        self.file_table.setEditTriggers(QAbstractItemView.EditTrigger.AllEditTriggers)
        self.file_table.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        for i in range(3):
            item = QTableWidgetItem("Clique para selecionar")
            item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            self.file_table.setItem(i, 0, item)
            self.file_table.setItem(i, 1, QTableWidgetItem())

        self.file_table.cellDoubleClicked.connect(self.abrir_dialogo_arquivo)
        self.HLayout_file_table.addWidget(self.file_table)
        self.horizontalSpacer_right = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.HLayout_file_table.addItem(self.horizontalSpacer_right)
        self.vertical_layout_table.addLayout(self.HLayout_file_table)

        self.read_files_button = QPushButton()
        self.read_files_button.setMinimumSize(QSize(75, 25))
        self.read_files_button.setMaximumSize(QSize(75, 25))
        self.read_files_button.setText("Read files")
        self.read_files_button.clicked.connect(self.read)
        self.vertical_layout_table.addWidget(self.read_files_button, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.gridLayout_6.addLayout(self.vertical_layout_table, 0, 0, 1, 1)

        self.horizontalLayout_radio = QHBoxLayout()
        self.h_spacer_1 = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_radio.addItem(self.h_spacer_1)

        self.time_radio = QRadioButton("Time Filter")
        self.time_radio.setDisabled(True)
        self.time_radio.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.time_radio.clicked.connect(self.radio_vars)

        self.mean_radio = QRadioButton("Average plot")
        self.mean_radio.setDisabled(True)
        self.mean_radio.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.mean_radio.clicked.connect(self.radio_vars)

        self.radio_group = QButtonGroup()
        self.radio_group.addButton(self.time_radio)
        self.radio_group.addButton(self.mean_radio)

        self.horizontalLayout_radio.addWidget(self.time_radio)
        self.horizontalLayout_radio.addWidget(self.mean_radio)

        self.h_spacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_radio.addItem(self.h_spacer_2)

        self.gridLayout_6.addLayout(self.horizontalLayout_radio, 1, 0, 1, 1)

        self.VLayout_figsave_PD = QVBoxLayout()
        self.VLayout_figsave_PD.setObjectName(u"VLayout_figsave_PD")
        self.HLayout_figname_PD = QHBoxLayout()
        self.HLayout_figname_PD.setObjectName(u"HLayout_figname_PD")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_figname_PD.addItem(self.horizontalSpacer_2)

        self.VLayout_figname_label_PD = QVBoxLayout()
        self.VLayout_figname_label_PD.setSpacing(0)
        self.VLayout_figname_label_PD.setObjectName(u"VLayout_figname_label_PD")
        self.figname_label_PD = QLabel(self.frame_variables_PD)
        self.figname_label_PD.setObjectName(u"figname_label_PD")
        self.figname_label_PD.setMinimumSize(QSize(0, 20))
        self.figname_label_PD.setMaximumSize(QSize(16777215, 20))

        self.VLayout_figname_label_PD.addWidget(self.figname_label_PD)

        self.LineEdit_PD = QLineEdit(self.frame_variables_PD)
        self.LineEdit_PD.setObjectName(u"LineEdit_PD")
        self.LineEdit_PD.setMinimumSize(QSize(150, 25))
        self.LineEdit_PD.setMaximumSize(QSize(150, 25))

        self.VLayout_figname_label_PD.addWidget(self.LineEdit_PD)

        self.HLayout_figname_PD.addLayout(self.VLayout_figname_label_PD)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_figname_PD.addItem(self.horizontalSpacer)

        self.VLayout_figsave_PD.addLayout(self.HLayout_figname_PD)

        self.HLayout_savebutton_PD = QHBoxLayout()
        self.HLayout_savebutton_PD.setObjectName(u"HLayout_savebutton_PD")
        self.horizontalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_savebutton_PD.addItem(self.horizontalSpacer_8)

        self.savebutton_PD = QPushButton(self.frame_variables_PD)
        self.savebutton_PD.setObjectName(u"savebutton_PD")
        self.savebutton_PD.setMinimumSize(QSize(150, 30))
        self.savebutton_PD.setMaximumSize(QSize(150, 30))

        self.HLayout_savebutton_PD.addWidget(self.savebutton_PD)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_savebutton_PD.addItem(self.horizontalSpacer_7)

        self.VLayout_figsave_PD.addLayout(self.HLayout_savebutton_PD)

        self.gridLayout_6.addLayout(self.VLayout_figsave_PD, 2, 0, 1, 1)

        self.VLayout_VarButton_PD.addWidget(self.frame_variables_PD)

        self.verticalSpacer_PD = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLayout_VarButton_PD.addItem(self.verticalSpacer_PD)

        self.import_button_PD = QPushButton(self.main_frame_PD)
        self.import_button_PD.setObjectName(u"import_button_PD")
        self.import_button_PD.setMinimumSize(QSize(150, 30))
        self.import_button_PD.setMaximumSize(QSize(150, 30))

        self.VLayout_VarButton_PD.addWidget(self.import_button_PD)

        self.gridLayout_3.addLayout(self.VLayout_VarButton_PD, 0, 0, 1, 1)

        self.Fig_Frame_PD = QFrame(self.main_frame_PD)
        self.Fig_Frame_PD.setObjectName(u"Fig_Frame_PD")
        sizePolicy.setHeightForWidth(self.Fig_Frame_PD.sizePolicy().hasHeightForWidth())
        self.Fig_Frame_PD.setSizePolicy(sizePolicy)
        self.Fig_Frame_PD.setFrameShape(QFrame.Shape.StyledPanel)
        self.Fig_Frame_PD.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3.addWidget(self.Fig_Frame_PD, 0, 1, 1, 1)

        self.set_bar_layout()
        self.Fig_Frame_PD.setLayout(self.graph_layout_barplot)
        self.frame_buttons_animation_time.setDisabled(True)

        self.retranslateUi()

        self.stylesheet = """
            #main_frame_PD {
                background-color: #C3C3C3;
                border: none;
            }

            [commomFrame='true'] {
                border-radius: 10px;
                border: none;
                background-color: #C3C3C3;
            }

            QTableWidget {
                background-color: #C3C3C3;
                color: white;
                gridline-color: #4e5d5f;
                font-size: 14px;
                border: 1px solid #4e5d5f;
            }

            QHeaderView::section {
                background-color: #3f5e5e;
                color: white;
                padding: 4px;
                border: 1px solid #4e5d5f;
            }

            QTableWidget::item {
                selection-background-color: #5ca39d;
                selection-color: black;
                padding: 4px;
            }

            QScrollBar:vertical {
                background: #2d3e3f;
                width: 4px;
                margin: 0px;
            }

            QScrollBar::handle:vertical {
                background: #5ca39d;
                border-radius: 5px;
                min-height: 20px;
            }

            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }

            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """
        self.main_frame_PD.setStyleSheet(self.stylesheet)

        shadow_elements = {
            'savebutton_PD',
            'import_button_PD',
            'Fig_Frame_PD'
        }
        for x in shadow_elements:
            effect = QtWidgets.QGraphicsDropShadowEffect(self.main_frame_PD)
            effect.setBlurRadius(18)
            effect.setXOffset(0)
            effect.setYOffset(0)
            effect.setColor(QColor(0, 0, 0, 255))
            getattr(self, x).setGraphicsEffect(effect)

        self.file_list = {}

    def set_bar_layout(self):
        self.graph_layout_barplot = QVBoxLayout()
        self.figure_barplot = Figure()
        self.canvas_barplot = FigureCanvas(self.figure_barplot)
        self.graph_layout_barplot.addWidget(self.canvas_barplot)
        self.frame_buttons_animation_time = QFrame()
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
        self.graph_layout_barplot.addWidget(self.frame_buttons_animation_time, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout_7 = QGridLayout(self.frame_buttons_animation_time)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.start_button_time = QPushButton(self.frame_buttons_animation_time)
        self.start_button_time.setObjectName(u"start_button_time")
        icon = QIcon()
        icon.addFile(u":/icons/icons/backward - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start_button_time.setIcon(icon)
        self.start_button_time.setIconSize(QSize(20, 20))
        self.start_button_time.clicked.connect(self.firts_in_time)

        self.gridLayout_7.addWidget(self.start_button_time, 0, 0, 1, 1)

        self.backward_button_time = QPushButton(self.frame_buttons_animation_time)
        self.backward_button_time.setObjectName(u"backward_button_time")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/arrow-left - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backward_button_time.setIcon(icon1)
        self.backward_button_time.setIconSize(QSize(20, 20))
        self.backward_button_time.clicked.connect(self.back_in_time)

        self.gridLayout_7.addWidget(self.backward_button_time, 0, 1, 1, 1)

        self.pause_button_time = QPushButton(self.frame_buttons_animation_time)
        self.pause_button_time.setObjectName(u"pause_button_time")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/pause - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pause_button_time.setIcon(icon2)
        self.pause_button_time.setIconSize(QSize(20, 20))
        self.pause_button_time.setCheckable(True)
        self.pause_button_time.setChecked(False)

        self.gridLayout_7.addWidget(self.pause_button_time, 0, 2, 1, 1)

        self.play_button_time = QPushButton(self.frame_buttons_animation_time)
        self.play_button_time.setObjectName(u"play_button_time")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/play - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.play_button_time.setIcon(icon3)
        self.play_button_time.setIconSize(QSize(20, 20))
        self.play_button_time.setCheckable(False)
        self.play_button_time.clicked.connect(self.animation)

        self.gridLayout_7.addWidget(self.play_button_time, 0, 3, 1, 1)

        self.forward_button_time = QPushButton(self.frame_buttons_animation_time)
        self.forward_button_time.setObjectName(u"forward_button_time")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/arrow-right - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.forward_button_time.setIcon(icon4)
        self.forward_button_time.setIconSize(QSize(20, 20))
        self.forward_button_time.clicked.connect(self.forward_in_time)

        self.gridLayout_7.addWidget(self.forward_button_time, 0, 4, 1, 1)

        self.finish_button_time = QPushButton(self.frame_buttons_animation_time)
        self.finish_button_time.setObjectName(u"finish_button_time")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/forward - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.finish_button_time.setIcon(icon5)
        self.finish_button_time.setIconSize(QSize(20, 20))
        self.finish_button_time.clicked.connect(self.last_in_time)

        self.gridLayout_7.addWidget(self.finish_button_time, 0, 5, 1, 1)
        self.canvas_barplot.figure.set_facecolor("#C3C3C3")

    def read(self):
        if hasattr(self, "data_files"):
            del self.data_files
        if hasattr(self, "variables_list_for_ai"):
            del self.variables_list_for_ai

        self.description_names = []
        for key in self.file_list.keys():
            for row in range(self.file_table.rowCount()):
                item = self.file_table.item(row, 0)
                if item and item.text() == key:
                    self.file_list[key]["description"] = self.file_table.item(row, 1).text()
                    self.description_names.append(self.file_table.item(row, 1).text())

        colors = random.sample(Cr.colors, len(self.description_names))
        self.c_ref = dict(zip(self.description_names, colors))
        self.time_radio.setDisabled(False)
        self.mean_radio.setDisabled(False)
        self.time_radio.setChecked(True)
        self.frame_buttons_animation_time.setDisabled(False)
        self.replace_param()

    def set_meandf(self):
        mean_dict = {}
        indexs = []
        for _, item in self.file_list.items():
            df = Ppo.ParticleDistribution(item["path"]).dataframe
            if not hasattr(self, "columns_name"):
                self.columns_name = [key for key in df.keys()]
            mean_dict[item["description"]] = df
            indexs.append(item["description"])
        self.average_dataframe = Df(float(0), columns=self.columns_name, index=indexs)

        for key, values in mean_dict.items():
            for col in self.columns_name:
                self.average_dataframe.loc[key, col] = mean_dict[key][col]

        self.average_dataframe['description'] = self.average_dataframe.index
        self.plot_average()

    def get_time(self):
        times_from_values = []
        self.min_df, self.max_df = 0, 0

        for key, item in self.data_files.items():
            times_from_values.append(list(sorted(set(item.index))))
            min_, max_ = item.min().min(), item.max().max()
            self.min_df = min_ if min_ < self.min_df else self.min_df
            self.max_df = max_ if max_ > self.max_df else self.max_df

        isequal = all(lista == times_from_values[0] for lista in times_from_values) if times_from_values else False
        if isequal:
            self.time_values = times_from_values[0]
            self.actual_time = self.time_values[0]

        self.set_bar_plot()

    def replace_param(self):
        self.data_files = {}
        for _, item in self.file_list.items():
            df = Ppo.ParticleDistribution(item["path"]).data
            df = df.drop_duplicates(subset='time', keep="first")
            df = df.set_index("time")
            self.data_files[item["description"]] = df

            if not hasattr(self, "variables_list_for_ai"):
                self.variables_list_for_ai = list(df.columns)
        self.get_time()

    def abrir_dialogo_arquivo(self, row, column):
        if column == 0:  # Apenas se clicar na primeira coluna
            caminho, _ = QFileDialog.getOpenFileName(self.main_frame_PD, "Selecionar Arquivo", "",
                                                     "Arquivos de Texto (*.txt *.log *.prt)")
            if caminho:
                ai_df = Ppo.ParticleDistribution(caminho)
                if ai_df.dataframe is not None:
                    nome_arquivo = os.path.basename(caminho)
                    self.file_table.setItem(row, column, QTableWidgetItem(nome_arquivo))
                    self.file_list[nome_arquivo] = {
                        'path': caminho
                    }
                    del ai_df
                else:
                    print('não foi')

    def radio_vars(self):
        selected_button = self.radio_group.checkedButton()
        if selected_button:
            if selected_button.text() == "Time Filter":
                self.replace_param()
            else:
                self.frame_buttons_animation_time.setDisabled(True)
                self.set_meandf()

    def firts_in_time(self):
        if self.actual_time == self.time_values[0]:
            return
        else:
            self.actual_time = self.time_values[0]
            self.updateplot()

    def last_in_time(self):
        if self.actual_time == self.time_values[-1]:
            return
        else:
            self.actual_time = self.time_values[-1]
            self.updateplot()

    def forward_in_time(self):
        if self.actual_time == self.time_values[-1]:
            return
        else:
            index = self.time_values.index(self.actual_time)
            self.actual_time = self.time_values[index + 1]
            self.updateplot()

    def back_in_time(self):
        if self.actual_time == self.time_values[0]:
            return
        else:
            index = self.time_values.index(self.actual_time)
            self.actual_time = self.time_values[index - 1]
            self.updateplot()

    def animation(self):
        self.worker = AnimationWorker(page=self)
        self.worker.start()

    def play_animation(self):
        self.forward_button_time.setDisabled(True)
        self.finish_button_time.setDisabled(True)
        self.start_button_time.setDisabled(True)
        self.backward_button_time.setDisabled(True)
        self.play_button_time.setDisabled(True)
        while True:
            index = self.time_values.index(self.actual_time)
            self.actual_time = self.time_values[index + 1]
            self.updateplot()

            if self.pause_button_time.isChecked():
                break
            if self.actual_time == self.time_values[-1]:
                break

            time.sleep(.2)
        self.pause_button_time.setChecked(False)
        self.forward_button_time.setDisabled(False)
        self.finish_button_time.setDisabled(False)
        self.start_button_time.setDisabled(False)
        self.backward_button_time.setDisabled(False)
        self.play_button_time.setDisabled(False)

    def updateplot(self):
        self.ax_bar.clear()

        df_zero = self.df_concat.loc[self.actual_time, :]
        df_melted = df_zero.melt(id_vars='description', value_vars=self.variables_list_for_ai,
                                 var_name='category', value_name='value')

        self.bar = sns.barplot(
            data=df_melted, x='category', y='value', hue='description', palette=self.c_ref,
            ax=self.ax_bar, order=self.category_order, hue_order=self.hue_order
        )

        self.figure_barplot.suptitle(f"Time: {self.actual_time} days")
        self.ax_bar.set_ylabel("mT")
        self.ax_bar.set_xlabel("")
        self.ax_bar.legend(title=None)
        self.ax_bar.set_ylim(self.min_df, self.max_df)
        self.ax_bar.set_xticklabels(self.ax_bar.get_xticklabels(), fontsize=9)
        for label in self.ax_bar.get_xticklabels():
            label.set_rotation(25)
            label.set_horizontalalignment('right')
        plt.tight_layout()

        self.canvas_barplot.draw()

    def set_bar_plot(self):
        self.figure_barplot.clear()
        self.ax_bar = self.figure_barplot.add_subplot(111)

        for description, df in self.data_files.items():
            df['description'] = description

        self.df_concat = pd.concat([dataframe for _, dataframe in self.data_files.items()])
        df_zero = self.df_concat.loc[self.actual_time, :]
        # df_zero = self.df_concat[self.df_concat["time"] == self.actual_time]
        df_melted = df_zero.melt(id_vars='description', value_vars=self.variables_list_for_ai,
                                 var_name='category', value_name='value')

        self.category_order = pd.unique(df_melted['category'])
        self.hue_order = pd.unique(df_melted['description'])

        self.bar = sns.barplot(
            data=df_melted, x='category', y='value', hue='description', palette=self.c_ref,
            ax=self.ax_bar, order=self.category_order, hue_order=self.hue_order
        )

        self.figure_barplot.suptitle(f"Time: {self.actual_time} days")

        self.ax_bar.set_ylabel("mT")
        self.ax_bar.set_xlabel("")
        self.ax_bar.legend(title=None)
        self.ax_bar.set_ylim(self.min_df, self.max_df)
        self.ax_bar.set_xticklabels(self.ax_bar.get_xticklabels(), fontsize=9)
        for label in self.ax_bar.get_xticklabels():
            label.set_rotation(25)
            label.set_horizontalalignment('right')
        plt.tight_layout()

        self.canvas_barplot.draw()

    def plot_average(self):
        self.ax_bar.clear()

        df_melted = self.average_dataframe.melt(id_vars='description', value_vars=self.variables_list_for_ai,
                                 var_name='category', value_name='value')

        self.bar = sns.barplot(
            data=df_melted, x='category', y='value', hue='description', palette=self.c_ref,
            ax=self.ax_bar, order=self.category_order, hue_order=self.hue_order
        )

        self.figure_barplot.suptitle(f"Time: {self.actual_time} days")
        self.ax_bar.set_ylabel("mT")
        self.ax_bar.set_xlabel("Diameter")
        self.ax_bar.legend(title=None)
        self.ax_bar.set_ylim(self.average_dataframe[self.columns_name].min().min(),
                             self.average_dataframe[self.columns_name].max().max())
        self.ax_bar.set_xticklabels(self.ax_bar.get_xticklabels(), fontsize=9)
        for label in self.ax_bar.get_xticklabels():
            label.set_rotation(25)
            label.set_horizontalalignment('right')
        plt.tight_layout()

        self.canvas_barplot.draw()

    def retranslateUi(self):
        # self.BarPlot_AI.setTitle(QCoreApplication.translate("Form", u"Bar Plot", None))
        self.figname_label_PD.setText(QCoreApplication.translate("Form", u"Fig name", None))
        self.savebutton_PD.setText(QCoreApplication.translate("Form", u"Save Figure", None))
        self.import_button_PD.setText(QCoreApplication.translate("Form", u"Import to Project", None))
