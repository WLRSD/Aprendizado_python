import sqlite3

# Função para criar o banco de dados e as tabelas
def create_db():
    connection = sqlite3.connect('exercises.db')  # Cria ou abre o banco de dados
    cursor = connection.cursor()

    # Criar tabela 'levels' (níveis de exercício)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS levels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE
    );
    ''')

    # Criar tabela 'exercises' (exercícios)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS exercises (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        level_id INTEGER,
        name TEXT,
        code_path TEXT,
        markdown_path TEXT,
        completed INTEGER,
        FOREIGN KEY (level_id) REFERENCES levels (id)
    );
    ''')

    connection.commit()  # Confirma as mudanças
    connection.close()  # Fecha a conexão com o banco

# Chama a função para criar o banco de dados e as tabelas
create_db()
