from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget
from ViewPages import VarInformation

class FileFormWidget(QWidget):
    remove_requested = Signal()
    checklist_requested = Signal()

    def __init__(self, file_info, parent=None):
        super().__init__(parent)

        self.ui = VarInformation.Ui_Form()
        self.ui.setupUi(self, file_info[0], file_info[1])

        self.ui.pushButton.clicked.connect(self.remove_requested.emit)
        self.ui.checkBox.clicked.connect(self.checklist_requested.emit)
