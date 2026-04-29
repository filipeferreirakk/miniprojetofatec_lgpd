from sqlalchemy import create_engine, text
from datetime import datetime

HOST = '200.19.224.150'
USER = 'alunos'
PASSWORD = 'AlunoFatec'
DATABASE = 'atividade2'
PORT = '5432'

connection_string = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(connection_string)

def testar_conexao():
    try:
        with engine.connect() as conn:
            print("Conexão estabelecida com sucesso!")
    except Exception as e:
        print(f"Erro ao conectar: {e}")

if __name__ == "__main__":
    testar_conexao()

def LGPD(row):
    linha_modificada = list(row)
    
    
    return tuple(linha_modificada)

def processar_usuarios():
    users = []
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM usuarios LIMIT 10;"))
        for row in result:
            row_anonimizada = LGPD(row)
            users.append(row_anonimizada)
            print(row_anonimizada)
            
    return users

if __name__ == "__main__":
    processar_usuarios()