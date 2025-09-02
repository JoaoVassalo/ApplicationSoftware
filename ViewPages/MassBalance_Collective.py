# -*- coding: utf-8 -*-
import pandas as pd
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
        self.main_frame_MB = frame

        self.main_frame_MB.setObjectName(u"main_frame_MB")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame_MB.sizePolicy().hasHeightForWidth())
        self.main_frame_MB.setSizePolicy(sizePolicy)
        self.main_frame_MB.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame_MB.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.main_frame_MB)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.VLayout_VarButton_MB = QVBoxLayout()
        self.VLayout_VarButton_MB.setSpacing(0)
        self.VLayout_VarButton_MB.setObjectName(u"VLayout_VarButton_MB")

        self.frame_variables_MB = QFrame(self.main_frame_MB)
        self.frame_variables_MB.setObjectName(u"frame_variables_MB")
        self.frame_variables_MB.setProperty("commomFrame", True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_variables_MB.sizePolicy().hasHeightForWidth())
        self.frame_variables_MB.setSizePolicy(sizePolicy1)
        self.frame_variables_MB.setMinimumSize(QSize(300, 0))
        self.frame_variables_MB.setMaximumSize(QSize(300, 16777215))
        self.frame_variables_MB.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_variables_MB.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_variables_MB)
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
        self.h_spacer_1 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_radio.addItem(self.h_spacer_1)

        self.line_radio = QRadioButton("Line Plot")
        self.line_radio.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.line_radio.clicked.connect(self.radio_vars)

        self.Bar_radio = QRadioButton("Bar Plot")
        self.Bar_radio.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.Bar_radio.clicked.connect(self.radio_vars)

        # Agrupando os botões
        self.radio_group = QButtonGroup()
        self.radio_group.addButton(self.line_radio)
        self.radio_group.addButton(self.Bar_radio)

        # Adicionando diretamente ao layout
        self.horizontalLayout_radio.addWidget(self.line_radio)
        self.horizontalLayout_radio.addWidget(self.Bar_radio)

        self.h_spacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_radio.addItem(self.h_spacer_2)

        self.gridLayout_6.addLayout(self.horizontalLayout_radio, 1, 0, 1, 1)

        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)

        self.HLayout_lineplot_MB = QHBoxLayout()
        self.HLayout_lineplot_MB.setObjectName(u"HLayout_lineplot_MB")
        self.horizontalSpacer_3 = QSpacerItem(5, 5, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.HLayout_lineplot_MB.addItem(self.horizontalSpacer_3)
        self.LinePlot_MB = QGroupBox()  # self.frame_variables_MB
        self.LinePlot_MB.setObjectName(u"LinePlot_MB")
        # sizePolicy2.setHeightForWidth(self.LinePlot_MB.sizePolicy().hasHeightForWidth())
        # self.LinePlot_MB.setSizePolicy(sizePolicy2)
        self.LinePlot_MB.setMinimumSize(QSize(150, 130))
        self.LinePlot_MB.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.vL_LinePlot_MB = QVBoxLayout(self.LinePlot_MB)
        self.vL_LinePlot_MB.setObjectName("vL_LinePlot_MB")
        self.HLayout_lineplot_MB.addWidget(self.LinePlot_MB)

        self.scrollArea = QScrollArea(self.LinePlot_MB)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.scrollAreaWidgetContent = QWidget()
        self.scrollArea.setWidget(self.scrollAreaWidgetContent)
        self.layoutscroll = QVBoxLayout()
        self.layoutscroll.setContentsMargins(5, 5, 5, 5)
        self.layoutscroll.setSpacing(5)
        self.scrollAreaWidgetContent.setLayout(self.layoutscroll)
        self.scrollAreaWidgetContent.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        self.scrollAreaWidgetContent.setMinimumWidth(150)
        # self.scrollAreaWidgetContent.adjustSize()
        self.vL_LinePlot_MB.addWidget(self.scrollArea)

        self.radio_linegroup = QButtonGroup()


        self.horizontalSpacer_4 = QSpacerItem(5, 5, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.HLayout_lineplot_MB.addItem(self.horizontalSpacer_4)
        self.gridLayout_6.addLayout(self.HLayout_lineplot_MB, 2, 0, 1, 1)

        self.VLayout_figsave_MB = QVBoxLayout()
        self.VLayout_figsave_MB.setObjectName(u"VLayout_figsave_MB")
        self.HLayout_figname_MB = QHBoxLayout()
        self.HLayout_figname_MB.setObjectName(u"HLayout_figname_MB")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_figname_MB.addItem(self.horizontalSpacer_2)

        self.VLayout_figname_label_MB = QVBoxLayout()
        self.VLayout_figname_label_MB.setSpacing(0)
        self.VLayout_figname_label_MB.setObjectName(u"VLayout_figname_label_MB")
        self.figname_label_MB = QLabel(self.frame_variables_MB)
        self.figname_label_MB.setObjectName(u"figname_label_MB")
        self.figname_label_MB.setMinimumSize(QSize(0, 20))
        self.figname_label_MB.setMaximumSize(QSize(16777215, 20))

        self.VLayout_figname_label_MB.addWidget(self.figname_label_MB)

        self.LineEdit_MB = QLineEdit(self.frame_variables_MB)
        self.LineEdit_MB.setObjectName(u"LineEdit_MB")
        self.LineEdit_MB.setMinimumSize(QSize(150, 25))
        self.LineEdit_MB.setMaximumSize(QSize(150, 25))

        self.VLayout_figname_label_MB.addWidget(self.LineEdit_MB)

        self.HLayout_figname_MB.addLayout(self.VLayout_figname_label_MB)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_figname_MB.addItem(self.horizontalSpacer)

        self.VLayout_figsave_MB.addLayout(self.HLayout_figname_MB)

        self.HLayout_savebutton_MB = QHBoxLayout()
        self.HLayout_savebutton_MB.setObjectName(u"HLayout_savebutton_MB")
        self.horizontalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_savebutton_MB.addItem(self.horizontalSpacer_8)

        self.savebutton_MB = QPushButton(self.frame_variables_MB)
        self.savebutton_MB.setObjectName(u"savebutton_MB")
        self.savebutton_MB.setMinimumSize(QSize(150, 30))
        self.savebutton_MB.setMaximumSize(QSize(150, 30))

        self.HLayout_savebutton_MB.addWidget(self.savebutton_MB)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_savebutton_MB.addItem(self.horizontalSpacer_7)

        self.VLayout_figsave_MB.addLayout(self.HLayout_savebutton_MB)

        self.gridLayout_6.addLayout(self.VLayout_figsave_MB, 3, 0, 1, 1)

        self.VLayout_VarButton_MB.addWidget(self.frame_variables_MB)

        self.verticalSpacer_MB = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLayout_VarButton_MB.addItem(self.verticalSpacer_MB)

        self.import_button_MB = QPushButton(self.main_frame_MB)
        self.import_button_MB.setObjectName(u"import_button_MB")
        self.import_button_MB.setMinimumSize(QSize(150, 30))
        self.import_button_MB.setMaximumSize(QSize(150, 30))

        self.VLayout_VarButton_MB.addWidget(self.import_button_MB)

        self.gridLayout_3.addLayout(self.VLayout_VarButton_MB, 0, 0, 1, 1)

        self.Fig_Frame_MB = QFrame(self.main_frame_MB)
        self.Fig_Frame_MB.setObjectName(u"Fig_Frame_MB")
        sizePolicy.setHeightForWidth(self.Fig_Frame_MB.sizePolicy().hasHeightForWidth())
        self.Fig_Frame_MB.setSizePolicy(sizePolicy)
        self.Fig_Frame_MB.setFrameShape(QFrame.Shape.StyledPanel)
        self.Fig_Frame_MB.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3.addWidget(self.Fig_Frame_MB, 0, 1, 1, 1)

        self.stacked_layout = QStackedLayout()
        self.line_plot_widget = QWidget()
        self.set_line_layout()
        self.line_plot_widget.setLayout(self.graph_layout_lineplot)
        self.bar_plot_widget = QWidget()
        self.set_bar_layout()
        self.bar_plot_widget.setLayout(self.graph_layout_barplot)

        self.stacked_layout.addWidget(self.line_plot_widget)
        self.stacked_layout.addWidget(self.bar_plot_widget)
        self.Fig_Frame_MB.setLayout(self.stacked_layout)

        self.retranslateUi()
        self.line_variables = []

        self.stylesheet = """
            #main_frame_MB {
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
        self.main_frame_MB.setStyleSheet(self.stylesheet)

        shadow_elements = {
            'savebutton_MB',
            'import_button_MB',
            'Fig_Frame_MB'
        }
        for x in shadow_elements:
            effect = QtWidgets.QGraphicsDropShadowEffect(self.main_frame_MB)
            effect.setBlurRadius(18)
            effect.setXOffset(0)
            effect.setYOffset(0)
            effect.setColor(QColor(0, 0, 0, 255))
            getattr(self, x).setGraphicsEffect(effect)

        self.file_list = {}

    def set_bar_layout(self):
        self.graph_layout_barplot = QVBoxLayout()
        self.figure_barplot = Figure()
        # self.figure_barplot, self.ax_bar = plt.subplots()
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

    def set_line_layout(self):
        self.graph_layout_lineplot = QVBoxLayout()
        self.figure_lineplot, self.ax_line = plt.subplots()
        self.canvas_lineplot = FigureCanvas(self.figure_lineplot)
        self.toolbar_lineplot = NavigationToolbar(self.canvas_lineplot)
        # self.toolbar = CustomNavigationToolbar(self.canvas, self.frame)  # Use the custom toolbar
        self.graph_layout_lineplot.addWidget(self.toolbar_lineplot)
        self.graph_layout_lineplot.addWidget(self.canvas_lineplot)
        self.canvas_lineplot.figure.set_facecolor("#C3C3C3")
        self.canvas_lineplot.setStyleSheet(
            "border: none;"
        )

    def radio_vars(self):
        selected_button = self.radio_group.checkedButton()
        if selected_button:
            if selected_button.text() == "Line Plot":
                self.set_page(var="L")
            else:
                self.set_page(var="B")

    def read(self):
        if hasattr(self, "data_files"):
            del self.data_files
        if hasattr(self, "line_variables"):
            del self.line_variables

        self.line_variables = []

        while self.layoutscroll.count():
            item = self.layoutscroll.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)

        self.description_names = []
        for key in self.file_list.keys():
            for row in range(self.file_table.rowCount()):
                item = self.file_table.item(row, 0)
                if item and item.text() == key:
                    self.file_list[key]["description"] = self.file_table.item(row, 1).text()
                    self.description_names.append(self.file_table.item(row, 1).text())

    def get_time(self):
        times_from_values = []
        self.min_df, self.max_df = 0, 0

        for key, item in self.data_files.items():
            self.data_files[key] = item.drop_duplicates(subset='time(days)', keep='first')
            times_from_values.append(list(sorted(set(item.iloc[:, 0]))))
            min_, max_ = item.min().min(), item.max().max()
            self.min_df = min_ if min_ < self.min_df else self.min_df
            self.max_df = max_ if max_ > self.max_df else self.max_df

        isequal = all(lista == times_from_values[0] for lista in times_from_values) if times_from_values else False
        if isequal:
            self.time_values = times_from_values[0]
            self.actual_time = self.time_values[0]

    def replace_param(self, type_):
        self.data_files = {}
        for _, item in self.file_list.items():
            df = Ppo.MassBalance(item["path"]).dataframe

            if not hasattr(self, "variables_list_for_ai"):
                var_list_cols = list(df.columns)
                self.x_value_col = var_list_cols[0]
                var_list_cols.pop(0)
                self.variables_list_for_ai = [value.replace("(mt)", f"").strip() for value in var_list_cols]

            novo_nome = {
                col: col.replace("(mt)", f" {item['description']}").strip()
                if type_ == "L" else col.replace("(mt)", f"").strip()
                for col in df.columns
            }
            df.rename(columns=novo_nome, inplace=True)
            self.data_files[item["description"]] = df

        self.variables_labels = []
        for _, item in self.data_files.items():
            for col in item.columns:
                if col != self.x_value_col:
                    self.variables_labels.append(col)

    def abrir_dialogo_arquivo(self, row, column):
        if column == 0:  # Apenas se clicar na primeira coluna
            caminho, _ = QFileDialog.getOpenFileName(self.main_frame_MB, "Selecionar Arquivo", "",
                                                     "Arquivos de Texto (*.txt *.log *.prt)")
            if caminho:
                ai_df = Ppo.MassBalance(caminho)
                if ai_df.dataframe is not None:
                    nome_arquivo = os.path.basename(caminho)
                    self.file_table.setItem(row, column, QTableWidgetItem(nome_arquivo))
                    self.file_list[nome_arquivo] = {
                        'path': caminho
                    }
                    del ai_df
                else:
                    print('não foi')

    def on_cb_line_selected(self, line):
        selectec_curve = self.radio_linegroup.checkedButton()
        if selectec_curve:
            self.plot_line(selectec_curve.text())

    def set_page(self, var):
        while self.layoutscroll.count():
            item = self.layoutscroll.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)

        if var == "L":
            self.scrollAreaWidgetContent.setDisabled(False)
            self.stacked_layout.setCurrentIndex(0)

            self.replace_param(type_="L")

            colors = random.sample(Cr.colors, len(self.variables_labels))
            self.c_ref = dict(zip(self.variables_labels, colors))
        else:
            self.scrollAreaWidgetContent.setDisabled(True)
            self.stacked_layout.setCurrentIndex(1)

            self.replace_param(type_="B")
            self.get_time()

            colors = random.sample(Cr.colors, len(self.description_names))
            self.c_ref = dict(zip(self.description_names, colors))

            self.set_bar_plot()

        for var_ in self.variables_list_for_ai:
            radio_line = QRadioButton(text=var_)
            radio_line.clicked.connect(lambda checked, cb=radio_line: self.on_cb_line_selected(cb))
            radio_line.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            self.radio_linegroup.addButton(radio_line)
            self.layoutscroll.addWidget(radio_line)

    def plot_line(self, column_selected):
        min_yaxis, max_yaxis = 0, 0
        self.ax_line.clear()

        for col in self.variables_list_for_ai:
            if column_selected == col:
                for _, item in self.data_files.items():
                    for variable in item.columns:
                        if col in variable:
                            min_yaxis = min(item[variable]) if min(item[variable]) < min_yaxis else min_yaxis
                            max_yaxis = max(item[variable]) if max(item[variable]) > max_yaxis else max_yaxis

                            self.ax_line.plot(
                                item[self.x_value_col],
                                item[variable],
                                label=f"{variable}",
                                color=self.c_ref[variable]
                            )

                self.ax_line.legend(loc="upper left")
                self.ax_line.set_xlabel(self.x_value_col)
                self.ax_line.set_ylabel(f"{column_selected} [mt]")
                self.ax_line.grid()
                self.canvas_lineplot.draw()

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

        df_zero = self.df_concat[self.df_concat[self.x_value_col] == self.actual_time]
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
            label.set_rotation(15)
            label.set_horizontalalignment('right')
        plt.tight_layout()

        self.canvas_barplot.draw()

    def set_bar_plot(self):
        self.figure_barplot.clear()
        self.ax_bar = self.figure_barplot.add_subplot(111)

        for description, df in self.data_files.items():
            df['description'] = description

        self.df_concat = pd.concat([dataframe for _, dataframe in self.data_files.items()])
        df_zero = self.df_concat[self.df_concat[self.x_value_col] == self.actual_time]
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
            label.set_rotation(15)
            label.set_horizontalalignment('right')
        plt.tight_layout()

        self.canvas_barplot.draw()

    def retranslateUi(self):
        # self.BarPlot_AI.setTitle(QCoreApplication.translate("Form", u"Bar Plot", None))
        self.LinePlot_MB.setTitle(QCoreApplication.translate("Form", u"Line Plot", None))
        self.figname_label_MB.setText(QCoreApplication.translate("Form", u"Fig name", None))
        self.savebutton_MB.setText(QCoreApplication.translate("Form", u"Save Figure", None))
        self.import_button_MB.setText(QCoreApplication.translate("Form", u"Import to Project", None))
