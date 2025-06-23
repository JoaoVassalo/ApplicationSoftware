# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Individual_Pages_POSprocessNLPxaY.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6 import QtWidgets
from PySide6.QtGui import (QColor, QIcon)
from PySide6.QtWidgets import (QComboBox, QFrame, QGridLayout,
                               QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QSpacerItem,
                               QTabWidget, QVBoxLayout, QWidget, QFileDialog)
from Functions import PosProcessOSCAR as Ppo
from ViewPages import AreaImpact_Collective as Ai_
from ViewPages import VolumeImpact_Collective as Vi_
from ViewPages import MassBalance_Collective as Mb_
from ViewPages import ChemicalComposition_Collective as Cc_
from ViewPages import ParticleDistribution_Collective as Pd_


class Ui_Form(object):
    def setupUi(self, Form, framepage):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(789, 556)

        self.framewindow = framepage

        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)

        self.IndividualAnalysis_Tab = QTabWidget(Form)
        self.IndividualAnalysis_Tab.setObjectName(u"IndividualAnalysis_Tab")
        self.IndividualAnalysis_Tab.setStyleSheet(u"")

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.AreaImpact_Page = QFrame()
        self.AreaImpact_Page.setObjectName(u"AreaImpact_Page")
        self.ai_frame = Ai_.Ui_Form()
        self.ai_frame.setupUi(self.AreaImpact_Page)
        self.IndividualAnalysis_Tab.addTab(self.AreaImpact_Page, "Area Impact")

        self.VolumeImpact_Page = QFrame()
        self.VolumeImpact_Page.setObjectName(u"VolumeImpact_Page")
        self.vi_frame = Vi_.Ui_Form()
        self.vi_frame.setupUi(self.VolumeImpact_Page)
        self.IndividualAnalysis_Tab.addTab(self.VolumeImpact_Page, "Volume Impact")

        self.MassBalance_Page = QFrame()
        self.MassBalance_Page.setObjectName(u"MassBalance_Page")
        self.mb_frame = Mb_.Ui_Form()
        self.mb_frame.setupUi(self.MassBalance_Page)
        self.IndividualAnalysis_Tab.addTab(self.MassBalance_Page, "Mass Balance")

        self.ChemicalComposition_Page = QFrame()
        self.ChemicalComposition_Page.setObjectName(u"MassBalance_Page")
        self.cc_frame = Cc_.Ui_Form()
        self.cc_frame.setupUi(self.ChemicalComposition_Page)
        self.IndividualAnalysis_Tab.addTab(self.ChemicalComposition_Page, "Chemical Composition")

        self.ParticlePage = QFrame()
        self.ParticlePage.setObjectName(u"MassBalance_Page")
        self.pd_frame = Pd_.Ui_Form()
        self.pd_frame.setupUi(self.ParticlePage)
        self.IndividualAnalysis_Tab.addTab(self.ParticlePage, "Particle Distribution")

        self.gridLayout_2.addWidget(self.IndividualAnalysis_Tab, 0, 0, 1, 1)

        self.retranslateUi(Form)

        self.IndividualAnalysis_Tab.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Form)
        self.getstyle = """
            [ViewCommomFrame_PPA="true"] {
                background-color: #C3C3C3;
                border: none;
            }

            [CommomButton="true"] {
                background-color: #C3C3C3;
                border-radius: 6px;
                font-size: 14px;
                font-style: italic;
                font-weight: bold;
                color: #4C5B61;
            }

            [CommomButton='true']:hover {
                color: #6F1A07;
                font-size: 14px;
            }

            [CommomButton='true']:checked {
                font-size: 14px;
            }
        """
        Form.setStyleSheet(self.getstyle)
        self.setstylesheet()

    def setstylesheet(self):
        self.IndividualAnalysis_Tab.setStyleSheet("""
            QTabWidget::pane { 
                border: 1px solid #2C423F; /* Green border */
                background: #C3C3C3; 
                border-bottom-left-radius: 6px;
                border-bottom-right-radius: 6px;
                border-top-right-radius: 6px;
            }
            QTabBar::tab {
                background: #C3C3C3; 
                padding: 6px; 
                border: 1px solid #2C423F; 
                border-bottom: none;
                border-top-left-radius: 2px; 
                border-top-right-radius: 2px; 
            }
            QTabBar::tab:selected { 
                background: #2C423F; /* Green background for selected tab */
                color: white;
                font-weight: bold;
            }
            QTabBar::tab:hover {
                background: #F5F9E9; /* Lighter green when hovering */
            }
        """)


    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
