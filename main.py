from sqlalchemy import create_engine, text
from datetime import datetime
import csv
from decorator_tempo import medir_tempo

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
        linha_modificada[2] = f"{cpf_original[:3]}.*** ***-**"

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


@medir_tempo
def atividade_2(usuarios_anonimizados):
    por_ano = {}
    
    for user in usuarios_anonimizados:
        ano = user[5].year
        if ano not in por_ano:
            por_ano[ano] = []
        por_ano[ano].append(user)
    
    for ano, registros in por_ano.items():
        filename = f"{ano}.csv"
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'nome', 'cpf', 'email', 'telefone', 'data_nascimento', 'created_on', 'updated_on'])
            writer.writerows(registros)
    print(f"Atividade 2 concluída: {len(por_ano)} arquivos gerados.")


@medir_tempo
def atividade_3():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT nome, cpf FROM usuarios;"))
        
        with open('todos.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['nome', 'cpf'])
            writer.writerows(result)
    print("Atividade 3 concluída: arquivo todos.csv gerado.")


def main():
    print("--- Iniciando Processamento LGPD ---")
    
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM usuarios;"))
        usuarios_brutos = result.fetchall()
    
    print(f"Total de registros recuperados: {len(usuarios_brutos)}")
    
    usuarios_anonimizados = [LGPD(row) for row in usuarios_brutos]
    print("Anonimização concluída.")

    print("\nExecutando Atividade 2...")
    atividade_2(usuarios_anonimizados)

    print("\nExecutando Atividade 3...")
    atividade_3()

    print("\n--- Processamento Finalizado com Sucesso ---")

if __name__ == "__main__":
    main()