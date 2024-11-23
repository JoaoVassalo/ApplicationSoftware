from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from index import Ui_MainWindow
from DownloadPage import Ui_PageDownload


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

# from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel
#
#
# # Página nova que será inserida
# class NewPage(QWidget):
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         layout.addWidget(QLabel("Você está na nova página!"))
#         self.setLayout(layout)
#
#
# # Janela principal
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         # Layout principal da janela
#         self.layout = QVBoxLayout(self)
#
#         # Botão para trocar o conteúdo
#         self.button = QPushButton("Ir para a nova página")
#         self.button.clicked.connect(self.show_new_page)
#
#         # Adicionando o botão ao layout
#         self.layout.addWidget(self.button)
#
#         # Área onde o novo widget será adicionado
#         self.content_area = QWidget()
#         self.content_area_layout = QVBoxLayout()
#         self.content_area.setLayout(self.content_area_layout)
#         self.layout.addWidget(self.content_area)
#
#     def show_new_page(self):
#         # Limpando o conteúdo atual da área
#         for i in reversed(range(self.content_area_layout.count())):
#             widget_to_remove = self.content_area_layout.itemAt(i).widget()
#             if widget_to_remove is not None:
#                 widget_to_remove.deleteLater()
#
#         # Inserindo a nova página
#         new_page = NewPage()
#         self.content_area_layout.addWidget(new_page)
#
#
# # Inicialização do aplicativo
# app = QApplication([])
#
# main_window = MainWindow()
# main_window.show()
#
# app.exec()
