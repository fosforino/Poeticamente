import streamlit as st
from Pages import Home, Scrittoio, Bacheca
import os

# --- CONFIGURAZIONE STREAMLIT ---
st.set_page_config(
    page_title="Poeticamente", 
    page_icon="🖋️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- STILE CSS GLOBALE (L'ANIMA DI POETICAMENTE) ---
def apply_global_style():
    st.markdown("""
    <style>
        /* Importazione Font */
        @import url('https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Playfair+Display:ital,wght@0,600;1,600&display=swap');

        /* Sfondo Pergamena Totale */
        .stApp, [data-testid="stSidebar"] { 
            background-color: #fdf5e6 !important; 
            color: #3e2723 !important; 
            font-family: 'EB Garamond', serif !important; 
        }

        /* Sidebar Styling */
        [data-testid="stSidebarContent"] {
            background-color: #f5f1e8 !important;
            border-right: 1px solid #d7ccc8;
        }

        /* Titolo Poetico */
        .poetic-title { 
            font-family: 'Playfair Display', serif; 
            font-size: 3.5rem; 
            text-align: center; 
            color: #3e2723; 
            margin-top: -10px;
            margin-bottom: 10px;
        }

        /* Bottoni Inchiostro e Oro */
        div.stButton > button { 
            background-color: #3e2723 !important; 
            color: #fdf5e6 !important; 
            border: 1px solid #c19a6b !important; 
            font-family: 'Playfair Display', serif !important; 
            transition: 0.3s all ease;
            border-radius: 8px !important;
        }
        
        div.stButton > button:hover {
            background-color: #c19a6b !important; 
            color: #3e2723 !important; 
            border-color: #3e2723 !important;
        }

        /* Codice d'Onore Box */
        .codice-onore {
            background-color: #f5f1e8;
            padding: 15px;
            border-left: 5px solid #3e2723;
            border-radius: 4px;
            font-style: italic;
            margin: 15px 0;
        }

        /* Centrare le immagini */
        .centered-image {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

def esegui_logout():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

apply_global_style()

# Verifica se l'immagine esiste (rinominala come 'logo.png' o carica il tuo file)
path_icona = "image_eda7ff.png" 

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    # --- SCHERMATA DI LOGIN ---
    col_logo_1, col_logo_2, col_logo_3 = st.columns([1, 0.8, 1])
    with col_logo_2:
        if os.path.exists(path_icona):
            st.image(path_icona, use_container_width=True)
    
    st.markdown("<h1 class='poetic-title'>Poeticamente</h1>", unsafe_allow_html=True)
    
    col_mid_1, col_mid_2, col_mid_3 = st.columns([1, 1.5, 1])
    
    with col_mid_2:
        st.markdown("<h3 style='text-align: center; font-family: Playfair Display;'>Identificazione del Poeta</h3>", unsafe_allow_html=True)
        
        nuovo_pseudo = st.text_input("Scegli il tuo Pseudonimo:")
        password_segreta = st.text_input("Chiave d'Accesso:", type="password")
        
        st.markdown("""
        <div class='codice-onore'>
            <strong>📜 Codice d'Onore:</strong><br>
            Prometto di onorare l'arte della parola, di rispettare gli altri poeti 
            e di non affidare il mio cuore a fredde automazioni.
        </div>
        """, unsafe_allow_html=True)
        
        accetto_codice = st.checkbox("Giuro solennemente di rispettarlo")
        captcha_input = st.text_input("Completa il verso: 'Nel mezzo del cammin di nostra...'")

        if st.button("Entra nello Scrittoio"):
            if (nuovo_pseudo.strip() and 
                password_segreta == "Ermetico_2026" and 
                accetto_codice and 
                captcha_input.strip().lower() == "vita"):
                
                st.session_state.authenticated = True
                st.session_state.utente = nuovo_pseudo.strip()
                st.rerun()
            else:
                st.error("L'accesso è negato. Verifica la Chiave o la sfida.")
    st.stop()

# --- INTERFACCIA PRINCIPALE ---
# Mostra l'icona anche nella sidebar
with st.sidebar:
    if os.path.exists(path_icona):
        st.image(path_icona, width=150)
    st.markdown(f"<h2 style='text-align: center;'>Poeta:<br>{st.session_state.utente}</h2>", unsafe_allow_html=True)
    st.markdown("---")

page = st.sidebar.radio("Scegli la tua meta:", ["Home", "Scrittoio", "Bacheca"])

st.sidebar.markdown("<br><br>", unsafe_allow_html=True)
if st.sidebar.button("Congeda il Profilo"):
    esegui_logout()

# Caricamento Pagine
if page == "Home": 
    Home.show()
elif page == "Scrittoio": 
    Scrittoio.show()
elif page == "Bacheca": 
    Bacheca.show()