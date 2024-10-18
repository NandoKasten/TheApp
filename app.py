import streamlit as st
import json

st.set_page_config(
    page_title="The App!",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="auto",
)


# Funktion zum Laden der Sprachdatei
def load_language_file():
    with open('languages.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# Funktion zum Abrufen des Textes basierend auf der gewählten Sprache
def get_text(key, lang):
    # Standardmäßig auf Englisch zurückgreifen
    return languages.get(lang, languages['en']).get(key, languages['en'].get(key, ""))

# Lade die Sprachdatei
languages = load_language_file()

selected_language = "de"
st.session_state.language = selected_language  # Speichere die gewählte Sprache im Session-State

pg = st.navigation([st.Page("pages/99_Settings.py"), st.Page("101_Mapping_Demo.py")])
pg.run()

def main():
    # --- Custom CSS ---
    st.markdown("""
        <style>
            /* Sidebar background color */
            .css-1d391kg, .css-1d391kg .css-1v3fvcr {
                background-color: #742774 !important;
            }
            /* Sidebar text color */
            .css-1d391kg, .css-1d391kg * {
                color: white !important;
            }
            /* Header color */
            .css-10trblm {
                color: #742774 !important;
            }
            /* Blur effect for API key */
            .blur {
                filter: blur(5px);
                transition: filter 0.3s;
            }
            .blur:hover {
                filter: blur(0);
            }
        </style>
    """, unsafe_allow_html=True)
   

    with st.sidebar:
        st.title(get_text("sidebarTitle", st.session_state.language))
        st.write(get_text("sidebarText1", st.session_state.language))
        st.write(get_text("sidebarText2", st.session_state.language))
        st.write(get_text("sidebarText3", st.session_state.language))

    st.header("Hallo aus dem Titel")
    st.write("Hallo aus dem write")

    st.markdown(f"""<h1 style="text-align: center; color: #742774;">🖥️ <i> {get_text("welcome", st.session_state.language)} </i> 💬</h1>""", unsafe_allow_html=True)


# Letztes Kommando

if __name__ == "__main__":
    main()