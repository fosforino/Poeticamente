import streamlit as st
import random
import time
from supabase import create_client, Client

# --- 1. CONNESSIONE DATABASE ---
URL_SUPABASE = st.secrets["SUPABASE_URL"]
KEY_SUPABASE = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(URL_SUPABASE, KEY_SUPABASE)

# --- 2. CONFIGURAZIONE PAGINA ED ESTETICA ---
st.set_page_config(page_title="Poeticamente", page_icon="✍️", layout="wide")
st.title("Poeticamente")
st.warning("🚧 Stiamo lavorando per voi: Poeticamente è attualmente in fase Beta Privata. L'accesso è riservato agli autori autorizzati.")
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display&family=EB+Garamond&display=swap');
    .stApp { background-color: #f5eedc; background-image: url("https://www.transparenttextures.com/patterns/cream-paper.png"); }
    [data-testid="stSidebar"] { background-color: #f0f2f6 !important; }
    .poesia-card {
        background: white; padding: 25px; border-radius: 12px; border-left: 6px solid #d4af37;
        margin-bottom: 15px; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); font-family: 'EB Garamond', serif;
    }
    </style>
    """, unsafe_allow_code_html=True)

# --- 3. BARRA LATERALE (NAVIGAZIONE E INFO) ---
st.sidebar.title("Poeticamente")   
if 'user_email' in st.session_state:
    st.sidebar.write(f"Poeta: **{st.session_state.user_email}**")

menu = st.sidebar.radio("Spostati in:", ["Lo Scrittoio", "La Bacheca Pubblica", "Gestisci Opere"])

# Spazio informativo Beta
st.sidebar.markdown("---")
st.sidebar.caption("🚀 **Versione 0.1-Beta**")
st.sidebar.info("L'app è in fase di rifinitura. I tuoi versi sono preziosi e protetti.")

if st.sidebar.button("Esci"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# --- LOGIN SIMBOLICO (In attesa di Auth reale) ---
if 'logged_in' not in st.session_state:
    st.title("Poeticamente")
    email = st.text_input("Inserisci la tua Email")
    codice = st.text_input("Codice (123456)", type="password")
    if st.button("Entra nella tua Stanza"):
        if codice == "123456": # Placeholder per futura sicurezza
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.rerun()
        else:
            st.error("Codice errato")
    st.stop()

# --- LOGICA DELLE SEZIONI (Placeholder) ---
if menu == "Lo Scrittoio":
    st.subheader("✍️ Crea o Modifica")
    titolo = st.text_input("Titolo")
    testo = st.text_area("Scrivi qui...", height=300)
    if st.button("SALVA SU POETICAMENTE"):
        data = {"titolo": titolo, "contenuto": testo, "autore": st.session_state.user_email}
        supabase.table("poesie").insert(data).execute()
        st.success("Versi custoditi con successo!")

elif menu == "La Bacheca Pubblica":
    st.subheader("📜 Opere della Community")
    res = supabase.table("poesie").select("*").execute()
    for p in res.data:
        st.markdown(f"""<div class='poesia-card'><h3>{p['titolo']}</h3><p>{p['contenuto']}</p>
                    <small>Scritto da: {p['autore']}</small></div>""", unsafe_allow_code_html=True)

elif menu == "Gestisci Opere":
    st.subheader("🛠️ La tua Stanza Privata")
    res = supabase.table("poesie").select("*").eq("autore", st.session_state.user_email).execute()
    for p in res.data:
        with st.expander(f"{p['titolo']}"):
            st.write(p['contenuto'])
            if st.button("Elimina", key=p['id']):
                supabase.table("poesie").delete().eq("id", p['id']).execute()
                st.rerun()