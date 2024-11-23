from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração do banco de dados
Base = declarative_base()


class Projeto(Base):
    __tablename__ = 'projetos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    caminho = Column(String, nullable=False)


# Inicialização do banco de dados
DATABASE_URL = "sqlite:///projetos.db"  # Altere o caminho, se necessário
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


# Funções utilitárias
def criar_projeto(nome, caminho):
    session = Session()
    projeto_existente = session.query(Projeto).filter_by(nome=nome).first()
    if projeto_existente:
        raise ValueError(f"O projeto '{nome}' já existe no banco de dados.")

    novo_projeto = Projeto(nome=nome, caminho=caminho)
    session.add(novo_projeto)
    session.commit()
    session.close()
    return novo_projeto


def listar_projetos():
    session = Session()
    projetos = session.query(Projeto).all()
    session.close()
    return projetos
