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
from ViewPages import AreaImpact_Page as Ai_
from ViewPages import VolumeImpact as Vi_
from ViewPages import MassBalance as Mb_
from ViewPages import ChemicalComposition as Cc_

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

        self.AreaImpact_Page = QWidget()
        self.AreaImpact_Page.setObjectName(u"AreaImpact_Page")
        self.gL_AiPage = QGridLayout(self.AreaImpact_Page)
        self.gL_AiPage.setObjectName(u"gridLayout")

        self.frame_to_button_AI = QFrame(self.AreaImpact_Page)
        self.frame_to_button_AI.setObjectName(u"frame_to_button_AI")
        self.frame_to_button_AI.setProperty("ViewCommomFrame_PPA", True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_to_button_AI.sizePolicy().hasHeightForWidth())
        self.frame_to_button_AI.setSizePolicy(sizePolicy)
        self.frame_to_button_AI.setMinimumSize(QSize(0, 50))
        self.frame_to_button_AI.setMaximumSize(QSize(16777215, 50))
        self.frame_to_button_AI.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_to_button_AI.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_to_button_AI)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, -1, -1, -1)
        self.selectfile_button_AI = QPushButton(self.frame_to_button_AI)
        self.selectfile_button_AI.setObjectName(u"selectfile_button_AI")
        self.selectfile_button_AI.setProperty('CommomButton', True)
        self.selectfile_button_AI.setMinimumSize(QSize(150, 30))
        self.selectfile_button_AI.setMaximumSize(QSize(150, 30))
        self.selectfile_button_AI.clicked.connect(self.search_file_ai)

        self.verticalLayout_2.addWidget(self.selectfile_button_AI)
        self.gL_AiPage.addWidget(self.frame_to_button_AI, 0, 0, 1, 1)
        self.IndividualAnalysis_Tab.addTab(self.AreaImpact_Page, "Area Impact")

        self.VolumeImpact_Page = QWidget()
        self.VolumeImpact_Page.setObjectName(u"VolumeImpact_Page")
        self.gL_ViPage = QGridLayout(self.VolumeImpact_Page)
        self.gL_ViPage.setObjectName(u"gridLayout_5")
        self.frame_to_button_VI = QFrame(self.VolumeImpact_Page)
        self.frame_to_button_VI.setObjectName(u"frame_to_button_VI")
        self.frame_to_button_VI.setProperty("ViewCommomFrame_PPA", True)
        sizePolicy.setHeightForWidth(self.frame_to_button_VI.sizePolicy().hasHeightForWidth())
        self.frame_to_button_VI.setSizePolicy(sizePolicy)
        self.frame_to_button_VI.setMinimumSize(QSize(0, 50))
        self.frame_to_button_VI.setMaximumSize(QSize(16777215, 50))
        self.frame_to_button_VI.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_to_button_VI.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_to_button_VI)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.selectfile_button_VI = QPushButton(self.frame_to_button_VI)
        self.selectfile_button_VI.setObjectName(u"selectfile_button_VI")
        self.selectfile_button_VI.setProperty('CommomButton', True)
        self.selectfile_button_VI.setMinimumSize(QSize(150, 30))
        self.selectfile_button_VI.setMaximumSize(QSize(150, 30))
        self.selectfile_button_VI.clicked.connect(self.search_file_vi)

        self.verticalLayout_3.addWidget(self.selectfile_button_VI)
        self.gL_ViPage.addWidget(self.frame_to_button_VI, 0, 0, 1, 1)
        self.IndividualAnalysis_Tab.addTab(self.VolumeImpact_Page, "Volume Impact")

        self.Massbalance_Page = QWidget()
        self.Massbalance_Page.setObjectName(u"Massbalance_Page")
        self.gL_Mbpage = QGridLayout(self.Massbalance_Page)
        self.gL_Mbpage.setObjectName(u"gridLayout_10")
        self.frame_to_button_MB = QFrame(self.Massbalance_Page)
        self.frame_to_button_MB.setObjectName(u"frame_to_button_MB")
        self.frame_to_button_MB.setProperty("ViewCommomFrame_PPA", True)
        sizePolicy.setHeightForWidth(self.frame_to_button_MB.sizePolicy().hasHeightForWidth())
        self.frame_to_button_MB.setSizePolicy(sizePolicy)
        self.frame_to_button_MB.setMinimumSize(QSize(0, 50))
        self.frame_to_button_MB.setMaximumSize(QSize(16777215, 50))
        self.frame_to_button_MB.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_to_button_MB.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_to_button_MB)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.selectfile_button_MB = QPushButton(self.frame_to_button_MB)
        self.selectfile_button_MB.setObjectName(u"selectfile_button_MB")
        self.selectfile_button_MB.setProperty('CommomButton', True)
        self.selectfile_button_MB.setMinimumSize(QSize(150, 30))
        self.selectfile_button_MB.setMaximumSize(QSize(150, 30))
        self.selectfile_button_MB.clicked.connect(self.search_file_mb)

        self.verticalLayout_5.addWidget(self.selectfile_button_MB)
        self.gL_Mbpage.addWidget(self.frame_to_button_MB, 0, 0, 1, 1)
        self.IndividualAnalysis_Tab.addTab(self.Massbalance_Page, "Mass Balance")

        self.Chemical_Page = QWidget()
        self.Chemical_Page.setObjectName(u"Chemical_Page")
        self.gL_CcPage = QGridLayout(self.Chemical_Page)
        self.gL_CcPage.setObjectName(u"gridLayout_13")
        self.frame_to_button_CC = QFrame(self.Chemical_Page)
        self.frame_to_button_CC.setObjectName(u"frame_to_button_CC")
        self.frame_to_button_CC.setProperty("ViewCommomFrame_PPA", True)
        sizePolicy.setHeightForWidth(self.frame_to_button_CC.sizePolicy().hasHeightForWidth())
        self.frame_to_button_CC.setSizePolicy(sizePolicy)
        self.frame_to_button_CC.setMinimumSize(QSize(0, 50))
        self.frame_to_button_CC.setMaximumSize(QSize(16777215, 50))
        self.frame_to_button_CC.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_to_button_CC.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_to_button_CC)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.selectfile_button_CC = QPushButton(self.frame_to_button_CC)
        self.selectfile_button_CC.setObjectName(u"selectfile_button_CC")
        self.selectfile_button_CC.setProperty('CommomButton', True)
        self.selectfile_button_CC.setMinimumSize(QSize(150, 30))
        self.selectfile_button_CC.setMaximumSize(QSize(150, 30))
        self.selectfile_button_CC.clicked.connect(self.search_file_cc)

        self.verticalLayout_6.addWidget(self.selectfile_button_CC)
        self.gL_CcPage.addWidget(self.frame_to_button_CC, 0, 0, 1, 1)
        self.IndividualAnalysis_Tab.addTab(self.Chemical_Page, "Chemical Composition")

        """ ------------------------------- """
        self.ParticleDistribution = QWidget()
        self.ParticleDistribution.setObjectName("ParticleDistribution")
        self.gL_PdPage = QGridLayout(self.ParticleDistribution)
        self.gL_PdPage.setObjectName("gL_PdPage")
        # self.ParticleDistribution.setLayout(self.gL_PdPage)
        self.frame_to_button_PD = QFrame(self.ParticleDistribution)
        self.frame_to_button_PD.setObjectName(u"frame_to_button_PD")
        self.frame_to_button_PD.setProperty("ViewCommomFrame_PPA", True)
        sizePolicy.setHeightForWidth(self.frame_to_button_PD.sizePolicy().hasHeightForWidth())
        self.frame_to_button_PD.setSizePolicy(sizePolicy)
        self.frame_to_button_PD.setMinimumSize(QSize(0, 50))
        self.frame_to_button_PD.setMaximumSize(QSize(16777215, 50))
        self.frame_to_button_PD.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_to_button_PD.setFrameShadow(QFrame.Shadow.Raised)
        self.vL_fB_PD = QVBoxLayout(self.frame_to_button_PD)
        self.vL_fB_PD.setObjectName(u"verticalLayout_6")
        self.vL_fB_PD.setContentsMargins(0, -1, -1, -1)
        self.selectfile_button_PD = QPushButton(self.frame_to_button_PD)
        self.selectfile_button_PD.setObjectName(u"selectfile_button_PD")
        self.selectfile_button_PD.setProperty('CommomButton', True)
        self.selectfile_button_PD.setMinimumSize(QSize(150, 30))
        self.selectfile_button_PD.setMaximumSize(QSize(150, 30))
        self.selectfile_button_PD.clicked.connect(self.search_file_pd)
        self.vL_fB_PD.addWidget(self.selectfile_button_PD)
        self.gL_PdPage.addWidget(self.frame_to_button_PD, 0, 0, 1, 1)
        self.IndividualAnalysis_Tab.addTab(self.ParticleDistribution, "Particle Distribution")

        self.gridLayout_2.addWidget(self.IndividualAnalysis_Tab, 0, 0, 1, 1)

        self.retranslateUi(Form)

        self.IndividualAnalysis_Tab.setCurrentIndex(0)

        self.gL_AiPage.setAlignment(self.frame_to_button_AI, Qt.AlignmentFlag.AlignTop)
        self.gL_ViPage.setAlignment(self.frame_to_button_VI, Qt.AlignmentFlag.AlignTop)
        self.gL_Mbpage.setAlignment(self.frame_to_button_MB, Qt.AlignmentFlag.AlignTop)
        self.gL_CcPage.setAlignment(self.frame_to_button_CC, Qt.AlignmentFlag.AlignTop)
        self.gL_PdPage.setAlignment(self.frame_to_button_PD, Qt.AlignmentFlag.AlignTop)

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

        shadow_elements = {
            'selectfile_button_AI'
        }
        for x in shadow_elements:
            effect = QtWidgets.QGraphicsDropShadowEffect(Form)
            effect.setBlurRadius(18)
            effect.setXOffset(0)
            effect.setYOffset(0)
            effect.setColor(QColor(0, 0, 0, 255))
            getattr(self, x).setGraphicsEffect(effect)

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

    @staticmethod
    def clear_frame_data(grid):
        if grid.count() > 1:
            child = grid.takeAt(1)
            if child.widget():
                child.widget().deleteLater()

    def set_ai_page(self):
        self.ai_df = Ppo.OilThick(self.ai_pathfile)
        if self.ai_df.dataframe is not None:
            self.main_frame_ai_ = QFrame()
            self.main_frame_page_ai = Ai_.Ui_Form()
            self.gL_AiPage.addWidget(self.main_frame_ai_)
            self.main_frame_page_ai.setupUi(self.main_frame_ai_, self.ai_df)
        else:
            print('não foi')

    def set_vi_page(self):
        self.vi_df = Ppo.TotalConc(self.vi_pathfile)
        if self.vi_df.dataframe is not None:
            self.main_frame_vi_ = QFrame()
            self.main_frame_page_vi = Vi_.Ui_Form()
            self.gL_ViPage.addWidget(self.main_frame_vi_)
            self.main_frame_page_vi.setupUi(self.main_frame_vi_, self.vi_df)
        else:
            print('não foi')

    def set_mb_page(self):
        self.mb_df = Ppo.MassBalance(self.mb_pathfile)
        if self.mb_df is not None:
            self.main_frame_mb_ = QFrame()
            self.main_frame_page_mb = Mb_.Ui_Form()
            self.gL_Mbpage.addWidget(self.main_frame_mb_)
            self.main_frame_page_mb.setupUi(self.main_frame_mb_, self.mb_df)
        else:
            print('não foi')

    def set_cc_page(self):
        self.cc_df = Ppo.ChemicComposi(self.cc_pathfile)
        if self.cc_df is not None:
            self.main_frame_cc_ = QFrame()
            self.main_frame_page_cc = Cc_.Ui_Form()
            self.gL_CcPage.addWidget(self.main_frame_cc_)
            self.main_frame_page_cc.setupUi(self.main_frame_cc_, self.cc_df)

    def search_file_ai(self):
        self.ai_pathfile, _ = QFileDialog.getOpenFileName(self.framewindow, "Selecionar Arquivo", "",
                                                   "Arquivos de Texto (*.txt *.log)")
        if self.ai_pathfile:
            self.clear_frame_data(self.gL_AiPage)
            self.set_ai_page()

    def search_file_vi(self):
        self.vi_pathfile, _ = QFileDialog.getOpenFileName(self.framewindow, "Selecionar Arquivo", "",
                                                      "Arquivos de Texto (*.txt *.log)")
        self.set_vi_page()

    def search_file_mb(self):
        self.mb_pathfile, _ = QFileDialog.getOpenFileName(self.framewindow, "Selecionar Arquivo", "",
                                                      "Arquivos de Texto (*.txt *.log)")
        self.set_mb_page()

    def search_file_cc(self):
        self.cc_pathfile, _ = QFileDialog.getOpenFileName(self.framewindow, "Selecionar Arquivo", "",
                                                      "Arquivos de Texto (*.txt *.log)")
        self.set_cc_page()

    def search_file_pd(self):
        return

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.selectfile_button_AI.setText(QCoreApplication.translate("Form", u"Select a file", None))
        self.selectfile_button_VI.setText(QCoreApplication.translate("Form", u"Select a file", None))
        # self.IndividualAnalysis_Tab.setTabText(self.IndividualAnalysis_Tab.indexOf(self.VolumeImpact_Page), QCoreApplication.translate("Form", u"Volume Impact", None))
        self.selectfile_button_MB.setText(QCoreApplication.translate("Form", u"Select a file", None))
        # self.IndividualAnalysis_Tab.setTabText(self.IndividualAnalysis_Tab.indexOf(self.Massbalance_Page), QCoreApplication.translate("Form", u"Mass Balance", None))
        self.selectfile_button_CC.setText(QCoreApplication.translate("Form", u"Select a file", None))
        self.selectfile_button_PD.setText(QCoreApplication.translate("Form", u"Select a file", None))
        # self.IndividualAnalysis_Tab.setTabText(self.IndividualAnalysis_Tab.indexOf(self.Chemical_Page), QCoreApplication.translate("Form", u"Chemical Composition", None))
