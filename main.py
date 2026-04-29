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
    
    nome_original = linha_modificada[1]
    
    if nome_original:
        partes_nome = nome_original.split(' ', 1)
        primeiro_nome = partes_nome[0]
        
        primeiro_nome_mascarado = primeiro_nome[0] + '*' * (len(primeiro_nome) - 1)
        
        if len(partes_nome) > 1:
            linha_modificada[1] = f"{primeiro_nome_mascarado} {partes_nome[1]}"
        else:
            linha_modificada[1] = primeiro_nome_mascarado

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