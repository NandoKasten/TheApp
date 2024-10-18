import streamlit as st



if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

mapping_demo = st.Page("pages/test/101_Mapping_Demo.py", title="Mapping Demo", icon=":material/dashboard:")
plotting_demo = st.Page("pages/test/102_Plotting_Demo.py", title="Plotting Demo", icon=":material/dashboard:s")
dataframe_demo = st.Page("pages/test/103_DataFrame_Demo.py", title="Data Frame Demo", icon=":material/bug_report:")


settings = st.Page("pages/settings/99_Settings.py", title="Settings", icon=":material/settings:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Tests": [mapping_demo, plotting_demo, dataframe_demo],
            "Tools": [settings],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()