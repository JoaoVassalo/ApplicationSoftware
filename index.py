from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt, QThread, Signal)
from PySide6.QtGui import (QFont, QIcon, QPixmap)
from PySide6.QtWidgets import (QComboBox, QDateEdit, QFrame,
                               QGridLayout, QHBoxLayout, QLabel, QLineEdit,
                               QProgressBar, QPushButton, QScrollArea,
                               QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
                               QWidget, QCheckBox, QMessageBox, QRadioButton)
from ViewPages import (Current_LonLat_Buttons, Current_CoordinateDepthProfile_Buttons,
                       Wind_LonLat_Buttons, Wind_AverageWind_Buttons, Temperature_LonLat_Buttons,
                       Temperature_Average_Buttons, Temperature_LatDepthProfile_Buttons,
                       Temperature_LonDepthProfile_Buttons, Temperature_Dataframe_Buttons, Salinity_LonLat_Buttons,
                       Salinity_Average_Buttons, Salinity_LatDepthProfile_Buttons, Salinity_LonDepthProfile_Buttons,
                       Salinity_Dataframe_Buttons, VarInfo_Widgets, ConcatDatasetForm, MergeDatasetForm, DatDatasetForm,
                       ImpDatasetForm, FilterDatasetForm, Individual_Pages_POSprocess)
import VarVerify
import os
import xarray as xr
from datetime import date, datetime, timedelta
from Functions import HycomPackage, CopernicusPackage, FileFunctions
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import cartopy.crs as ccrs
from matplotlib.patches import Rectangle
import time


class DownloadWorker(QThread):
    progress_download = Signal(str)
    finished_download = Signal(str)
    error_download = Signal(str)

    def __init__(self, package, page):
        super().__init__()
        self.package = package
        self.page = page
        self._stop = False

    def run(self):
        try:
            self.progress_download.emit("Download in progress!")
            process_result = self.package.download()
            if isinstance(process_result, bool) and process_result:
                self.finished_download.emit("Download is finished!")
                self.page.DownloadButton.setChecked(False)
                self.page.checkcomponents()
                self.page.set_combobox_files()
            elif type(process_result) is str:
                self.error_download.emit(f"Erro ao realizar o download: {str(process_result)}")
                self.page.DownloadButton.setChecked(False)
                self.page.checkcomponents()
                self.page.set_combobox_files()
        except Exception as e:
            self.page.DownloadButton.setChecked(False)
            self.page.checkcomponents()
            self.error_download.emit(f"Erro ao realizar o download: {str(e)}")

    def stop_download(self):
        self._stop = True
        self.package.stop()
        self.finished_download.emit(f"Download canceled!")


class FileWorker(QThread):
    progress_file = Signal()
    finished_file = Signal()
    error_file = Signal(str)

    def __init__(self, package, page):
        super().__init__()
        self.package = package
        self.page = page

    def run(self):
        try:
            self.progress_file.emit()
            self.page.toggle_progress_bar_execute()
            time.sleep(2)
            self.package.run()
            time.sleep(2)
            self.page.clear_filterframe_container()
            self.page.toggle_progress_bar_execute()
            self.page.ExcuteButton.setChecked(False)
            self.page.ExcuteButton.setText('Execute')
            self.page.set_combobox_files()
            self.finished_file.emit()
        except Exception as e:
            self.page.toggle_progress_bar_execute()
            self.page.ExcuteButton.setChecked(False)
            self.page.ExcuteButton.setText('Execute')
            self.error_file.emit(f"Erro!: {str(e)}")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.showFullScreen()
        MainWindow.setFixedSize(MainWindow.size())

        self.project = MainWindow.project
        self.hycom_catalogs = {f'{catalog.nome}': catalog for catalog in MainWindow.hycomCatalog}
        self.copernicus_catalogs = {f'{catalog.nome}': catalog for catalog in MainWindow.copernicusCatalog}

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_screen_widget = QFrame(self.centralwidget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_screen_widget.sizePolicy().hasHeightForWidth())
        self.main_screen_widget.setSizePolicy(sizePolicy)
        self.main_screen_widget.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_screen_widget.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.main_screen_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.download_page = QWidget()
        self.download_page.setObjectName(u"download_page")
        self.download_page.setMinimumSize(QSize(859, 0))
        self.verticalLayout_3 = QVBoxLayout(self.download_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.download_page_header = QFrame(self.download_page)
        self.download_page_header.setObjectName(u"download_page_header")
        font = QFont()
        font.setFamilies([u"NovaFlat"])
        font.setBold(True)
        self.download_page_header.setFont(font)
        self.download_page_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.download_page_header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.download_page_header)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.download_page_header)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setProperty('HeaderTitleCommon', True)
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_11, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.download_page_header)

        self.download_page_screen = QFrame(self.download_page)
        self.download_page_screen.setObjectName(u"download_page_screen")
        sizePolicy.setHeightForWidth(self.download_page_screen.sizePolicy().hasHeightForWidth())
        self.download_page_screen.setSizePolicy(sizePolicy)
        self.download_page_screen.setFrameShape(QFrame.Shape.StyledPanel)
        self.download_page_screen.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.download_page_screen)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_layout = QWidget(self.download_page_screen)
        self.widget_layout.setObjectName(u"widget_layout")
        self.gridLayout_3 = QGridLayout(self.widget_layout)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticallayout_13 = QVBoxLayout()
        self.verticallayout_13.setObjectName(u"verticallayout_13")

        self.coord_date_file_widgets = QWidget(self.widget_layout)
        self.coord_date_file_widgets.setObjectName(u"coord_date_file_widgets")
        self.coord_date_file_widgets.setProperty('DownloadCommomFrame', True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.coord_date_file_widgets.sizePolicy().hasHeightForWidth())
        self.coord_date_file_widgets.setSizePolicy(sizePolicy1)
        self.coord_date_file_widgets.setMinimumSize(QSize(520, 280))
        self.horizontalLayout_3 = QHBoxLayout(self.coord_date_file_widgets)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_coordinates = QFrame(self.coord_date_file_widgets)
        self.frame_coordinates.setObjectName(u"frame_coordinates")
        self.frame_coordinates.setProperty('DownloadCommomFrame', True)
        self.frame_coordinates.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_coordinates.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_coordinates)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.coordinateLabel = QLabel(self.frame_coordinates)
        self.coordinateLabel.setObjectName(u"coordinateLabel")
        self.coordinateLabel.setProperty("TitleCommon", True)
        self.coordinateLabel.setMinimumSize(QSize(110, 0))
        self.coordinateLabel.setMaximumSize(QSize(110, 20))
        font1 = QFont()
        font1.setBold(True)
        self.coordinateLabel.setFont(font1)
        self.coordinateLabel.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.coordinateLabel, 0, 0, 1, 2)

        self.coord_boxs = QFrame(self.frame_coordinates)
        self.coord_boxs.setObjectName(u"coord_boxs")
        self.coord_boxs.setProperty('DownloadCommomFrame', True)
        self.coord_boxs.setMinimumSize(QSize(100, 0))
        self.coord_boxs.setMaximumSize(QSize(200, 16777215))
        self.coord_boxs.setFrameShape(QFrame.Shape.StyledPanel)
        self.coord_boxs.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.coord_boxs)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_northbox = QHBoxLayout()
        self.horizontalLayout_northbox.setObjectName(u"horizontalLayout_northbox")
        self.horizontalSpacer_7 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_northbox.setContentsMargins(0, 35, 0, 0)

        self.horizontalLayout_northbox.addItem(self.horizontalSpacer_7)

        self.verticalLayout_northbox = QVBoxLayout()
        self.verticalLayout_northbox.setObjectName(u"verticalLayout_northbox")
        self.verticalLayout_northbox.setContentsMargins(32, -1, -1, -1)
        self.label_24 = QLabel(self.coord_boxs)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setProperty("LabelDownloadCommon", True)
        self.label_24.setMinimumSize(QSize(100, 0))
        self.label_24.setMaximumSize(QSize(100, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_24.setFont(font2)
        self.label_24.setAlignment(
            Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_northbox.addWidget(self.label_24)

        self.North_value = QLineEdit(self.coord_boxs)
        self.North_value.setObjectName(u"North_value")
        self.North_value.setProperty('commonLineEditDownloadPage', True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.North_value.sizePolicy().hasHeightForWidth())
        self.North_value.setSizePolicy(sizePolicy2)
        self.North_value.setMinimumSize(QSize(60, 30))
        self.North_value.setMaximumSize(QSize(60, 30))
        self.North_value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.North_value.setText('80')
        self.North_value.textChanged.connect(self.rebuild_graph)

        self.verticalLayout_northbox.addWidget(self.North_value)

        self.horizontalLayout_northbox.addLayout(self.verticalLayout_northbox)

        self.horizontalSpacer_8 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_northbox.addItem(self.horizontalSpacer_8)

        self.verticalLayout_19.addLayout(self.horizontalLayout_northbox)

        self.horizontalLayout_weast_east_box = QHBoxLayout()
        self.horizontalLayout_weast_east_box.setSpacing(6)
        self.horizontalLayout_weast_east_box.setObjectName(u"horizontalLayout_weast_east_box")
        self.horizontalLayout_weast_east_box.setContentsMargins(12, -1, -1, 20)
        self.horizontalSpacer_11 = QSpacerItem(18, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_weast_east_box.addItem(self.horizontalSpacer_11)

        self.verticalLayout_weastbox = QVBoxLayout()
        self.verticalLayout_weastbox.setObjectName(u"verticalLayout_weastbox")
        self.label_25 = QLabel(self.coord_boxs)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setProperty("LabelDownloadCommon", True)
        self.label_25.setMinimumSize(QSize(100, 0))
        self.label_25.setMaximumSize(QSize(100, 16777215))
        self.label_25.setFont(font2)
        self.label_25.setAlignment(
            Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_weastbox.addWidget(self.label_25)

        self.Weast_value = QLineEdit(self.coord_boxs)
        self.Weast_value.setObjectName(u"Weast_value")
        self.Weast_value.setProperty('commonLineEditDownloadPage', True)
        sizePolicy2.setHeightForWidth(self.Weast_value.sizePolicy().hasHeightForWidth())
        self.Weast_value.setSizePolicy(sizePolicy2)
        self.Weast_value.setMinimumSize(QSize(60, 30))
        self.Weast_value.setMaximumSize(QSize(60, 30))
        self.Weast_value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Weast_value.setText('-180')
        self.Weast_value.textChanged.connect(self.rebuild_graph)

        self.verticalLayout_weastbox.addWidget(self.Weast_value)

        self.horizontalLayout_weast_east_box.addLayout(self.verticalLayout_weastbox)

        self.horizontalSpacer_9 = QSpacerItem(18, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_weast_east_box.addItem(self.horizontalSpacer_9)

        self.verticalLayout_eastbox = QVBoxLayout()
        self.verticalLayout_eastbox.setObjectName(u"verticalLayout_eastbox")
        self.label_26 = QLabel(self.coord_boxs)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setProperty("LabelDownloadCommon", True)
        self.label_26.setMinimumSize(QSize(100, 0))
        self.label_26.setMaximumSize(QSize(100, 16777215))
        self.label_26.setFont(font2)
        self.label_26.setAlignment(
            Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_eastbox.addWidget(self.label_26)

        self.East_value = QLineEdit(self.coord_boxs)
        self.East_value.setObjectName(u"East_value")
        self.East_value.setProperty('commonLineEditDownloadPage', True)
        sizePolicy2.setHeightForWidth(self.East_value.sizePolicy().hasHeightForWidth())
        self.East_value.setSizePolicy(sizePolicy2)
        self.East_value.setMinimumSize(QSize(60, 30))
        self.East_value.setMaximumSize(QSize(60, 30))
        self.East_value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.East_value.setText('180')
        self.East_value.textChanged.connect(self.rebuild_graph)

        self.verticalLayout_eastbox.addWidget(self.East_value)

        self.horizontalLayout_weast_east_box.addLayout(self.verticalLayout_eastbox)

        self.horizontalSpacer_10 = QSpacerItem(18, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_weast_east_box.addItem(self.horizontalSpacer_10)

        self.verticalLayout_19.addLayout(self.horizontalLayout_weast_east_box)

        self.horizontalLayout_southbox = QHBoxLayout()
        self.horizontalLayout_southbox.setObjectName(u"horizontalLayout_southbox")
        self.horizontalSpacer_12 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_southbox.setContentsMargins(0, 0, 0, 35)

        self.horizontalLayout_southbox.addItem(self.horizontalSpacer_12)

        self.verticalLayout_southbox = QVBoxLayout()
        self.verticalLayout_southbox.setObjectName(u"verticalLayout_southbox")
        self.verticalLayout_southbox.setContentsMargins(32, -1, -1, -1)
        self.label_27 = QLabel(self.coord_boxs)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setProperty("LabelDownloadCommon", True)
        self.label_27.setMinimumSize(QSize(100, 0))
        self.label_27.setMaximumSize(QSize(100, 16777215))
        self.label_27.setFont(font2)
        self.label_27.setAlignment(
            Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_southbox.addWidget(self.label_27)

        self.South_value = QLineEdit(self.coord_boxs)
        self.South_value.setObjectName(u"South_value")
        self.South_value.setProperty('commonLineEditDownloadPage', True)
        sizePolicy2.setHeightForWidth(self.South_value.sizePolicy().hasHeightForWidth())
        self.South_value.setSizePolicy(sizePolicy2)
        self.South_value.setMinimumSize(QSize(60, 30))
        self.South_value.setMaximumSize(QSize(60, 30))
        self.South_value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.South_value.setText('-80')
        self.South_value.textChanged.connect(self.rebuild_graph)

        self.verticalLayout_southbox.addWidget(self.South_value)

        self.horizontalLayout_southbox.addLayout(self.verticalLayout_southbox)

        self.horizontalSpacer_19 = QSpacerItem(28, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_southbox.addItem(self.horizontalSpacer_19)

        self.verticalLayout_19.addLayout(self.horizontalLayout_southbox)

        self.gridLayout_4.addWidget(self.coord_boxs, 1, 0, 1, 1)

        self.frame_map_coord = QFrame(self.frame_coordinates)
        self.frame_map_coord.setObjectName(u"frame_map_coord")
        self.frame_map_coord.setProperty('DownloadCommomFrame', True)
        sizePolicy1.setHeightForWidth(self.frame_map_coord.sizePolicy().hasHeightForWidth())
        self.frame_map_coord.setSizePolicy(sizePolicy1)
        self.frame_map_coord.setMinimumSize(QSize(200, 0))
        self.frame_map_coord.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_map_coord.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_4.addWidget(self.frame_map_coord, 1, 1, 1, 1)

        self.graphlayout_map = QVBoxLayout(self.frame_map_coord)
        self.figure = Figure()
        self.figure.set_size_inches(2.6, 2.6)
        self.canva = FigureCanvas(self.figure)
        sizePolicyCanvas = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicyCanvas.setHeightForWidth(self.canva.sizePolicy().hasHeightForWidth())
        self.canva.setSizePolicy(sizePolicyCanvas)
        self.canva.figure.set_facecolor("#C3C3C3")
        self.graphlayout_map.addWidget(self.canva)

        self.set_global_graph()
        self.rebuild_graph()

        self.horizontalLayout_3.addWidget(self.frame_coordinates)

        self.line_4 = QFrame(self.coord_date_file_widgets)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setProperty("commonLine", True)
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_4)

        self.frame_date = QFrame(self.coord_date_file_widgets)
        self.frame_date.setObjectName(u"frame_date")
        self.frame_date.setProperty('DownloadCommomFrame', True)
        self.frame_date.setMinimumSize(QSize(250, 0))
        self.frame_date.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_date.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget = QWidget(self.frame_date)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(9, 9, 224, 264))
        self.verticalLayout_date = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_date.setObjectName(u"verticalLayout_date")
        self.verticalLayout_date.setContentsMargins(0, 0, 0, 0)
        self.dateLabel = QLabel(self.layoutWidget)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setProperty("TitleCommon", True)
        self.dateLabel.setMinimumSize(QSize(110, 0))
        self.dateLabel.setMaximumSize(QSize(110, 20))
        self.dateLabel.setFont(font1)
        self.dateLabel.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_date.addWidget(self.dateLabel)

        self.verticalSpacer_10 = QSpacerItem(18, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_date.addItem(self.verticalSpacer_10)

        self.horizontalLayout_InitialDate = QHBoxLayout()
        self.horizontalLayout_InitialDate.setObjectName(u"horizontalLayout_InitialDate")
        self.horizontalSpacer_29 = QSpacerItem(18, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_InitialDate.addItem(self.horizontalSpacer_29)

        self.verticalLayout_InitialDate = QVBoxLayout()
        self.verticalLayout_InitialDate.setObjectName(u"verticalLayout_InitialDate")
        self.initialdateLabel = QLabel(self.layoutWidget)
        self.initialdateLabel.setObjectName(u"initialdateLabel")
        self.initialdateLabel.setProperty("LabelDownloadCommon", True)
        self.initialdateLabel.setMinimumSize(QSize(170, 30))
        self.initialdateLabel.setMaximumSize(QSize(170, 30))
        self.initialdateLabel.setFont(font2)

        self.verticalLayout_InitialDate.addWidget(self.initialdateLabel)

        self.Initial_date = QDateEdit(self.layoutWidget)
        self.Initial_date.setObjectName(u"Initial_date")
        self.Initial_date.setProperty('commonDateEdit', True)
        self.Initial_date.setMinimumSize(QSize(170, 30))
        self.Initial_date.setMaximumSize(QSize(170, 30))

        self.verticalLayout_InitialDate.addWidget(self.Initial_date)

        self.horizontalLayout_InitialDate.addLayout(self.verticalLayout_InitialDate)

        self.horizontalSpacer_28 = QSpacerItem(18, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_InitialDate.addItem(self.horizontalSpacer_28)

        self.verticalLayout_date.addLayout(self.horizontalLayout_InitialDate)

        self.verticalSpacer_9 = QSpacerItem(18, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_date.addItem(self.verticalSpacer_9)

        self.horizontalLayout_FinalDate = QHBoxLayout()
        self.horizontalLayout_FinalDate.setObjectName(u"horizontalLayout_FinalDate")
        self.horizontalSpacer_31 = QSpacerItem(18, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_FinalDate.addItem(self.horizontalSpacer_31)

        self.verticalLayout_FinalDate = QVBoxLayout()
        self.verticalLayout_FinalDate.setObjectName(u"verticalLayout_FinalDate")
        self.finaldateLabel = QLabel(self.layoutWidget)
        self.finaldateLabel.setObjectName(u"finaldateLabel")
        self.finaldateLabel.setProperty("LabelDownloadCommon", True)
        self.finaldateLabel.setMinimumSize(QSize(170, 30))
        self.finaldateLabel.setMaximumSize(QSize(170, 30))
        self.finaldateLabel.setFont(font2)

        self.verticalLayout_FinalDate.addWidget(self.finaldateLabel)

        self.Final_date = QDateEdit(self.layoutWidget)
        self.Final_date.setObjectName(u"Final_date")
        self.Final_date.setProperty('commonDateEdit', True)
        self.Final_date.setMinimumSize(QSize(170, 30))
        self.Final_date.setMaximumSize(QSize(170, 30))

        self.verticalLayout_FinalDate.addWidget(self.Final_date)

        self.horizontalLayout_FinalDate.addLayout(self.verticalLayout_FinalDate)

        self.horizontalSpacer_30 = QSpacerItem(18, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_FinalDate.addItem(self.horizontalSpacer_30)

        self.verticalLayout_date.addLayout(self.horizontalLayout_FinalDate)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_date.addItem(self.verticalSpacer_8)

        self.horizontalLayout_3.addWidget(self.frame_date)

        self.line_3 = QFrame(self.coord_date_file_widgets)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setProperty("commonLine", True)
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.frame_download = QFrame(self.coord_date_file_widgets)
        self.frame_download.setObjectName(u"frame_download")
        self.frame_download.setProperty('DownloadCommomFrame', True)
        self.frame_download.setMaximumSize(QSize(200, 16777215))
        self.frame_download.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_download.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_download)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.downloadLabel = QLabel(self.frame_download)
        self.downloadLabel.setObjectName(u"downloadLabel")
        self.downloadLabel.setProperty("TitleCommon", True)
        self.downloadLabel.setMinimumSize(QSize(110, 0))
        self.downloadLabel.setMaximumSize(QSize(110, 20))
        self.downloadLabel.setFont(font1)
        self.downloadLabel.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_17.addWidget(self.downloadLabel)

        self.verticalSpacer_4 = QSpacerItem(17, 9, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_4)

        self.horizontalLayout_filename = QHBoxLayout()
        self.horizontalLayout_filename.setObjectName(u"horizontalLayout_filename")
        self.horizontalSpacer_26 = QSpacerItem(18, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_filename.addItem(self.horizontalSpacer_26)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.filenameLabel = QLabel(self.frame_download)
        self.filenameLabel.setObjectName(u"filenameLabel")
        self.filenameLabel.setProperty("LabelDownloadCommon", True)
        self.filenameLabel.setFont(font2)

        self.verticalLayout_10.addWidget(self.filenameLabel)

        self.FileName = QLineEdit(self.frame_download)
        self.FileName.setObjectName(u"FileName")
        self.FileName.setProperty('commonLineEditDownloadPage', True)
        sizePolicy2.setHeightForWidth(self.FileName.sizePolicy().hasHeightForWidth())
        self.FileName.setSizePolicy(sizePolicy2)
        self.FileName.setMinimumSize(QSize(170, 30))
        self.FileName.setMaximumSize(QSize(170, 30))

        self.verticalLayout_10.addWidget(self.FileName)

        self.horizontalLayout_filename.addLayout(self.verticalLayout_10)

        self.horizontalSpacer_27 = QSpacerItem(18, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_filename.addItem(self.horizontalSpacer_27)

        self.verticalLayout_17.addLayout(self.horizontalLayout_filename)

        self.verticalSpacer_7 = QSpacerItem(17, 9, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_7)

        self.horizontalLayout_downloadbutton = QHBoxLayout()
        self.horizontalLayout_downloadbutton.setObjectName(u"horizontalLayout_downloadbutton")
        self.horizontalSpacer_20 = QSpacerItem(18, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_downloadbutton.addItem(self.horizontalSpacer_20)

        self.DownloadButton = QPushButton(self.frame_download)
        self.DownloadButton.setObjectName(u"DownloadButton")
        self.DownloadButton.setMinimumSize(QSize(120, 30))
        self.DownloadButton.setMaximumSize(QSize(120, 30))
        self.DownloadButton.setCheckable(True)
        self.DownloadButton.clicked.connect(self.start_download)

        self.horizontalLayout_downloadbutton.addWidget(self.DownloadButton)

        self.horizontalSpacer_21 = QSpacerItem(18, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_downloadbutton.addItem(self.horizontalSpacer_21)

        self.verticalLayout_17.addLayout(self.horizontalLayout_downloadbutton)

        self.verticalSpacer_6 = QSpacerItem(17, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_6)

        self.horizontalLayout_progressbar = QHBoxLayout()
        self.horizontalLayout_progressbar.setObjectName(u"horizontalLayout_progressbar")
        self.horizontalSpacer_23 = QSpacerItem(18, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_progressbar.addItem(self.horizontalSpacer_23)

        self.progressBar = QProgressBar(self.frame_download)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(120, 30))
        self.progressBar.setMaximumSize(QSize(120, 30))
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setHidden(False)
        self.progressBar.setRange(0, 1) # Range fixo para não animar
        self.is_running = False

        self.horizontalLayout_progressbar.addWidget(self.progressBar)

        self.horizontalSpacer_22 = QSpacerItem(18, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_progressbar.addItem(self.horizontalSpacer_22)

        self.verticalLayout_17.addLayout(self.horizontalLayout_progressbar)

        self.verticalSpacer_3 = QSpacerItem(17, 9, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3.addWidget(self.frame_download)

        self.gridLayout_3.addWidget(self.coord_date_file_widgets, 5, 0, 1, 1)

        self.variablesLabel = QLabel(self.widget_layout)
        self.variablesLabel.setObjectName(u"variablesLabel")
        self.variablesLabel.setProperty("TitleCommon", True)
        sizePolicy2.setHeightForWidth(self.variablesLabel.sizePolicy().hasHeightForWidth())
        self.variablesLabel.setSizePolicy(sizePolicy2)
        self.variablesLabel.setMinimumSize(QSize(90, 20))
        self.variablesLabel.setMaximumSize(QSize(90, 20))
        self.variablesLabel.setFont(font1)
        self.variablesLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.variablesLabel, 2, 0, 1, 1)

        self.horizontalLayout_button_catalogList = QHBoxLayout()
        self.horizontalLayout_button_catalogList.setSpacing(6)
        self.horizontalLayout_button_catalogList.setObjectName(u"horizontalLayout_button_catalogList")
        self.horizontalLayout_button_catalogList.setContentsMargins(22, 0, -1, -1)
        self.horizontalSpacer_13 = QSpacerItem(18, 17, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_button_catalogList.addItem(self.horizontalSpacer_13)

        self.DataBase_Frame = QFrame(self.widget_layout)
        self.DataBase_Frame.setObjectName(u"DataBase_Frame")
        self.DataBase_Frame.setMinimumSize(QSize(80, 30))
        self.DataBase_Frame.setMaximumSize(QSize(80, 30))
        self.DataBase_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.DataBase_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.DataBase_Frame.mousePressEvent = self.change_database

        self.Hycom_Button = QPushButton(self.DataBase_Frame)
        self.Hycom_Button.setObjectName(u"Hycom_Button")
        self.Hycom_Button.setGeometry(QRect(2, 2, 26, 26))
        self.Hycom_Button.setMinimumSize(QSize(26, 26))
        self.Hycom_Button.setMaximumSize(QSize(26, 26))
        self.Hycom_Button.setStyleSheet(u"QPushButton {\n"
                                        "    color: #333;\n"
                                        "    border-radius: 13px;\n"
                                        "    border-style: outset;\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                        "        );\n"
                                        "    padding: 5px;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                        "        );\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    border-style: inset;\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                        "        );\n"
                                        "    }")
        self.CopernicusButton = QPushButton(self.DataBase_Frame)
        self.CopernicusButton.setObjectName(u"CopernicusButton")
        self.CopernicusButton.setGeometry(QRect(52, 2, 26, 26))
        self.CopernicusButton.setMinimumSize(QSize(26, 26))
        self.CopernicusButton.setMaximumSize(QSize(26, 26))
        self.CopernicusButton.setStyleSheet(u"QPushButton {\n"
                                            "    color: #333;\n"
                                            "    border-radius: 13px;\n"
                                            "    border-style: outset;\n"
                                            "    background: qradialgradient(\n"
                                            "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                            "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                            "        );\n"
                                            "    padding: 5px;\n"
                                            "    }\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "    background: qradialgradient(\n"
                                            "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                            "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                            "        );\n"
                                            "    }\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "    border-style: inset;\n"
                                            "    background: qradialgradient(\n"
                                            "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                            "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                            "        );\n"
                                            "    }")
        self.CopernicusButton.setHidden(True)

        self.horizontalLayout_button_catalogList.addWidget(self.DataBase_Frame)

        self.horizontalSpacer_14 = QSpacerItem(38, 17, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_button_catalogList.addItem(self.horizontalSpacer_14)

        self.Catalog_Combox = QComboBox(self.widget_layout)
        self.Catalog_Combox.setObjectName(u"Catalog_Combox")
        self.Catalog_Combox.setProperty('CommomComboBox', True)
        self.Catalog_Combox.setMinimumSize(QSize(350, 31))
        self.Catalog_Combox.setMaximumSize(QSize(350, 31))

        self.horizontalLayout_button_catalogList.addWidget(self.Catalog_Combox)

        self.horizontalSpacer_15 = QSpacerItem(18, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_button_catalogList.addItem(self.horizontalSpacer_15)

        self.horizontalLayout_databaseName = QHBoxLayout()
        self.horizontalLayout_databaseName.setObjectName(u"horizontalLayout_databaseName")
        self.horizontalSpacer_18 = QSpacerItem(18, 17, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_databaseName.addItem(self.horizontalSpacer_18)

        self.HycomLabel = QLabel(self.widget_layout)
        self.HycomLabel.setObjectName(u"HycomLabel")
        self.HycomLabel.setProperty("TitleCommon", True)
        self.HycomLabel.setFont(font1)
        self.HycomLabel.setStyleSheet(u"color: rgb(249, 134, 0);")
        self.HycomLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_databaseName.addWidget(self.HycomLabel)

        self.horizontalSpacer_17 = QSpacerItem(18, 17, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_databaseName.addItem(self.horizontalSpacer_17)

        self.CopernicusLabel = QLabel(self.widget_layout)
        self.CopernicusLabel.setObjectName(u"CopernicusLabel")
        self.CopernicusLabel.setProperty("TitleCommon", True)
        self.CopernicusLabel.setFont(font1)
        self.CopernicusLabel.setStyleSheet(u"color: rgb(176, 176, 176);")
        self.CopernicusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_databaseName.addWidget(self.CopernicusLabel)

        self.horizontalSpacer_16 = QSpacerItem(18, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_databaseName.addItem(self.horizontalSpacer_16)

        self.verticallayout_13.addItem(self.horizontalLayout_databaseName)
        self.verticallayout_13.addItem(self.horizontalLayout_button_catalogList)

        self.gridLayout_3.addLayout(self.verticallayout_13, 0, 0, 1, 1)

        self.horizontalLayout_6.addItem(self.verticallayout_13)

        self.frame_to_info = QFrame(self.widget_layout)
        self.frame_to_info.setObjectName(u"frame_to_info")
        self.frame_to_info.setProperty('DownloadCommomFrame', True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_to_info.sizePolicy().hasHeightForWidth())
        self.frame_to_info.setSizePolicy(sizePolicy1)
        self.frame_to_info.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_to_info.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_to_info)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.fromDateLabel = QLabel(self.frame_to_info)
        self.fromDateLabel.setObjectName(u"fromDateLabel")
        self.fromDateLabel.setProperty("LabelDownloadCommon", True)
        self.fromDateLabel.setMinimumSize(QSize(80, 20))
        self.fromDateLabel.setMaximumSize(QSize(100, 20))
        self.fromDateLabel.setText(QCoreApplication.translate("MainWindow", u"From date", None))

        self.verticalLayout_14.addWidget(self.fromDateLabel)

        self.fromDateEdit = QLineEdit(self.frame_to_info)
        self.fromDateEdit.setObjectName(u"fromDateEdit")
        self.fromDateEdit.setProperty('commonLineEditDownloadPage', True)
        self.fromDateEdit.setMinimumSize(QSize(80, 25))
        self.fromDateEdit.setMaximumSize(QSize(100, 25))
        self.fromDateEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fromDateEdit.setReadOnly(True)

        self.verticalLayout_14.addWidget(self.fromDateEdit)

        self.horizontalLayout_8.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.toDateLabel = QLabel(self.frame_to_info)
        self.toDateLabel.setObjectName(u"toDateLabel")
        self.toDateLabel.setProperty("LabelDownloadCommon", True)
        self.toDateLabel.setMinimumSize(QSize(80, 20))
        self.toDateLabel.setMaximumSize(QSize(100, 20))
        self.toDateLabel.setText(QCoreApplication.translate("MainWindow", u"To date", None))

        self.verticalLayout_15.addWidget(self.toDateLabel)

        self.toDateEdit = QLineEdit(self.frame_to_info)
        self.toDateEdit.setObjectName(u"toDateEdit")
        self.toDateEdit.setProperty('commonLineEditDownloadPage', True)
        self.toDateEdit.setMinimumSize(QSize(80, 25))
        self.toDateEdit.setMaximumSize(QSize(100, 25))
        self.toDateEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.toDateEdit.setReadOnly(True)

        self.verticalLayout_15.addWidget(self.toDateEdit)

        self.horizontalLayout_8.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.regionLabel = QLabel(self.frame_to_info)
        self.regionLabel.setObjectName(u"regionLabel")
        self.regionLabel.setProperty("LabelDownloadCommon", True)
        self.regionLabel.setMinimumSize(QSize(80, 20))
        self.regionLabel.setMaximumSize(QSize(100, 20))
        self.regionLabel.setText(QCoreApplication.translate("MainWindow", u"Region", None))

        self.verticalLayout_16.addWidget(self.regionLabel)

        self.regionEdit = QLineEdit(self.frame_to_info)
        self.regionEdit.setObjectName(u"regionEdit")
        self.regionEdit.setProperty('commonLineEditDownloadPage', True)
        self.regionEdit.setMinimumSize(QSize(80, 25))
        self.regionEdit.setMaximumSize(QSize(100, 25))
        self.regionEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.regionEdit.setReadOnly(True)

        self.verticalLayout_16.addWidget(self.regionEdit)

        self.horizontalLayout_8.addLayout(self.verticalLayout_16)

        self.horizontalLayout_6.addWidget(self.frame_to_info)

        self.gridLayout_3.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)


        self.variables_checkbox_widget = QWidget(self.widget_layout)
        self.variables_checkbox_widget.setObjectName(u"variables_checkbox_widget")
        sizePolicy1.setHeightForWidth(self.variables_checkbox_widget.sizePolicy().hasHeightForWidth())
        self.variables_checkbox_widget.setSizePolicy(sizePolicy1)
        self.variables_checkbox_widget.setMinimumSize(QSize(760, 120))

        self.gridLayout_3.addWidget(self.variables_checkbox_widget, 4, 0, 1, 1)

        self.list_catalog = [f'{key}/{item.type}' for key, item in self.hycom_catalogs.items()]
        self.Catalog_Combox.addItems(self.list_catalog)
        self.Catalog_Combox.setCurrentIndex(0)

        self.current_catalog = self.list_catalog[0].split('/')[0]
        self.adicionar_checkboxes(database='H')

        self.Catalog_Combox.currentIndexChanged.connect(self.change_variables)

        self.variablesLabel.raise_()
        self.coord_date_file_widgets.raise_()
        self.variables_checkbox_widget.raise_()

        self.gridLayout_2.addWidget(self.widget_layout, 0, 0, 1, 1)

        self.verticalLayout_3.addWidget(self.download_page_screen)

        self.stackedWidget.addWidget(self.download_page)
        self.view_page = QWidget()
        self.view_page.setObjectName(u"view_page")
        self.verticalLayout_8 = QVBoxLayout(self.view_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.view_page_header = QFrame(self.view_page)
        self.view_page_header.setObjectName(u"view_page_header")
        self.view_page_header.setFont(font)
        self.view_page_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.view_page_header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.view_page_header)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.view_header = QLabel(self.view_page_header)
        self.view_header.setObjectName(u"view_header")
        self.view_header.setProperty('HeaderTitleCommon', True)
        self.view_header.setFont(font)
        self.view_header.setStyleSheet(u"")
        self.view_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.view_header, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_8.addWidget(self.view_page_header)

        self.view_page_main_screen = QFrame(self.view_page)
        self.view_page_main_screen.setObjectName(u"view_page_main_screen")
        sizePolicy.setHeightForWidth(self.view_page_main_screen.sizePolicy().hasHeightForWidth())
        self.view_page_main_screen.setSizePolicy(sizePolicy)
        self.view_page_main_screen.setFrameShape(QFrame.Shape.StyledPanel)
        self.view_page_main_screen.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.view_page_main_screen)
        self.gridLayout_5.setObjectName(u"gridLayout_5")

        self.frame = QFrame(self.view_page_main_screen)
        self.frame.setObjectName(u"frame")
        self.frame.setProperty('ViewCommomFrame', True)
        self.frame.setMinimumSize(QSize(0, 110))
        self.frame.setMaximumSize(QSize(16777215, 110))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setProperty('ViewCommomFrame', True)
        self.frame_3.setMinimumSize(QSize(220, 78))
        self.frame_3.setMaximumSize(QSize(220, 78))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(180, 25))
        self.label_6.setMaximumSize(QSize(180, 25))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"border: none;")
        self.label_6.setAlignment(
            Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_11.addWidget(self.label_6)

        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setProperty('CommomComboBox', True)
        self.comboBox.setMinimumSize(QSize(180, 25))
        self.comboBox.setMaximumSize(QSize(180, 25))

        self.comboBox.addItem('Choose a file...')
        self.comboBox.setCurrentIndex(0)
        self.comboBox.currentIndexChanged.connect(self.on_item_selected)

        self.verticalLayout_11.addWidget(self.comboBox)

        self.verticalLayout_12.addLayout(self.verticalLayout_11)

        self.gridLayout_6.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setProperty('ViewCommomFrame', True)
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        # self.frame_4.setStyleSheet("""
        #     QPushButton {
        #         background-color: rgb(61, 80, 95);
        #         border-radius: 10px; /* Arredondamento das bordas */
        #         border: 2px solid #F98600;
        #         min-width: 100px; /* Largura mínima */
        #         max-width: 200px;
        #         min-height: 20px; /* Altura mínima */
        #         color: white;
        #     }
        #
        #     QPushButton:hover {
        #         color: #F98600;
        #         font-size: 14px;
        #     }
        #
        #     QPushButton:checked {
        #         color: white;
        #         background-color: rgb(125, 63, 0);
        #         font-size: 14px;
        #     }
        #
        #     QRadioButton {
        #         min-width: 55px;
        #         max-width: 95px;
        #         height:20px;
        #     }
        # """)
        self.gridLayout_forVar = QGridLayout(self.frame_4)
        self.gridLayout_forVar.setSpacing(0)

        self.frame_to_radio_variables = QFrame()
        self.frame_to_radio_variables.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.layoutForRadioVar = QHBoxLayout(self.frame_to_radio_variables)
        self.layoutForRadioVar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_forVar.addWidget(self.frame_to_radio_variables)

        self.frame_to_buttons_variables = QFrame()
        self.frame_to_buttons_variables.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.frame_4_buttons_layout = QHBoxLayout(self.frame_to_buttons_variables)
        self.gridLayout_forVar.addWidget(self.frame_to_buttons_variables)
        self.frame_4_buttons_layout.setSpacing(5)
        self.frame_4_buttons_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.frame_4, 0, 1, 1, 1)

        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)

        self.verticalLayout_8.addWidget(self.view_page_main_screen)

        self.stackedWidget.addWidget(self.view_page)
        self.file_page = QWidget()
        self.file_page.setObjectName(u"file_page")
        self.verticalLayout_4 = QVBoxLayout(self.file_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.file_page_header = QFrame(self.file_page)
        self.file_page_header.setObjectName(u"file_page_header")
        self.file_page_header.setFont(font)
        self.file_page_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.file_page_header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.file_page_header)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.file_header = QLabel(self.file_page_header)
        self.file_header.setObjectName(u"file_header")
        self.file_header.setProperty('HeaderTitleCommon', True)
        self.file_header.setFont(font)
        self.file_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.file_header, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_4.addWidget(self.file_page_header)

        self.file_page_main_screen = QFrame(self.file_page)
        self.file_page_main_screen.setObjectName(u"file_page_main_screen")
        sizePolicy.setHeightForWidth(self.file_page_main_screen.sizePolicy().hasHeightForWidth())
        self.file_page_main_screen.setSizePolicy(sizePolicy)
        # self.file_page_main_screen.setStyleSheet(u"QWidget{\n"
        #                                          "	color:white;\n"
        #                                          "	background-color: rgb(61, 80, 95);\n"
        #                                          "	border-radius: 10px;\n"
        #                                          "}\n"
        #                                          "\n"
        #                                          "\n"
        #                                          "\n"
        #                                          "")
        self.file_page_main_screen.setFrameShape(QFrame.Shape.StyledPanel)
        self.file_page_main_screen.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.file_page_main_screen)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame_5 = QFrame(self.file_page_main_screen)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filechooseLabel = QLabel(self.frame_5)
        self.filechooseLabel.setObjectName(u"filechooseLabel")
        self.filechooseLabel.setMinimumSize(QSize(200, 31))
        self.filechooseLabel.setMaximumSize(QSize(200, 31))
        self.filechooseLabel.setFont(font2)

        self.horizontalLayout.addWidget(self.filechooseLabel)

        self.FileListCombox = QComboBox(self.frame_5)
        self.FileListCombox.setObjectName(u"FileListCombox")
        self.FileListCombox.setProperty('CommomComboBox', True)
        self.FileListCombox.setMinimumSize(QSize(270, 30))
        self.FileListCombox.setMaximumSize(QSize(270, 30))

        self.FileListCombox.addItem('Choose a file...')
        self.FileListCombox.setCurrentIndex(0)
        self.FileListCombox.currentIndexChanged.connect(self.on_item_selected_fileview)

        self.horizontalLayout.addWidget(self.FileListCombox)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_32)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.gridLayout_9.addWidget(self.frame_5, 0, 0, 1, 3)

        self.fileList_View = []

        self.InformationAreaFiles = QScrollArea(self.file_page_main_screen)
        self.InformationAreaFiles.setObjectName(u"InformationAreaFiles")
        self.InformationAreaFiles.setMinimumSize(QSize(600, 0))
        self.InformationAreaFiles.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 600, 502))
        self.InformationAreaFiles.setWidget(self.scrollAreaWidgetContents)
        self.layout_for_file_forms = QVBoxLayout(self.scrollAreaWidgetContents)
        self.layout_for_file_forms.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scrollAreaWidgetContents.setLayout(self.layout_for_file_forms)

        self.gridLayout_9.addWidget(self.InformationAreaFiles, 1, 0, 1, 1)

        self.line = QFrame(self.file_page_main_screen)
        self.line.setObjectName(u"line")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy3)
        self.line.setMinimumSize(QSize(5, 0))
        self.line.setMaximumSize(QSize(5, 16777215))
        self.line.setStyleSheet(u"background-color: rgb(38, 58, 68);")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_9.addWidget(self.line, 1, 1, 1, 1)

        self.FunctionsFrame = QFrame(self.file_page_main_screen)
        self.FunctionsFrame.setObjectName(u"FunctionsFrame")
        self.FunctionsFrame.setMaximumSize(QSize(350, 16777215))
        self.FunctionsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.FunctionsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.FunctionsFrame)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.ButtonsFilesFrame = QFrame(self.FunctionsFrame)
        self.ButtonsFilesFrame.setObjectName(u"ButtonsFilesFrame")
        sizePolicy1.setHeightForWidth(self.ButtonsFilesFrame.sizePolicy().hasHeightForWidth())
        self.ButtonsFilesFrame.setSizePolicy(sizePolicy1)
        self.ButtonsFilesFrame.setStyleSheet(u"")
        self.ButtonsFilesFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ButtonsFilesFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.ButtonsFilesFrame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.ConcatButrton = QPushButton(self.ButtonsFilesFrame)
        self.ConcatButrton.setObjectName(u"ConcatButrton")
        self.ConcatButrton.setMinimumSize(QSize(100, 30))
        self.ConcatButrton.setMaximumSize(QSize(120, 30))
        # self.ConcatButrton.setStyleSheet(u"QPushButton{\n"
        #                                  "	background-color: rgb(61, 80, 95);\n"
        #                                  "	border-radius: 15px;\n"
        #                                  "	border: 2px solid #F98600;\n"
        #                                  "}\n"
        #                                  "\n"
        #                                  "QPushButton:hover{\n"
        #                                  "	color: #F98600;\n"
        #                                  "	font-size: 14px;\n"
        #                                  "}\n"
        #                                  "\n"
        #                                  "QPushButton:checked{\n"
        #                                  "	color: white;\n"
        #                                  "	\n"
        #                                  "	background-color: rgb(125, 63, 0);\n"
        #                                  "	font-size: 14px;\n"
        #                                  "}")
        self.ConcatButrton.setCheckable(True)
        self.ConcatButrton.clicked.connect(self.concat_files)

        self.gridLayout_7.addWidget(self.ConcatButrton, 0, 0, 1, 1)

        self.MergeButton = QPushButton(self.ButtonsFilesFrame)
        self.MergeButton.setObjectName(u"MergeButton")
        self.MergeButton.setMinimumSize(QSize(100, 30))
        self.MergeButton.setMaximumSize(QSize(120, 30))
        # self.MergeButton.setStyleSheet(u"QPushButton{\n"
        #                                "	background-color: rgb(61, 80, 95);\n"
        #                                "	border-radius: 15px;\n"
        #                                "	border: 2px solid #F98600;\n"
        #                                "}\n"
        #                                "\n"
        #                                "QPushButton:hover{\n"
        #                                "	color: #F98600;\n"
        #                                "	font-size: 14px;\n"
        #                                "}\n"
        #                                "\n"
        #                                "QPushButton:checked{\n"
        #                                "	color: white;\n"
        #                                "	background-color: rgb(125, 63, 0);\n"
        #                                "	font-size: 14px;\n"
        #                                "}")
        self.MergeButton.setCheckable(True)
        self.MergeButton.clicked.connect(self.merge_files)

        self.gridLayout_7.addWidget(self.MergeButton, 0, 1, 1, 1)

        self.FilterButton = QPushButton(self.ButtonsFilesFrame)
        self.FilterButton.setObjectName(u"FilterButton")
        self.FilterButton.setMinimumSize(QSize(100, 30))
        self.FilterButton.setMaximumSize(QSize(120, 30))
        # self.FilterButton.setStyleSheet(u"QPushButton{\n"
        #                                 "	background-color: rgb(61, 80, 95);\n"
        #                                 "	border-radius: 15px;\n"
        #                                 "	border: 2px solid #F98600;\n"
        #                                 "}\n"
        #                                 "\n"
        #                                 "QPushButton:hover{\n"
        #                                 "	color: #F98600;\n"
        #                                 "	font-size: 14px;\n"
        #                                 "}\n"
        #                                 "\n"
        #                                 "QPushButton:checked{\n"
        #                                 "	color: white;\n"
        #                                 "	background-color: rgb(125, 63, 0);\n"
        #                                 "	font-size: 14px;\n"
        #                                 "}")
        self.FilterButton.setCheckable(True)
        self.FilterButton.clicked.connect(self.filter_file)

        self.gridLayout_7.addWidget(self.FilterButton, 1, 0, 1, 1)

        self.ImpButton = QPushButton(self.ButtonsFilesFrame)
        self.ImpButton.setObjectName(u"ImpButton")
        self.ImpButton.setMinimumSize(QSize(100, 30))
        self.ImpButton.setMaximumSize(QSize(120, 30))
        # self.ImpButton.setStyleSheet(u"QPushButton{\n"
        #                              "	background-color: rgb(61, 80, 95);\n"
        #                              "	border-radius: 15px;\n"
        #                              "	border: 2px solid #F98600;\n"
        #                              "}\n"
        #                              "\n"
        #                              "QPushButton:hover{\n"
        #                              "	color: #F98600;\n"
        #                              "	font-size: 14px;\n"
        #                              "}\n"
        #                              "\n"
        #                              "QPushButton:checked{\n"
        #                              "	color: white;\n"
        #                              "	background-color: rgb(125, 63, 0);\n"
        #                              "	font-size: 14px;\n"
        #                              "}")
        self.ImpButton.setCheckable(True)
        self.ImpButton.clicked.connect(self.imp_file)

        self.gridLayout_7.addWidget(self.ImpButton, 1, 1, 1, 1)

        self.DatButton = QPushButton(self.ButtonsFilesFrame)
        self.DatButton.setObjectName(u"DatButton")
        self.DatButton.setMinimumSize(QSize(100, 30))
        self.DatButton.setMaximumSize(QSize(120, 30))
        # self.DatButton.setStyleSheet(u"QPushButton{\n"
        #                              "	background-color: rgb(61, 80, 95);\n"
        #                              "	border-radius: 15px;\n"
        #                              "	border: 2px solid #F98600;\n"
        #                              "}\n"
        #                              "\n"
        #                              "QPushButton:hover{\n"
        #                              "	color: #F98600;\n"
        #                              "	font-size: 14px;\n"
        #                              "}\n"
        #                              "\n"
        #                              "QPushButton:checked{\n"
        #                              "	color: white;\n"
        #                              "	background-color: rgb(125, 63, 0);\n"
        #                              "	font-size: 14px;\n"
        #                              "}")
        self.DatButton.setCheckable(True)
        self.DatButton.clicked.connect(self.dat_file)

        self.gridLayout_7.addWidget(self.DatButton, 2, 0, 1, 1)

        self.DeleteButton = QPushButton(self.ButtonsFilesFrame)
        self.DeleteButton.setObjectName(u"DeleteButton")
        self.DeleteButton.setMinimumSize(QSize(100, 30))
        self.DeleteButton.setMaximumSize(QSize(120, 30))
        # self.DeleteButton.setStyleSheet(u"QPushButton{\n"
        #                                 "	background-color: rgb(61, 80, 95);\n"
        #                                 "	border-radius: 15px;\n"
        #                                 "	border: 2px solid #F98600;\n"
        #                                 "}\n"
        #                                 "\n"
        #                                 "QPushButton:hover{\n"
        #                                 "	color: #F98600;\n"
        #                                 "	font-size: 14px;\n"
        #                                 "}\n"
        #                                 "\n"
        #                                 "QPushButton:checked{\n"
        #                                 "	color: white;\n"
        #                                 "	background-color: rgb(125, 63, 0);\n"
        #                                 "	font-size: 14px;\n"
        #                                 "}")
        self.DeleteButton.setCheckable(True)
        self.DeleteButton.clicked.connect(self.delele_file)

        self.gridLayout_7.addWidget(self.DeleteButton, 2, 1, 1, 1)

        self.gridLayout_10.addWidget(self.ButtonsFilesFrame, 0, 0, 1, 1)

        self.FilterFieldFile = QFrame(self.FunctionsFrame)
        self.FilterFieldFile.setObjectName(u"FilterFieldFile")
        sizePolicy1.setHeightForWidth(self.FilterFieldFile.sizePolicy().hasHeightForWidth())
        self.FilterFieldFile.setSizePolicy(sizePolicy1)
        self.FilterFieldFile.setMinimumSize(QSize(0, 200))
        self.FilterFieldFile.setFrameShape(QFrame.Shape.StyledPanel)
        self.FilterFieldFile.setFrameShadow(QFrame.Shadow.Raised)
        self.filterFieldFile_layout = QGridLayout()
        self.FilterFieldFile.setLayout(self.filterFieldFile_layout)

        self.gridLayout_10.addWidget(self.FilterFieldFile, 1, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_35 = QSpacerItem(28, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_35)

        self.frame_8 = QFrame(self.FunctionsFrame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.ExcuteButton = QPushButton(self.frame_8)
        self.ExcuteButton.setObjectName(u"ExcuteButton")
        self.ExcuteButton.setMinimumSize(QSize(100, 30))
        self.ExcuteButton.setMaximumSize(QSize(100, 30))
        # self.ExcuteButton.setStyleSheet(u"QPushButton{\n"
        #                                 "	background-color: rgb(61, 80, 95);\n"
        #                                 "	border-radius: 15px;\n"
        #                                 "	border: 2px solid #F98600;\n"
        #                                 "}\n"
        #                                 "\n"
        #                                 "QPushButton:checked{\n"
        #                                 "	color: #F98600;\n"
        #                                 "	font-size: 14px;\n"
        #                                 "}")
        self.ExcuteButton.setCheckable(True)
        self.ExcuteButton.setChecked(False)
        self.ExcuteButton.clicked.connect(self.execute_function)

        self.gridLayout_8.addWidget(self.ExcuteButton, 0, 0, 1, 1)

        self.progressBarExecute = QProgressBar(self.frame_8)
        self.progressBarExecute.setObjectName(u"progressBarExecute")
        self.progressBarExecute.setMinimumSize(QSize(100, 30))
        self.progressBarExecute.setMaximumSize(QSize(100, 30))
        self.progressBarExecute.setValue(24)
        self.progressBarExecute.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBarExecute.setRange(0, 1) # Range fixo para não animar
        self.progressBarExecute.setVisible(True)
        self.pbe_is_running = False

        self.gridLayout_8.addWidget(self.progressBarExecute, 1, 0, 1, 1)

        self.horizontalLayout_7.addWidget(self.frame_8)

        self.horizontalSpacer_36 = QSpacerItem(28, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_36)

        self.gridLayout_10.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)

        self.gridLayout_9.addWidget(self.FunctionsFrame, 1, 2, 1, 1)

        self.verticalLayout_4.addWidget(self.file_page_main_screen)

        self.stackedWidget.addWidget(self.file_page)
        self.simulation_page = QWidget()
        self.simulation_page.setObjectName(u"simulation_page")
        self.verticalLayout_2 = QVBoxLayout(self.simulation_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_17 = QFrame(self.simulation_page)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFont(font)
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(self.frame_17)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setProperty('HeaderTitleCommon', True)
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_10, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_2.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.simulation_page)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)

        self.layout_simulation_page = QGridLayout()
        self.frame_18.setLayout(self.layout_simulation_page)
        # self.layout_simulation_page.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)

        self.frame_buttons_analysis = QFrame()
        self.frame_buttons_analysis.setObjectName(u"frame_buttons_analysis")
        self.frame_buttons_analysis.setMaximumSize(QSize(500, 35))
        self.frame_buttons_analysis.setMinimumSize(QSize(500, 35))
        self.frame_buttons_analysis.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_buttons_analysis.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_for_frame_buttons = QHBoxLayout(self.frame_buttons_analysis)
        self.horizontalLayout_for_frame_buttons.setSpacing(0)
        self.horizontalLayout_for_frame_buttons.setObjectName(u"horizontalLayout_for_frame_buttons")
        self.horizontalLayout_for_frame_buttons.setContentsMargins(0, 0, 0, 0)

        font_to_buttons = QFont()
        font_to_buttons.setPointSize(10)
        font_to_buttons.setItalic(True)

        self.indivudualButton = QPushButton(self.frame_buttons_analysis)
        self.indivudualButton.setObjectName(u"indivudualButton")
        self.indivudualButton.setProperty('CommomButtonSimulationAnalysis', True)
        self.indivudualButton.setCheckable(True)
        self.indivudualButton.setMinimumSize(QSize(250, 35))
        self.indivudualButton.setMaximumSize(QSize(250, 35))
        self.indivudualButton.setStyleSheet(u"QPushButton {\n"
                                            "border-top-left-radius: 6px;\n"
                                            "border-bottom-left-radius: 6px;\n"
                                            "padding: 10px;\n"
                                            "background-color: #C3C3C3;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "background-color: #829191;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:checked {\n"
                                            "background-color: #2C423F;\n"
                                            "color: #C3C3C3;\n"
                                            "}\n")
        self.indivudualButton.clicked.connect(self.ib_clicked)
        self.horizontalLayout_for_frame_buttons.addWidget(self.indivudualButton)

        self.collectiveButton = QPushButton(self.frame_buttons_analysis)
        self.collectiveButton.setObjectName(u"collectiveButton")
        self.collectiveButton.setProperty('CommomButtonSimulationAnalysis', True)
        self.collectiveButton.setCheckable(True)
        self.collectiveButton.setMinimumSize(QSize(250, 35))
        self.collectiveButton.setMaximumSize(QSize(250, 35))
        self.collectiveButton.setStyleSheet(u"QPushButton {\n"
                                            "border-top-right-radius: 6px;\n"
                                            "border-bottom-right-radius: 6px;\n"
                                            "padding: 10px;\n"
                                            "background-color: #C3C3C3;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "background-color: #829191;\n"
                                            "}\n"
                                            "QPushButton:checked {\n"
                                            "background-color: #2C423F;\n"
                                            "color: #C3C3C3;\n"
                                            "}\n")
        self.collectiveButton.clicked.connect(self.cb_clicked)

        self.indivudualButton.setFont(font_to_buttons)
        self.collectiveButton.setFont(font_to_buttons)
        self.indivudualButton.setText(u"Individual File Analysis")
        self.collectiveButton.setText(u"Collective File Analysis")

        self.horizontalLayout_for_frame_buttons.addWidget(self.collectiveButton)

        self.layout_simulation_page.addWidget(self.frame_buttons_analysis)
        self.layout_simulation_page.setAlignment(self.frame_buttons_analysis,
                                                 Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_2.addWidget(self.frame_18)

        self.stackedWidget.addWidget(self.simulation_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.verticalLayout_9 = QVBoxLayout(self.settings_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_25 = QFrame(self.settings_page)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFont(font)
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_14 = QLabel(self.frame_25)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setProperty('HeaderTitleCommon', True)
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_14, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_9.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.settings_page)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_9.addWidget(self.frame_26)

        self.stackedWidget.addWidget(self.settings_page)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.gridLayout.addWidget(self.main_screen_widget, 1, 2, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(70, 0))
        self.icon_only_widget.setMaximumSize(QSize(70, 16777215))
        # self.icon_only_widget.setStyleSheet(u"QWidget{\n"
        #                                     "	background-color: rgb(61, 80, 95);\n"
        #                                     "	border-radius: 10px\n"
        #                                     "}")
        self.icon_only_widget.setHidden(False)
        self.verticalLayout_5 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 20, -1, -1)
        self.logo_icon_only = QHBoxLayout()
        self.logo_icon_only.setObjectName(u"logo_icon_only")
        self.horizontalSpacer_4 = QSpacerItem(10, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.logo_icon_only.addItem(self.horizontalSpacer_4)

        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/icons/icons/home - branco.png"))
        self.label.setScaledContents(True)

        self.logo_icon_only.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(10, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.logo_icon_only.addItem(self.horizontalSpacer_3)

        self.verticalLayout_5.addLayout(self.logo_icon_only)

        self.icons_up_only = QVBoxLayout()
        self.icons_up_only.setSpacing(20)
        self.icons_up_only.setObjectName(u"icons_up_only")
        self.icons_up_only.setContentsMargins(-1, 20, -1, -1)
        self.DB_1 = QPushButton(self.icon_only_widget)
        self.DB_1.setObjectName(u"DB_1")
        self.DB_1.setProperty("commonButton", True)
        self.DB_1.setMinimumSize(QSize(0, 30))
        self.DB_1.setMaximumSize(QSize(16777215, 30))
        icon = QIcon()
        icon.addFile(u":/icons/icons/download - branco.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.DB_1.setIcon(icon)
        self.DB_1.setIconSize(QSize(100, 20))
        self.DB_1.setCheckable(False)
        self.DB_1.setChecked(False)
        self.DB_1.setToolTip('Download Page')
        self.DB_1.setToolTipDuration(20000)

        self.icons_up_only.addWidget(self.DB_1)

        self.VB_1 = QPushButton(self.icon_only_widget)
        self.VB_1.setObjectName(u"VB_1")
        self.VB_1.setProperty("commonButton", True)
        self.VB_1.setMinimumSize(QSize(0, 30))
        self.VB_1.setMaximumSize(QSize(16777215, 30))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/olho - branco.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.VB_1.setIcon(icon1)
        self.VB_1.setIconSize(QSize(100, 20))
        self.VB_1.setCheckable(False)
        self.VB_1.setToolTip('Data View Page')
        self.VB_1.setToolTipDuration(20000)

        self.icons_up_only.addWidget(self.VB_1)

        self.CB_1 = QPushButton(self.icon_only_widget)
        self.CB_1.setObjectName(u"CB_1")
        self.CB_1.setProperty("commonButton", True)
        self.CB_1.setMinimumSize(QSize(0, 30))
        self.CB_1.setMaximumSize(QSize(16777215, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/documentoPLUS - branco.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.CB_1.setIcon(icon2)
        self.CB_1.setIconSize(QSize(100, 20))
        self.CB_1.setCheckable(False)
        self.CB_1.setToolTip('File Modification Page')
        self.CB_1.setToolTipDuration(20000)

        self.icons_up_only.addWidget(self.CB_1)

        self.SB_1 = QPushButton(self.icon_only_widget)
        self.SB_1.setObjectName(u"SB_1")
        self.SB_1.setProperty("commonButton", True)
        self.SB_1.setMinimumSize(QSize(0, 30))
        self.SB_1.setMaximumSize(QSize(16777215, 30))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/histograma - branco.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SB_1.setIcon(icon3)
        self.SB_1.setIconSize(QSize(100, 20))
        self.SB_1.setCheckable(False)
        self.SB_1.setToolTip('Simulation Data Page')
        self.SB_1.setToolTipDuration(20000)

        self.icons_up_only.addWidget(self.SB_1)

        self.verticalLayout_5.addLayout(self.icons_up_only)

        self.verticalSpacer = QSpacerItem(20, 343, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.icons_down_only = QVBoxLayout()
        self.icons_down_only.setSpacing(20)
        self.icons_down_only.setObjectName(u"icons_down_only")
        self.ConfigB_1 = QPushButton(self.icon_only_widget)
        self.ConfigB_1.setObjectName(u"ConfigB_1")
        self.ConfigB_1.setProperty("commonButton", True)
        self.ConfigB_1.setMinimumSize(QSize(0, 30))
        self.ConfigB_1.setMaximumSize(QSize(16777215, 30))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/ajustes - branco.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ConfigB_1.setIcon(icon4)
        self.ConfigB_1.setIconSize(QSize(100, 20))
        self.ConfigB_1.setCheckable(False)
        self.ConfigB_1.setToolTip('Settings')
        self.ConfigB_1.setToolTipDuration(20000)

        self.icons_down_only.addWidget(self.ConfigB_1)

        self.LogoutB_1 = QPushButton(self.icon_only_widget)
        self.LogoutB_1.setObjectName(u"LogoutB_1")
        self.LogoutB_1.setProperty("commonButton", True)
        self.LogoutB_1.setMinimumSize(QSize(0, 30))
        self.LogoutB_1.setMaximumSize(QSize(16777215, 30))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/sair - branco.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.LogoutB_1.setIcon(icon5)
        self.LogoutB_1.setIconSize(QSize(100, 20))
        self.LogoutB_1.setCheckable(False)
        self.LogoutB_1.setToolTip('Log out')
        self.LogoutB_1.setToolTipDuration(20000)

        self.icons_down_only.addWidget(self.LogoutB_1)

        self.verticalLayout_5.addLayout(self.icons_down_only)

        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 3, 1)

        self.header_widget = QWidget(self.centralwidget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMinimumSize(QSize(861, 60))
        self.header_widget.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_5 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menu_button = QPushButton(self.header_widget)
        self.menu_button.setObjectName(u"menu_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.menu_button.sizePolicy().hasHeightForWidth())
        self.menu_button.setSizePolicy(sizePolicy4)

        self.menu_button.setMinimumSize(QSize(30, 35))
        self.menu_button.setMaximumSize(QSize(50, 55))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/Logo branco.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_button.setIcon(icon6)
        self.menu_button.setIconSize(QSize(40, 45))
        self.menu_button.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.menu_button)

        self.label_4 = QLabel(self.header_widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_6 = QSpacerItem(682, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.gridLayout.addWidget(self.header_widget, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.LogoutB_1.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(4)

        self.DB_1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.VB_1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.CB_1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.SB_1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.ConfigB_1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))

        self.current_checked_button = None

        self.frame_container = QFrame()
        self.gridLayout_5.addWidget(self.frame_container)

        self.file = None
        self.currentButton_onfilepage = None
        self.varname_obj = {
            'Current': VarVerify.CurrentVar(),
            'Wind': VarVerify.WindVar(),
            'Temperature': VarVerify.TemperatureVar(),
            'Salinity': VarVerify.SalinityVar()
        }
        self.variables_names = None

        QMetaObject.connectSlotsByName(MainWindow)

    def get_variables_to_download(self):
        # Getting variables values to download
        layout = self.variables_checkbox_widget.layout()
        self.variables_to_download = []
        if layout is not None:
            for i in range(layout.count()):
                item = layout.itemAt(i)
                widget_item = item.widget()
                if isinstance(widget_item, QCheckBox) and widget_item.isChecked():
                    self.variables_to_download.append(widget_item.text())

        if len(self.variables_to_download) == 0:
            QMessageBox.warning(self.download_page_screen, "Erro", "You must select at least one variable "
                                                                   "to download.")
            self.DownloadButton.setChecked(False)
            return
        else:
            try:
                # Getting coordinates to download
                self.north_coord = float(self.North_value.text())
                self.south_coord = float(self.South_value.text())
                self.east_coord = float(self.East_value.text())
                self.weast_coord = float(self.Weast_value.text())

                self.coords_required = {
                    'N': self.north_coord,
                    'S': self.south_coord,
                    'W': self.weast_coord,
                    'E': self.east_coord
                }

                # Getting file name
                self.file_name = f'{self.FileName.text()}.nc'

                if self.weast_coord > self.east_coord:
                    QMessageBox.warning(self.download_page_screen, "Erro", "Weast coordinate value must be "
                                                                           "smaller than East coordinate.")
                    self.DownloadButton.setChecked(False)
                    return
                elif self.south_coord > self.north_coord:
                    QMessageBox.warning(self.download_page_screen, "Erro", "South coordinate value must be "
                                                                           "smaller than North coordinate.")
                    self.DownloadButton.setChecked(False)
                    return
                elif self.FileName.text() == '':
                    QMessageBox.warning(self.download_page_screen, "Erro", "Please enter a valid file name.")
                    self.DownloadButton.setChecked(False)
                    return

            except Exception:
                QMessageBox.warning(self.download_page_screen, "Erro", "Please make sure you have enter all "
                                                                       "coordinate values.")
                self.DownloadButton.setChecked(False)
                return

        # Getting initial and final date to download
        self.initial_date_download = date(year=self.Initial_date.date().year(), month=self.Initial_date.date().month(),
                                          day=self.Initial_date.date().day())
        self.final_date_download = date(year=self.Final_date.date().year(), month=self.Final_date.date().month(),
                                        day=self.Final_date.date().day())

        self.checkcomponents()

    def checkcomponents(self):
        if self.DownloadButton.isChecked():
            self.frame_date.setDisabled(True)
            self.frame_coordinates.setDisabled(True)
            self.variables_checkbox_widget.setDisabled(True)
            self.Catalog_Combox.setDisabled(True)
            self.DataBase_Frame.setDisabled(True)
            self.FileName.setDisabled(True)
            self.toggle_progress()
            self.DownloadButton.setText('Stop')
            self.set_package()
        else:
            self.frame_date.setDisabled(False)
            self.frame_coordinates.setDisabled(False)
            self.variables_checkbox_widget.setDisabled(False)
            self.Catalog_Combox.setDisabled(False)
            self.DataBase_Frame.setDisabled(False)
            self.FileName.setDisabled(False)
            self.toggle_progress()
            self.DownloadButton.setText('Download')

    def set_package(self):
        if self.Hycom_Button.isVisible():
            self.package = HycomPackage.HycomDownloader(initial_date=self.initial_date_download,
                                                   final_date=self.final_date_download,
                                                   variables=self.variables_to_download,
                                                   coordenates=self.coords_required,
                                                   catalog=self.hycom_catalogs[self.current_catalog].url,
                                                   file_name=self.file_name,
                                                   project_path=self.project.caminho)
        else:
            self.package = CopernicusPackage.CopernicusDownloader(initial_date=self.initial_date_download,
                                                             final_date=self.final_date_download,
                                                             variables=self.variables_to_download,
                                                             coordenates=self.coords_required,
                                                             catalog=self.copernicus_catalogs[self.current_catalog],
                                                             file_name=self.file_name,
                                                             project_path=self.project.caminho
                                                             )

        self.worker = DownloadWorker(
            package=self.package,
            page=self
        )

        self.worker.progress_download.connect(self.update_progress)
        self.worker.finished_download.connect(self.download_finished)
        self.worker.error_download.connect(self.handle_error)

        self.worker.start()

    def update_progress(self, message):
        QMessageBox.warning(self.download_page_screen, message, f"File {self.file_name} "
                                                                                f"will be saved "
                                                                                f"on {self.project.caminho}.")

    def download_finished(self, message):
        if 'canceled!' in message:
            QMessageBox.warning(self.download_page_screen, message, f"Download was not concluded.")
        else:
            QMessageBox.warning(self.download_page_screen, message, f"File was saved on "
                                                                    f"{self.project.caminho}.")

    def handle_error(self, error_message):
        QMessageBox.warning(self.download_page_screen, "Error!", f"{error_message}.")

    def stopdownload(self):
        self.checkcomponents()
        self.worker.stop_download()
        self.worker.wait()
        del self.worker, self.package

    def start_download(self):
        if self.DownloadButton.isChecked():
            self.get_variables_to_download()
        else:
            self.stopdownload()

    def clear_variable_widget(self):
        layout = self.variables_checkbox_widget.layout()
        if layout is not None:
            while layout.count():  # Remove todos os widgets filhos
                item = layout.takeAt(0)
                widget_to_remove = item.widget()
                if widget_to_remove is not None:
                    widget_to_remove.deleteLater()

    def adicionar_checkboxes(self, database: str):
        self.clear_variable_widget()

        layout = self.variables_checkbox_widget.layout() or QHBoxLayout(self.variables_checkbox_widget)
        list_var = [variable_name.nome for variable_name in self.hycom_catalogs[self.current_catalog].variaveis] \
            if database == 'H' else [variable_name.nome for variable_name in
                                     self.copernicus_catalogs[self.current_catalog].variaveis]
        for opcao in list_var:
            checkbox = QCheckBox(opcao)
            checkbox.setStyleSheet(u"border: none;\n"
                                   u"font-size: 12px;\n"
                                   u"font-style: italic;\n"
                                   u"font-weight: bold;\n"
                                   u"color: #4C5B61\n"
                                   )
            layout.addWidget(checkbox)

        self.fromDateEdit.clear()
        self.toDateEdit.clear()
        self.regionEdit.clear()

        if database == 'H':
            list_date = {
                'start': self.hycom_catalogs[self.current_catalog].data_inicial,
                'finish': self.hycom_catalogs[self.current_catalog].data_final,
            }
            region_to_info = self.hycom_catalogs[self.current_catalog].region
        else:
            list_date = {
                'start': self.copernicus_catalogs[self.current_catalog].data_inicial,
                'finish': self.copernicus_catalogs[self.current_catalog].data_final,
            }
            region_to_info = self.copernicus_catalogs[self.current_catalog].region

        if list_date['start'] == list_date['finish']:
            list_date['finish'] = datetime.now().date() - timedelta(weeks=1)

        self.fromDateEdit.setText(f'{list_date['start'].month}/{list_date['start'].day}/{list_date['start'].year}')
        self.toDateEdit.setText(f'{list_date['finish'].month}/{list_date['finish'].day}/{list_date['finish'].year}')
        self.regionEdit.setText(region_to_info)

    def change_variables(self):
        self.current_catalog = self.list_catalog[self.Catalog_Combox.currentIndex()].split('/')[0]
        self.adicionar_checkboxes(database='H') if self.Hycom_Button.isVisible() else self.adicionar_checkboxes(
            database='C')

    def change_database(self, e):
        if self.CopernicusButton.isVisible():
            self.CopernicusButton.setHidden(True)
            self.CopernicusLabel.setStyleSheet(u"color: rgb(176, 176, 176);")
            self.Hycom_Button.setVisible(True)
            self.HycomLabel.setStyleSheet(u"color: rgb(249, 134, 0);")

            self.list_catalog = [f'{key}/{item.type}' for key, item in self.hycom_catalogs.items()]
            self.Catalog_Combox.clear()
            self.Catalog_Combox.addItems(self.list_catalog)
            self.Catalog_Combox.setCurrentIndex(0)

            self.current_catalog = self.list_catalog[0].split('/')[0]
            self.adicionar_checkboxes(database='H')

        else:
            self.Hycom_Button.setHidden(True)
            self.HycomLabel.setStyleSheet(u"color: rgb(176, 176, 176);")
            self.CopernicusButton.setVisible(True)
            self.CopernicusLabel.setStyleSheet(u"color: rgb(249, 134, 0);")

            self.list_catalog = [f'{key}/{item.type}' for key, item in self.copernicus_catalogs.items()]
            self.Catalog_Combox.clear()
            self.Catalog_Combox.addItems(self.list_catalog)
            self.Catalog_Combox.setCurrentIndex(0)

            self.current_catalog = self.list_catalog[0].split('/')[0]
            self.adicionar_checkboxes(database='C')

    def set_combobox_files(self):
        """
        Function to set files that exist on project folder and list then into the combobox placed within view page
        :return:
        """
        list_projects = [
            f for f in os.listdir(self.project.caminho)
            if os.path.isfile(os.path.join(self.project.caminho, f)) and f.endswith('.nc')
        ]

        self.comboBox.clear()
        self.FileListCombox.clear()

        self.comboBox.addItem('Choose a file...')
        self.FileListCombox.addItem('Choose a file...')

        for i in range(len(list_projects)):
            self.comboBox.addItem("")
            self.comboBox.setItemText(i + 1, QCoreApplication.translate("MainWindow",
                                                                        f"{list_projects[i]}", None))

            self.FileListCombox.addItem("")
            self.FileListCombox.setItemText(i + 1, QCoreApplication.translate("MainWindow",
                                                                        f"{list_projects[i]}", None))

        self.FileListCombox.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(0)

    def on_button_clicked(self, clicked_button, func):
        if self.current_checked_button and self.current_checked_button != clicked_button:
            self.current_checked_button.setChecked(False)

        self.current_checked_button = clicked_button
        func()

    def set_oneradio_only(self, var_file):
        labelFile = QLabel(text=f'Only {var_file} variable on file')
        self.layoutForRadioVar.addWidget(labelFile)

    def on_radio_selected(self, selected_radio):
        self.clear_frame_container()
        self.frame_container = QFrame()
        self.gridLayout_5.addWidget(self.frame_container)
        for i in reversed(range(self.frame_4_buttons_layout.count())):
            widget_to_remove = self.frame_4_buttons_layout.itemAt(i).widget()
            if widget_to_remove:
                widget_to_remove.setParent(None)

        self.obj = self.varname_obj[selected_radio.text()]
        self.verify = self.obj.check(f'{self.project.caminho}\\{self.comboBox.currentText()}')
        if isinstance(self.verify, bool):
            self.variables_names = self.obj.get_var_names(f'{self.project.caminho}\\{self.comboBox.currentText()}')
            self.set_graphbuttons(selected_radio.text())
        else:
            QMessageBox.warning(self.view_page_main_screen, "Warning", f"{self.verify}")

    def clear_frame_container(self):
        if self.gridLayout_5.count() > 1:
            child = self.gridLayout_5.takeAt(1)
            if child.widget():
                child.widget().deleteLater()

    def plot_lonlat_windprofile(self):
        self.clear_frame_container()
        self.frame_container = QFrame()
        self.ui_wind_page = Wind_LonLat_Buttons.Ui_WindButton_LonLatProfile()
        self.gridLayout_5.addWidget(self.frame_container)
        self.ui_wind_page.setupUi(self, self.frame_container, self.file, self.variables_names)

    def plot_average_wind(self):
        self.clear_frame_container()
        self.frame_container = QFrame()
        self.ui_wind_page = Wind_AverageWind_Buttons.Ui_WindButton_LonLatProfile()
        self.gridLayout_5.addWidget(self.frame_container)
        self.ui_wind_page.setupUi(self, self.frame_container, self.file, self.variables_names)

    def plot_lonlat_currentprofile(self):
        self.clear_frame_container()
        self.frame_container = QFrame()
        self.ui_current_page = Current_LonLat_Buttons.Ui_WindButton_LonLatProfile()
        self.gridLayout_5.addWidget(self.frame_container)
        self.ui_current_page.setupUi(self, self.frame_container, self.file, self.variables_names)

    def plot_section_profile(self):
        self.clear_frame_container()
        self.frame_container = QFrame()
        self.ui_current_page = Current_CoordinateDepthProfile_Buttons.Ui_WindButton_LonLatProfile()
        self.gridLayout_5.addWidget(self.frame_container)
        self.ui_current_page.setupUi(self, self.frame_container, self.file, self.variables_names)

    def plot_lonlat_salinityprofile(self):
        self.clear_frame_container()
        self.frame_container = QFrame()
        self.ui_salinity_page = Salinity_LonLat_Buttons.Ui_WindButton_LonLatProfile()
        self.gridLayout_5.addWidget(self.frame_container)
        self.ui_salinity_page.setupUi(self, self.frame_container, self.file, self.variables_names)

    def plot_average_salinity(self):
        self.clear_frame_container()
        self.frame_container = QFrame()
        self.ui_salinity_page = Salinity_Average_Buttons.Ui_WindButton_LonLatProfile()
        self.gridLayout_5.addWidget(self.frame_container)
        self.ui_salinity_page.setupUi(self, self.frame_container, self.file, self.variables_names)

    def plot_depth_lat_salinity(self):
        self.clear_frame_container()
        self.frame_container = QFrame()
        self.ui_salinity_page = Salinity_LatDepthProfile_Buttons.Ui_WindButton_LonLatProfile()
        self.gridLayout_5.addWidget(self.frame_container)
        self.ui_salinity_page.setupUi(self, self.frame_container, self.file, self.variables_names)

    def plot_depth_lon_salinity(self):
        self.clear_frame_container()
        self.frame_container = QFrame()
        self.ui_salinity_page = Salinity_LonDepthProfile_Buttons.Ui_WindButton_LonLatProfile()
        self.gridLayout_5.addWidget(self.frame_container)
        self.ui_salinity_page.setupUi(self, self.frame_container, self.file, self.variables_names)

    def plot_table_salinity(self):
        self.clear_frame_container()
        self.frame_container = QFrame()
        self.ui_salinity_page = Salinity_Dataframe_Buttons.Ui_WindButton_LonLatProfile()
        self.gridLayout_5.addWidget(self.frame_container)
        self.ui_salinity_page.setupUi(self, self.frame_container, self.file, self.variables_names)

    def plot_lonlat_temperatureprofile(self):
        self.clear_frame_container()
        self.frame_container = QFrame()
        self.ui_temperature_page = Temperature_LonLat_Buttons.Ui_WindButton_LonLatProfile()
        self.gridLayout_5.addWidget(self.frame_container)
        self.ui_temperature_page.setupUi(self, self.frame_container, self.file, self.variables_names)

    def plot_average_temperature(self):
        self.clear_frame_container()
        self.frame_container = QFrame()
        self.ui_temperature_page = Temperature_Average_Buttons.Ui_WindButton_LonLatProfile()
        self.gridLayout_5.addWidget(self.frame_container)
        self.ui_temperature_page.setupUi(self, self.frame_container, self.file, self.variables_names)

    def plot_depth_lat_temperature(self):
        self.clear_frame_container()
        self.frame_container = QFrame()
        self.ui_temperature_page = Temperature_LatDepthProfile_Buttons.Ui_WindButton_LonLatProfile()
        self.gridLayout_5.addWidget(self.frame_container)
        self.ui_temperature_page.setupUi(self, self.frame_container, self.file, self.variables_names)

    def plot_depth_lon_temperature(self):
        self.clear_frame_container()
        self.frame_container = QFrame()
        self.ui_temperature_page = Temperature_LonDepthProfile_Buttons.Ui_WindButton_LonLatProfile()
        self.gridLayout_5.addWidget(self.frame_container)
        self.ui_temperature_page.setupUi(self, self.frame_container, self.file, self.variables_names)

    def plot_table_temperature(self):
        self.clear_frame_container()
        self.frame_container = QFrame()
        self.ui_temperature_page = Temperature_Dataframe_Buttons.Ui_WindButton_LonLatProfile()
        self.gridLayout_5.addWidget(self.frame_container)
        self.ui_temperature_page.setupUi(self, self.frame_container, self.file, self.variables_names)

    def set_graphbuttons(self, var_set):
        button_configs = {
            'Wind': [
                {"text": "Lon vs Lat", "func": self.plot_lonlat_windprofile},
                {"text": "Average Wind", "func": self.plot_average_wind}
            ],
            'Current': [
                {"text": "Lon vs Lat", "func": self.plot_lonlat_currentprofile},
                {"text": "Section Profile", "func": self.plot_section_profile}
            ],
            'Salinity': [
                {"text": "Lon vs Lat", "func": self.plot_lonlat_salinityprofile},
                {"text": "Average Salinity", "func": self.plot_average_salinity},
                {"text": "Depth vs Lat", "func": self.plot_depth_lat_salinity},
                {"text": "Depth vs Lon", "func": self.plot_depth_lon_salinity},
                {"text": "Table Salinity", "func": self.plot_table_salinity}
            ],
            'Temperature': [
                {"text": "Lon vs Lat", "func": self.plot_lonlat_temperatureprofile},
                {"text": "Average Temperature", "func": self.plot_average_temperature},
                {"text": "Depth vs Lat", "func": self.plot_depth_lat_temperature},
                {"text": "Depth vs Lon", "func": self.plot_depth_lon_temperature},
                {"text": "Table Temperature", "func": self.plot_table_temperature}
            ]
        }

        if var_set in button_configs:
            for button_config in button_configs[var_set]:
                button = QPushButton(button_config["text"], self.frame_to_buttons_variables)
                button.setProperty('CommomButtonsViews', True)
                button.setCheckable(True)
                button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

                button.clicked.connect(lambda checked, b=button, f=button_config["func"]:
                                       self.on_button_clicked(b, f))
                self.frame_4_buttons_layout.addWidget(button)

    def update_frame_buttons(self, variable):
        for i in reversed(range(self.layoutForRadioVar.count())):
            widget_to_remove = self.layoutForRadioVar.itemAt(i).widget()
            if widget_to_remove:
                widget_to_remove.setParent(None)

        for i in reversed(range(self.frame_4_buttons_layout.count())):
            widget_to_remove = self.frame_4_buttons_layout.itemAt(i).widget()
            if widget_to_remove:
                widget_to_remove.setParent(None)

        if len(variable) == 1:
            self.obj = self.varname_obj[variable[0]]
            self.verify = self.obj.check(f'{self.project.caminho}\\{self.comboBox.currentText()}')
            if isinstance(self.verify, bool):
                self.variables_names = self.obj.get_var_names(f'{self.project.caminho}\\{self.comboBox.currentText()}')
                self.set_oneradio_only(variable[0])
                self.set_graphbuttons(variable[0])
            else:
                QMessageBox.warning(self.view_page_main_screen, "Warning", f"{self.verify}")
        else:
            for var_ in variable:
                radioB = QRadioButton(var_, self.frame_to_radio_variables)
                radioB.clicked.connect(lambda checked, rb=radioB: self.on_radio_selected(rb))
                self.layoutForRadioVar.addWidget(radioB)

    def on_item_selected(self):
        if hasattr(self, 'file'):
            del self.file
        if hasattr(self, 'frame_container'):
            self.clear_frame_container()
            self.frame_container = QFrame()
            self.gridLayout_5.addWidget(self.frame_container)
        if self.comboBox.currentText() != '' and self.comboBox.currentText() != 'Choose a file...':
            with xr.open_dataset(f'{self.project.caminho}\\{self.comboBox.currentText()}') as self.file:
                variable_name_map = {
                    'eastward_sea_water_velocity': 'Current',
                    'northward_sea_water_velocity': 'Current',
                    'sea_water_salinity': 'Salinity',
                    'sea_water_temperature': 'Temperature',
                    '10 metre U wind component': 'Wind',
                    '10 metre V wind component': 'Wind'
                }

                var_list = set()

                for var in self.file.variables:
                    if self.file.variables[var].ndim > 1:
                        attrs = self.file[var].attrs
                        standard_name = attrs.get('standard_name', None)
                        long_name = attrs.get('long_name', None)

                        if standard_name in variable_name_map:
                            var_list.add(variable_name_map[standard_name])
                        elif long_name in variable_name_map:
                            var_list.add(variable_name_map[long_name])
                    else:
                        pass

                var_list = list(var_list)
                self.update_frame_buttons(variable=var_list)

    def on_item_selected_fileview(self):
        if self.FileListCombox.currentIndex() == 0:
            return
        elif self.FileListCombox.currentText() == '' or self.FileListCombox.currentText() == 'Choose a file...':
            return
        else:
            current_file = self.FileListCombox.currentText()
            file = xr.open_dataset(f'{self.project.caminho}\\{current_file}')
            info_dict = [current_file, file]
            try:
                file_widget = VarInfo_Widgets.FileFormWidget(info_dict, self.scrollAreaWidgetContents)
                file_widget.remove_requested.connect(lambda: self.remove_file_widget(file_widget))
                file_widget.checklist_requested.connect(lambda: self.file_to_list(file_widget))
                self.layout_for_file_forms.addWidget(file_widget)
                del file
            except Exception as e:
                QMessageBox.warning(self.file_page_main_screen, "Warning", f'{e}')

    def file_to_list(self, widget):
        if widget.ui.checkBox.isChecked():
            self.fileList_View.append(widget.ui.file_name)
        else:
            self.fileList_View.remove(widget.ui.file_name)

    def remove_file_widget(self, widget):
        if widget.ui.file_name in self.fileList_View:
            self.currentButton_onfilepage.setChecked(False)
            self.clear_filterframe_container()
            self.fileList_View.remove(widget.ui.file_name)
        self.layout_for_file_forms.removeWidget(widget)
        widget.deleteLater()

    def clear_filterframe_container(self):
        if self.filterFieldFile_layout.count() >= 1:
            child = self.filterFieldFile_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        if self.currentButton_onfilepage:
            self.currentButton_onfilepage.setChecked(False)

    def concat_files(self):

        def update_kargs():
            self.func_file = FileFunctions.Concat(self.fileList_View, self.project.caminho,
                                                  self.concatframe.file_name.text())
            self.func_file.set_kargs(dim=self.concatframe.comboBox.currentText())

        def check_variables():
            varlist_files = []
            for file in self.fileList_View:
                f = xr.open_dataset(f'{self.project.caminho}\\{file}')
                varlist_files.append(list(f.variables))
            del f

            if all(set(var_) == set(varlist_files[0]) for var_ in varlist_files):
                return True
            else:
                return False

        if self.ConcatButrton.isChecked():
            if len(self.fileList_View) < 2:
                QMessageBox.warning(self.file_page_main_screen, "Warning", "You must select at least two files "
                                                                       "to concatenate.")
                self.ConcatButrton.setChecked(False)
                return
            else:
                check_var = check_variables()
                if not check_var:
                    QMessageBox.warning(self.file_page_main_screen, "Error", "You must select at least two files "
                                                                               "that contain the same variables to "
                                                                             "concatenate.")
                    self.ConcatButrton.setChecked(False)
                else:
                    self.currentButton_onfilepage = self.ConcatButrton
                    self.clear_filterframe_container()
                    self.MergeButton.setChecked(False)
                    self.DatButton.setChecked(False)
                    self.FilterButton.setChecked(False)
                    self.ImpButton.setChecked(False)
                    self.DeleteButton.setChecked(False)

                    self.frame_filter = QFrame()
                    self.concatframe = ConcatDatasetForm.Ui_Form()
                    self.filterFieldFile_layout.addWidget(self.frame_filter)
                    self.concatframe.setupUi(self, self.frame_filter, self.fileList_View)
                    self.concatframe.file_name.textChanged.connect(update_kargs)
                    self.concatframe.comboBox.currentTextChanged.connect(update_kargs)

                    self.func_file = FileFunctions.Concat(self.fileList_View, self.project.caminho,
                                                          self.concatframe.file_name.text())
                    self.func_file.set_kargs(dim=self.concatframe.comboBox.currentText())
        else:
            self.clear_filterframe_container()
            self.func_file = None

    def merge_files(self):
        def update_kargs():
            self.func_file = FileFunctions.Merge(self.fileList_View, self.project.caminho,
                                                 self.mergeframe.lineEdit.text())

        if self.MergeButton.isChecked():
            if len(self.fileList_View) < 2:
                QMessageBox.warning(self.file_page_main_screen, "Warning", "You must select at least two files "
                                                                           "to merge.")
                self.MergeButton.setChecked(False)
            else:
                self.currentButton_onfilepage = self.MergeButton
                self.clear_filterframe_container()
                self.ConcatButrton.setChecked(False)
                self.DatButton.setChecked(False)
                self.FilterButton.setChecked(False)
                self.ImpButton.setChecked(False)
                self.DeleteButton.setChecked(False)

                self.frame_filter = QFrame()
                self.mergeframe = MergeDatasetForm.Ui_Form()
                self.filterFieldFile_layout.addWidget(self.frame_filter)
                self.mergeframe.setupUi(self, self.frame_filter)
                self.mergeframe.lineEdit.textChanged.connect(update_kargs)

                self.func_file = FileFunctions.Merge(self.fileList_View, self.project.caminho,
                                                          self.mergeframe.lineEdit.text())
        else:
            self.clear_filterframe_container()
            self.func_file = None

    def dat_file(self):
        def update_kargs():
            self.func_file = FileFunctions.Dat(self.fileList_View, self.project.caminho,
                                               self.datframe.lineEdit.text())
            self.func_file.set_kargs(u_component=self.datframe.comboBox_2.currentText(),
                                     v_component=self.datframe.comboBox_3.currentText())

        if self.DatButton.isChecked():
            if len(self.fileList_View) < 1:
                QMessageBox.warning(self.file_page_main_screen, "Warning", "You must select one .nc file "
                                                                           "to create .dat file.")
                self.DatButton.setChecked(False)
            elif len(self.fileList_View) > 1:
                QMessageBox.warning(self.file_page_main_screen, "Warning", "You must select only one .nc file "
                                                                           "to create .dat file.")
                self.DatButton.setChecked(False)
            else:
                self.currentButton_onfilepage = self.DatButton
                self.clear_filterframe_container()
                self.ConcatButrton.setChecked(False)
                self.MergeButton.setChecked(False)
                self.FilterButton.setChecked(False)
                self.ImpButton.setChecked(False)
                self.DeleteButton.setChecked(False)

                self.frame_filter = QFrame()
                self.datframe = DatDatasetForm.Ui_Form()
                self.filterFieldFile_layout.addWidget(self.frame_filter)
                self.datframe.setupUi(self, self.frame_filter, self.fileList_View)
                self.datframe.comboBox_2.currentIndexChanged.connect(update_kargs)
                self.datframe.comboBox_3.currentIndexChanged.connect(update_kargs)
                self.datframe.lineEdit.textChanged.connect(update_kargs)

                self.func_file = FileFunctions.Dat(self.fileList_View, self.project.caminho,
                                                   self.datframe.lineEdit.text())
                self.func_file.set_kargs(u_component=self.datframe.comboBox_2.currentText(),
                                         v_component=self.datframe.comboBox_3.currentText())
        else:
            self.clear_filterframe_container()
            self.func_file = None

    def imp_file(self):
        def update_kargs():
            self.func_file = FileFunctions.Imp(self.fileList_View, self.project.caminho,
                                               self.impframe.lineEdit.text())
            self.func_file.set_kargs(type=self.impframe.comboBox_4.currentText(),
                                     u_component=self.impframe.comboBox_2.currentText(),
                                     v_component=self.impframe.comboBox_3.currentText())

        if self.ImpButton.isChecked():
            if len(self.fileList_View) < 1:
                QMessageBox.warning(self.file_page_main_screen, "Warning", "You must select one .nc file "
                                                                           "to create .imp file.")
                self.ImpButton.setChecked(False)
            elif len(self.fileList_View) > 1:
                QMessageBox.warning(self.file_page_main_screen, "Warning", "You must select only one .nc file "
                                                                           "to create .imp file.")
                self.ImpButton.setChecked(False)
            else:
                self.currentButton_onfilepage = self.ImpButton
                self.clear_filterframe_container()
                self.ConcatButrton.setChecked(False)
                self.MergeButton.setChecked(False)
                self.FilterButton.setChecked(False)
                self.DatButton.setChecked(False)
                self.DeleteButton.setChecked(False)

                self.frame_filter = QFrame()
                self.impframe = ImpDatasetForm.Ui_Form()
                self.filterFieldFile_layout.addWidget(self.frame_filter)
                self.impframe.setupUi(self, self.frame_filter, self.fileList_View)
                self.impframe.comboBox_4.currentIndexChanged.connect(update_kargs)
                self.impframe.comboBox_2.currentIndexChanged.connect(update_kargs)
                self.impframe.comboBox_3.currentIndexChanged.connect(update_kargs)
                self.impframe.lineEdit.textChanged.connect(update_kargs)

                self.func_file = FileFunctions.Imp(self.fileList_View, self.project.caminho,
                                                   self.impframe.lineEdit.text())
                self.func_file.set_kargs(type=self.impframe.comboBox_4.currentText(),
                                         u_component=self.impframe.comboBox_2.currentText(),
                                         v_component=self.impframe.comboBox_3.currentText())

        else:
            self.clear_filterframe_container()
            self.func_file = None

    def filter_file(self):
        def update_kargs():
            self.func_file = FileFunctions.Filter(self.fileList_View, self.project.caminho,
                                                  self.filterframe.lineEdit.text())
            self.func_file.set_kargs(var=self.filterframe.comboBox_5.currentText(),
                                     dim=self.filterframe.comboBox.currentText(),
                                     start=self.filterframe.comboBox_2.currentText(),
                                     stop=self.filterframe.comboBox_3.currentText())

        if self.FilterButton.isChecked():
            if len(self.fileList_View) < 1:
                QMessageBox.warning(self.file_page_main_screen, "Warning", "You must select one .nc file "
                                                                           "to filter.")
                self.FilterButton.setChecked(False)
            elif len(self.fileList_View) > 1:
                QMessageBox.warning(self.file_page_main_screen, "Warning", "You must select only one .nc file "
                                                                           "to filter.")
                self.FilterButton.setChecked(False)
            else:
                self.currentButton_onfilepage = self.FilterButton
                self.clear_filterframe_container()
                self.ConcatButrton.setChecked(False)
                self.MergeButton.setChecked(False)
                self.DatButton.setChecked(False)
                self.ImpButton.setChecked(False)
                self.DeleteButton.setChecked(False)

                self.frame_filter = QFrame()
                self.filterframe = FilterDatasetForm.Ui_Form()
                self.filterFieldFile_layout.addWidget(self.frame_filter)
                self.filterframe.setupUi(self, self.frame_filter, self.fileList_View)
                self.filterframe.comboBox.currentIndexChanged.connect(update_kargs)
                self.filterframe.comboBox_2.currentIndexChanged.connect(update_kargs)
                self.filterframe.comboBox_3.currentIndexChanged.connect(update_kargs)
                self.filterframe.lineEdit.textChanged.connect(update_kargs)

                self.func_file = FileFunctions.Filter(self.fileList_View, self.project.caminho,
                                                      self.filterframe.lineEdit.text())
                self.func_file.set_kargs(var=self.filterframe.comboBox_5.currentText(),
                                         dim=self.filterframe.comboBox.currentText(),
                                         start=self.filterframe.comboBox_2.currentText(),
                                         stop=self.filterframe.comboBox_3.currentText())

        else:
            self.clear_filterframe_container()
            self.func_file = None

    def delele_file(self):
        if self.DeleteButton.isChecked():
            if len(self.fileList_View) == 0:
                QMessageBox.warning(self.file_page_main_screen, "Warning", "You must select at least one .nc file "
                                                                           "to delete.")
                self.DeleteButton.setChecked(False)
            else:
                self.currentButton_onfilepage = self.DeleteButton
                self.clear_filterframe_container()
                self.ConcatButrton.setChecked(False)
                self.MergeButton.setChecked(False)
                self.DatButton.setChecked(False)
                self.ImpButton.setChecked(False)
                self.FilterButton.setChecked(False)

                self.func_file = FileFunctions.Delete(self.fileList_View, self.project.caminho, '')
        else:
            self.clear_filterframe_container()
            self.func_file = None

    def execute_function(self):
        if self.ExcuteButton.isChecked():
            self.ExcuteButton.setText('Stop')

            self.filepage_worker = FileWorker(
                package=self.func_file,
                page=self
            )

            self.filepage_worker.progress_file.connect(self.update_progress_for_file_page)
            self.filepage_worker.finished_file.connect(self.download_finished_for_file_page)
            self.filepage_worker.error_file.connect(self.handle_error_for_file_page)

            self.filepage_worker.start()
        else:
            self.filepage_worker.terminate()
            self.filepage_worker.wait()
            self.ExcuteButton.setText('Execute')
            self.toggle_progress_bar_execute()
            self.user_stop_for_file_page()

    def update_progress_for_file_page(self):
        QMessageBox.warning(self.download_page_screen, "Working in progress!", f"Please wait until the function "
                                                                               f"is executed.")

    def download_finished_for_file_page(self):
        QMessageBox.warning(self.download_page_screen, "Progress is finished!", f"Function concluded.")

    def handle_error_for_file_page(self, error_message):
        QMessageBox.warning(self.download_page_screen, "Error!", f"{error_message}.")

    def user_stop_for_file_page(self):
        QMessageBox.warning(self.download_page_screen, "Error!", f"Function stopped by user.")

    def toggle_progress(self):
        self.is_running = not self.is_running
        if self.is_running:
            self.progressBar.setRange(0, 0)  # Modo indeterminado - animação rodando
        else:
            self.progressBar.setRange(0, 1)  # Range fixo para não animar

    def toggle_progress_bar_execute(self):
        self.pbe_is_running = not self.pbe_is_running
        if self.pbe_is_running:
            self.progressBarExecute.setRange(0, 0)
        else:
            self.progressBarExecute.setRange(0, 1)

    def set_global_graph(self):
        self.figure.clear()
        self.canva.draw()

        self.ax = self.figure.add_subplot(111, projection=ccrs.PlateCarree())
        self.ax.set_global()
        self.ax.coastlines()
        self.ax.set_position([0, 0, 1, 1])
        self.canva.draw()

    def rebuild_graph(self):
        north_value = float(self.North_value.text())
        south_value = float(self.South_value.text())
        weast_value = float(self.Weast_value.text())
        east_value = float(self.East_value.text())

        for patch in self.ax.patches:
            patch.remove()

        self.ax.add_patch(
            Rectangle(
                (weast_value, south_value),
                east_value - weast_value,
                north_value - south_value,
                linewidth=.2,
                edgecolor='#2C423F',
                facecolor='#829191'
            )
        )

        self.canva.draw()
        return

    def clear_frame_for_simulalitonpage(self):
        if self.layout_simulation_page.count() > 1:
            child = self.layout_simulation_page.takeAt(1)
            if child.widget():
                child.widget().deleteLater()

    def cb_clicked(self):
        self.indivudualButton.setChecked(False)
        self.indivudualButton.setDisabled(False)
        self.collectiveButton.setDisabled(True)
        self.set_posprocess_page("c")

    def ib_clicked(self):
        self.collectiveButton.setChecked(False)
        self.collectiveButton.setDisabled(False)
        self.indivudualButton.setDisabled(True)
        self.set_posprocess_page("i")

    def set_posprocess_page(self, p: str):
        self.clear_frame_for_simulalitonpage()
        self.frame_analysis = QFrame()
        self.ui_analysis_page = Individual_Pages_POSprocess.Ui_Form() if p == "i" else None
        if self.ui_analysis_page:
            self.layout_simulation_page.addWidget(self.frame_analysis)
            self.ui_analysis_page.setupUi(self.frame_analysis, self.frame_18)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"DOWNLOAD PAGE", None))
        self.coordinateLabel.setText(QCoreApplication.translate("MainWindow", u"COORDINATES", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"North", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"West", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"East", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"South", None))
        self.dateLabel.setText(QCoreApplication.translate("MainWindow", u"DATE", None))
        self.initialdateLabel.setText(QCoreApplication.translate("MainWindow", u"Initial date", None))
        self.finaldateLabel.setText(QCoreApplication.translate("MainWindow", u"Final date", None))
        self.downloadLabel.setText(QCoreApplication.translate("MainWindow", u"DOWNLOAD", None))
        self.filenameLabel.setText(QCoreApplication.translate("MainWindow", u"File name", None))
        self.FileName.setPlaceholderText("")
        self.DownloadButton.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.variablesLabel.setText(QCoreApplication.translate("MainWindow", u"VARIABLES", None))
        self.Hycom_Button.setText("")
        self.CopernicusButton.setText("")

        self.HycomLabel.setText(QCoreApplication.translate("MainWindow", u"HYCOM", None))
        self.CopernicusLabel.setText(QCoreApplication.translate("MainWindow", u"COPERNICUS", None))
        self.view_header.setText(QCoreApplication.translate("MainWindow", u"VIEW PAGE", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Choose a file", None))
        self.set_combobox_files()

        self.file_header.setText(QCoreApplication.translate("MainWindow", u"FILE PAGE", None))
        self.filechooseLabel.setText(
            QCoreApplication.translate("MainWindow", u"Choose a file to see information:", None))

        self.ConcatButrton.setText(QCoreApplication.translate("MainWindow", u"Concat", None))
        self.MergeButton.setText(QCoreApplication.translate("MainWindow", u"Merge", None))
        self.FilterButton.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.ImpButton.setText(QCoreApplication.translate("MainWindow", u".IMP", None))
        self.DatButton.setText(QCoreApplication.translate("MainWindow", u".DAT", None))
        self.DeleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.ExcuteButton.setText(QCoreApplication.translate("MainWindow", u"Execute", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"SIMULATION PAGE", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.label.setText("")
        self.DB_1.setText("")
        self.VB_1.setText("")
        self.CB_1.setText("")
        self.SB_1.setText("")
        self.ConfigB_1.setText("")
        self.LogoutB_1.setText("")
        self.menu_button.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"GeoEnergia Lab", None))
