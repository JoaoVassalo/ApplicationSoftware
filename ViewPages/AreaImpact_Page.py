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
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np

class Ui_Form:
    def setupUi(self, frame, df):
        self.main_frame_AI = frame
        self.data = df

        self.main_frame_AI.setObjectName(u"main_frame_AI")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame_AI.sizePolicy().hasHeightForWidth())
        self.main_frame_AI.setSizePolicy(sizePolicy)
        self.main_frame_AI.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame_AI.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.main_frame_AI)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.VLayout_VarButton_AI = QVBoxLayout()
        self.VLayout_VarButton_AI.setSpacing(0)
        self.VLayout_VarButton_AI.setObjectName(u"VLayout_VarButton_AI")
        self.frame_variables_AI = QFrame(self.main_frame_AI)
        self.frame_variables_AI.setObjectName(u"frame_variables_AI")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_variables_AI.sizePolicy().hasHeightForWidth())
        self.frame_variables_AI.setSizePolicy(sizePolicy1)
        self.frame_variables_AI.setMinimumSize(QSize(300, 0))
        self.frame_variables_AI.setMaximumSize(QSize(300, 16777215))
        self.frame_variables_AI.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_variables_AI.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_variables_AI)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.HLayout_barplot_AI = QHBoxLayout()
        self.HLayout_barplot_AI.setObjectName(u"HLayout_barplot_AI")
        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_barplot_AI.addItem(self.horizontalSpacer_6)

        self.BarPlot_AI = QGroupBox(self.frame_variables_AI)
        self.BarPlot_AI.setObjectName(u"BarPlot_AI")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.BarPlot_AI.sizePolicy().hasHeightForWidth())
        self.BarPlot_AI.setSizePolicy(sizePolicy2)
        self.BarPlot_AI.setMinimumSize(QSize(0, 130))
        self.BarPlot_AI.setMaximumSize(QSize(16777215, 130))
        self.vL_BarPlot_AI = QVBoxLayout(self.BarPlot_AI)
        self.vL_BarPlot_AI.setObjectName(u"verticalLayout")

        self.HLayout_barplot_AI.addWidget(self.BarPlot_AI)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_barplot_AI.addItem(self.horizontalSpacer_5)


        self.gridLayout_6.addLayout(self.HLayout_barplot_AI, 0, 0, 1, 1)

        self.HLayout_lineplot_AI = QHBoxLayout()
        self.HLayout_lineplot_AI.setObjectName(u"HLayout_lineplot_AI")
        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_lineplot_AI.addItem(self.horizontalSpacer_3)

        self.LinePlot_AI = QGroupBox(self.frame_variables_AI)
        self.LinePlot_AI.setObjectName(u"LinePlot_AI")
        sizePolicy2.setHeightForWidth(self.LinePlot_AI.sizePolicy().hasHeightForWidth())
        self.LinePlot_AI.setSizePolicy(sizePolicy2)
        self.LinePlot_AI.setMinimumSize(QSize(0, 130))
        self.LinePlot_AI.setMaximumSize(QSize(16777215, 130))
        self.vL_LinePlot_AI = QVBoxLayout(self.LinePlot_AI)
        self.vL_LinePlot_AI.setObjectName("vL_LinePlot_AI")

        self.HLayout_lineplot_AI.addWidget(self.LinePlot_AI)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_lineplot_AI.addItem(self.horizontalSpacer_4)


        self.gridLayout_6.addLayout(self.HLayout_lineplot_AI, 1, 0, 1, 1)

        self.VLayout_figsave_AI = QVBoxLayout()
        self.VLayout_figsave_AI.setObjectName(u"VLayout_figsave_AI")
        self.HLayout_figname_AI = QHBoxLayout()
        self.HLayout_figname_AI.setObjectName(u"HLayout_figname_AI")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_figname_AI.addItem(self.horizontalSpacer_2)

        self.VLayout_figname_label_AI = QVBoxLayout()
        self.VLayout_figname_label_AI.setSpacing(0)
        self.VLayout_figname_label_AI.setObjectName(u"VLayout_figname_label_AI")
        self.figname_label_AI = QLabel(self.frame_variables_AI)
        self.figname_label_AI.setObjectName(u"figname_label_AI")
        self.figname_label_AI.setMinimumSize(QSize(0, 20))
        self.figname_label_AI.setMaximumSize(QSize(16777215, 20))

        self.VLayout_figname_label_AI.addWidget(self.figname_label_AI)

        self.LineEdit_AI = QLineEdit(self.frame_variables_AI)
        self.LineEdit_AI.setObjectName(u"LineEdit_AI")
        self.LineEdit_AI.setMinimumSize(QSize(150, 25))
        self.LineEdit_AI.setMaximumSize(QSize(150, 25))

        self.VLayout_figname_label_AI.addWidget(self.LineEdit_AI)


        self.HLayout_figname_AI.addLayout(self.VLayout_figname_label_AI)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_figname_AI.addItem(self.horizontalSpacer)


        self.VLayout_figsave_AI.addLayout(self.HLayout_figname_AI)

        self.HLayout_savebutton_AI = QHBoxLayout()
        self.HLayout_savebutton_AI.setObjectName(u"HLayout_savebutton_AI")
        self.horizontalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_savebutton_AI.addItem(self.horizontalSpacer_8)

        self.savebutton_AI = QPushButton(self.frame_variables_AI)
        self.savebutton_AI.setObjectName(u"savebutton_AI")
        self.savebutton_AI.setMinimumSize(QSize(150, 30))
        self.savebutton_AI.setMaximumSize(QSize(150, 30))

        self.HLayout_savebutton_AI.addWidget(self.savebutton_AI)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_savebutton_AI.addItem(self.horizontalSpacer_7)


        self.VLayout_figsave_AI.addLayout(self.HLayout_savebutton_AI)


        self.gridLayout_6.addLayout(self.VLayout_figsave_AI, 2, 0, 1, 1)


        self.VLayout_VarButton_AI.addWidget(self.frame_variables_AI)

        self.verticalSpacer_AI = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLayout_VarButton_AI.addItem(self.verticalSpacer_AI)

        self.import_button_AI = QPushButton(self.main_frame_AI)
        self.import_button_AI.setObjectName(u"import_button_AI")
        self.import_button_AI.setMinimumSize(QSize(150, 30))
        self.import_button_AI.setMaximumSize(QSize(150, 30))

        self.VLayout_VarButton_AI.addWidget(self.import_button_AI)


        self.gridLayout_3.addLayout(self.VLayout_VarButton_AI, 0, 0, 1, 1)

        self.Fig_Frame_AI = QFrame(self.main_frame_AI)
        self.Fig_Frame_AI.setObjectName(u"Fig_Frame_AI")
        sizePolicy.setHeightForWidth(self.Fig_Frame_AI.sizePolicy().hasHeightForWidth())
        self.Fig_Frame_AI.setSizePolicy(sizePolicy)
        self.Fig_Frame_AI.setFrameShape(QFrame.Shape.StyledPanel)
        self.Fig_Frame_AI.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_3.addWidget(self.Fig_Frame_AI, 0, 1, 1, 1)

        self.hori_frame = QHBoxLayout(self.Fig_Frame_AI)

        self.retranslateUi()
        self.bar_variables = []
        self.line_variables = []
        self.graph_layout = QVBoxLayout()
        self.figure = Figure(figsize=(6, 6))
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.Fig_Frame_AI)
        # self.toolbar = CustomNavigationToolbar(self.canvas, self.frame)  # Use the custom toolbar
        self.graph_layout.addWidget(self.toolbar)
        self.graph_layout.addWidget(self.canvas)
        self.hori_frame.addLayout(self.graph_layout)
        self.Fig_Frame_AI.setLayout(self.hori_frame)

        self.set_graph()
        self.set_page()

    def on_cb_bar_selected(self, bar):
        if bar.isChecked():
            if len(self.bar_variables) == 0:
                for i in range(self.vL_LinePlot_AI.count()):
                    widget = self.vL_LinePlot_AI.itemAt(i).widget()
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
            if len(self.line_variables) == 0:
                for i in range(self.vL_BarPlot_AI.count()):
                    widget = self.vL_BarPlot_AI.itemAt(i).widget()
                    if isinstance(widget, QCheckBox):
                        widget.blockSignals(True)
                        widget.setChecked(False)
                        widget.blockSignals(False)
                        self.bar_variables.remove(widget.text()) if widget.text() in self.bar_variables else None

            self.line_variables.append(line.text())
        else:
            self.line_variables.remove(line.text())

    def set_page(self):
        self.variables_list_for_ai = list(self.data.dataframe.columns)
        self.variables_list_for_ai.pop(0)

        for var_ in self.variables_list_for_ai:
            checkbutton_bar = QCheckBox(text=var_, parent=self.BarPlot_AI)
            checkbutton_bar.clicked.connect(lambda checked, cb=checkbutton_bar: self.on_cb_bar_selected(cb))
            self.vL_BarPlot_AI.addWidget(checkbutton_bar)

            checkbutton_line = QCheckBox(text=var_, parent=self.LinePlot_AI)
            checkbutton_line.clicked.connect(lambda checked, cb=checkbutton_line: self.on_cb_line_selected(cb))
            self.vL_LinePlot_AI.addWidget(checkbutton_line)

    def set_graph(self):
        self.ax_mass = self.figure.add_subplot(111)
        self.ax_area = self.ax_mass.twinx()

        self.ax_mass.set_xlabel("Time (days)", fontsize=10)
        self.ax_mass.set_ylabel("Mass [ton]", fontsize=10)
        self.ax_mass.yaxis.set_label_position("left")
        self.ax_mass.yaxis.tick_left()

        self.ax_area.set_ylabel("Area [km²]", fontsize=10)
        self.ax_area.yaxis.set_label_position("right")
        self.ax_area.yaxis.tick_right()

        mass_ticks = np.linspace(min(self.data.dataframe['Polluting Mass [ton]']),
                                 max(self.data.dataframe['Polluting Mass [ton]']), 8)  # Divide em 7 partes iguais
        area_ticks = np.linspace(self.data.dataframe.min().min(),
                                 self.data.dataframe.max().max(), 8)  # Mesmo número de divisões

        self.ax_mass.set_yticks(mass_ticks)
        self.ax_area.set_yticks(area_ticks)

        # self.ax_mass.set_ylim(min(self.data.dataframe['Polluting Mass [ton]']),
        #                       max(self.data.dataframe['Polluting Mass [ton]']))
        # self.ax_area.set_ylim(self.data.dataframe.min().min(), self.data.dataframe.max().max())

        self.ax_mass.tick_params(axis="both", labelsize=8)
        self.ax_area.tick_params(axis="y", labelsize=8)

        self.ax_mass.grid(True, linestyle="--", color='gray')
        self.ax_area.grid(True, linestyle=":", color='black')
        # self.ax_area.yaxis.set_major_locator(self.ax_mass.yaxis.get_major_locator())
        self.canvas.draw()


    def retranslateUi(self):
        self.BarPlot_AI.setTitle(QCoreApplication.translate("Form", u"Bar Plot", None))
        self.LinePlot_AI.setTitle(QCoreApplication.translate("Form", u"Line Plot", None))
        self.figname_label_AI.setText(QCoreApplication.translate("Form", u"Fig name", None))
        self.savebutton_AI.setText(QCoreApplication.translate("Form", u"Save Figure", None))
        self.import_button_AI.setText(QCoreApplication.translate("Form", u"Import to Project", None))
