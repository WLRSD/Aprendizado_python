import os
import streamlit as st

def file_exists(directory, filename):
    return os.path.exists(os.path.join(directory, filename))

def load_file_content(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Arquivo não encontrado: {filepath}"

def display_code_and_markdown(code_path, markdown_path):
    code_content = load_file_content(code_path)
    markdown_content = load_file_content(markdown_path)

    tab = st.radio("Escolha o conteúdo para visualizar", ("Código", "Markdown"), key="unique_key_for_radio")

    if tab == "Código":
        st.code(code_content, language="python")
    elif tab == "Markdown":
        st.markdown(markdown_content)

def list_exercise_directories():
    base_path = "exercícios"
    level_dirs = []
    
    if os.path.exists(base_path):
        level_dirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
        level_dirs.sort(key=lambda x: int(x.split()[-1]))  

    return level_dirs

def display_exercises():
    st.title("Gestão de Exercícios de Python")

    level_dirs = list_exercise_directories()
    
    if level_dirs:
        selected_level = st.selectbox("Escolha um nível", level_dirs)

        code_files = [f for f in os.listdir(f"exercícios/{selected_level}") if f.endswith(".py")]
        markdown_files = [f for f in os.listdir(f"exercícios/{selected_level}") if f.endswith(".md")]

        if code_files and markdown_files:
            selected_code_file = st.selectbox("Escolha o arquivo Python", code_files)
            selected_markdown_file = st.selectbox("Escolha o arquivo Markdown", markdown_files)

            code_path = os.path.join("exercícios", selected_level, selected_code_file)
            markdown_path = os.path.join("exercícios", selected_level, selected_markdown_file)

            display_code_and_markdown(code_path, markdown_path)
        else:
            st.write("Não há arquivos .py ou .md no diretório selecionado.")
    else:
        st.write("Nenhum nível encontrado. Por favor, crie um nível abaixo.")

display_exercises()
