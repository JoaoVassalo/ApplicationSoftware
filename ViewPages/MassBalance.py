# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MassBalancePDqXpC.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, QThread)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QFrame, QGridLayout, QHBoxLayout, QPushButton, QSizePolicy, QVBoxLayout)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PySide6.QtGui import QColor
from PySide6 import QtWidgets
import seaborn as sns
import time


class AnimationWorker(QThread):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def run(self):
        self.page.play_animation()


class Ui_Form(object):
    def setupUi(self, frame, df):
        # self.main_frame_MB = frame
        self.data = df
        self.data.dataframe.columns = self.data.dataframe.columns.str.replace(r"\(mt\)$", "", regex=True)
        self.time_values = list(sorted(set(self.data.dataframe.iloc[:, 0])))
        self.time_df_values = list(self.data.dataframe.iloc[:, 0])
        self.actual_time = self.time_values[0]

        self.gridLayout = QGridLayout(frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_frame_MB = QFrame(frame)
        self.main_frame_MB.setObjectName(u"main_frame_MB")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame_MB.sizePolicy().hasHeightForWidth())
        self.main_frame_MB.setSizePolicy(sizePolicy)
        self.main_frame_MB.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame_MB.setFrameShadow(QFrame.Shadow.Raised)
        self.main_frame_MB_layout = QHBoxLayout(self.main_frame_MB)

        self.gridLayout.addWidget(self.main_frame_MB, 0, 0, 1, 1)

        self.frame = QFrame(frame)
        self.frame.setObjectName(u"frame")
        self.frame.setProperty("commomFrame", True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(0, 80))
        self.frame.setMaximumSize(QSize(16777215, 80))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.saveFigure_MB = QPushButton(self.frame)
        self.saveFigure_MB.setObjectName(u"saveFigure_MB")
        self.saveFigure_MB.setProperty('commomButton', True)
        self.saveFigure_MB.setMinimumSize(QSize(150, 30))
        self.saveFigure_MB.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_2.addWidget(self.saveFigure_MB)
        self.horizontalLayout_2.addStretch()

        self.frame_buttons_animation_time = QFrame(self.frame)
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
        self.horizontalLayout_2.addWidget(self.frame_buttons_animation_time)
        self.horizontalLayout_2.addStretch()

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

        self.exportButton_MB = QPushButton(self.frame)
        self.exportButton_MB.setObjectName(u"exportButton_MB")
        self.exportButton_MB.setProperty('commomButton', True)
        self.exportButton_MB.setMinimumSize(QSize(150, 30))
        self.exportButton_MB.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_2.addWidget(self.exportButton_MB)

        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.graph_layout = QVBoxLayout()
        self.figure = Figure(figsize=(6, 6))
        self.canvas = FigureCanvas(self.figure)
        self.graph_layout.addWidget(self.canvas)
        self.canvas.figure.set_facecolor("#C3C3C3")

        self.main_frame_MB_layout.addLayout(self.graph_layout)

        shadow_elements = {
            'frame_buttons_animation_time',
            'main_frame_MB'
        }
        for x in shadow_elements:
            effect = QtWidgets.QGraphicsDropShadowEffect(self.main_frame_MB)
            effect.setBlurRadius(18)
            effect.setXOffset(0)
            effect.setYOffset(0)
            effect.setColor(QColor(0, 0, 0, 255))
            getattr(self, x).setGraphicsEffect(effect)

        self.retranslateUi(frame)
        QMetaObject.connectSlotsByName(frame)

        frame.setStyleSheet(
            """
            #main_frame_MB {
                background-color: #C3C3C3;
                border-radius: 3px;
            }
            
            #frame {
                background-color: #C3C3C3;
                border: none;
            }
            
            [commomButton='true'] {
                background-color: #C3C3C3;
                border: none;
                font-size: 14px;
                font-style: italic;
                font-weight: bold;
                color: #4C5B61;
            }
            
            [commomButton='true']:hover {
                color: #6F1A07;
                font-size: 14px;
            }
            """
        )

        self.set_plot()

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
        index = self.time_df_values.index(self.actual_time)
        next_row = self.data.dataframe.iloc[index, 1:]

        for bar, new_height in zip(self.bar.patches, next_row.values):
            bar.set_height(new_height)
        self.text_annotation.set_text(f"Time = {self.actual_time} days")

        self.canvas.draw()

    def set_plot(self):
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)

        first_row = self.data.dataframe.iloc[0, 1:]

        self.bar = sns.barplot(x=first_row.index, y=first_row.values, color='#C2C1A5', ax=self.ax)
        self.text_annotation = self.ax.text(0.95, 0.95, f"Time = {self.actual_time} days",
                transform=self.ax.transAxes, fontsize=12, ha="right", va="top")

        self.ax.set_ylabel("mT")
        self.ax.set_xlabel("")
        self.ax.set_ylim(self.data.dataframe.min().min(), self.data.dataframe.max().max())
        self.ax.set_xticklabels(self.ax.get_xticklabels(), fontsize=9)
        plt.tight_layout()

        self.canvas.draw()

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.saveFigure_MB.setText(QCoreApplication.translate("Form", u"Save Figure", None))
        self.start_button_time.setText("")
        self.backward_button_time.setText("")
        self.pause_button_time.setText("")
        self.play_button_time.setText("")
        self.forward_button_time.setText("")
        self.finish_button_time.setText("")
        self.exportButton_MB.setText(QCoreApplication.translate("Form", u"Export as .csv", None))
