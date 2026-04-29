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
    
    nome = linha_modificada[1]
    if nome:
        partes = nome.split(' ', 1)
        primeiro = partes[0]
        p_mascarado = primeiro[0] + '*' * (len(primeiro) - 1)
        linha_modificada[1] = f"{p_mascarado} {partes[1]}" if len(partes) > 1 else p_mascarado

    cpf_original = linha_modificada[2]
    if cpf_original:
        linha_modificada[2] = f"{cpf_original[:3]}.***.***-**"

    email_original = linha_modificada[3]
    if email_original and '@' in email_original:
        usuario, dominio = email_original.split('@')
        usuario_mascarado = usuario[0] + '*' * (len(usuario) - 1)
        linha_modificada[3] = f"{usuario_mascarado}@{dominio}"

    tel_original = linha_modificada[4]
    if tel_original:
        apenas_numeros = ''.join(filter(str.isdigit, tel_original))
        linha_modificada[4] = apenas_numeros[-4:]

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