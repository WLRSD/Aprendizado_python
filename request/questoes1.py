import os
import sqlite3
import streamlit as st

# Função para criar o banco de dados e as tabelas (essa função deve ser chamada uma vez no início)
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

# Função para adicionar um novo nível ao banco de dados
def create_level(level_name):
    connection = sqlite3.connect('exercises.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO levels (name) VALUES (?)', (level_name,))
    connection.commit()
    connection.close()
    st.success(f"Nível '{level_name}' criado com sucesso!")

# Função para adicionar um exercício ao banco de dados
def create_exercise(level_id, exercise_name, code_path, markdown_path):
    connection = sqlite3.connect('exercises.db')
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO exercises (level_id, name, code_path, markdown_path, completed)
    VALUES (?, ?, ?, ?, ?)
    ''', (level_id, exercise_name, code_path, markdown_path, 0))  # 0 significa que o exercício ainda não foi feito
    connection.commit()
    connection.close()
    st.success(f"Exercício '{exercise_name}' criado com sucesso!")

# Função para buscar os exercícios de um nível
def get_exercises(level_id):
    connection = sqlite3.connect('exercises.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id, name, code_path, markdown_path, completed FROM exercises WHERE level_id = ?', (level_id,))
    exercises = cursor.fetchall()
    connection.close()
    return exercises

# Função para marcar exercício como feito
def mark_as_done(exercise_id):
    connection = sqlite3.connect('exercises.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE exercises SET completed = 1 WHERE id = ?', (exercise_id,))
    connection.commit()
    connection.close()

# Função para listar os níveis de exercícios
def list_levels():
    connection = sqlite3.connect('exercises.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id, name FROM levels')
    levels = cursor.fetchall()
    connection.close()
    return levels

# Função para listar as pastas de exercício
def list_exercise_directories():
    # Caminho onde os exercícios estão armazenados
    base_path = "exercícios"
    level_dirs = []

    # Verifica se o caminho base existe
    if os.path.exists(base_path):
        # Lista todos os diretórios dentro de "exercicios"
        level_dirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

        # Ordenar os diretórios de forma numérica (do nível 1 ao nível 10)
        level_dirs.sort(key=lambda x: int(x.split()[-1]))  # Ordena pelos números dos níveis

    return level_dirs

# Função para verificar se um arquivo existe
def file_exists(directory, filename):
    return os.path.exists(os.path.join(directory, filename))

# Função para criar os arquivos .py e .md
def create_code_and_markdown_files(directory, exercise_name):
    # Criar o arquivo Python
    code_file_path = os.path.join(directory, f"{exercise_name}.py")
    if not file_exists(directory, f"{exercise_name}.py"):
        with open(code_file_path, "w") as file:
            file.write("# Código para o exercício\n")
        st.success(f"Arquivo {code_file_path} criado com sucesso!")
    else:
        st.info(f"O arquivo {code_file_path} já existe.")

    # Criar o arquivo Markdown
    markdown_file_path = os.path.join(directory, f"{exercise_name}.md")
    if not file_exists(directory, f"{exercise_name}.md"):
        with open(markdown_file_path, "w") as file:
            file.write("# Descrição do exercício\n")
        st.success(f"Arquivo {markdown_file_path} criado com sucesso!")
    else:
        st.info(f"O arquivo {markdown_file_path} já existe.")

# Função para listar os arquivos dentro de um diretório
def list_files_in_directory(directory):
    try:
        # Verifica se o diretório existe
        if os.path.exists(directory):
            # Lista os arquivos no diretório
            files = os.listdir(directory)
            return files
        else:
            return None
    except Exception as e:
        return f"Erro ao acessar o diretório: {e}"

# Criar o banco de dados e as tabelas caso ainda não exista
create_db()

# Layout do título
st.title("Gestão de Exercícios de Python")

# Obter níveis do banco
levels = list_levels()

# Verificar se há níveis
if levels:
    level_names = [level[1] for level in levels]
    selected_level_name = st.selectbox("Escolha um nível", level_names)

    # Obter o id do nível selecionado
    selected_level_id = next(level[0] for level in levels if level[1] == selected_level_name)

    # Exibir os exercícios do nível selecionado
    st.subheader("Exercícios Criados")
    exercises = get_exercises(selected_level_id)

    # Verificar se há exercícios
    if exercises:
        exercise_count = len(exercises)
        exercises_per_page = 3  # Número de exercícios por "página"
        max_page = (exercise_count // exercises_per_page) + (1 if exercise_count % exercises_per_page > 0 else 0)

        # Verificar se existe algum exercício no nível
        if exercise_count > 0:
            page = st.slider("Escolha a página", min_value=0, max_value=max_page, step=1)
        else:
            page = 0  # Caso não haja exercícios, o slider será desabilitado

        start = page * exercises_per_page
        end = start + exercises_per_page
        exer_page = exercises[start:end]

        cols = st.columns(exercises_per_page)

        for i, exercise in enumerate(exer_page):
            with cols[i % exercises_per_page]:
                # Adicionando uma borda ao redor de cada exercício
                with st.container():
                    st.markdown(f"""
                    <div style='border: 2px solid #ddd; padding: 10px; border-radius: 8px; margin-bottom: 10px;'>
                    <p><strong>Exercício:</strong> {exercise[1]}</p>
                    <p><strong>Código:</strong> {exercise[2]}</p>
                    <p><strong>Markdown:</strong> {exercise[3]}</p>
                    <p><strong>Status:</strong> {'Feito' if exercise[4] == 1 else 'Não Feito'}</p>
                    """, unsafe_allow_html=True)

                    if exercise[4] == 0:
                        st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)  # Centraliza o botão
                        if st.button("Marcar como Feita", key=exercise[0]):
                            mark_as_done(exercise[0])
                            st.success(f"Exercício '{exercise[1]}' marcado como feito!")
                        st.markdown("</div>", unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.write("Nenhum exercício criado ainda.")
else:
    st.write("Nenhum nível encontrado. Por favor, crie um nível abaixo.")

# Criação de um novo nível
st.subheader("Criar Novo Nível")
new_level_name = st.text_input("Nome do novo nível")
if st.button("Criar Novo Nível") and new_level_name:
    create_level(new_level_name)

# Criação de um novo exercício
st.subheader("Criar Novo Exercício")
exercise_name = st.text_input("Nome do exercício")

# Listar as pastas de exercício para selecionar o caminho
level_dirs = list_exercise_directories()

# Verificar se há pastas e exibir as opções
if level_dirs:
    selected_code_path = st.selectbox("Escolha o caminho do arquivo .py", level_dirs)
    selected_markdown_path = st.selectbox("Escolha o caminho do arquivo .md", level_dirs)

    # Verificar os arquivos dentro das pastas selecionadas
    code_files = list_files_in_directory(os.path.join("exercícios", selected_code_path))
    markdown_files = list_files_in_directory(os.path.join("exercícios", selected_markdown_path))

    # Se não houver arquivos .py ou .md, oferecer a opção de criar
    if not code_files:
        st.write(f"Não há arquivos .py no diretório {selected_code_path}.")
        create_code_and_markdown_files(os.path.join("exercícios", selected_code_path), exercise_name)
    if not markdown_files:
        st.write(f"Não há arquivos .md no diretório {selected_markdown_path}.")
        create_code_and_markdown_files(os.path.join("exercícios", selected_markdown_path), exercise_name)

    if st.button("Criar Exercício") and exercise_name and selected_code_path and selected_markdown_path:
        code_path = os.path.join("exercícios", selected_code_path, f"{exercise_name}.py")
        markdown_path = os.path.join("exercícios", selected_markdown_path, f"{exercise_name}.md")
        create_exercise(selected_level_id, exercise_name, code_path, markdown_path)
else:
    st.write("Nenhuma pasta encontrada para selecionar. Certifique-se de que as pastas de exercício estão corretamente configuradas.")
