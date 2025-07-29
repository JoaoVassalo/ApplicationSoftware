from PySide6.QtWidgets import QApplication, QMainWindow
from database import Session, HycomCatalogo, CopernicusCatalogo
from index import Ui_MainWindow
from PySide6.QtGui import QColor, QMouseEvent
from PySide6.QtCore import Qt, QEvent
from PySide6 import QtWidgets


class MainAppWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.session = Session()
        catalogs_from_hycom = self.session.query(HycomCatalogo).all()
        catalogs_from_copernicus = self.session.query(CopernicusCatalogo).all()

        self.hycomCatalog = catalogs_from_hycom
        self.copernicusCatalog = catalogs_from_copernicus
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.minimum_width = 1200
        self.minimum_height = 800
        self.setMinimumSize(self.minimum_width, self.minimum_height)
        self.ui.maximizebutton.clicked.connect(self.resize_requested)

        self.old_pos = None
        self.ui.header_widget.installEventFilter(self)

        for x in shadow_elements:
            effect = QtWidgets.QGraphicsDropShadowEffect(self)
            effect.setBlurRadius(18)
            effect.setXOffset(0)
            effect.setYOffset(0)
            effect.setColor(QColor(0, 0, 0, 255))
            getattr(self.ui, x).setGraphicsEffect(effect)

    def resize_requested(self):
        if self.isMaximized():
            self.showNormal()
            self.setMinimumSize(self.minimum_width, self.minimum_height)
            self.resize(self.minimum_width, self.minimum_height)
        else:
            self.setMinimumSize(self.minimum_width, self.minimum_height)
            self.setMaximumSize(16777215, 16777215)
            self.showMaximized()

    def eventFilter(self, watched, event: QMouseEvent, /):
        if watched == self.ui.header_widget:
            if event.type() == QEvent.Type.MouseButtonPress and event.button() == Qt.MouseButton.LeftButton:

                if self.isMaximized():
                    self.showNormal()
                    self.setMinimumSize(self.minimum_width, self.minimum_height)
                    self.resize(self.minimum_width, self.minimum_height)

                self.old_pos = event.globalPosition().toPoint()
                return True

            elif event.type() == QEvent.Type.MouseMove and self.old_pos is not None:
                delta = event.globalPosition().toPoint() - self.old_pos
                self.move(self.pos() + delta)
                self.old_pos = event.globalPosition().toPoint()
                return True

            elif event.type() == QEvent.Type.MouseButtonRelease:
                self.old_pos = None

        return super().eventFilter(watched, event)


shadow_elements = {
    'icon_only_widget',
    'header_widget',
    'main_screen_widget',
    'download_page',
    'view_page',
    'simulation_page',
    'frame_25',  # setting page
    'file_page',
    'frame_to_info',
    'coord_date_file_widgets',
    'frame',
    'frame_buttons_analysis',
    'frame_5',
    'FunctionsFrame',
    'InformationAreaFiles',
    'RenameButton',
    'DatButton',
    'ImpButton',
    'FilterButton',
    'MergeButton',
    'ConcatButrton',
    'ExcuteButton'
}

if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet("""
            #header_widget {
                border-radius: 10px;
                background-color: #2C423F;
            }
            
            #header_widget > #label_4 {
                color: white;
                font-size: 18px;
                font-style: italic;
                font-weight: bold;
            }
            
            #icon_only_widget {
                border-radius: 10px;
                background-color: #2C423F;
            }
            
            #centralwidget {
                background-color: white;
            }
            
            [commonButton="true"] {
                background-color: #2C423F;
                border: none;
            }
            
            [commonButton="true"]:hover {
                background-color: #E0E2DB;
                border: 1px solid #5F7470;
                border-radius: 10px;
            }
            
            #menu_button {
                background-color: #2C423F;
                border: none;
            }
            
            [windowbuttons="true"] {
                background-color: #2C423F;
                border-radius: 12px;
                /*border: 1px solid #E0E2DB;*/
                width: 25px;
                height: 25px;
            }
            
            [windowbuttons="true"]:hover {
                background-color: #E0E2DB;
            }
            
            [DownloadCommomFrame="true"] {
                background-color: #C3C3C3;
                border: none;
                border-radius: 7px;
            }
            
            [ViewCommomFrame='true'] {
                background-color: #C3C3C3;
                border: none;
                border-radius: 4px;
            }
            
            [ViewCommomFrame_Animations='true'] {
                background-color: #C3C3C3;
                border: none;
                border-radius: 4px;
            }
            
            [ValueLabel_ViewPages='true'] {
                border: 1px solid #2C423F;
                border-radius: 3px;
            }
            
            [CommomButton_Animations='true'] {
                background-color: transparent;
                border: none;
                padding: 10px; /* Adicione um padding maior para ajustar o tamanho do fundo */
            }
            
            [CommomButton_Animations='true']:hover {
                background-color: rgba(255, 165, 0, 0.2); /* Cor de fundo no hover */
                border-radius: 5px; /* Bordas arredondadas */
            }
            
            [CommomButton_Animations='true']:pressed {
                background-color: rgba(255, 165, 0, 0.5); /* Cor de fundo ao pressionar */
            }
            
            [commonLine="true"] {
                background-color: #949B96;
            }
            
            #DataBase_Frame {
                background-color: #829191;
                border-radius: 15px;
                border: 2px solid #2C423F;
            }
            
            [TitleCommon="true"] {
                font-size: 12px;
                font-style: italic;
                font-weight: bold;
                color: #2C423F
            }
            
            [LabelDownloadCommon="true"] {
                font-size: 14px;
                font-style: italic;
                font-weight: bold;
                color: #4C5B61
            }
            
            [CommomComboBox='true'] {
                background-color: #C3C3C3; /*829191*/
                border-radius: 15px;
                border: 2px solid #2C423F;
                color: black;
                padding-left: 15px;
                padding-right: 10px;
            }
            
            [CommomComboBox='true']::down-arrow {
                width: 15px;
                height: 15px;
                image: url(':/icons/icons/seta_baixo - branca.png');
            }
            
            [CommomComboBox='true']::drop-down {
                border: none;
                width: 15px;  /*tamanho da seta*/
                background-color: #2C423F;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 10px;
            }
            
            QComboBox QAbstractiItemView {
                border: 1px solid #2C423F;
                background-color: white;
                color: black;
                selection-background-color: orange;
                selection-color: black;
                padding: 5px;
                border-radius: 5px;
            }
            
            #comboBox {
                border-radius: 12px;
            }
            
            [HeaderTitleCommon="true"] {
                font-size: 14px;
                color: #2C423F;
            }
            
            [commonLineEditDownloadPage="true"] {
                border-radius: 15px;
                border: 2px solid #2C423F;
                color: black;
                background-color: #C3C3C3; /*829191*/
            }
            
            #fromDateEdit, #toDateEdit, #regionEdit {
                border-radius: 10px;
            }
            
            #FileName {
                padding-left: 15px;
                padding-right: 10px;
            }
            
            #variables_checkbox_widget {
                border: 2px solid #2C423F;
                border-radius: 10px;
                background-color: #C3C3C3; /*829191*/
            }
            
            [commonDateEdit="true"] {
                background-color: #C3C3C3; /*829191*/
                border-radius: 15px;
                border: 2px solid #2C423F;
                color: black;
                padding-left: 15px;
                padding-right: 10px;
            }
            
            [commonDateEdit="true"]::up-button {
                width: 15px;
                height: 15px;
                subcontrol-origin: border;
                subcontrol-position: top right;
                padding-right: 3px;
                margin: 2px;
                border: none;
                background-color: #2C423F;
                border-top-right-radius: 10px;
            }
            
            [commonDateEdit="true"]::up-arrow {
                border: none;
                width: 10px;
                height: 10px;
                border-left: 1px solid black;
                border-bottom: 1px solid black;
                margin: 2px;
                image: url(':/icons/icons/seta_cima - branca.png');
            }
            
            [commonDateEdit="true"]::down-button {
                width: 15px;
                height: 15px;
                subcontrol-origin: border;
                subcontrol-position: bottom right;
                padding-right: 3px;
                margin: 2px;
                border: none;
                background-color: #2C423F;
                border-bottom-right-radius: 10px;
            }
            
            [commonDateEdit="true"]::down-arrow {
                border: none;
                width: 10px;
                height: 10px;
                border-left: 1px solid black;
                border-top: 1px solid black;
                margin: 2px;
                image: url(':/icons/icons/seta_baixo - branca.png');
            }
            
            QCheckBox::indicator:checked {
                background-color: #2C423F;
                border: 1px solid black;
                border-radius: 5px;
                image: url(':/icons/icons/confirmar - branca.png');
            }
            
            QCheckBox::indicator:unchecked {
                background-color: #C3C3C3;
                border: 1px solid black;
                border-radius: 5px;
            }
            
            QCheckBox::indicator {
                width: 15px;
                height: 15px;
            }
            
            #DownloadButton {
                background-color: #C3C3C3;
                border-radius: 10px;
                border: 1px solid #F98600;
                font-size: 14px;
                font-style: italic;
                font-weight: bold;
                color: #4C5B61
            }
            
            #DownloadButton:hover {
                background-color: #6F1A07;
            }
            
            #DownloadButton:checked {
                color: #F98600;
                font-size: 14px;
            }
            
            [CommomButtonsViews='true'] {
                background-color: #C3C3C3;
                border-radius: 6px;
                border: 1px solid #F98600;
                font-size: 14px;
                font-style: italic;
                font-weight: bold;
                color: #4C5B61;
                min-width: 100px; /* Largura mínima */
                max-width: 200px;
                min-height: 20px; /* Altura mínima */
            }
            
            [CommomButtonsViews='true']:hover {
                background-color: #6F1A07;
            }
            
            [CommomButtonsViews='true']:checked {
                color: #F98600;
                font-size: 14px;
            }
            
            [CommomButtonViewPageFunc='true'] {
                background-color: #C3C3C3;
                border-radius: 6px;
                font-size: 14px;
                font-style: italic;
                font-weight: bold;
                color: #4C5B61;
            }
            
            [CommomButtonViewPageFunc='true']:hover {
                color: #6F1A07;
                font-size: 14px;
            }
            
            [CommomButtonViewPageFunc='true']:checked {
                font-size: 14px;"
            }
            
            [NameLabel_ViewPages='true'] {
                font-size: 16px;
                font-style: italic;
                font-weight: bold;
                color: #4C5B61;
            }
            
            [CommomComboboxView='true'] {
                padding-left: 15px;
                color: #7AE7C7;
                background-color: black;
            }
            
            #scrollAreaWidgetContents {
                background-color: #C3C3C3;
            }
            
            QToolTip {
                background-color: #5F7470;
                color: black;
                border: 1px solid #5F7470;
                border-radius: 10px;
                padding: 4px;
            }
            
            [CommomFrame_PPA="true"] {
                background-color: #C3C3C3;
            }
            
            /*
            ------------------------------------------------------------------------------------------------------------
            #frame_buttons_analysis {
                background-color: black;
            }
            
            #indivudualButton {
                width: 250px;
                height: 35px;
                border: 1px solid black;
                border-top-left-radius: 6px;
                border-bottom-left-radius: 6px;
                border-right: none; /* Remove a borda do meio */
                padding: 10px;
                background-color: #C3C3C3;
                color: black;
            }
            
            #collectiveButton {
                width: 250px;
                height: 35px;
                border: 1px solid black;
                border-top-right-radius: 6px;
                border-bottom-right-radius: 6px;
                border-left: none; /* Remove a borda do meio */
                padding: 10px;
                background-color: #C3C3C3;
            }
            
            [CommomTableDataframe='true'] {
                background-color: #F0F0F0;
                gridline-color: #C0C0C0;
                font-size: 14px;
                border: 1px solid #C0C0C0;
            }
            
            [CommomTableDataframe='true'] QHeaderView::section {
                background-color: #4A90E2;
                color: white;
                font-weight: bold;
                padding: 5px;
                border: 1px solid #C0C0C0;
            }
            
            [CommomTableDataframe='true'] QTableView::item {
                padding: 5px;
            }
            
            [CommomTableDataframe='true'] QTableView::item:selected {
                background-color: #4CAF50;
                color: white;
            }
            
            222823
            ------------------------------------------------------------------------------------------------------------
            */
        """)
    window = MainAppWindow()
    window.show()
    app.exec()
