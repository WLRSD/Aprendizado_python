import streamlit as st

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "Questões", "Avaliações", "Admin"]


def login():

    st.header("Logar em")
    role = st.selectbox("Escolha o usuário", ROLES)

    if st.button("acessar"):
        st.session_state.role = role
        st.rerun()


def logout():
    st.session_state.role = None
    st.rerun()


role = st.session_state.role

logout_page = st.Page(logout, title="Sair da conta", icon=":material/logout:")
settings = st.Page("config.py", title="Configuração", icon=":material/settings:")
request_1 = st.Page(
    "request/request_1.py",
    title="Questões",
    icon=":material/help:",
    default=(role == "Questões"),
)
request_2 = st.Page(
    "request/request_2.py", title="Questões", icon=":material/bug_report:"
)
respond_1 = st.Page(
    "respond/respond_1.py",
    title="Avaliações",
    icon=":material/healing:",
    default=(role == "Avaliações"),
)
respond_2 = st.Page(
    "respond/respond_2.py", title="Avaliações", icon=":material/handyman:"
)
admin_1 = st.Page(
    "admin/admin_1.py",
    title="Admin 1",
    icon=":material/person_add:",
    default=(role == "Admin"),
)
admin_2 = st.Page("admin/admin_2.py", title="Admin 2", icon=":material/security:")

account_pages = [logout_page, settings]
request_pages = [request_1, request_2]
respond_pages = [respond_1, respond_2]
admin_pages = [admin_1, admin_2]

st.title("Login")
st.logo("images/image.png", icon_image="images/icon_blue.png")

page_dict = {}
if st.session_state.role in ["Questões", "Admin"]:
    page_dict["Questões"] = request_pages
if st.session_state.role in ["Avaliações", "Admin"]:
    page_dict["Avaliações"] = respond_pages
if st.session_state.role == "Admin":
    page_dict["Admin"] = admin_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()