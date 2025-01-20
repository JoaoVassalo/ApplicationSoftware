from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
import os
from LoginPage import Ui_Form
from database import Session, Projeto, Configuracao, HycomCatalogo, CopernicusCatalogo
from index import Ui_MainWindow
from PySide6.QtGui import QColor
from PySide6 import QtWidgets


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
    'icon_only_widget',
    'header_widget',
    'main_screen_widget',
    'download_page',
    'view_page',
    'simulation_page',
    'settings_page',
    'file_page'
}

if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet("""
            #header_widget {
                border-radius: 10px;
                background-color: #2C423F;
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
            
            [DownloadCommomFrame="true"] {
                background-color: #C3C3C3;
                border: none;
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
            
            #Catalog_Combox {
                background-color: #829191;
                border-radius: 15px;
                border: 2px solid #2C423F;
                color: black;
                padding-left: 15px;
                padding-right: 10px;
            }
            
            #Catalog_Combox::down-arrow {
                width: 15px;
                height: 15px;
                image: url(':/icons/icons/seta_baixo - branca.png');
            }
            
            #Catalog_Combox::drop-down {
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
            
            [HeaderTitleCommon="true"] {
                font-size: 14px;
                color: #2C423F;
            }
    
            QToolTip {
                background-color: #5F7470;
                color: black;
                border: 1px solid #5F7470;
                border-radius: 10px;
                padding: 4px;
            }
        """)
    window = MainWindow()
    window.show()
    app.exec()
