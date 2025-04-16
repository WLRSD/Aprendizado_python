import streamlit as st

if "role" not in st.session_state:
    st.session_state.role = "Página inicial"

ROLES = ["Página inicial", "Questões", "Avaliações", "Admin"]

# apenas um teste
def login():

    st.header("Logar em")
    role = st.selectbox("Escolha o usuário", ROLES)

    if st.button("acessar"):
        st.session_state.role = role
        st.rerun()


def logout():
    st.session_state.role = "Home"
    st.rerun()


role = st.session_state.role

logout_page = st.Page(logout, title="Sair da conta", icon=":material/logout:")
config = st.Page("config.py", title="Configuração", icon=":material/settings:")
questoes = st.Page(
    "request/questoes1.py",
    title="Questões",
    icon=":material/help:",
    default=(role == "Questões"),
)
questoes2 = st.Page(
    "request/questoes2.py", title="Questões", icon=":material/bug_report:"
)
avaliacoes = st.Page(
    "respond/avaliacoes1.py",
    title="Avaliações",
    icon=":material/healing:",
    default=(role == "Avaliações"),
)
avaliacoes2 = st.Page(
    "respond/avaliacoes2.py", title="Avaliações", icon=":material/handyman:"
)
admin1 = st.Page(
    "admin/admin1.py",
    title="Admin 1",
    icon=":material/person_add:",
    default=(role == "Admin"),
)
admin2 = st.Page("admin/admin2.py", title="Admin 2", icon=":material/security:")

conta = [logout_page, config]
questoes_paginas = [questoes, questoes2]
avaliacoes_paginas = [avaliacoes, avaliacoes2]
admin_paginas = [admin1, admin2]

st.title(st.session_state.role)
st.logo("images/image.png", icon_image="images/icon_blue.png")

page_dict = {}
if st.session_state.role in ["Questões", "Admin"]:
    page_dict["Questões"] = questoes_paginas
if st.session_state.role in ["Avaliações", "Admin"]:
    page_dict["Avaliações"] = avaliacoes_paginas
if st.session_state.role == "Admin":
    page_dict["Admin"] = admin_paginas

if len(page_dict) > 0:
    pg = st.navigation({"Account": conta} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()