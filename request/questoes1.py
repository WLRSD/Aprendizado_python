import streamlit as st

# Inicializa 'exercicios' e 'niveis' no session_state se não estiverem presentes
if "exercicios" not in st.session_state:
    st.session_state.exercicios = {"Fundamentos de Python": [], "Estruturas Condicionais": []}

if "niveis" not in st.session_state:
    st.session_state.niveis = ["Fundamentos de Python", "Estruturas Condicionais"]

# Função para exibir os níveis com as caixas clicáveis
def exibir_nivel_caixas():
    st.subheader("Escolha um nível de exercício")

    # Exibindo os níveis como caixas clicáveis
    for nivel in st.session_state.niveis:
        if st.button(nivel, key=nivel):  # A chave 'key' ajuda a evitar o erro de IDs duplicados
            st.session_state.selected_level = nivel
            st.session_state.exercicio_nome = ""  # Limpa o nome do exercício ao mudar de nível
            st.session_state.exercicio_criado = False  # Marca que o exercício não foi criado
            st.rerun()  # Recarrega a página

    # Exibindo os exercícios criados para o nível selecionado
    st.subheader("Exercícios Criados:")
    if st.session_state.selected_level:
        nivel_selecionado = st.session_state.selected_level
        exercicios_criados = st.session_state.exercicios.get(nivel_selecionado, [])
        
        if exercicios_criados:
            for exercicio in exercicios_criados:
                st.markdown(f"- {exercicio}")  # Exibe o exercício
        else:
            st.write("Nenhum exercício criado ainda.")

# Função para mostrar o input de exercício
def mostrar_input_exercicio(nivel):
    st.subheader(f"Digite o nome do exercício para o nível {nivel}:")
    
    nome_exercicio = st.text_input("Nome do exercício", value=st.session_state.get("exercicio_nome", ""))

    if st.button("Enviar") and nome_exercicio != "":
        nome_exercicio = nome_exercicio.lower()  # Converte o nome do exercício para minúsculo
        if nome_exercicio in [ex.lower() for ex in st.session_state.exercicios[nivel]]:
            st.error(f"O exercício '{nome_exercicio}' já foi criado para o nível {nivel}.")
        else:
            st.session_state.exercicios[nivel].append(nome_exercicio)  # Adiciona o novo exercício
            st.session_state.exercicio_nome = nome_exercicio
            st.session_state.exercicio_criado = True  # Marca que o exercício foi criado
            st.success(f"Exercício '{nome_exercicio}' criado com sucesso!")

# Layout do título e botão "Criar" no topo
col1, col2 = st.columns([5, 1])

with col1:
    st.title("Questões")

with col2:
    if st.button("Criar Novo Nível"):
        # Quando o botão "Criar Novo Nível" for clicado, exibe um campo de texto para adicionar um novo nível
        st.session_state.selected_level = None  # Limpa o nível selecionado
        novo_nivel = st.text_input("Digite o nome do novo nível:")
        if st.button("Adicionar Novo Nível") and novo_nivel:
            novo_nivel = novo_nivel.strip()  # Limpeza do nome do nível
            if novo_nivel not in st.session_state.niveis:
                st.session_state.niveis.append(novo_nivel)  # Adiciona o novo nível à lista
                st.session_state.exercicios[novo_nivel] = []  # Cria a chave para os exercícios desse nível
                st.success(f"Nível '{novo_nivel}' criado com sucesso!")  # Mensagem de sucesso
                st.experimental_rerun()  # Recarrega a página para refletir o novo nível
            else:
                st.error(f"O nível '{novo_nivel}' já existe.")

# Se o usuário não tiver escolhido um nível, exibe a tela inicial
if "selected_level" not in st.session_state:
    st.session_state.selected_level = None  # Inicializa o valor, caso não esteja presente ainda

# Se o usuário não estiver logado, exibe a tela inicial de login
if not st.session_state.selected_level:
    exibir_nivel_caixas()  # Exibe os botões de seleção de nível
else:
    st.write(f"Você está logado no nível: {st.session_state.selected_level}")

    # Exibe os exercícios criados para o nível selecionado
    st.subheader("Exercícios Criados:")
    for exercicio in st.session_state.exercicios[st.session_state.selected_level]:
        st.markdown(f"- {exercicio}")  # Exibe o exercício

    # Mostra o nome do exercício ou exibe que nenhum foi selecionado
    if st.session_state.exercicio_criado:
        st.write(f"Nome do exercício: {st.session_state.exercicio_nome}")
    else:
        mostrar_input_exercicio(st.session_state.selected_level)

    # O botão "Voltar para escolha do nível" deve estar disponível em todas as etapas
    if st.button("Voltar para escolha do nível"):
        st.session_state.pop("selected_level", None)
        st.session_state.pop("exercicio_nome", None)
        st.session_state.pop("exercicio_criado", None)
        st.rerun()  # Recarrega a página
