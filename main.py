from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
import os
from LoginPage import Ui_Form
from database import Session, Projeto, Configuracao, HycomCatalogo, CopernicusCatalogo
from index import Ui_MainWindow
from PySide6.QtGui import QPainter, QColor
from PySide6 import QtWidgets, QtCharts


class MainAppWindow(QMainWindow):
    def __init__(self, project, Hcatalog, Ccatalog):
        super().__init__()
        self.project = project
        self.hycomCatalog = Hcatalog
        self.copernicusCatalog = Ccatalog
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        for x in shadow_elements:
            effect = QtWidgets.QGraphicsDropShadowEffect(self)
            effect.setBlurRadius(18)
            effect.setXOffset(0)
            effect.setYOffset(0)
            effect.setColor(QColor(0, 0, 0, 255))
            getattr(self.ui, x).setGraphicsEffect(effect)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Inicializar sessão do banco de dados
        self.session = Session()

        # Carregar listas de projetos
        self.load_project_lists()

        # Conectar botões às funcionalidades
        self.ui.pushButton.clicked.connect(self.open_project)  # Abrir projeto
        self.ui.pushButton_2.clicked.connect(self.create_project)  # Criar projeto
        self.ui.pushButton_3.clicked.connect(self.delete_project)  # Deletar projeto

    def load_project_lists(self):
        """
        Recarrega as listas de projetos nos dois QComboBox.
        """
        # Limpa os combo boxes
        self.ui.comboBox.clear()
        self.ui.comboBox_2.clear()

        projetos = self.session.query(Projeto).all()
        for projeto in projetos:
            self.ui.comboBox.addItem(projeto.nome)  # Lista para abrir projeto
            self.ui.comboBox_2.addItem(projeto.nome)  # Lista para deletar projeto

    def create_project(self):
        """
        Cria um novo projeto, salva no banco e no disco.
        """
        nome_projeto = self.ui.lineEdit.text().strip()
        if not nome_projeto:
            QMessageBox.warning(self, "Erro", "O nome do projeto não pode estar vazio.")
            return

        folder_raiz = self.session.query(Configuracao).filter_by(chave="folder_raiz").first().valor
        caminho_projeto = os.path.join(folder_raiz, nome_projeto)

        try:
            os.makedirs(caminho_projeto, exist_ok=False)
        except FileExistsError:
            QMessageBox.warning(self, "Erro", "Já existe um projeto com esse nome.")
            return

        # Salvar no banco de dados -------------------------------------------------------------------------------------
        novo_projeto = Projeto(nome=nome_projeto, caminho=caminho_projeto)
        self.session.add(novo_projeto)
        self.session.commit()

        QMessageBox.information(self, "Sucesso", f"Projeto '{nome_projeto}' criado em: {caminho_projeto}")

        try:
            projeto = self.session.query(Projeto).filter_by(nome=nome_projeto).first()
            catalogs_from_hycom = self.session.query(HycomCatalogo).all()
            catalogs_from_copernicus = self.session.query(CopernicusCatalogo).all()
            self.mainapp = MainAppWindow(projeto, catalogs_from_hycom, catalogs_from_copernicus)
            self.mainapp.show()
            self.close()
        except Exception as e:
            raise QMessageBox.warning(self, "Erro", f"{e}")

    def open_project(self):
        """
        Exibe informações do projeto selecionado.
        """
        projeto_selecionado = self.ui.comboBox.currentText()
        if not projeto_selecionado:
            QMessageBox.warning(self, "Erro", "Nenhum projeto selecionado.")
            return

        projeto = self.session.query(Projeto).filter_by(nome=projeto_selecionado).first()
        if projeto:
            catalogs_from_hycom = self.session.query(HycomCatalogo).all()
            catalogs_from_copernicus = self.session.query(CopernicusCatalogo).all()
            self.mainapp = MainAppWindow(projeto, catalogs_from_hycom, catalogs_from_copernicus)
            self.mainapp.show()
            self.close()
        else:
            QMessageBox.warning(self, "Erro", "Projeto não encontrado no banco de dados.")

    def delete_project(self):
        """
        Remove um projeto selecionado do banco de dados e do disco.
        """
        projeto_selecionado = self.ui.comboBox_2.currentText()
        if not projeto_selecionado:
            QMessageBox.warning(self, "Erro", "Nenhum projeto selecionado.")
            return

        projeto = self.session.query(Projeto).filter_by(nome=projeto_selecionado).first()
        if projeto:
            confirmacao = QMessageBox.question(
                self,
                "Confirmar Exclusão",
                f"Tem certeza de que deseja deletar o projeto '{projeto.nome}'?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if confirmacao == QMessageBox.StandardButton.Yes:
                # Remover do disco -------------------------------------------------------------------------------------
                try:
                    os.rmdir(projeto.caminho)
                except OSError:
                    QMessageBox.warning(self, "Erro", f"Não foi possível excluir a pasta '{projeto.caminho}'. Certifique-se de que está vazia.")
                    return

                # Remover do banco de dados ----------------------------------------------------------------------------
                self.session.delete(projeto)
                self.session.commit()

                QMessageBox.information(self, "Sucesso", f"Projeto '{projeto.nome}' foi deletado.")
                self.load_project_lists()
        else:
            QMessageBox.warning(self, "Erro", "Projeto não encontrado no banco de dados.")


shadow_elements = {
    'icon_text_widget',
    'icon_only_widget',
    'header_widget',
    'main_screen_widget'
}

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
