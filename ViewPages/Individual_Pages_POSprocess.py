# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Individual_Pages_POSprocessNLPxaY.ui'
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
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(789, 556)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.IndividualAnalysis_Tab = QTabWidget(Form)
        self.IndividualAnalysis_Tab.setObjectName(u"IndividualAnalysis_Tab")
        self.IndividualAnalysis_Tab.setStyleSheet(u"")
        self.AreaImpact_Page = QWidget()
        self.AreaImpact_Page.setObjectName(u"AreaImpact_Page")
        self.gridLayout = QGridLayout(self.AreaImpact_Page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_to_button_AI = QFrame(self.AreaImpact_Page)
        self.frame_to_button_AI.setObjectName(u"frame_to_button_AI")
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
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.selectfile_button_AI = QPushButton(self.frame_to_button_AI)
        self.selectfile_button_AI.setObjectName(u"selectfile_button_AI")
        self.selectfile_button_AI.setMinimumSize(QSize(150, 30))
        self.selectfile_button_AI.setMaximumSize(QSize(150, 30))

        self.verticalLayout_2.addWidget(self.selectfile_button_AI)


        self.gridLayout.addWidget(self.frame_to_button_AI, 0, 0, 1, 1)

        self.main_frame_AI = QFrame(self.AreaImpact_Page)
        self.main_frame_AI.setObjectName(u"main_frame_AI")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_frame_AI.sizePolicy().hasHeightForWidth())
        self.main_frame_AI.setSizePolicy(sizePolicy1)
        self.main_frame_AI.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame_AI.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.main_frame_AI)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.VLayout_VarButton_AI = QVBoxLayout()
        self.VLayout_VarButton_AI.setSpacing(0)
        self.VLayout_VarButton_AI.setObjectName(u"VLayout_VarButton_AI")
        self.frame_variables_AI = QFrame(self.main_frame_AI)
        self.frame_variables_AI.setObjectName(u"frame_variables_AI")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_variables_AI.sizePolicy().hasHeightForWidth())
        self.frame_variables_AI.setSizePolicy(sizePolicy2)
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
        sizePolicy.setHeightForWidth(self.BarPlot_AI.sizePolicy().hasHeightForWidth())
        self.BarPlot_AI.setSizePolicy(sizePolicy)
        self.BarPlot_AI.setMinimumSize(QSize(0, 130))
        self.BarPlot_AI.setMaximumSize(QSize(16777215, 130))
        self.verticalLayout = QVBoxLayout(self.BarPlot_AI)
        self.verticalLayout.setObjectName(u"verticalLayout")

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
        sizePolicy.setHeightForWidth(self.LinePlot_AI.sizePolicy().hasHeightForWidth())
        self.LinePlot_AI.setSizePolicy(sizePolicy)
        self.LinePlot_AI.setMinimumSize(QSize(0, 130))
        self.LinePlot_AI.setMaximumSize(QSize(16777215, 130))

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
        sizePolicy1.setHeightForWidth(self.Fig_Frame_AI.sizePolicy().hasHeightForWidth())
        self.Fig_Frame_AI.setSizePolicy(sizePolicy1)
        self.Fig_Frame_AI.setFrameShape(QFrame.Shape.StyledPanel)
        self.Fig_Frame_AI.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2 = QLabel(self.Fig_Frame_AI)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 190, 151, 51))

        self.gridLayout_3.addWidget(self.Fig_Frame_AI, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.main_frame_AI, 1, 0, 1, 1)

        self.IndividualAnalysis_Tab.addTab(self.AreaImpact_Page, "Area Impact")
        self.VolumeImpact_Page = QWidget()
        self.VolumeImpact_Page.setObjectName(u"VolumeImpact_Page")
        self.gridLayout_5 = QGridLayout(self.VolumeImpact_Page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_to_button_VI = QFrame(self.VolumeImpact_Page)
        self.frame_to_button_VI.setObjectName(u"frame_to_button_VI")
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
        self.selectfile_button_VI.setMinimumSize(QSize(150, 30))
        self.selectfile_button_VI.setMaximumSize(QSize(150, 30))

        self.verticalLayout_3.addWidget(self.selectfile_button_VI)


        self.gridLayout_5.addWidget(self.frame_to_button_VI, 0, 0, 1, 1)

        self.main_frame_VI = QFrame(self.VolumeImpact_Page)
        self.main_frame_VI.setObjectName(u"main_frame_VI")
        sizePolicy1.setHeightForWidth(self.main_frame_VI.sizePolicy().hasHeightForWidth())
        self.main_frame_VI.setSizePolicy(sizePolicy1)
        self.main_frame_VI.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame_VI.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.main_frame_VI)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.VLayout_VarButton_VI = QVBoxLayout()
        self.VLayout_VarButton_VI.setSpacing(0)
        self.VLayout_VarButton_VI.setObjectName(u"VLayout_VarButton_VI")
        self.frame_variables_VI = QFrame(self.main_frame_VI)
        self.frame_variables_VI.setObjectName(u"frame_variables_VI")
        sizePolicy2.setHeightForWidth(self.frame_variables_VI.sizePolicy().hasHeightForWidth())
        self.frame_variables_VI.setSizePolicy(sizePolicy2)
        self.frame_variables_VI.setMinimumSize(QSize(300, 0))
        self.frame_variables_VI.setMaximumSize(QSize(300, 16777215))
        self.frame_variables_VI.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_variables_VI.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_variables_VI)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.HLayout_barplot_VI = QHBoxLayout()
        self.HLayout_barplot_VI.setObjectName(u"HLayout_barplot_VI")
        self.horizontalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_barplot_VI.addItem(self.horizontalSpacer_9)

        self.BarPlot_VI = QGroupBox(self.frame_variables_VI)
        self.BarPlot_VI.setObjectName(u"BarPlot_VI")
        sizePolicy.setHeightForWidth(self.BarPlot_VI.sizePolicy().hasHeightForWidth())
        self.BarPlot_VI.setSizePolicy(sizePolicy)
        self.BarPlot_VI.setMinimumSize(QSize(0, 130))
        self.BarPlot_VI.setMaximumSize(QSize(16777215, 130))
        self.verticalLayout_4 = QVBoxLayout(self.BarPlot_VI)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.HLayout_barplot_VI.addWidget(self.BarPlot_VI)

        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_barplot_VI.addItem(self.horizontalSpacer_10)


        self.gridLayout_7.addLayout(self.HLayout_barplot_VI, 0, 0, 1, 1)

        self.HLayout_lineplot_VI = QHBoxLayout()
        self.HLayout_lineplot_VI.setObjectName(u"HLayout_lineplot_VI")
        self.horizontalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_lineplot_VI.addItem(self.horizontalSpacer_11)

        self.LinePlot_VI = QGroupBox(self.frame_variables_VI)
        self.LinePlot_VI.setObjectName(u"LinePlot_VI")
        sizePolicy.setHeightForWidth(self.LinePlot_VI.sizePolicy().hasHeightForWidth())
        self.LinePlot_VI.setSizePolicy(sizePolicy)
        self.LinePlot_VI.setMinimumSize(QSize(0, 130))
        self.LinePlot_VI.setMaximumSize(QSize(16777215, 130))

        self.HLayout_lineplot_VI.addWidget(self.LinePlot_VI)

        self.horizontalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_lineplot_VI.addItem(self.horizontalSpacer_12)


        self.gridLayout_7.addLayout(self.HLayout_lineplot_VI, 1, 0, 1, 1)

        self.VLayout_figsave_VI = QVBoxLayout()
        self.VLayout_figsave_VI.setObjectName(u"VLayout_figsave_VI")
        self.HLayout_figname_VI = QHBoxLayout()
        self.HLayout_figname_VI.setObjectName(u"HLayout_figname_VI")
        self.horizontalSpacer_13 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_figname_VI.addItem(self.horizontalSpacer_13)

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

        self.horizontalSpacer_14 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_figname_VI.addItem(self.horizontalSpacer_14)


        self.VLayout_figsave_VI.addLayout(self.HLayout_figname_VI)

        self.HLayout_savebutton_VI = QHBoxLayout()
        self.HLayout_savebutton_VI.setObjectName(u"HLayout_savebutton_VI")
        self.horizontalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_savebutton_VI.addItem(self.horizontalSpacer_15)

        self.savebutton_VI = QPushButton(self.frame_variables_VI)
        self.savebutton_VI.setObjectName(u"savebutton_VI")
        self.savebutton_VI.setMinimumSize(QSize(150, 30))
        self.savebutton_VI.setMaximumSize(QSize(150, 30))

        self.HLayout_savebutton_VI.addWidget(self.savebutton_VI)

        self.horizontalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_savebutton_VI.addItem(self.horizontalSpacer_16)


        self.VLayout_figsave_VI.addLayout(self.HLayout_savebutton_VI)


        self.gridLayout_7.addLayout(self.VLayout_figsave_VI, 2, 0, 1, 1)


        self.VLayout_VarButton_VI.addWidget(self.frame_variables_VI)

        self.verticalSpacer_VI = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLayout_VarButton_VI.addItem(self.verticalSpacer_VI)

        self.import_button_VI = QPushButton(self.main_frame_VI)
        self.import_button_VI.setObjectName(u"import_button_VI")
        self.import_button_VI.setMinimumSize(QSize(150, 30))
        self.import_button_VI.setMaximumSize(QSize(150, 30))

        self.VLayout_VarButton_VI.addWidget(self.import_button_VI)


        self.gridLayout_4.addLayout(self.VLayout_VarButton_VI, 0, 0, 1, 1)

        self.Fig_Frame_VI = QFrame(self.main_frame_VI)
        self.Fig_Frame_VI.setObjectName(u"Fig_Frame_VI")
        sizePolicy1.setHeightForWidth(self.Fig_Frame_VI.sizePolicy().hasHeightForWidth())
        self.Fig_Frame_VI.setSizePolicy(sizePolicy1)
        self.Fig_Frame_VI.setFrameShape(QFrame.Shape.StyledPanel)
        self.Fig_Frame_VI.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.Fig_Frame_VI)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 180, 151, 51))

        self.gridLayout_4.addWidget(self.Fig_Frame_VI, 0, 1, 1, 1)


        self.gridLayout_5.addWidget(self.main_frame_VI, 1, 0, 1, 1)

        self.IndividualAnalysis_Tab.addTab(self.VolumeImpact_Page, "Volume Impact")
        self.Massbalance_Page = QWidget()
        self.Massbalance_Page.setObjectName(u"Massbalance_Page")
        self.gridLayout_10 = QGridLayout(self.Massbalance_Page)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frame_to_button_MB = QFrame(self.Massbalance_Page)
        self.frame_to_button_MB.setObjectName(u"frame_to_button_MB")
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
        self.selectfile_button_MB.setMinimumSize(QSize(150, 30))
        self.selectfile_button_MB.setMaximumSize(QSize(150, 30))

        self.verticalLayout_5.addWidget(self.selectfile_button_MB)


        self.gridLayout_10.addWidget(self.frame_to_button_MB, 0, 0, 1, 1)

        self.main_frame_MB = QFrame(self.Massbalance_Page)
        self.main_frame_MB.setObjectName(u"main_frame_MB")
        sizePolicy1.setHeightForWidth(self.main_frame_MB.sizePolicy().hasHeightForWidth())
        self.main_frame_MB.setSizePolicy(sizePolicy1)
        self.main_frame_MB.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame_MB.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.main_frame_MB)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.VLayout_VarButton_MB = QVBoxLayout()
        self.VLayout_VarButton_MB.setSpacing(0)
        self.VLayout_VarButton_MB.setObjectName(u"VLayout_VarButton_MB")
        self.frame_variables_MB = QFrame(self.main_frame_MB)
        self.frame_variables_MB.setObjectName(u"frame_variables_MB")
        sizePolicy2.setHeightForWidth(self.frame_variables_MB.sizePolicy().hasHeightForWidth())
        self.frame_variables_MB.setSizePolicy(sizePolicy2)
        self.frame_variables_MB.setMinimumSize(QSize(300, 0))
        self.frame_variables_MB.setMaximumSize(QSize(300, 16777215))
        self.frame_variables_MB.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_variables_MB.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_variables_MB)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.HLayout_barplot_MB = QHBoxLayout()
        self.HLayout_barplot_MB.setObjectName(u"HLayout_barplot_MB")
        self.horizontalSpacer_17 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_barplot_MB.addItem(self.horizontalSpacer_17)

        self.BarPlot_MB = QGroupBox(self.frame_variables_MB)
        self.BarPlot_MB.setObjectName(u"BarPlot_MB")
        sizePolicy.setHeightForWidth(self.BarPlot_MB.sizePolicy().hasHeightForWidth())
        self.BarPlot_MB.setSizePolicy(sizePolicy)
        self.BarPlot_MB.setMinimumSize(QSize(0, 130))
        self.BarPlot_MB.setMaximumSize(QSize(16777215, 130))
        self.gridLayout_11 = QGridLayout(self.BarPlot_MB)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.scrollArea_BarPlot_MB = QScrollArea(self.BarPlot_MB)
        self.scrollArea_BarPlot_MB.setObjectName(u"scrollArea_BarPlot_MB")
        self.scrollArea_BarPlot_MB.setWidgetResizable(True)
        self.scrollAreaWidgetContents_Barplot_MB = QWidget()
        self.scrollAreaWidgetContents_Barplot_MB.setObjectName(u"scrollAreaWidgetContents_Barplot_MB")
        self.scrollAreaWidgetContents_Barplot_MB.setGeometry(QRect(0, 0, 66, 92))
        self.scrollArea_BarPlot_MB.setWidget(self.scrollAreaWidgetContents_Barplot_MB)

        self.gridLayout_11.addWidget(self.scrollArea_BarPlot_MB, 0, 0, 1, 1)


        self.HLayout_barplot_MB.addWidget(self.BarPlot_MB)

        self.horizontalSpacer_18 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_barplot_MB.addItem(self.horizontalSpacer_18)


        self.gridLayout_9.addLayout(self.HLayout_barplot_MB, 0, 0, 1, 1)

        self.HLayout_lineplot_MB = QHBoxLayout()
        self.HLayout_lineplot_MB.setObjectName(u"HLayout_lineplot_MB")
        self.horizontalSpacer_19 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_lineplot_MB.addItem(self.horizontalSpacer_19)

        self.LinePlot_MB = QGroupBox(self.frame_variables_MB)
        self.LinePlot_MB.setObjectName(u"LinePlot_MB")
        sizePolicy.setHeightForWidth(self.LinePlot_MB.sizePolicy().hasHeightForWidth())
        self.LinePlot_MB.setSizePolicy(sizePolicy)
        self.LinePlot_MB.setMinimumSize(QSize(0, 130))
        self.LinePlot_MB.setMaximumSize(QSize(16777215, 130))
        self.gridLayout_12 = QGridLayout(self.LinePlot_MB)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.scrollArea_LinePlot_MB = QScrollArea(self.LinePlot_MB)
        self.scrollArea_LinePlot_MB.setObjectName(u"scrollArea_LinePlot_MB")
        self.scrollArea_LinePlot_MB.setWidgetResizable(True)
        self.scrollAreaWidgetContents_LinePlot_MB = QWidget()
        self.scrollAreaWidgetContents_LinePlot_MB.setObjectName(u"scrollAreaWidgetContents_LinePlot_MB")
        self.scrollAreaWidgetContents_LinePlot_MB.setGeometry(QRect(0, 0, 66, 92))
        self.scrollArea_LinePlot_MB.setWidget(self.scrollAreaWidgetContents_LinePlot_MB)

        self.gridLayout_12.addWidget(self.scrollArea_LinePlot_MB, 0, 0, 1, 1)


        self.HLayout_lineplot_MB.addWidget(self.LinePlot_MB)

        self.horizontalSpacer_20 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_lineplot_MB.addItem(self.horizontalSpacer_20)


        self.gridLayout_9.addLayout(self.HLayout_lineplot_MB, 1, 0, 1, 1)

        self.VLayout_figsave_MB = QVBoxLayout()
        self.VLayout_figsave_MB.setObjectName(u"VLayout_figsave_MB")
        self.HLayout_figname_MB = QHBoxLayout()
        self.HLayout_figname_MB.setObjectName(u"HLayout_figname_MB")
        self.horizontalSpacer_21 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_figname_MB.addItem(self.horizontalSpacer_21)

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

        self.horizontalSpacer_22 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_figname_MB.addItem(self.horizontalSpacer_22)


        self.VLayout_figsave_MB.addLayout(self.HLayout_figname_MB)

        self.HLayout_savebutton_MB = QHBoxLayout()
        self.HLayout_savebutton_MB.setObjectName(u"HLayout_savebutton_MB")
        self.horizontalSpacer_23 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_savebutton_MB.addItem(self.horizontalSpacer_23)

        self.savebutton_MB = QPushButton(self.frame_variables_MB)
        self.savebutton_MB.setObjectName(u"savebutton_MB")
        self.savebutton_MB.setMinimumSize(QSize(150, 30))
        self.savebutton_MB.setMaximumSize(QSize(150, 30))

        self.HLayout_savebutton_MB.addWidget(self.savebutton_MB)

        self.horizontalSpacer_24 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HLayout_savebutton_MB.addItem(self.horizontalSpacer_24)


        self.VLayout_figsave_MB.addLayout(self.HLayout_savebutton_MB)


        self.gridLayout_9.addLayout(self.VLayout_figsave_MB, 2, 0, 1, 1)


        self.VLayout_VarButton_MB.addWidget(self.frame_variables_MB)

        self.verticalSpacer_MB = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLayout_VarButton_MB.addItem(self.verticalSpacer_MB)

        self.import_button_MB = QPushButton(self.main_frame_MB)
        self.import_button_MB.setObjectName(u"import_button_MB")
        self.import_button_MB.setMinimumSize(QSize(150, 30))
        self.import_button_MB.setMaximumSize(QSize(150, 30))

        self.VLayout_VarButton_MB.addWidget(self.import_button_MB)


        self.gridLayout_8.addLayout(self.VLayout_VarButton_MB, 0, 0, 1, 1)

        self.Fig_Frame_MB = QFrame(self.main_frame_MB)
        self.Fig_Frame_MB.setObjectName(u"Fig_Frame_MB")
        sizePolicy1.setHeightForWidth(self.Fig_Frame_MB.sizePolicy().hasHeightForWidth())
        self.Fig_Frame_MB.setSizePolicy(sizePolicy1)
        self.Fig_Frame_MB.setFrameShape(QFrame.Shape.StyledPanel)
        self.Fig_Frame_MB.setFrameShadow(QFrame.Shadow.Raised)
        self.label_3 = QLabel(self.Fig_Frame_MB)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 190, 151, 51))

        self.gridLayout_8.addWidget(self.Fig_Frame_MB, 0, 1, 1, 1)


        self.gridLayout_10.addWidget(self.main_frame_MB, 1, 0, 1, 1)

        self.IndividualAnalysis_Tab.addTab(self.Massbalance_Page, "Mass Balance")
        self.Chemical_Page = QWidget()
        self.Chemical_Page.setObjectName(u"Chemical_Page")
        self.gridLayout_13 = QGridLayout(self.Chemical_Page)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.frame_to_button_CC = QFrame(self.Chemical_Page)
        self.frame_to_button_CC.setObjectName(u"frame_to_button_CC")
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
        self.selectfile_button_CC.setMinimumSize(QSize(150, 30))
        self.selectfile_button_CC.setMaximumSize(QSize(150, 30))

        self.verticalLayout_6.addWidget(self.selectfile_button_CC)


        self.gridLayout_13.addWidget(self.frame_to_button_CC, 0, 0, 1, 1)

        self.main_frame_CC = QFrame(self.Chemical_Page)
        self.main_frame_CC.setObjectName(u"main_frame_CC")
        self.main_frame_CC.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame_CC.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_14 = QGridLayout(self.main_frame_CC)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.frame_fig_CC = QFrame(self.main_frame_CC)
        self.frame_fig_CC.setObjectName(u"frame_fig_CC")
        sizePolicy1.setHeightForWidth(self.frame_fig_CC.sizePolicy().hasHeightForWidth())
        self.frame_fig_CC.setSizePolicy(sizePolicy1)
        self.frame_fig_CC.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fig_CC.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_14.addWidget(self.frame_fig_CC, 0, 0, 3, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_28 = QSpacerItem(5, 17, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_28)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.TimeLabel_FilterLabel = QLabel(self.main_frame_CC)
        self.TimeLabel_FilterLabel.setObjectName(u"TimeLabel_FilterLabel")
        self.TimeLabel_FilterLabel.setMinimumSize(QSize(180, 22))
        self.TimeLabel_FilterLabel.setMaximumSize(QSize(180, 22))

        self.verticalLayout_7.addWidget(self.TimeLabel_FilterLabel)

        self.frame_buttons_CC = QFrame(self.main_frame_CC)
        self.frame_buttons_CC.setObjectName(u"frame_buttons_CC")
        self.frame_buttons_CC.setMinimumSize(QSize(180, 50))
        self.frame_buttons_CC.setMaximumSize(QSize(180, 50))
        self.frame_buttons_CC.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_buttons_CC.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_buttons_CC)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.start_button_CC = QPushButton(self.frame_buttons_CC)
        self.start_button_CC.setObjectName(u"start_button_CC")
        icon = QIcon()
        icon.addFile(u":/icons/icons/backward - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start_button_CC.setIcon(icon)
        self.start_button_CC.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.start_button_CC)

        self.backward_button_CC = QPushButton(self.frame_buttons_CC)
        self.backward_button_CC.setObjectName(u"backward_button_CC")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/arrow-left - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backward_button_CC.setIcon(icon1)
        self.backward_button_CC.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.backward_button_CC)

        self.pause_button_CC = QPushButton(self.frame_buttons_CC)
        self.pause_button_CC.setObjectName(u"pause_button_CC")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/pause - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pause_button_CC.setIcon(icon2)
        self.pause_button_CC.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pause_button_CC)

        self.play_button_CC = QPushButton(self.frame_buttons_CC)
        self.play_button_CC.setObjectName(u"play_button_CC")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/play - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.play_button_CC.setIcon(icon3)
        self.play_button_CC.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.play_button_CC)

        self.forward_button_CC = QPushButton(self.frame_buttons_CC)
        self.forward_button_CC.setObjectName(u"forward_button_CC")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/arrow-right - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.forward_button_CC.setIcon(icon4)
        self.forward_button_CC.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.forward_button_CC)

        self.last_button_CC = QPushButton(self.frame_buttons_CC)
        self.last_button_CC.setObjectName(u"last_button_CC")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/forward - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.last_button_CC.setIcon(icon5)
        self.last_button_CC.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.last_button_CC)


        self.verticalLayout_7.addWidget(self.frame_buttons_CC)

        self.TimeValue_exit_CC = QLabel(self.main_frame_CC)
        self.TimeValue_exit_CC.setObjectName(u"TimeValue_exit_CC")
        self.TimeValue_exit_CC.setMinimumSize(QSize(180, 22))
        self.TimeValue_exit_CC.setMaximumSize(QSize(180, 22))
        self.TimeValue_exit_CC.setStyleSheet(u"border: 2px solid #212b33")
        self.TimeValue_exit_CC.setText(u"Aqui vai o valor de tempo")
        self.TimeValue_exit_CC.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.TimeValue_exit_CC)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_27 = QSpacerItem(5, 17, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_27)


        self.gridLayout_14.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_25 = QSpacerItem(5, 17, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_25)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.OilComponent_Label = QLabel(self.main_frame_CC)
        self.OilComponent_Label.setObjectName(u"OilComponent_Label")
        self.OilComponent_Label.setMinimumSize(QSize(180, 22))
        self.OilComponent_Label.setMaximumSize(QSize(180, 22))

        self.verticalLayout_8.addWidget(self.OilComponent_Label)

        self.comboBox_Components_CC = QComboBox(self.main_frame_CC)
        self.comboBox_Components_CC.setObjectName(u"comboBox_Components_CC")
        self.comboBox_Components_CC.setMinimumSize(QSize(180, 30))
        self.comboBox_Components_CC.setMaximumSize(QSize(180, 30))

        self.verticalLayout_8.addWidget(self.comboBox_Components_CC)


        self.horizontalLayout_2.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_26 = QSpacerItem(5, 17, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_26)


        self.gridLayout_14.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.oil_initial_composition_CC = QLabel(self.main_frame_CC)
        self.oil_initial_composition_CC.setObjectName(u"oil_initial_composition_CC")
        self.oil_initial_composition_CC.setMinimumSize(QSize(180, 22))
        self.oil_initial_composition_CC.setMaximumSize(QSize(180, 22))

        self.verticalLayout_9.addWidget(self.oil_initial_composition_CC)

        self.frame_composition_table_CC = QFrame(self.main_frame_CC)
        self.frame_composition_table_CC.setObjectName(u"frame_composition_table_CC")
        sizePolicy2.setHeightForWidth(self.frame_composition_table_CC.sizePolicy().hasHeightForWidth())
        self.frame_composition_table_CC.setSizePolicy(sizePolicy2)
        self.frame_composition_table_CC.setMinimumSize(QSize(250, 0))
        self.frame_composition_table_CC.setMaximumSize(QSize(250, 16777215))
        self.frame_composition_table_CC.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_composition_table_CC.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_9.addWidget(self.frame_composition_table_CC)


        self.gridLayout_14.addLayout(self.verticalLayout_9, 2, 1, 1, 1)


        self.gridLayout_13.addWidget(self.main_frame_CC, 1, 0, 1, 1)

        self.IndividualAnalysis_Tab.addTab(self.Chemical_Page, "Chemical Composition")

        self.gridLayout_2.addWidget(self.IndividualAnalysis_Tab, 0, 0, 1, 1)

        self.retranslateUi(Form)

        self.IndividualAnalysis_Tab.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.selectfile_button_AI.setText(QCoreApplication.translate("Form", u"Select a file", None))
        self.BarPlot_AI.setTitle(QCoreApplication.translate("Form", u"Bar Plot", None))
        self.LinePlot_AI.setTitle(QCoreApplication.translate("Form", u"Line Plot", None))
        self.figname_label_AI.setText(QCoreApplication.translate("Form", u"Fig name", None))
        self.savebutton_AI.setText(QCoreApplication.translate("Form", u"Save Figure", None))
        self.import_button_AI.setText(QCoreApplication.translate("Form", u"Import to Project", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Area Impact", None))
        self.IndividualAnalysis_Tab.setTabText(self.IndividualAnalysis_Tab.indexOf(self.AreaImpact_Page), QCoreApplication.translate("Form", u"Area Impact", None))
        self.selectfile_button_VI.setText(QCoreApplication.translate("Form", u"Select a file", None))
        self.BarPlot_VI.setTitle(QCoreApplication.translate("Form", u"Bar Plot", None))
        self.LinePlot_VI.setTitle(QCoreApplication.translate("Form", u"Line Plot", None))
        self.figname_label_VI.setText(QCoreApplication.translate("Form", u"Fig name", None))
        self.savebutton_VI.setText(QCoreApplication.translate("Form", u"Save Figure", None))
        self.import_button_VI.setText(QCoreApplication.translate("Form", u"Import to Project", None))
        self.label.setText(QCoreApplication.translate("Form", u"Volume Impact", None))
        self.IndividualAnalysis_Tab.setTabText(self.IndividualAnalysis_Tab.indexOf(self.VolumeImpact_Page), QCoreApplication.translate("Form", u"Volume Impact", None))
        self.selectfile_button_MB.setText(QCoreApplication.translate("Form", u"Select a file", None))
        self.BarPlot_MB.setTitle(QCoreApplication.translate("Form", u"Bar Plot", None))
        self.LinePlot_MB.setTitle(QCoreApplication.translate("Form", u"Line Plot", None))
        self.figname_label_MB.setText(QCoreApplication.translate("Form", u"Fig name", None))
        self.savebutton_MB.setText(QCoreApplication.translate("Form", u"Save Figure", None))
        self.import_button_MB.setText(QCoreApplication.translate("Form", u"Import to Project", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Mass Balance", None))
        self.IndividualAnalysis_Tab.setTabText(self.IndividualAnalysis_Tab.indexOf(self.Massbalance_Page), QCoreApplication.translate("Form", u"Mass Balance", None))
        self.selectfile_button_CC.setText(QCoreApplication.translate("Form", u"Select a file", None))
        self.TimeLabel_FilterLabel.setText(QCoreApplication.translate("Form", u"Time Filter", None))
        self.start_button_CC.setText("")
        self.backward_button_CC.setText("")
        self.pause_button_CC.setText("")
        self.play_button_CC.setText("")
        self.forward_button_CC.setText("")
        self.last_button_CC.setText("")
        self.OilComponent_Label.setText(QCoreApplication.translate("Form", u"Oil Component", None))
        self.oil_initial_composition_CC.setText(QCoreApplication.translate("Form", u"Initial Composition", None))
        self.IndividualAnalysis_Tab.setTabText(self.IndividualAnalysis_Tab.indexOf(self.Chemical_Page), QCoreApplication.translate("Form", u"Chemical Composition", None))
