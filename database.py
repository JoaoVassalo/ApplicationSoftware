from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os
from DbCatalogs.HycomCatalogs import hycom_catalogs
from DbCatalogs.CopernicusCatalogs import copernicus_catalogs

# Configuração do banco de dados
Base = declarative_base()

# class Projeto(Base):
#     __tablename__ = 'projetos'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     nome = Column(String, nullable=False)
#     caminho = Column(String, nullable=False)

class Configuracao(Base):
    __tablename__ = 'configuracoes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    chave = Column(String, nullable=False, unique=True)
    valor = Column(String, nullable=False)

class HycomCatalogo(Base):
    __tablename__ = 'Catalogos_hycom'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False, unique=True)
    url = Column(String, nullable=False)
    data_inicial = Column(Date, nullable=False)
    data_final = Column(Date or String, nullable=False)
    type = Column(String, nullable=False)
    region = Column(String, nullable=False)
    variaveis = relationship("VariavelHycomCatalogo", back_populates="catalogo", cascade="all, delete-orphan")

class VariavelHycomCatalogo(Base):
    __tablename__ = 'variaveis_catalogoshycom'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    catalogo_id = Column(Integer, ForeignKey('Catalogos_hycom.id'), nullable=False)
    catalogo = relationship("HycomCatalogo", back_populates="variaveis")

class CopernicusCatalogo(Base):
    __tablename__ = 'Catalogos_copernicus'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False, unique=True)
    type = Column(String, nullable=False)
    data_inicial = Column(Date, nullable=False)
    data_final = Column(Date or String, nullable=False)
    region = Column(String, nullable=False)
    variaveis = relationship("VariavelCopernicusCatalogo", back_populates="catalogo", cascade="all, delete-orphan")

class VariavelCopernicusCatalogo(Base):
    __tablename__ = 'variaveis_catalogoscopernicus'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    catalogo_id = Column(Integer, ForeignKey('Catalogos_copernicus.id'), nullable=False)
    catalogo = relationship("CopernicusCatalogo", back_populates="variaveis")

def criar_hycom_catalogo(nome, url, data_inicial, data_final, type_catalog, regiao, variaveis):
    """Cria um novo catálogo com suas variáveis."""
    with Session() as session:
        catalogo_existente = session.query(HycomCatalogo).filter_by(nome=nome).first()
        if catalogo_existente:
            # raise ValueError(f"O catálogo '{nome}' já existe no banco de dados.")
            return

        novo_catalogo = HycomCatalogo(
            nome=nome,
            url=url,
            data_inicial=data_inicial,
            data_final=data_final,
            type=type_catalog,
            region=regiao,
            variaveis=[VariavelHycomCatalogo(nome=var) for var in variaveis]
        )
        session.add(novo_catalogo)
        session.commit()
        return novo_catalogo

def criar_copernicus_catalogo(nome, product, data_inicial, data_final, region_, variaveis):
    """Cria um novo catálogo com suas variáveis."""
    with Session() as session:
        catalogo_existente = session.query(CopernicusCatalogo).filter_by(nome=nome).first()
        if catalogo_existente:
            # raise ValueError(f"O catálogo '{nome}' já existe no banco de dados.")
            return

        novo_catalogo = CopernicusCatalogo(
            nome=nome,
            type=product,
            data_inicial=data_inicial,
            data_final=data_final,
            region=region_,
            variaveis=[VariavelCopernicusCatalogo(nome=var) for var in variaveis]
        )
        session.add(novo_catalogo)
        session.commit()
        return novo_catalogo

def listar_catalogos():
    """Lista todos os catálogos e suas variáveis."""
    with Session() as session:
        catalogos = session.query(HycomCatalogo).all()
        return catalogos

# Funções utilitárias
# def criar_projeto(nome, caminho):
#     with Session() as session:
#         projeto_existente = session.query(Projeto).filter_by(nome=nome).first()
#         if projeto_existente:
#             raise ValueError(f"O projeto '{nome}' já existe no banco de dados.")
#
#         novo_projeto = Projeto(nome=nome, caminho=caminho)
#         session.add(novo_projeto)
#         session.commit()
#         return novo_projeto
#
# def listar_projetos():
#     with Session() as session:
#         projetos = session.query(Projeto).all()
#         return projetos

# def create_main_folder(default_folder=r"C:\Users\UDESC\Documents\Folder_NewProjeto"):
#     print('Criando Main Folder')
#     try:
#         with Session() as session:
#             folder_raiz = session.query(Configuracao).filter_by(chave="folder_raiz").first()
#             if not folder_raiz:
#                 # Cria a pasta principal, se necessário
#                 os.makedirs(default_folder, exist_ok=True)
#                 folder_raiz = Configuracao(chave="folder_raiz", valor=default_folder)
#                 session.add(folder_raiz)
#                 session.commit()
#             return folder_raiz.valor
#     except Exception as e:
#         print(f"Erro ao criar o diretório: {e}")
#         return None

# Inicialização do banco de dados
DATABASE_URL = "sqlite:///projetos.db"  # Altere o caminho, se necessário
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# if __name__ == '__main__':
#     create_main_folder()

for key, item in hycom_catalogs.items():
    criar_hycom_catalogo(nome=key, url=item.url, data_inicial=item.i_date, data_final=item.f_date,
                         type_catalog=item.type, regiao=item.region, variaveis=item.variables)

for key, item in copernicus_catalogs.items():
    criar_copernicus_catalogo(nome=key, product=item.type, data_inicial=item.i_date, data_final=item.f_date,
                   region_=item.region, variaveis=item.variables)
