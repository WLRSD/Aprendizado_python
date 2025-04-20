import os
import streamlit as st

# Função para verificar se um arquivo existe
def file_exists(directory, filename):
    return os.path.exists(os.path.join(directory, filename))

# Função para carregar o conteúdo de um arquivo
def load_file_content(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Arquivo não encontrado: {filepath}"

# Função para exibir o código ou markdown do exercício
def display_code_and_markdown(code_path, markdown_path):
    code_content = load_file_content(code_path)
    markdown_content = load_file_content(markdown_path)

    # Criando um radio para alternar entre código e markdown
    tab = st.radio("Escolha o conteúdo para visualizar", ("Código", "Markdown"), key="unique_key_for_radio")

    if tab == "Código":
        st.code(code_content, language="python")
    elif tab == "Markdown":
        st.markdown(markdown_content)

# Função para listar as pastas de exercício
def list_exercise_directories():
    base_path = "exercícios"
    level_dirs = []
    
    # Verifica se o caminho base existe
    if os.path.exists(base_path):
        # Lista todos os diretórios dentro de "exercicios"
        level_dirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
        
        # Ordenar os diretórios de forma numérica (do nível 1 ao nível 10)
        level_dirs.sort(key=lambda x: int(x.split()[-1]))  # Ordena pelos números dos níveis

    return level_dirs

# Função para exibir a página de exercícios
def display_exercises():
    st.title("Gestão de Exercícios de Python")

    # Listando as pastas de exercício
    level_dirs = list_exercise_directories()
    
    if level_dirs:
        # Se houver pastas, pedir para o usuário escolher a pasta
        selected_level = st.selectbox("Escolha um nível", level_dirs)

        # Listar arquivos dentro do diretório escolhido
        code_files = [f for f in os.listdir(f"exercícios/{selected_level}") if f.endswith(".py")]
        markdown_files = [f for f in os.listdir(f"exercícios/{selected_level}") if f.endswith(".md")]

        # Verificar se os arquivos .py e .md existem
        if code_files and markdown_files:
            selected_code_file = st.selectbox("Escolha o arquivo Python", code_files)
            selected_markdown_file = st.selectbox("Escolha o arquivo Markdown", markdown_files)

            code_path = os.path.join("exercícios", selected_level, selected_code_file)
            markdown_path = os.path.join("exercícios", selected_level, selected_markdown_file)

            # Exibir código e markdown
            display_code_and_markdown(code_path, markdown_path)
        else:
            st.write("Não há arquivos .py ou .md no diretório selecionado.")
    else:
        st.write("Nenhum nível encontrado. Por favor, crie um nível abaixo.")

# Chamar a função para exibir os exercícios
display_exercises()
