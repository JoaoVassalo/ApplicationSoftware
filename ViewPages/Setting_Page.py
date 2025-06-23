import sys
import os
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QRadioButton, QButtonGroup, QFileDialog, QSpacerItem, QSizePolicy)
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import QUrl, QSize, Signal
from PySide6.QtWebEngineWidgets import QWebEngineView


class ConfigPage(QWidget):
    path_change = Signal()

    def __init__(self):
        super().__init__()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        v_layout_path = QVBoxLayout()
        h_layout_pathinfo = QHBoxLayout()
        h_layout_pathbutton = QHBoxLayout()
        v_layout_docview = QVBoxLayout()
        h_layout_radio = QHBoxLayout()

        pathlabel = QLabel("📂 Project path:")
        info_button = QPushButton()
        info_button.setObjectName("info_button")
        icon_info = QIcon()
        icon_info.addFile(u":/icons/icons/informação - branco.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        info_button.setIcon(icon_info)
        info_button.setIconSize(QSize(16, 16))
        spacer_pathlabel = QSpacerItem(28, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        h_layout_pathinfo.addWidget(pathlabel)
        h_layout_pathinfo.addWidget(info_button)
        h_layout_pathinfo.addItem(spacer_pathlabel)
        h_layout_pathinfo.setSpacing(3)

        self.pathline = QLineEdit()
        self.pathline.setReadOnly(True)
        browse_button = QPushButton("Browser")
        browse_button.clicked.connect(self.open_dialog)
        self.apply_button = QPushButton("Load")
        self.apply_button.clicked.connect(self.load_path)
        self.apply_button.setDisabled(True)
        spacer_pathline = QSpacerItem(28, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        h_layout_pathbutton.addWidget(self.pathline)
        h_layout_pathbutton.addWidget(browse_button)
        h_layout_pathbutton.addWidget(self.apply_button)
        h_layout_pathbutton.addItem(spacer_pathline)
        h_layout_pathbutton.setSpacing(3)

        v_layout_path.addLayout(h_layout_pathinfo)
        v_layout_path.addLayout(h_layout_pathbutton)

        doc_label = QLabel("📄 Document View:")
        radio_group = QButtonGroup()
        report_radio = QRadioButton("Report")
        manual_radio = QRadioButton("Manual")
        report_radio.setChecked(True)
        radio_group.addButton(report_radio)
        radio_group.addButton(manual_radio)
        h_layout_radio.addWidget(report_radio)
        h_layout_radio.addWidget(manual_radio)
        h_layout_radio.setSpacing(5)
        pdf_viewer = QWebEngineView()
        pdf_viewer.setUrl(QUrl.fromLocalFile(os.path.abspath("relatorio.pdf")))

        v_layout_docview.addWidget(doc_label)
        v_layout_docview.addLayout(h_layout_radio)
        v_layout_docview.addWidget(pdf_viewer)

        main_layout.addLayout(v_layout_path)
        main_layout.addLayout(v_layout_docview)
        self.setLayout(main_layout)
        self.setStyleSheet(
            """
            #info_button {
                background-color: #C3C3C3;
                border: none;
            }
            
            """
        )

    def open_dialog(self):
        caminho = QFileDialog.getExistingDirectory(self, "Selecionar Caminho", "")
        if caminho:
            self.pathline.setText(caminho)
            self.apply_button.setDisabled(False)

    def load_path(self):
        self.apply_button.setDisabled(True)
        self.path_change.emit()
