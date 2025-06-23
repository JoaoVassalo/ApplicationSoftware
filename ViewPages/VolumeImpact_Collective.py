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
                               QSizePolicy, QSpacerItem, QVBoxLayout, QCheckBox)
from PySide6.QtWidgets import (
    QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QFileDialog, QAbstractItemView, QAbstractScrollArea
)
from PySide6.QtCore import Qt
import sys
import os
from PySide6.QtGui import QColor
from PySide6 import QtWidgets
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from Functions import ColorReference as Cr
import random
from Functions import PosProcessOSCAR as Ppo


class Ui_Form:
    def setupUi(self, frame):
        self.main_frame_VI = frame

        self.main_frame_VI.setObjectName(u"main_frame_VI")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame_VI.sizePolicy().hasHeightForWidth())
        self.main_frame_VI.setSizePolicy(sizePolicy)
        self.main_frame_VI.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame_VI.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.main_frame_VI)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.VLayout_VarButton_VI = QVBoxLayout()
        self.VLayout_VarButton_VI.setSpacing(0)
        self.VLayout_VarButton_VI.setObjectName(u"VLayout_VarButton_VI")

        self.frame_variables_VI = QFrame(self.main_frame_VI)
        self.frame_variables_VI.setObjectName(u"frame_variables_VI")
        self.frame_variables_VI.setProperty("commomFrame", True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_variables_VI.sizePolicy().hasHeightForWidth())
        self.frame_variables_VI.setSizePolicy(sizePolicy1)
        self.frame_variables_VI.setMinimumSize(QSize(300, 0))
        self.frame_variables_VI.setMaximumSize(QSize(300, 16777215))
        self.frame_variables_VI.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_variables_VI.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_variables_VI)
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

        # self.HLayout_barplot_AI = QHBoxLayout()
        # self.HLayout_barplot_AI.setObjectName(u"HLayout_barplot_AI")
        # self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        # self.HLayout_barplot_AI.addItem(self.horizontalSpacer_6)
        # self.BarPlot_AI = QGroupBox(self.frame_variables_VI)
        # self.BarPlot_AI.setObjectName(u"BarPlot_AI")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        # sizePolicy2.setHeightForWidth(self.BarPlot_AI.sizePolicy().hasHeightForWidth())
        # self.BarPlot_AI.setSizePolicy(sizePolicy2)
        # self.BarPlot_AI.setMinimumSize(QSize(0, 130))
        # self.BarPlot_AI.setMaximumSize(QSize(16777215, 130))
        # self.vL_BarPlot_AI = QVBoxLayout(self.BarPlot_AI)
        # self.vL_BarPlot_AI.setObjectName(u"verticalLayout")
        # self.HLayout_barplot_AI.addWidget(self.BarPlot_AI)
        # self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        # self.HLayout_barplot_AI.addItem(self.horizontalSpacer_5)
        # self.gridLayout_6.addLayout(self.HLayout_barplot_AI, 1, 0, 1, 1)

        self.HLayout_lineplot_VI = QHBoxLayout()
        self.HLayout_lineplot_VI.setObjectName(u"HLayout_lineplot_VI")
        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.HLayout_lineplot_VI.addItem(self.horizontalSpacer_3)
        self.LinePlot_VI = QGroupBox(self.frame_variables_VI)
        self.LinePlot_VI.setObjectName(u"LinePlot_VI")
        sizePolicy2.setHeightForWidth(self.LinePlot_VI.sizePolicy().hasHeightForWidth())
        self.LinePlot_VI.setSizePolicy(sizePolicy2)
        self.LinePlot_VI.setMinimumSize(QSize(0, 130))
        self.LinePlot_VI.setMaximumSize(QSize(16777215, 130))
        self.vL_LinePlot_VI = QVBoxLayout(self.LinePlot_VI)
        self.vL_LinePlot_VI.setObjectName("vL_LinePlot_VI")
        self.HLayout_lineplot_VI.addWidget(self.LinePlot_VI)
        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.HLayout_lineplot_VI.addItem(self.horizontalSpacer_4)
        self.gridLayout_6.addLayout(self.HLayout_lineplot_VI, 1, 0, 1, 1)

        self.VLayout_figsave_VI = QVBoxLayout()
        self.VLayout_figsave_VI.setObjectName(u"VLayout_figsave_VI")
        self.HLayout_figname_VI = QHBoxLayout()
        self.HLayout_figname_VI.setObjectName(u"HLayout_figname_VI")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_figname_VI.addItem(self.horizontalSpacer_2)

        self.VLayout_figname_label_VI = QVBoxLayout()
        self.VLayout_figname_label_VI.setSpacing(0)
        self.VLayout_figname_label_VI.setObjectName(u"VLayout_figname_label_VI")
        self.figname_label_VI = QLabel(self.frame_variables_VI)
        self.figname_label_VI.setObjectName(u"figname_label_VI")
        self.figname_label_VI.setMinimumSize(QSize(0, 20))
        self.figname_label_VI.setMaximumSize(QSize(16777215, 20))

        self.VLayout_figname_label_VI.addWidget(self.figname_label_VI)

        self.LineEdit_VI = QLineEdit(self.frame_variables_VI)
        self.LineEdit_VI.setObjectName(u"LineEdit_VI")
        self.LineEdit_VI.setMinimumSize(QSize(150, 25))
        self.LineEdit_VI.setMaximumSize(QSize(150, 25))

        self.VLayout_figname_label_VI.addWidget(self.LineEdit_VI)

        self.HLayout_figname_VI.addLayout(self.VLayout_figname_label_VI)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_figname_VI.addItem(self.horizontalSpacer)

        self.VLayout_figsave_VI.addLayout(self.HLayout_figname_VI)

        self.HLayout_savebutton_VI = QHBoxLayout()
        self.HLayout_savebutton_VI.setObjectName(u"HLayout_savebutton_VI")
        self.horizontalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_savebutton_VI.addItem(self.horizontalSpacer_8)

        self.savebutton_AI = QPushButton(self.frame_variables_VI)
        self.savebutton_AI.setObjectName(u"savebutton_AI")
        self.savebutton_AI.setMinimumSize(QSize(150, 30))
        self.savebutton_AI.setMaximumSize(QSize(150, 30))

        self.HLayout_savebutton_VI.addWidget(self.savebutton_AI)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_savebutton_VI.addItem(self.horizontalSpacer_7)

        self.VLayout_figsave_VI.addLayout(self.HLayout_savebutton_VI)

        self.gridLayout_6.addLayout(self.VLayout_figsave_VI, 2, 0, 1, 1)

        self.VLayout_VarButton_VI.addWidget(self.frame_variables_VI)

        self.verticalSpacer_VI = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLayout_VarButton_VI.addItem(self.verticalSpacer_VI)

        self.import_button_VI = QPushButton(self.main_frame_VI)
        self.import_button_VI.setObjectName(u"import_button_VI")
        self.import_button_VI.setMinimumSize(QSize(150, 30))
        self.import_button_VI.setMaximumSize(QSize(150, 30))

        self.VLayout_VarButton_VI.addWidget(self.import_button_VI)

        self.gridLayout_3.addLayout(self.VLayout_VarButton_VI, 0, 0, 1, 1)

        self.Fig_Frame_VI = QFrame(self.main_frame_VI)
        self.Fig_Frame_VI.setObjectName(u"Fig_Frame_VI")
        sizePolicy.setHeightForWidth(self.Fig_Frame_VI.sizePolicy().hasHeightForWidth())
        self.Fig_Frame_VI.setSizePolicy(sizePolicy)
        self.Fig_Frame_VI.setFrameShape(QFrame.Shape.StyledPanel)
        self.Fig_Frame_VI.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_3.addWidget(self.Fig_Frame_VI, 0, 1, 1, 1)

        self.hori_frame = QHBoxLayout(self.Fig_Frame_VI)

        self.retranslateUi()
        self.bar_variables = []
        self.line_variables = []
        self.graph_layout = QVBoxLayout()
        self.figure, self.ax_mass = plt.subplots()  # Figure(figsize=(6, 6))
        self.ax_area = self.ax_mass.twinx()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.Fig_Frame_VI)
        # self.toolbar = CustomNavigationToolbar(self.canvas, self.frame)  # Use the custom toolbar
        self.graph_layout.addWidget(self.toolbar)
        self.graph_layout.addWidget(self.canvas)
        self.hori_frame.addLayout(self.graph_layout)
        self.Fig_Frame_VI.setLayout(self.hori_frame)

        self.canvas.figure.set_facecolor("#C3C3C3")

        self.stylesheet = """
            #main_frame_VI {
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
        self.main_frame_VI.setStyleSheet(self.stylesheet)

        shadow_elements = {
            'savebutton_AI',
            'import_button_VI',
            'Fig_Frame_VI'
        }
        for x in shadow_elements:
            effect = QtWidgets.QGraphicsDropShadowEffect(self.main_frame_VI)
            effect.setBlurRadius(18)
            effect.setXOffset(0)
            effect.setYOffset(0)
            effect.setColor(QColor(0, 0, 0, 255))
            getattr(self, x).setGraphicsEffect(effect)

        self.file_list = {}

    def read(self):
        if hasattr(self, "data_files"):
            del self.data_files
        if hasattr(self, "line_variables"):
            del self.line_variables

        self.line_variables = []

        while self.vL_LinePlot_VI.count():
            item = self.vL_LinePlot_VI.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)

        for key in self.file_list.keys():
            for row in range(self.file_table.rowCount()):
                item = self.file_table.item(row, 0)
                if item and item.text() == key:
                    self.file_list[key]["description"] = self.file_table.item(row, 1).text()

        self.data_files = {}
        for _, item in self.file_list.items():
            df = Ppo.TotalConc(item["path"]).dataframe
            if not hasattr(self, "variables_list_for_ai"):
                self.variables_list_for_ai = list(df.columns)
                self.x_value_col = self.variables_list_for_ai[0]
                self.variables_list_for_ai.pop(0)
            novo_nome = {
                col: col.replace("[ton]", f"{item['description']}").replace("[km³]", f"{item['description']}").strip()
                for col in df.columns
            }
            df.rename(columns=novo_nome, inplace=True)
            self.data_files[item["description"]] = df

        self.set_graph()
        self.set_page()

    def abrir_dialogo_arquivo(self, row, column):
        if column == 0:  # Apenas se clicar na primeira coluna
            caminho, _ = QFileDialog.getOpenFileName(self.main_frame_VI, "Selecionar Arquivo", "",
                                                     "Arquivos de Texto (*.txt *.log *.prt)")
            if caminho:
                ai_df = Ppo.TotalConc(caminho)
                if ai_df.dataframe is not None:
                    nome_arquivo = os.path.basename(caminho)
                    self.file_table.setItem(row, column, QTableWidgetItem(nome_arquivo))
                    self.file_list[nome_arquivo] = {
                        'path': caminho
                    }
                    del ai_df
                else:
                    print('não foi')

    def on_cb_bar_selected(self, bar):
        if bar.isChecked():
            if len(self.bar_variables) == 0:
                for i in range(self.vL_LinePlot_VI.count()):
                    widget = self.vL_LinePlot_VI.itemAt(i).widget()
                    if isinstance(widget, QCheckBox):
                        widget.blockSignals(True)
                        widget.setChecked(False)
                        widget.blockSignals(False)
                        self.line_variables.remove(widget.text()) if widget.text() in self.line_variables else None

            self.bar_variables.append(bar.text())
            self.plot_bar()
        else:
            self.bar_variables.remove(bar.text())
            self.plot_bar()

    def on_cb_line_selected(self, line):
        if line.isChecked():
            # if len(self.line_variables) == 0:
            #     for i in range(self.vL_BarPlot_AI.count()):
            #         widget = self.vL_BarPlot_AI.itemAt(i).widget()
            #         if isinstance(widget, QCheckBox):
            #             widget.blockSignals(True)
            #             widget.setChecked(False)
            #             widget.blockSignals(False)
            #             self.bar_variables.remove(widget.text()) if widget.text() in self.bar_variables else None

            self.line_variables.append(line.text())
            self.plot_line()
        else:
            self.line_variables.remove(line.text())
            self.plot_line()

    def set_page(self):
        for var_ in self.variables_list_for_ai:
            # checkbutton_bar = QCheckBox(text=var_, parent=self.BarPlot_AI)
            # checkbutton_bar.clicked.connect(lambda checked, cb=checkbutton_bar: self.on_cb_bar_selected(cb))
            # self.vL_BarPlot_AI.addWidget(checkbutton_bar)

            checkbutton_line = QCheckBox(text=var_, parent=self.LinePlot_VI)
            checkbutton_line.clicked.connect(lambda checked, cb=checkbutton_line: self.on_cb_line_selected(cb))
            self.vL_LinePlot_VI.addWidget(checkbutton_line)

        self.variables_labels = []
        for _, item in self.data_files.items():
            for col in item.columns:
                if col != self.x_value_col:
                    self.variables_labels.append(col)

        colors = random.sample(Cr.colors, len(self.variables_labels))
        self.c_ref = dict(zip(self.variables_labels, colors))

        units = [self.ax_mass if nm.startswith("Polluting Mass") else self.ax_area for nm in self.variables_labels]
        self.ax_ref = dict(zip(self.variables_labels, units))

        min_max_mass = []
        min_max_area = []
        for _, item in self.data_files.items():
            for nmvar in item.columns:
                if nmvar.startswith('Polluting Mass'):
                    min_max_mass.append(item[nmvar].max())
                elif not nmvar.startswith("Polluting Mass") and nmvar != self.x_value_col:
                    min_max_area.append(item[nmvar].max())
        self.min_max_mass = min(min_max_mass)
        self.min_max_area = min(min_max_area)

    def plot_line(self):
        min_mass, max_mass = 0, self.min_max_mass
        min_area, max_area = 0, self.min_max_area
        for col in self.line_variables:
            for _, item in self.data_files.items():
                if col.startswith("Polluting Mass"):
                    for coldf in item.columns:
                        if coldf.startswith("Polluting Mass"):
                            min_mass = item[coldf].min() if item[coldf].min() < min_mass else min_mass
                            max_mass = item[coldf].max() if item[coldf].max() > max_mass else max_mass
                else:
                    for coldf in item.columns:
                        if not coldf.startswith("Polluting Mass") and coldf != self.x_value_col and col.split("[")[
                            0] in coldf:
                            min_area = item[coldf].min() if item[coldf].min() < min_area else min_area
                            max_area = item[coldf].max() if item[coldf].max() > max_area else max_area

        self.set_graph(min_mass=min_mass, max_mass=max_mass, min_area=min_area, max_area=max_area)

        for col in self.line_variables:
            col = col.split('[')[0]
            for _, item in self.data_files.items():
                for coldf in item.columns:
                    if col in coldf:
                        self.ax_ref[coldf].plot(
                            item[self.x_value_col],
                            item[coldf],
                            label=f"{coldf}",
                            color=self.c_ref[coldf]
                        )
            self.ax_mass.legend(loc="upper left")
            self.ax_area.legend(loc="upper right")
        self.update_grid()
        self.canvas.draw()
        return

    def plot_bar(self):
        # min_mass, max_mass = 0, self.min_max_mass
        # min_area, max_area = 0, self.min_max_area
        # for col in self.bar_variables:
        #     if "[ton]" in col:
        #         min_mass = self.data.dataframe[col].min() if self.data.dataframe[col].min() < min_mass else min_mass
        #         max_mass = self.data.dataframe[col].max() if self.data.dataframe[col].max() > max_mass else max_mass
        #     else:
        #         min_area = self.data.dataframe[col].min() if self.data.dataframe[col].min() < min_area else min_area
        #         max_area = self.data.dataframe[col].max() if self.data.dataframe[col].max() > max_area else max_area
        #
        # self.set_graph(min_mass=min_mass, max_mass=max_mass, min_area=min_area, max_area=max_area)
        #
        # for col in self.bar_variables:
        #     self.ax_ref[col].bar(
        #         self.data.dataframe[self.x_value_col],
        #         self.data.dataframe[col],
        #         label=f"{col}",
        #         color=self.c_ref[col]
        #     )
        #     self.ax_mass.legend(loc="upper left")
        #     self.ax_area.legend(loc="upper right")
        # self.update_grid()
        # self.canvas.draw()
        return

    def update_grid(self):
        """Ativa a grade do eixo correspondente aos dados plotados."""
        has_data_on_mass = len(self.ax_mass.lines) > 0  # Verifica se há curvas no eixo primário
        has_data_on_area = len(self.ax_area.lines) > 0  # Verifica se há curvas no eixo secundário

        if has_data_on_mass and has_data_on_area:
            # Ambos os eixos têm dados: Sincronizar grades
            self.ax_mass.grid(True, linestyle="--", color='gray', axis="both")
            self.ax_area.grid(False, axis="both")
        elif has_data_on_mass:
            # Apenas o eixo primário tem dados
            self.ax_mass.grid(True, linestyle="--", color='gray', axis="both")
            self.ax_area.grid(False, axis="both")
        elif has_data_on_area:
            # Apenas o eixo secundário tem dados
            self.ax_area.grid(True, linestyle="--", color='black', axis="y")
            self.ax_mass.grid(True, linestyle="--", color="black", axis="x")
        else:
            # Nenhum dado (pode desativar as grades)
            self.ax_mass.grid(False, axis="both")
            self.ax_area.grid(False, axis="both")
        self.canvas.draw()
        return

    def set_graph(self, **kwargs):
        self.ax_mass.clear()
        self.ax_area.clear()

        self.ax_mass.set_xlabel("Time (days)", fontsize=10)
        self.ax_mass.set_ylabel("Mass [ton]", fontsize=10)
        self.ax_mass.yaxis.set_label_position("left")
        self.ax_mass.yaxis.tick_left()

        self.ax_area.set_xlabel("Time (days)", fontsize=10)
        self.ax_area.set_ylabel("Volume [km³]", fontsize=10)
        self.ax_area.yaxis.set_label_position("right")
        self.ax_area.yaxis.tick_right()

        if kwargs:
            mass_ticks = np.linspace(kwargs["min_mass"],
                                     kwargs["max_mass"],
                                     8)
            area_ticks = np.linspace(kwargs["min_area"],
                                     kwargs["max_area"],
                                     8)
        else:
            mass_lists = [item[col] for _, item in self.data_files.items() for col in item.columns if
                          col.startswith("Polluting Mass")]
            area_lists = []
            for _, item in self.data_files.items():
                for col in item.columns:
                    if not col.startswith("Polluting Mass"):
                        area_lists.append(item[col])
                        area_lists.append(item[col])

            min_mass = min([item for sublist in mass_lists for item in sublist])
            max_mass = max([item for sublist in mass_lists for item in sublist])
            min_area = min([item for sublist in area_lists for item in sublist])
            max_area = max([item for sublist in area_lists for item in sublist])

            mass_ticks = np.linspace(min_mass, max_mass, 8)
            area_ticks = np.linspace(min_area, max_area, 8)

        self.ax_mass.set_yticks(mass_ticks)
        self.ax_area.set_yticks(area_ticks)

        self.ax_mass.tick_params(axis="both", labelsize=8)
        self.ax_area.tick_params(axis="both", labelsize=8)

        self.canvas.draw()

    def retranslateUi(self):
        # self.BarPlot_AI.setTitle(QCoreApplication.translate("Form", u"Bar Plot", None))
        self.LinePlot_VI.setTitle(QCoreApplication.translate("Form", u"Line Plot", None))
        self.figname_label_VI.setText(QCoreApplication.translate("Form", u"Fig name", None))
        self.savebutton_AI.setText(QCoreApplication.translate("Form", u"Save Figure", None))
        self.import_button_VI.setText(QCoreApplication.translate("Form", u"Import to Project", None))
