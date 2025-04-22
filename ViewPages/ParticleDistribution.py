# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ParticleDistributioncobFLj.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QFrame, QGridLayout, QSizePolicy, QVBoxLayout)
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class Ui_Form(object):
    def setupUi(self, Form, df):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(770, 447)

        self.data = df

        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_frame_PD = QFrame(Form)
        self.main_frame_PD.setObjectName(u"main_frame_PD")
        self.main_layout = QVBoxLayout()
        self.main_frame_PD.setLayout(self.main_layout)

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame_PD.sizePolicy().hasHeightForWidth())
        self.main_frame_PD.setSizePolicy(sizePolicy)
        self.main_frame_PD.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame_PD.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.main_frame_PD, 0, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

        Form.setStyleSheet(
            "#main_frame_PD {\n"
            "   background-color: #C3C3C3;\n"
            "   border: none;"
            "}"
        )

        self.figure = Figure(figsize=(6, 6))
        self.canvas = FigureCanvas(self.figure)
        self.main_layout.addWidget(self.canvas)
        self.plot_graph()

    def plot_graph(self):
        diameters = list(self.data.keys())
        values = list(self.data.values())

        self.figure.clear()
        self.canvas.draw()
        self.ax = self.figure.add_subplot(111)

        self.ax.bar(diameters, values, color='#2C423F')
        self.ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.3)

        self.ax.set_xlabel('Diameter (um)')
        self.ax.set_ylabel('Fractional size distribution by mass')

        self.canvas.draw()
        self.canvas.figure.set_facecolor("#C3C3C3")

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
