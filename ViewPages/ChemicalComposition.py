# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChemicalCompositionYboxFi.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt, QThread)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QPushButton, QScrollArea, QSizePolicy,
                               QSpacerItem, QVBoxLayout, QWidget, QRadioButton, QMessageBox)
from ViewPages import GroupSelectionPage as GSW
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import time
from PySide6.QtGui import QColor
from PySide6 import QtWidgets


class AnimationWorker(QThread):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def run(self):
        self.page.start_anim()


class Groups:
    def __init__(self, complist, alldata):
        self.composition_list = complist
        self.filter_datacomp(alldata.dataframe)

    def filter_datacomp(self, df):
        data = {
            key: pd.DataFrame(item.loc[self.composition_list].sum(axis=0)).T
            for key, item in df.items()
        }
        for _, item in data.items():
            item.columns = item.columns.str.replace(r"\(mt\)$", "", regex=True)
        setattr(self, "data", data)


class Ui_Form(object):
    def setupUi(self, Form, df):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(770, 447)

        self.data = df
        self.groups = {}

        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")

        self.frame_to_groups = QFrame(Form)
        self.frame_to_groups.setObjectName(u"frame_to_groups")
        self.frame_to_groups.setMinimumSize(QSize(150, 0))
        self.frame_to_groups.setMaximumSize(QSize(150, 16777215))
        self.frame_to_groups.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_to_groups.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_2 = QVBoxLayout(self.frame_to_groups)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.grouplabel_name = QLabel()  # self.frame_to_groups
        self.grouplabel_name.setObjectName(u"grouplabel_name")

        self.verticalLayout_2.addWidget(self.grouplabel_name)

        # self.horizontalLayout_4 = QHBoxLayout()
        # self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_group_buttons = QFrame()  # self.frame_to_groups
        self.frame_group_buttons.setObjectName(u"frame_group_buttons")
        # self.frame_group_buttons.setProperty("commomFrame_group", True)
        self.frame_group_buttons.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed))
        # sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.frame_group_buttons.sizePolicy().hasHeightForWidth())
        # self.frame_group_buttons.setSizePolicy(sizePolicy)
        self.frame_group_buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_group_buttons.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_3 = QHBoxLayout()  # self.frame_group_buttons
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, 0)
        self.frame_group_buttons.setLayout(self.horizontalLayout_3)

        self.plusbutton = QPushButton(self.frame_group_buttons)
        self.plusbutton.setObjectName(u"plusbutton")
        icon_plus = QIcon()
        icon_plus.addFile(u":/icons/icons/mais - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.plusbutton.setIcon(icon_plus)
        self.plusbutton.setIconSize(QSize(19, 19))
        # sizePolicy.setHeightForWidth(self.plusbutton.sizePolicy().hasHeightForWidth())
        # self.plusbutton.setSizePolicy(sizePolicy)
        self.plusbutton.setMinimumSize(QSize(21, 21))
        self.plusbutton.setMaximumSize(QSize(21, 21))
        self.plusbutton.clicked.connect(self.open_gsw_page)

        self.horizontalLayout_3.addWidget(self.plusbutton)

        self.minusbutton = QPushButton(self.frame_group_buttons)
        self.minusbutton.setObjectName(u"minusbutton")
        icon_minus = QIcon()
        icon_minus.addFile(u":/icons/icons/menos - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minusbutton.setIcon(icon_minus)
        self.minusbutton.setIconSize(QSize(19, 19))
        # sizePolicy.setHeightForWidth(self.minusbutton.sizePolicy().hasHeightForWidth())
        # self.minusbutton.setSizePolicy(sizePolicy)
        self.minusbutton.setMinimumSize(QSize(21, 21))
        self.minusbutton.setMaximumSize(QSize(21, 21))
        self.minusbutton.clicked.connect(self.delete_radio)

        self.horizontalLayout_3.addWidget(self.minusbutton)

        self.editbutton = QPushButton(self.frame_group_buttons)
        self.editbutton.setObjectName(u"editbutton")
        icon_edit = QIcon()
        icon_edit.addFile(u":/icons/icons/editar - verde escuro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.editbutton.setIcon(icon_edit)
        self.editbutton.setIconSize(QSize(10, 10))
        self.editbutton.setMinimumSize(QSize(21, 21))
        self.editbutton.setMaximumSize(QSize(21, 21))
        self.editbutton.clicked.connect(self.editgroup)

        self.horizontalLayout_3.addWidget(self.editbutton)

        self.verticalLayout_2.addWidget(self.frame_group_buttons)

        # self.horizontalLayout_4.addWidget(self.frame_group_buttons)

        # self.horizontalSpacer = QSpacerItem(28, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        # self.horizontalLayout_4.addItem(self.horizontalSpacer)

        # self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.scrollArea = QScrollArea(self.frame_to_groups)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setProperty("commomFrame_group", True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 128, 220))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollcontentLayout = QVBoxLayout()
        self.scrollcontentLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scrollAreaWidgetContents.setLayout(self.scrollcontentLayout)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.plot_button = QPushButton(self.frame_to_groups)
        self.plot_button.setObjectName(u"plot_button")
        self.plot_button.clicked.connect(self.create_data)

        self.verticalLayout_2.addWidget(self.plot_button)

        self.gridLayout.addWidget(self.frame_to_groups, 0, 0, 1, 1)

        self.main_frame_CC = QFrame(Form)
        self.main_frame_CC.setObjectName(u"main_frame_CC")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_frame_CC.sizePolicy().hasHeightForWidth())
        self.main_frame_CC.setSizePolicy(sizePolicy1)
        self.main_frame_CC.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame_CC.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.main_frame_CC, 0, 1, 1, 1)

        self.frame_to_buttons = QFrame(Form)
        self.frame_to_buttons.setObjectName(u"frame_to_buttons")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_to_buttons.sizePolicy().hasHeightForWidth())
        self.frame_to_buttons.setSizePolicy(sizePolicy2)
        self.frame_to_buttons.setMinimumSize(QSize(0, 80))
        self.frame_to_buttons.setMaximumSize(QSize(16777215, 80))
        self.frame_to_buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_to_buttons.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2 = QHBoxLayout(self.frame_to_buttons)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.import_button_CC_2 = QPushButton(self.frame_to_buttons)
        self.import_button_CC_2.setObjectName(u"import_button_CC_2")
        self.import_button_CC_2.setProperty('commomButton', True)
        self.import_button_CC_2.setMinimumSize(QSize(150, 30))
        self.import_button_CC_2.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_2.addWidget(self.import_button_CC_2)
        self.horizontalLayout_2.addStretch()

        self.frame_buttons_animation_time = QFrame(self.frame_to_buttons)
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
        self.play_button_time.clicked.connect(self.play_animation)

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

        self.horizontalLayout_2.addWidget(self.frame_buttons_animation_time)
        self.horizontalLayout_2.addStretch()

        self.import_button_CC = QPushButton(self.frame_to_buttons)
        self.import_button_CC.setObjectName(u"import_button_CC")
        self.import_button_CC.setProperty('commomButton', True)
        self.import_button_CC.setMinimumSize(QSize(150, 30))
        self.import_button_CC.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_2.addWidget(self.import_button_CC)

        self.gridLayout.addWidget(self.frame_to_buttons, 1, 0, 1, 2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

        self.gsw_widget = None
        self.radiobuttons = []
        self.list_to_edit = None

        self.graph_layout = QVBoxLayout()
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.graph_layout.addWidget(self.canvas)
        self.canvas.figure.set_facecolor("#C3C3C3")

        self.main_frame_CC.setLayout(self.graph_layout)

        Form.setStyleSheet(
            """
            #main_frame_CC {
                background-color: #C3C3C3;
                border-radius: 3px;
            }

            #frame_to_buttons {
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
            
            [commomFrame_group='true'] {
                border-radius: 3px;
                border: 1px solid #2C423F;
            }
            
            #frame_group_buttons {
                background-color: #C3C3C3;
                border: none;
            }
            
            #frame_to_groups {
                background-color: #C3C3C3;
                border-radius: 3px;
                border: 1px solid #2C423F;
            }
            """
        )

        shadow_elements = {
            'frame_buttons_animation_time',
            'main_frame_CC'
        }
        for x in shadow_elements:
            effect = QtWidgets.QGraphicsDropShadowEffect(self.main_frame_CC)
            effect.setBlurRadius(18)
            effect.setXOffset(0)
            effect.setYOffset(0)
            effect.setColor(QColor(0, 0, 0, 255))
            getattr(self, x).setGraphicsEffect(effect)

    def start_anim(self):
        self.forward_button_time.setDisabled(True)
        self.finish_button_time.setDisabled(True)
        self.start_button_time.setDisabled(True)
        self.backward_button_time.setDisabled(True)
        self.play_button_time.setDisabled(True)
        if self.time_selected == self.time_selection[-1]:
            return
        else:
            while True:
                index = self.time_selection.index(self.time_selected)
                self.time_selected = self.time_selection[index + 1]
                self.updateplot()

                if self.pause_button_time.isChecked():
                    break
                if self.time_selected == self.time_selection[-1]:
                    break

                time.sleep(.2)
            self.pause_button_time.setChecked(False)
            self.forward_button_time.setDisabled(False)
            self.finish_button_time.setDisabled(False)
            self.start_button_time.setDisabled(False)
            self.backward_button_time.setDisabled(False)
            self.play_button_time.setDisabled(False)

    def updateplot(self):
        self.ax.clear()

        self.df_plot = self.dict_final[self.time_selected]
        self.dataploted = self.df_plot.T.plot(kind="barh", colormap="viridis", ax=self.ax)
        self.ax.set_xlabel("mT")
        self.ax.set_ylabel("")
        self.ax.grid(axis="y", linestyle="--", alpha=0.7)
        self.ax.set_yticklabels(self.ax.get_yticklabels(), fontsize=9)
        self.ax.set_xlim([0, self.max_value])

        self.canvas.draw()

    def plot_data(self):
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)

        self.max_value = 0
        for _, item in self.dict_final.items():
            max_item = item.max().max()
            if max_item > self.max_value:
                self.max_value = max_item

        self.df_plot = self.dict_final[self.time_selected]

        self.dataploted = self.df_plot.T.plot(kind="barh", colormap="viridis", ax=self.ax)

        self.ax.set_xlabel("mT")
        self.ax.set_ylabel("")
        self.ax.grid(axis="y", linestyle="--", alpha=0.7)
        self.ax.set_yticklabels(self.ax.get_yticklabels(), fontsize=9)
        self.ax.set_xlim([0, self.max_value])

        self.canvas.draw()

    def create_data(self):
        self.dict_final = {}

        for tempo in self.data.dataframe.keys():
            lista_df = []
            for nome_grupo, classe_grupo in self.groups.items():
                if tempo in classe_grupo.data:
                    df_grupo = classe_grupo.data[tempo].copy()
                    df_grupo.index = [nome_grupo]
                    lista_df.append(df_grupo)

            if lista_df:
                self.dict_final[tempo] = pd.concat(lista_df)

        self.time_selection = [key for key in self.dict_final.keys()]
        self.time_selected = self.time_selection[0]

        self.plot_data()

    def firts_in_time(self):
        if self.time_selected == self.time_selection[0]:
            return
        else:
            self.time_selected = self.time_selection[0]
            self.updateplot()

    def last_in_time(self):
        if self.time_selected == self.time_selection[-1]:
            return
        else:
            self.time_selected = self.time_selection[-1]
            self.updateplot()

    def forward_in_time(self):
        if self.time_selected == self.time_selection[-1]:
            return
        else:
            index = self.time_selection.index(self.time_selected)
            self.time_selected = self.time_selection[index + 1]
            self.updateplot()

    def back_in_time(self):
        if self.time_selected == self.time_selection[0]:
            return
        else:
            index = self.time_selection.index(self.time_selected)
            self.time_selected = self.time_selection[index - 1]
            self.updateplot()

    def play_animation(self):
        self.worker = AnimationWorker(page=self)
        self.worker.start()

    def add_group(self):
        layout = self.scrollcontentLayout.layout()
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget_to_remove = item.widget()
                if widget_to_remove is not None:
                    widget_to_remove.deleteLater()

        self.radiobuttons = []
        for key in self.groups.keys():
            radio = QRadioButton(key)
            self.scrollcontentLayout.addWidget(radio)
            self.radiobuttons.append(radio)

    def open_gsw_page(self):
        if self.gsw_widget is None:
            self.gsw_widget = GSW.GroupSelectionWidget(self.data.composition)

        self.gsw_widget.group_update.connect(self.update_group)
        self.gsw_widget.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.gsw_widget.setWindowFlag(Qt.WindowType.Window)
        self.gsw_widget.show()

    def update_group(self, groupname, grouplist):
        self.gsw_widget.close()
        setattr(self, "gsw_widget", None)
        self.groups[groupname] = Groups(grouplist, self.data)
        self.add_group()
        self.list_to_edit = None

    def open_gsw_edit_page(self):
        if self.gsw_widget is None:
            self.gsw_widget = GSW.GroupSelectionWidget(self.data.composition, self.list_to_edit, self.old_group_name)

        self.gsw_widget.group_update.connect(self.update_group_edit)
        self.gsw_widget.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.gsw_widget.setWindowFlag(Qt.WindowType.Window)
        self.gsw_widget.show()

    def update_group_edit(self, group_new_name, group_new_list):
        self.gsw_widget.close()
        setattr(self, "gsw_widget", None)
        if group_new_name == self.old_group_name:
            self.groups[group_new_name] = Groups(group_new_list, self.data)
        else:
            self.groups[group_new_name] = self.groups.pop(self.old_group_name)
            self.groups[group_new_name] = Groups(group_new_list, self.data)
        self.add_group()
        self.list_to_edit = None

    def delete_radio(self):
        selected = None
        for radio in self.radiobuttons:
            if radio.isChecked():
                selected = radio
                break
        if selected:
            self.scrollcontentLayout.removeWidget(selected)
            self.radiobuttons.remove(selected)
            del self.groups[selected.text()]
            selected.deleteLater()
        else:
            QMessageBox.warning(self.main_frame_CC, "Erro", "You must select a group to delete.")

    def editgroup(self):
        for radio_ in self.radiobuttons:
            if radio_.isChecked():
                self.old_group_name = radio_.text()
                self.list_to_edit = self.groups[self.old_group_name].composition_list
                break
        if self.list_to_edit:
            self.open_gsw_edit_page()
        else:
            QMessageBox.warning(self.main_frame_CC, "Erro", "You must select a group to edit.")

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.grouplabel_name.setText(QCoreApplication.translate("Form", u"Groups:", None))
        self.plusbutton.setText("")
        self.minusbutton.setText("")
        self.editbutton.setText("")
        self.plot_button.setText(QCoreApplication.translate("Form", u"Plot", None))
        self.import_button_CC_2.setText(QCoreApplication.translate("Form", u"Save Figure", None))
        self.start_button_time.setText("")
        self.backward_button_time.setText("")
        self.pause_button_time.setText("")
        self.play_button_time.setText("")
        self.forward_button_time.setText("")
        self.finish_button_time.setText("")
        self.import_button_CC.setText(QCoreApplication.translate("Form", u"Export as .csv", None))
