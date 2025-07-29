from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt, QThread, Signal)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QMessageBox)
from PySide6.QtGui import QColor
from PySide6 import QtWidgets
from ViewPages import ColorEscale as Cs
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import time
from datetime import datetime
import os


class AnimationWorker(QThread):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def run(self):
        self.page.play_animation()


class SaveWorker(QThread):
    error_message = Signal(str)
    def __init__(self, page):
        super().__init__()
        self.page = page

    def run(self):
        self.page.save_animation()

        self.page.SaveAnimationButton.setText('Save Animation')
        self.page.SaveAnimationButton.setChecked(False)
        self.page.SaveAnimationButton.setDisabled(False)
        self.page.SaveFigButton.setDisabled(False)
        self.page.play_button_time.setDisabled(False)
        self.page.frame_buttons_animation_2_depth.setDisabled(False)
        self.page.frame_buttons_animation_step.setDisabled(False)

        if hasattr(self.page, 'ani') and self.page.running_stopped_by_user:
            os.remove(self.page.save_name) if os.path.exists(self.page.save_name) else None
        elif hasattr(self.page, 'exception_to_save'):
            self.error_message.emit(self.page.exception_to_save)

        del self.page.ani
        plt.close(self.page.fig_anim)


class AnimationStoppedException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Ui_WindButton_LonLatProfile(object):
    def setupUi(self, page, WindButton_LonLatProfile, dataset, variables):
        if not WindButton_LonLatProfile.objectName():
            WindButton_LonLatProfile.setObjectName(u"WindButton_LonLatProfile")
        WindButton_LonLatProfile.resize(546, 436)

        self.mainpage = page
        self.dataset = dataset
        self.u_name, self.v_name = variables['u'], variables['v']
        self.time_name = variables['time']
        self.depth_name = variables['depth']
        self.lon_name, self.lat_name = variables['longitude'], variables['latitude']

        self.horizontalLayout = QHBoxLayout(WindButton_LonLatProfile)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(WindButton_LonLatProfile)
        self.frame.setObjectName(u"frame")
        self.frame.setProperty('ViewCommomFrame', True)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.hori_frame = QHBoxLayout(self.frame)

        self.verticalLayout_ScaleButton = QVBoxLayout()
        self.verticalLayout_ScaleButton.setAlignment(Qt.AlignmentFlag.AlignBottom)

        self.ColorScaleButton = QPushButton()
        self.ColorScaleButton.setObjectName(u"ColorScale")
        self.ColorScaleButton.setProperty('CommomButtonViewPageFunc', True)
        self.ColorScaleButton.setMinimumSize(QSize(100, 30))
        self.ColorScaleButton.setMaximumSize(QSize(100, 30))
        self.ColorScaleButton.clicked.connect(self.open_color_scale_widget)

        self.verticalLayout_ScaleButton.addWidget(self.ColorScaleButton)
        self.hori_frame.addLayout(self.verticalLayout_ScaleButton)

        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(WindButton_LonLatProfile)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setProperty('ViewCommomFrame', True)
        self.frame_2.setMinimumSize(QSize(320, 0))
        self.frame_2.setMaximumSize(QSize(320, 16777215))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_34 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_34)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.TimeFilterLabel = QLabel(self.frame_2)
        self.TimeFilterLabel.setObjectName(u"TimeFilterLabel")
        self.TimeFilterLabel.setProperty('NameLabel_ViewPages', True)
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
        self.frame_buttons_animation_time.setProperty('ViewCommomFrame_Animations', True)
        self.frame_buttons_animation_time.setMinimumSize(QSize(180, 50))
        self.frame_buttons_animation_time.setMaximumSize(QSize(180, 50))
        self.frame_buttons_animation_time.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_buttons_animation_time.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_buttons_animation_time)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.start_button_time = QPushButton(self.frame_buttons_animation_time)
        self.start_button_time.setObjectName(u"start_button_time")
        self.start_button_time.setProperty('CommomButton_Animations', True)
        icon = QIcon()
        icon.addFile(u":/icons/icons/backward - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start_button_time.setIcon(icon)
        self.start_button_time.setIconSize(QSize(20, 20))
        self.start_button_time.clicked.connect(self.firts_in_time)

        self.gridLayout_7.addWidget(self.start_button_time, 0, 0, 1, 1)

        self.backward_button_time = QPushButton(self.frame_buttons_animation_time)
        self.backward_button_time.setObjectName(u"backward_button_time")
        self.backward_button_time.setProperty('CommomButton_Animations', True)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/arrow-left - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backward_button_time.setIcon(icon1)
        self.backward_button_time.setIconSize(QSize(20, 20))
        self.backward_button_time.clicked.connect(self.back_in_time)

        self.gridLayout_7.addWidget(self.backward_button_time, 0, 1, 1, 1)

        self.pause_button_time = QPushButton(self.frame_buttons_animation_time)
        self.pause_button_time.setObjectName(u"pause_button_time")
        self.pause_button_time.setProperty('CommomButton_Animations', True)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/pause - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pause_button_time.setIcon(icon2)
        self.pause_button_time.setIconSize(QSize(20, 20))
        self.pause_button_time.setCheckable(True)
        self.pause_button_time.setChecked(False)

        self.gridLayout_7.addWidget(self.pause_button_time, 0, 2, 1, 1)

        self.play_button_time = QPushButton(self.frame_buttons_animation_time)
        self.play_button_time.setObjectName(u"play_button_time")
        self.play_button_time.setProperty('CommomButton_Animations', True)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/play - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.play_button_time.setIcon(icon3)
        self.play_button_time.setIconSize(QSize(20, 20))
        self.play_button_time.setCheckable(False)
        self.play_button_time.clicked.connect(self.play_time_animation)

        self.gridLayout_7.addWidget(self.play_button_time, 0, 3, 1, 1)

        self.forward_button_time = QPushButton(self.frame_buttons_animation_time)
        self.forward_button_time.setObjectName(u"forward_button_time")
        self.forward_button_time.setProperty('CommomButton_Animations', True)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/arrow-right - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.forward_button_time.setIcon(icon4)
        self.forward_button_time.setIconSize(QSize(20, 20))
        self.forward_button_time.clicked.connect(self.forward_in_time)

        self.gridLayout_7.addWidget(self.forward_button_time, 0, 4, 1, 1)

        self.finish_button_time = QPushButton(self.frame_buttons_animation_time)
        self.finish_button_time.setObjectName(u"finish_button_time")
        self.finish_button_time.setProperty('CommomButton_Animations', True)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/forward - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.finish_button_time.setIcon(icon5)
        self.finish_button_time.setIconSize(QSize(20, 20))
        self.finish_button_time.clicked.connect(self.last_in_time)

        self.gridLayout_7.addWidget(self.finish_button_time, 0, 5, 1, 1)

        self.verticalLayout_13.addWidget(self.frame_buttons_animation_time)

        self.TimeValueLabel = QLabel(self.frame_2)
        self.TimeValueLabel.setObjectName(u"TimeValueLabel")
        self.TimeValueLabel.setProperty('ValueLabel_ViewPages', True)
        self.TimeValueLabel.setMinimumSize(QSize(180, 22))
        self.TimeValueLabel.setMaximumSize(QSize(180, 22))
        self.TimeValueLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.TimeValueLabel)

        self.horizontalLayout_7.addLayout(self.verticalLayout_13)

        self.horizontalSpacer_35 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_35)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_36 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_36)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.DepthFilterLabel = QLabel(self.frame_2)
        self.DepthFilterLabel.setObjectName(u"DepthFilterLabel")
        self.DepthFilterLabel.setProperty('NameLabel_ViewPages', True)
        self.DepthFilterLabel.setMinimumSize(QSize(180, 22))
        self.DepthFilterLabel.setMaximumSize(QSize(180, 22))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.DepthFilterLabel.setFont(font1)

        self.verticalLayout_14.addWidget(self.DepthFilterLabel)

        self.frame_buttons_animation_2_depth = QFrame(self.frame_2)
        self.frame_buttons_animation_2_depth.setObjectName(u"frame_buttons_animation_2_depth")
        self.frame_buttons_animation_2_depth.setProperty('ViewCommomFrame_Animations', True)
        self.frame_buttons_animation_2_depth.setMinimumSize(QSize(180, 50))
        self.frame_buttons_animation_2_depth.setMaximumSize(QSize(180, 50))
        self.frame_buttons_animation_2_depth.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_buttons_animation_2_depth.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_buttons_animation_2_depth)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.start_button_depth = QPushButton(self.frame_buttons_animation_2_depth)
        self.start_button_depth.setObjectName(u"start_button_depth")
        self.start_button_depth.setProperty('CommomButton_Animations', True)
        self.start_button_depth.setIcon(icon)
        self.start_button_depth.setIconSize(QSize(20, 20))
        self.start_button_depth.clicked.connect(self.first_in_depth)

        self.gridLayout_8.addWidget(self.start_button_depth, 0, 0, 1, 1)

        self.backward_button_depth = QPushButton(self.frame_buttons_animation_2_depth)
        self.backward_button_depth.setObjectName(u"backward_button_depth")
        self.backward_button_depth.setProperty('CommomButton_Animations', True)
        self.backward_button_depth.setIcon(icon1)
        self.backward_button_depth.setIconSize(QSize(20, 20))
        self.backward_button_depth.clicked.connect(self.back_in_depth)

        self.gridLayout_8.addWidget(self.backward_button_depth, 0, 1, 1, 1)

        self.pause_button_depth = QPushButton(self.frame_buttons_animation_2_depth)
        self.pause_button_depth.setObjectName(u"pause_button_depth")
        self.pause_button_depth.setProperty('CommomButton_Animations', True)
        self.pause_button_depth.setIcon(icon2)
        self.pause_button_depth.setIconSize(QSize(20, 20))
        self.pause_button_depth.setCheckable(True)
        self.pause_button_depth.setChecked(False)

        self.gridLayout_8.addWidget(self.pause_button_depth, 0, 2, 1, 1)

        self.play_button_depth = QPushButton(self.frame_buttons_animation_2_depth)
        self.play_button_depth.setObjectName(u"play_button_depth")
        self.play_button_depth.setProperty('CommomButton_Animations', True)
        self.play_button_depth.setIcon(icon3)
        self.play_button_depth.setIconSize(QSize(20, 20))
        self.play_button_depth.setCheckable(False)
        self.play_button_depth.clicked.connect(self.play_depth_animation)

        self.gridLayout_8.addWidget(self.play_button_depth, 0, 3, 1, 1)

        self.forward_button_depth = QPushButton(self.frame_buttons_animation_2_depth)
        self.forward_button_depth.setObjectName(u"forward_button_depth")
        self.forward_button_depth.setProperty('CommomButton_Animations', True)
        self.forward_button_depth.setIcon(icon4)
        self.forward_button_depth.setIconSize(QSize(20, 20))
        self.forward_button_depth.clicked.connect(self.forward_in_depth)

        self.gridLayout_8.addWidget(self.forward_button_depth, 0, 4, 1, 1)

        self.finish_button_depth = QPushButton(self.frame_buttons_animation_2_depth)
        self.finish_button_depth.setObjectName(u"finish_button_depth")
        self.finish_button_depth.setProperty('CommomButton_Animations', True)
        self.finish_button_depth.setIcon(icon5)
        self.finish_button_depth.setIconSize(QSize(20, 20))
        self.finish_button_depth.clicked.connect(self.last_in_depth)

        self.gridLayout_8.addWidget(self.finish_button_depth, 0, 5, 1, 1)

        self.verticalLayout_14.addWidget(self.frame_buttons_animation_2_depth)

        self.DepthValueLabel = QLabel(self.frame_2)
        self.DepthValueLabel.setObjectName(u"DepthValueLabel")
        self.DepthValueLabel.setProperty('ValueLabel_ViewPages', True)
        self.DepthValueLabel.setMinimumSize(QSize(180, 22))
        self.DepthValueLabel.setMaximumSize(QSize(180, 22))
        self.DepthValueLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.DepthValueLabel.setWordWrap(False)

        self.verticalLayout_14.addWidget(self.DepthValueLabel)

        self.horizontalLayout_8.addLayout(self.verticalLayout_14)

        self.horizontalSpacer_37 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_37)

        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_38 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_38)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.StepFilterLabel = QLabel(self.frame_2)
        self.StepFilterLabel.setObjectName(u"StepFilterLabel")
        self.StepFilterLabel.setProperty('NameLabel_ViewPages', True)
        self.StepFilterLabel.setMinimumSize(QSize(180, 22))
        self.StepFilterLabel.setMaximumSize(QSize(180, 22))
        self.StepFilterLabel.setFont(font1)

        self.verticalLayout_15.addWidget(self.StepFilterLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_32 = QSpacerItem(18, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_32)

        self.frame_buttons_animation_step = QFrame(self.frame_2)
        self.frame_buttons_animation_step.setObjectName(u"frame_buttons_animation_step")
        self.frame_buttons_animation_step.setProperty('ViewCommomFrame_Animations', True)
        self.frame_buttons_animation_step.setMinimumSize(QSize(80, 50))
        self.frame_buttons_animation_step.setMaximumSize(QSize(80, 50))
        self.frame_buttons_animation_step.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_buttons_animation_step.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_buttons_animation_step)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.backward_button_step = QPushButton(self.frame_buttons_animation_step)
        self.backward_button_step.setObjectName(u"backward_button_step")
        self.backward_button_step.setProperty('CommomButton_Animations', True)
        self.backward_button_step.setIcon(icon1)
        self.backward_button_step.setIconSize(QSize(20, 20))
        self.backward_button_step.clicked.connect(self.back_in_step)

        self.gridLayout_9.addWidget(self.backward_button_step, 0, 0, 1, 1)

        self.forward_button_step = QPushButton(self.frame_buttons_animation_step)
        self.forward_button_step.setObjectName(u"forward_button_step")
        self.forward_button_step.setProperty('CommomButton_Animations', True)
        self.forward_button_step.setIcon(icon4)
        self.forward_button_step.setIconSize(QSize(20, 20))
        self.forward_button_step.clicked.connect(self.forward_in_step)

        self.gridLayout_9.addWidget(self.forward_button_step, 0, 1, 1, 1)

        self.horizontalLayout_2.addWidget(self.frame_buttons_animation_step)

        self.horizontalSpacer_33 = QSpacerItem(18, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_33)

        self.verticalLayout_15.addLayout(self.horizontalLayout_2)

        self.StepValueLabel = QLabel(self.frame_2)
        self.StepValueLabel.setObjectName(u"StepValueLabel")
        self.StepValueLabel.setProperty('ValueLabel_ViewPages', True)
        self.StepValueLabel.setMinimumSize(QSize(180, 22))
        self.StepValueLabel.setMaximumSize(QSize(180, 22))
        self.StepValueLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.StepValueLabel)

        self.horizontalLayout_14.addLayout(self.verticalLayout_15)

        self.horizontalSpacer_39 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_39)

        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_40 = QSpacerItem(18, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_40)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.SaveFigButton = QPushButton(self.frame_2)
        self.SaveFigButton.setObjectName(u"SaveFigButton")
        self.SaveFigButton.setProperty('CommomButtonViewPageFunc', True)
        self.SaveFigButton.setMinimumSize(QSize(120, 30))
        self.SaveFigButton.setMaximumSize(QSize(120, 30))

        self.SaveFigButton.clicked.connect(self.save_figure)

        self.horizontalLayout_6.addWidget(self.SaveFigButton)

        self.SaveAnimationButton = QPushButton(self.frame_2)
        self.SaveAnimationButton.setObjectName(u"SaveAnimationButton")
        self.SaveAnimationButton.setProperty('CommomButtonViewPageFunc', True)
        self.SaveAnimationButton.setMinimumSize(QSize(120, 30))
        self.SaveAnimationButton.setMaximumSize(QSize(120, 30))
        self.SaveAnimationButton.setCheckable(True)
        self.SaveAnimationButton.setChecked(False)
        self.SaveAnimationButton.clicked.connect(self.start_save_animation)

        self.horizontalLayout_6.addWidget(self.SaveAnimationButton)

        self.horizontalLayout_15.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer_41 = QSpacerItem(18, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_41)

        self.verticalLayout.addLayout(self.horizontalLayout_15)

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

        self.graph_num = QVBoxLayout()
        self.graph_num.setSpacing(5)
        self.graph_num.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vecmean = Figure(figsize=(2, 2))
        self.canvasmean = FigureCanvas(self.vecmean)
        self.graph_num.addWidget(self.canvasmean, alignment=Qt.AlignmentFlag.AlignCenter)

        self.meanvectorlabel = QLabel(self.frame)
        self.meanvectorlabel.setObjectName(u"AverageWindDirection")
        self.meanvectorlabel.setProperty('ValueLabel_ViewPages', True)
        self.meanvectorlabel.setMinimumSize(QSize(180, 22))
        self.meanvectorlabel.setMaximumSize(QSize(180, 22))
        # self.meanvectorlabel.setStyleSheet(u"border: 1px solid #212b33")
        self.meanvectorlabel.setText(u"Average Current Direction")
        self.meanvectorlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.graph_num.addWidget(self.meanvectorlabel, alignment=Qt.AlignmentFlag.AlignCenter)

        # Adicionar os dois layouts verticais ao layout horizontal principal
        self.hori_frame.addLayout(self.graph_layout)
        self.hori_frame.addLayout(self.graph_num)

        self.frame.setLayout(self.hori_frame)

        shadow_elements = {
            'frame',
            'frame_2',
            'frame_buttons_animation_time',
            'frame_buttons_animation_2_depth',
            'frame_buttons_animation_step',
            'SaveFigButton',
            'SaveAnimationButton',
            'ColorScaleButton'
        }

        try:
            for x in shadow_elements:
                effect = QtWidgets.QGraphicsDropShadowEffect(WindButton_LonLatProfile)
                effect.setBlurRadius(18)
                effect.setXOffset(0)
                effect.setYOffset(0)
                effect.setColor(QColor(0, 0, 0, 255))
                getattr(self, x).setGraphicsEffect(effect)

            self.f_magnitude = lambda x_, y_: np.sqrt(x_ ** 2 + y_ ** 2)
            self.lat = [lat_value for lat_value in self.dataset[self.lat_name].values]
            self.lon = [lon_value for lon_value in self.dataset[self.lon_name].values]
            self.time = self.dataset[self.time_name].values
            self.depth = self.dataset[self.depth_name].values
            self.time_selected = self.time[0]
            self.sel_time(self.time_selected)
            self.step = 1
            self.lats_step = self.step
            self.sel_step(self.step)
            self.depth_selected = self.depth[0]
            self.sel_depth()
            self.var_selected = None
            self.color_scale_widget = None
            self.current_min, self.current_max = self.set_magvector(data=self.dataset)
            self.current_scale = "RdYlGn_r"
            self.plot_first_graph()
            self.plot_first_average_graph()
        except Exception as e:
            raise e

    def sel_time(self, value_time):
        time_to_format = str(value_time).split('.')[0]
        self.t_formated = datetime.strptime(time_to_format, '%Y-%m-%dT%H:%M:%S').strftime('%m-%d-%Y-%Hh')
        self.TimeValueLabel.setText(f'{self.t_formated}')

    def sel_step(self, value_step):
        self.StepValueLabel.setText(f'{value_step}')

    def sel_depth(self):
        self.DepthValueLabel.setText(f'{self.depth_selected} metros')

    def first_in_depth(self):
        if self.depth_selected == self.depth[0]:
            return
        else:
            self.depth_selected = self.depth[0]
            self.sel_depth()
            self.plot_current_vec()
            self.plot_average_vec_current()

    def back_in_depth(self):
        if self.depth_selected == self.depth[0]:
            return
        else:
            index = np.where(self.depth == self.depth_selected)[0][0]
            self.depth_selected = self.depth[index - 1]
            self.sel_depth()
            self.plot_current_vec()
            self.plot_average_vec_current()

    def forward_in_depth(self):
        if self.depth_selected == self.depth[-1]:
            return
        else:
            index = np.where(self.depth == self.depth_selected)[0][0]
            self.depth_selected = self.depth[index + 1]
            self.sel_depth()
            self.plot_current_vec()
            self.plot_average_vec_current()

    def last_in_depth(self):
        if self.depth_selected == self.depth[-1]:
            return
        else:
            self.depth_selected = self.depth[-1]
            self.sel_depth()
            self.plot_current_vec()
            self.plot_average_vec_current()

    def forward_in_step(self):
        max_step = min(len(self.lat), len(self.lon)) - 1
        if self.step == max_step:
            return
        else:
            self.step += 1
            self.sel_step(self.step)
            self.plot_current_vec()
            self.plot_average_vec_current()

    def back_in_step(self):
        if self.step == 1:
            return
        else:
            self.step -= 1
            self.sel_step(self.step)
            self.plot_current_vec()
            self.plot_average_vec_current()

    def firts_in_time(self):
        if self.time_selected == self.time[0]:
            return
        else:
            self.time_selected = self.time[0]
            self.sel_time(self.time_selected)
            self.plot_current_vec()
            self.plot_average_vec_current()

    def last_in_time(self):
        if self.time_selected == self.time[-1]:
            return
        else:
            self.time_selected = self.time[-1]
            self.sel_time(self.time_selected)
            self.plot_current_vec()
            self.plot_average_vec_current()

    def forward_in_time(self):
        if self.time_selected == self.time[-1]:
            return
        else:
            index = np.where(self.time == self.time_selected)[0][0]
            self.time_selected = self.time[index + 1]
            self.sel_time(self.time_selected)
            self.plot_current_vec()
            self.plot_average_vec_current()

    def back_in_time(self):
        if self.time_selected == self.time[0]:
            return
        else:
            index = np.where(self.time == self.time_selected)[0][0]
            self.time_selected = self.time[index - 1]
            self.sel_time(self.time_selected)
            self.plot_current_vec()
            self.plot_average_vec_current()

    def open_color_scale_widget(self):
        if self.color_scale_widget is None:
            self.color_scale_widget = Cs.ColorScaleWidget(self.current_scale)

        self.color_scale_widget.scale_updated.connect(self.update_color_scale)
        self.color_scale_widget.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.color_scale_widget.setWindowFlag(Qt.WindowType.Window)
        self.color_scale_widget.show()

    def update_color_scale(self, min_value, max_value, scale):
        self.current_min = min_value
        self.current_max = max_value
        self.current_scale = scale
        self.plot_first_graph()
        self.color_scale_widget.close()

    def play_depth_animation(self):
        self.var_selected = 'depth'
        self.worker = AnimationWorker(page=self)
        self.worker.start()

    def play_time_animation(self):
        self.var_selected = 'time'
        self.worker = AnimationWorker(page=self)
        self.worker.start()

    def plot_average_vec_current(self):
        dict_to_sel = {
            self.time_name: self.time_selected,
            self.depth_name: self.depth_selected
        }

        u = self.dataset[self.u_name].sel(dict_to_sel).values
        v = self.dataset[self.v_name].sel(dict_to_sel).values

        u_mean = np.nanmean(u)
        v_mean = np.nanmean(v)

        mag = np.sqrt(u_mean ** 2 + v_mean ** 2)
        desired_mag = 4
        if mag != 0:
            scale = desired_mag / mag
            u_mean *= scale
            v_mean *= scale

        self.arrow.remove()
        self.arrow = self.ax_mean.arrow(0, 0, u_mean, v_mean, head_width=0.5, head_length=0.5, fc='#08090A', ec='#08090A')

        self.canvasmean.draw()

    def plot_first_average_graph(self):
        self.vecmean.clear()
        self.canvasmean.draw()

        dict_to_sel = {
            self.time_name: self.time_selected,
            self.depth_name: self.depth_selected
        }

        u = self.dataset[self.u_name].sel(dict_to_sel).values
        v = self.dataset[self.v_name].sel(dict_to_sel).values

        u_mean = np.nanmean(u)
        v_mean = np.nanmean(v)

        mag = np.sqrt(u_mean ** 2 + v_mean ** 2)
        desired_mag = 4
        if mag != 0:
            scale = desired_mag / mag
            u_mean *= scale
            v_mean *= scale

        self.ax_mean = self.vecmean.add_subplot(111)

        self.arrow = self.ax_mean.arrow(0, 0, u_mean, v_mean, head_width=0.5, head_length=0.5, fc='white', ec='#08090A')

        self.ax_mean.text(0, 5.2, "N", fontsize=12, ha='center', color='#08090A')
        self.ax_mean.text(5.2, 0, "E", fontsize=12, va='center', color='#08090A')
        self.ax_mean.text(0, -6, "S", fontsize=12, ha='center', color='#08090A')
        self.ax_mean.text(-6.2, 0, "W", fontsize=12, va='center', color='#08090A')

        self.ax_mean.set_xlim(-5, 5)
        self.ax_mean.set_ylim(-5, 5)
        self.ax_mean.axhline(0, color='#08090A', lw=0.5)
        self.ax_mean.axvline(0, color='#08090A', lw=0.5)
        self.ax_mean.set_aspect('equal', adjustable='box')

        self.ax_mean.axis('off')

        self.canvasmean.draw()
        self.canvasmean.figure.set_facecolor("#C3C3C3")

    def start_save_animation(self):
        if self.SaveAnimationButton.isChecked():
            self.SaveAnimationButton.setText('Stop Saving')
            self.SaveFigButton.setDisabled(True)
            self.play_button_time.setDisabled(True)
            self.frame_buttons_animation_2_depth.setDisabled(True)
            self.frame_buttons_animation_step.setDisabled(True)
            self.is_running = True
            self.running_stopped_by_user = False
            self.save_worker = SaveWorker(page=self)
            self.save_worker.error_message.connect(self.error_animation_save)
            self.save_worker.start()
            return
        else:
            self.is_running = False
            self.SaveAnimationButton.setText('Stopping...')
            self.SaveAnimationButton.setChecked(False)
            self.SaveAnimationButton.setDisabled(True)
            self.SaveFigButton.setDisabled(False)
            self.play_button_time.setDisabled(False)
            self.frame_buttons_animation_2_depth.setDisabled(False)
            self.frame_buttons_animation_step.setDisabled(False)
            return

    def update(self, frame):
        if frame == 0:
            return

        if not self.is_running:
            self.SaveAnimationButton.setDisabled(True)
            self.ani.event_source.stop()
            self.running_stopped_by_user = True
            return
        else:
            dict_to_sel = {
                self.time_name: self.time[frame],
                self.depth_name: self.depth_selected
            }

            u_plot = self.dataset[self.u_name].sel(dict_to_sel).values[::self.step,
                     ::self.step]
            v_plot = self.dataset[self.v_name].sel(dict_to_sel).values[::self.step,
                     ::self.step]

            vec_mag = self.f_magnitude(u_plot, v_plot)
            u_norm = u_plot / vec_mag
            v_norm = v_plot / vec_mag
            colors_ = self.cmap_anim(self.norm_anim(vec_mag))
            colors_ = colors_.reshape(-1, 4)

            time_to_format = str(self.time[frame]).split('.')[0]
            t_formated = datetime.strptime(time_to_format, '%Y-%m-%dT%H:%M:%S').strftime('%m-%d-%Y-%Hh')
            plt.title(t_formated, fontsize=20)

            self.quiver_anim.set_UVC(u_norm, v_norm)
            self.quiver_anim.set_color(colors_)

    def save_animation(self):
        self.time_anim = list(self.dataset[self.time_name].values)
        lon, lat = self.dataset[self.lon_name].values, self.dataset[self.lat_name].values
        lons, lats = np.meshgrid(lon, lat)
        self.lon2d_anim, self.lat2d_anim = lons[::self.step, ::self.step], lats[::self.step, ::self.step]

        self.fig_anim, self.axs = plt.subplots(figsize=(12, 12), subplot_kw={'projection': ccrs.Mercator()})
        self.axs.set_extent([min(lon), max(lon), min(lat), max(lat)], crs=ccrs.PlateCarree())

        time_to_format = str(self.time[0]).split('.')[0]
        t_formated = datetime.strptime(time_to_format, '%Y-%m-%dT%H:%M:%S').strftime('%m-%d-%Y-%Hh')
        plt.title(t_formated, fontsize=20)

        self.axs.add_feature(cfeature.COASTLINE)
        self.axs.add_feature(cfeature.BORDERS, linestyle="-")
        self.axs.add_feature(cfeature.STATES, linestyle=":")
        self.axs.add_feature(cfeature.LAND, color='#5F7470')
        self.axs.add_feature(cfeature.LAKES, color='#2A324B')

        lat_label_step = (max(lat) - min(lat)) // 3 if (max(lat) - min(lat)) > 3 else 3
        lon_label_step = (max(lon) - min(lon)) // 3 if (max(lon) - min(lon)) > 3 else 3

        gl = self.axs.gridlines(draw_labels=True, linestyle="--", alpha=0.5)
        gl.top_labels = False
        gl.right_labels = False
        gl.bottom_labels = True
        gl.left_labels = True
        gl.xlocator = plt.MultipleLocator(lon_label_step)
        gl.ylocator = plt.MultipleLocator(lat_label_step)
        gl.xlabel_style = {'fontsize': 9, 'color': '#08090A'}
        gl.ylabel_style = {'fontsize': 9, 'color': '#08090A'}

        self.axs.annotate('Longitude', xy=(0.5, -0.08), xycoords='axes fraction',
                          ha='center', fontsize=12, color='#08090A')

        self.axs.annotate('Latitude', xy=(-0.08, 0.5), xycoords='axes fraction',
                          ha='center', rotation=90, fontsize=12, color='#08090A')

        self.cmap_anim = cm.get_cmap(self.current_scale)
        self.norm_anim = plt.Normalize(vmin=self.current_min, vmax=self.current_max)

        cbar = self.fig_anim.colorbar(cm.ScalarMappable(norm=self.norm_anim, cmap=self.cmap_anim), ax=self.axs,
                                      orientation='vertical', pad=0.05)
        cbar.set_label(f'Vector magnitude [{self.dataset[self.u_name].attrs['units']}]', fontsize=18)
        cbar.ax.tick_params(labelsize=16)

        u_first = self.dataset[self.u_name].sel({self.time_name: self.time[0], self.depth_name: self.depth_selected}).values[::self.step,
                 ::self.step]
        v_first = self.dataset[self.v_name].sel({self.time_name: self.time[0], self.depth_name: self.depth_selected}).values[::self.step,
                 ::self.step]
        vec_mag_first = self.f_magnitude(u_first, v_first)
        u_norm_first = u_first / vec_mag_first
        v_norm_first = v_first / vec_mag_first
        colors = self.cmap_anim(self.norm_anim(vec_mag_first))
        colors = colors.reshape(-1, 4)

        self.quiver_anim = self.axs.quiver(self.lon2d_anim, self.lat2d_anim, u_norm_first, v_norm_first, color=colors,
                                           scale=30, transform=ccrs.PlateCarree())

        try:
            self.ani = FuncAnimation(
                self.fig_anim, self.update, frames=len(self.time) - 1, interval=5000
            )

            path_to_save = os.path.join(self.mainpage.project.caminho, 'Animations')
            os.makedirs(path_to_save, exist_ok=True)
            file_path = os.path.join(path_to_save, 'SeaWaterVelocity')

            self.save_name = (f'{file_path} for {self.mainpage.comboBox.currentText()[:-3]} _ '
                              f'{int(self.depth_selected)}m.gif')
            self.ani.save(
                self.save_name,
                writer='pillow',
                fps=3
            )
        except Exception as e:
            self.exception_to_save = str(e)

        self.is_running = False

    def error_animation_save(self, message):
        QMessageBox.warning(self.frame, "Save animation error", message)

    def save_figure(self):
        lon, lat = self.dataset[self.lon_name].values, self.dataset[self.lat_name].values

        fig, ax = plt.subplots(figsize=(12, 12), subplot_kw={'projection': ccrs.Mercator()})
        ax.set_extent([min(lon), max(lon), min(lat), max(lat)], crs=ccrs.PlateCarree())

        ax.add_feature(cfeature.COASTLINE)
        ax.add_feature(cfeature.BORDERS, linestyle="-")
        ax.add_feature(cfeature.STATES, linestyle=":")

        lat_label_step = (max(lat) - min(lat)) // 3 if (max(lat) - min(lat)) > 3 else 3
        lon_label_step = (max(lon) - min(lon)) // 3 if (max(lon) - min(lon)) > 3 else 3

        gl = ax.gridlines(draw_labels=True, linestyle="--", alpha=0.5)
        gl.top_labels = False
        gl.right_labels = False
        gl.bottom_labels = True
        gl.left_labels = True
        gl.xlocator = plt.MultipleLocator(lon_label_step)
        gl.ylocator = plt.MultipleLocator(lat_label_step)
        gl.xlabel_style = {'fontsize': 6, 'color': '#08090A'}
        gl.ylabel_style = {'fontsize': 6, 'color': '#08090A'}

        ax.annotate('Longitude', xy=(0.5, -0.08), xycoords='axes fraction',
                         ha='center', fontsize=10, color='#08090A')

        ax.annotate('Latitude', xy=(-0.08, 0.5), xycoords='axes fraction',
                         ha='center', rotation=90, fontsize=10, color='#08090A')

        dict_to_sel = {
            self.time_name: self.time_selected,
            self.depth_name: self.depth_selected
        }

        u_plot = self.dataset[self.u_name].sel(dict_to_sel).values[::self.step, ::self.step]
        v_plot = self.dataset[self.v_name].sel(dict_to_sel).values[::self.step, ::self.step]

        lons, lats = np.meshgrid(lon, lat)
        lon_plot, lat_plot = lons[::self.step, ::self.step], lats[::self.step, ::self.step]

        vec_mag = self.f_magnitude(u_plot, v_plot)
        u_norm = u_plot / vec_mag
        v_norm = v_plot / vec_mag

        cmap = cm.get_cmap(self.current_scale)
        norm = plt.Normalize(vmin=self.current_min, vmax=self.current_max)
        colors_ = cmap(norm(vec_mag))
        colors_ = colors_.reshape(-1, 4)

        ax.quiver(lon_plot, lat_plot, u_norm, v_norm, color=colors_, scale=30,
                                     transform=ccrs.PlateCarree())
        cbar = plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, orientation='vertical', pad=0.05)
        cbar.set_label(f'Magnitude dos Vetores [{self.dataset[self.u_name].units}]', fontsize=18)
        cbar.ax.tick_params(labelsize=16)
        cbar.ax.yaxis.set_tick_params(color='#08090A')
        plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='#08090A')

        plt.title(f'{self.t_formated} - {self.depth_selected}m', fontsize=20)

        path_to_save = os.path.join(self.mainpage.project.caminho, 'figs')
        
        os.makedirs(path_to_save, exist_ok=True)

        file_path = os.path.join(path_to_save, 'SeaWater Velocity')

        plt.savefig(f'{file_path} for {self.mainpage.comboBox.currentText()[:-3]} _ '

                    f'{self.t_formated} _ {self.depth_selected}m.png', transparent=True)
        plt.close()

    def cls_components(self):
        self.pause_button_time.setChecked(False)
        self.pause_button_depth.setChecked(False)
        self.start_button_time.setDisabled(True)
        self.backward_button_time.setDisabled(True)
        self.play_button_time.setDisabled(True)
        self.forward_button_time.setDisabled(True)
        self.finish_button_time.setDisabled(True)
        self.start_button_depth.setDisabled(True)
        self.backward_button_depth.setDisabled(True)
        self.play_button_depth.setDisabled(True)
        self.forward_button_depth.setDisabled(True)
        self.finish_button_depth.setDisabled(True)
        self.SaveAnimationButton.setDisabled(True)
        self.SaveFigButton.setDisabled(True)
        self.frame_buttons_animation_step.setDisabled(True)
        self.frame.setDisabled(True)
        self.mainpage.frame.setDisabled(True)

    def opn_components(self):
        self.frame_buttons_animation_2_depth.setDisabled(False)
        self.frame_buttons_animation_time.setDisabled(False)
        self.start_button_time.setDisabled(False)
        self.backward_button_time.setDisabled(False)
        self.play_button_time.setDisabled(False)
        self.forward_button_time.setDisabled(False)
        self.finish_button_time.setDisabled(False)
        self.start_button_depth.setDisabled(False)
        self.backward_button_depth.setDisabled(False)
        self.play_button_depth.setDisabled(False)
        self.forward_button_depth.setDisabled(False)
        self.finish_button_depth.setDisabled(False)
        self.SaveAnimationButton.setDisabled(False)
        self.SaveFigButton.setDisabled(False)
        self.frame_buttons_animation_step.setDisabled(False)
        self.frame.setDisabled(False)
        self.mainpage.frame.setDisabled(False)

    def play_animation(self):
        if (self.var_selected == 'time' and self.time_selected == self.time[-1]) or (
                self.var_selected == 'depth' and self.depth_selected == self.depth[-1]):
            return
        else:
            self.cls_components()

            if self.var_selected == 'time':
                self.frame_buttons_animation_2_depth.setDisabled(True)

                while True:
                    index = np.where(self.time == self.time_selected)[0][0]
                    self.time_selected = self.time[index + 1]
                    self.sel_time(self.time_selected)
                    self.plot_current_vec()
                    self.plot_average_vec_current()

                    if self.pause_button_time.isChecked():
                        break
                    if self.time_selected >= self.time[-1]:
                        break

                    time.sleep(.2)
                    QApplication.processEvents()
            else:
                self.frame_buttons_animation_time.setDisabled(True)

                while True:
                    index = np.where(self.depth == self.depth_selected)[0][0]
                    self.depth_selected = self.depth[index + 1]
                    self.sel_depth()
                    self.plot_current_vec()
                    self.plot_average_vec_current()

                    if self.pause_button_depth.isChecked():
                        break
                    if self.depth_selected >= self.depth[-1]:
                        break

                    time.sleep(.2)
                    QApplication.processEvents()

            self.opn_components()

    def set_magvector(self, data):
        """
        Funcition to compute the vector magnitiude to normalize color map
        :param data:
        :return: min and max value to normalize the color map
        """
        mag = [self.f_magnitude(data[self.u_name][:, :, :, :], data[self.v_name][:, :, :, :])]
        magnitude_min = np.nanmin(mag)
        magnitude_max = np.nanmax(mag)
        if magnitude_max == magnitude_min:
            magnitude_max += 1e-6
        return magnitude_min, magnitude_max

    def plot_current_vec(self):
        if self.step != self.lats_step:
            self.plot_first_graph()
        else:
            dict_to_sel = {
                self.time_name: self.time_selected,
                self.depth_name: self.depth_selected
            }

            u_plot = self.dataset[self.u_name].sel(dict_to_sel).values[
                     ::self.step,
                     ::self.step]
            v_plot = self.dataset[self.v_name].sel(dict_to_sel).values[
                     ::self.step,
                     ::self.step]

            vec_mag = self.f_magnitude(u_plot, v_plot)
            u_norm = u_plot / vec_mag
            v_norm = v_plot / vec_mag

            cmap = cm.get_cmap(self.current_scale)
            norm = plt.Normalize(vmin=self.current_min, vmax=self.current_max)
            colors_ = cmap(norm(vec_mag))
            colors_ = colors_.reshape(-1, 4)

            self.quiver.set_UVC(u_norm, v_norm)
            self.quiver.set_color(colors_)

            self.canvas.draw()

    def plot_first_graph(self):
        self.figure.clear()
        self.canvas.draw()

        lon, lat = self.dataset[self.lon_name].values, self.dataset[self.lat_name].values

        # Novo gráfico
        self.ax = self.figure.add_subplot(111, projection=ccrs.Mercator())
        self.ax.set_extent([min(lon), max(lon), min(lat), max(lat)], crs=ccrs.PlateCarree())

        dict_to_sel = {
            self.time_name: self.time_selected,
            self.depth_name: self.depth_selected
        }

        u_plot = self.dataset[self.u_name].sel(dict_to_sel).values[::self.step, ::self.step]
        v_plot = self.dataset[self.v_name].sel(dict_to_sel).values[::self.step, ::self.step]

        self.lons, self.lats = np.meshgrid(lon, lat)
        lon_plot, lat_plot = self.lons[::self.step, ::self.step], self.lats[::self.step, ::self.step]

        # Calcula magnitude e normaliza vetores
        vec_mag = self.f_magnitude(u_plot, v_plot)
        u_norm = u_plot / vec_mag
        v_norm = v_plot / vec_mag

        # Mapa de cores
        cmap = cm.get_cmap(self.current_scale)
        norm = Normalize(vmin=self.current_min, vmax=self.current_max)
        colors_ = cmap(norm(vec_mag)).reshape(-1, 4)

        # Plota vetores
        self.quiver = self.ax.quiver(lon_plot, lat_plot, u_norm, v_norm, color=colors_, scale=30,
                                     transform=ccrs.PlateCarree())

        # Barra de cores
        cbar = plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=self.ax, orientation='vertical', pad=0.05)
        cbar.set_label(f'Magnitude dos Vetores [{self.dataset[self.u_name].units}]', fontsize=6, color="#08090A")
        cbar.ax.tick_params(labelsize=8)
        cbar.ax.yaxis.set_tick_params(color='#08090A')
        plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='#08090A')

        # Recursos geográficos
        self.ax.add_feature(cfeature.COASTLINE)
        self.ax.add_feature(cfeature.BORDERS, linestyle="-")
        self.ax.add_feature(cfeature.STATES, linestyle=":")

        # Linhas de paralelos e meridianos
        lat_label_step = (max(lat) - min(lat)) // 3 if (max(lat) - min(lat)) > 3 else 3
        lon_label_step = (max(lon) - min(lon)) // 3 if (max(lon) - min(lon)) > 3 else 3

        gl = self.ax.gridlines(draw_labels=True, linestyle="--", alpha=0.5)
        gl.top_labels = False
        gl.right_labels = False
        gl.bottom_labels = True
        gl.left_labels = True
        gl.xlocator = plt.MultipleLocator(lon_label_step)
        gl.ylocator = plt.MultipleLocator(lat_label_step)
        gl.xlabel_style = {'fontsize': 6, 'color': '#08090A'}
        gl.ylabel_style = {'fontsize': 6, 'color': '#08090A'}

        self.ax.annotate('Longitude', xy=(0.5, -0.09), xycoords='axes fraction',
                             ha='center', fontsize=8, color='#08090A')

        self.ax.annotate('Latitude', xy=(-0.15, 0.5), xycoords='axes fraction',
                             ha='center', rotation=90, fontsize=8, color='#08090A')

        # Canvas e ajustes
        self.canvas.draw()
        self.figure.canvas.draw_idle()
        self.canvas.figure.subplots_adjust(
            top=0.975,
            bottom=0.116,
            left=0.124,
            right=0.97,
            hspace=0.2,
            wspace=0.2
        )
        self.canvas.figure.set_facecolor("#C3C3C3")

        self.lats_step = self.step

    def retranslateUi(self, WindButton_LonLatProfile):
        WindButton_LonLatProfile.setWindowTitle(QCoreApplication.translate("WindButton_LonLatProfile", u"Form", None))
        self.TimeFilterLabel.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"Time Filter", None))
        self.start_button_time.setText("")
        self.backward_button_time.setText("")
        self.pause_button_time.setText("")
        self.play_button_time.setText("")
        self.forward_button_time.setText("")
        self.finish_button_time.setText("")
        self.DepthFilterLabel.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"Depth Filter", None))
        self.start_button_depth.setText("")
        self.backward_button_depth.setText("")
        self.pause_button_depth.setText("")
        self.play_button_depth.setText("")
        self.forward_button_depth.setText("")
        self.finish_button_depth.setText("")
        self.StepFilterLabel.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"Step Filter", None))
        self.backward_button_step.setText("")
        self.forward_button_step.setText("")
        self.StepValueLabel.setText(
            QCoreApplication.translate("WindButton_LonLatProfile", u"Aqui vai o valor de step", None))
        self.SaveFigButton.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"Save Figure", None))
        self.SaveAnimationButton.setText(
            QCoreApplication.translate("WindButton_LonLatProfile", u"Save Animation", None))
        self.ColorScaleButton.setText(QCoreApplication.translate("WindButton_LonLatProfile", u"Set Color Scale", None))
