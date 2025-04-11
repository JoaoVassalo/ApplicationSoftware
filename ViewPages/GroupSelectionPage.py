from PySide6.QtWidgets import (
    QWidget, QFormLayout, QComboBox, QDoubleSpinBox, QVBoxLayout, QPushButton, QGridLayout,
    QLabel, QLineEdit, QHBoxLayout, QScrollArea, QCheckBox, QMessageBox
)
from PySide6.QtCore import Signal, QSize
from PySide6.QtGui import QFont, QPixmap, QImage, QStandardItemModel, QStandardItem
import matplotlib.pyplot as plt
import numpy as np


class GroupSelectionWidget(QWidget):
    group_update = Signal(str, list)

    def __init__(self, allcomposition: list, selectedcompostion: list = None, namegroup: str = None):
        super().__init__()
        self.composition = allcomposition
        self.allselected = selectedcompostion or []
        self.old_name = namegroup

        self.setWindowTitle('Group Configuration')
        self.setFixedSize(280, 390)

        layout_page = QVBoxLayout(self)

        self.layout_groupname = QHBoxLayout()
        self.label = QLabel(text="Group name: ")
        self.label.setMinimumSize(QSize(90, 16))
        self.label.setMaximumSize(QSize(90, 16))
        self.group_name = QLineEdit()
        if self.old_name:
            self.group_name.setText(f"{self.old_name}")
        self.group_name.setMinimumSize(QSize(160, 30))
        self.group_name.setMaximumSize(QSize(160, 30))
        self.layout_groupname.addWidget(self.label)
        self.layout_groupname.addWidget(self.group_name)

        layout_page.addLayout(self.layout_groupname)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_area.setWidget(self.scroll_content)
        self.layout_scroll = QVBoxLayout()
        self.scroll_content.setLayout(self.layout_scroll)

        layout_page.addWidget(self.scroll_area)

        self.layoutforbuttons = QHBoxLayout()

        self.save_group_button = QPushButton(text="Save Group")
        self.save_group_button.setMinimumSize(QSize(90, 30))
        self.save_group_button.setMaximumSize(QSize(90, 30))
        self.save_group_button.clicked.connect(self.update_group)
        self.cancel_group_button = QPushButton(text="Cancel")
        self.cancel_group_button.setMinimumSize(QSize(90, 30))
        self.cancel_group_button.setMaximumSize(QSize(90, 30))
        self.fontbutton = QFont()
        self.fontbutton.setPointSize(10)
        self.fontbutton.setItalic(True)
        self.save_group_button.setFont(self.fontbutton)
        self.cancel_group_button.setFont(self.fontbutton)

        self.layoutforbuttons.addWidget(self.save_group_button)
        self.layoutforbuttons.addWidget(self.cancel_group_button)

        layout_page.addLayout(self.layoutforbuttons)

        self.checkboxes = []
        for item in self.composition:
            checkbox = QCheckBox(item)
            if item in self.allselected:
                checkbox.setChecked(True)
            self.layout_scroll.addWidget(checkbox)
            self.checkboxes.append(checkbox)

    def update_group(self):
        selected_items = [cb.text() for cb in self.checkboxes if cb.isChecked()]
        if len(selected_items) <= 1:
            QMessageBox.warning(self, "Erro", "You must select at least two composition to create a group.")
        elif self.group_name.text() == '':
            QMessageBox.warning(self, "Erro", "You must give a name for the group.")
        else:
            self.group_update.emit(self.group_name.text(), selected_items)
