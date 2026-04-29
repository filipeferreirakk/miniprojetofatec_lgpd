# Projeto de Adequação LGPD

Este projeto realiza o processamento de uma base de dados de usuários para garantir a conformidade com a Lei Geral de Proteção de Dados (LGPD). O sistema conecta-se a um banco PostgreSQL, recupera os registros e aplica técnicas de anonimização em campos sensíveis.

Como funciona:
1. O script principal acessa o banco de dados e aplica máscaras em Nomes, CPFs, E-mails e Telefones.
2. São gerados arquivos CSV individuais para cada ano de nascimento encontrado na base.
3. É gerado um arquivo chamado 'todos.csv' contendo apenas Nome e CPF originais para fins de auditoria.
4. O tempo de execução das tarefas é monitorado e registrado em um arquivo de log.

Como rodar:
1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale as bibliotecas necessárias com o comando: pip install -r requirements.txt
3. Execute o projeto com o comando: python main.py
4. Os arquivos gerados (.csv) e o log de performance (execucao.log) aparecerão na pasta do projeto.