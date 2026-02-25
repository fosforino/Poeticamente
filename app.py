import streamlit as st
import time
import random
import streamlit.components.v1 as components
from supabase import create_client, Client

# --- 1. CONFIGURAZIONE SUPABASE ---
URL = "https://eeavavlfgeeusijiljfw.supabase.co"
KEY = "sb_publishable_PP-gOScRnNcN9JiD4uN4lQ_hCN0xL7j"
supabase: Client = create_client(URL, KEY)

# --- 2. CONFIGURAZIONE ESTETICA "PERGAMENA" ---
st.set_page_config(page_title="Poeticamente", page_icon="🖋️", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Playfair+Display:ital,wght@0,600;1,600&display=swap');
    
    .stApp {
        background-color: #fdf5e6 !important;
        background-image: radial-gradient(#f4e4bc 1px, transparent 1px) !important;
        background-size: 20px 20px !important;
        color: #2b1d0e !important;
        font-family: 'EB Garamond', serif !important;
    }

    .poetic-title {
        font-family: 'Playfair Display', serif;
        font-size: 4.5rem;
        text-align: center;
        color: #1a1a1a;
        margin-top: -40px;
    }

    .welcome-club {
        background-color: rgba(255, 255, 255, 0.5);
        border: 1px solid #d4af37 !important;
        padding: 30px;
        text-align: center;
        font-style: italic;
        font-size: 1.4rem;
        margin: 25px auto;
        max-width: 850px;
    }

    .stButton button {
        background-color: #2b1d0e !important;
        color: #fdf5e6 !important;
        border: 1px solid #d4af37 !important;
        font-family: 'Playfair Display', serif !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        padding: 10px 25px !important;
    }

    .stTextInput input, .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.3) !important;
        border: none !important;
        border-bottom: 1px solid #d4af37 !important;
        font-family: 'EB Garamond', serif !important;
        font-size: 1.3rem !important;
    }

    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. FUNZIONI DATABASE ---
def conta_opere_demo():
    try:
        res = supabase.table("Poesie").select("id", count="exact").eq("tipo_account", "demo").execute()
        return res.count if res.count is not None else 0
    except Exception:
        return 0

def pubblica_opera(titolo, versi):
    data = {
        "titolo": titolo,
        "versi": versi,
        "tipo_account": "demo",
        "autore": "Poeta_Anonimo",
        "likes": 0
    }
    try:
        supabase.table("Poesie").insert(data).execute()
        return True
    except Exception as e:
        st.error(f"Errore di inchiostrazione: {e}")
        return False

# --- 4. INTERFACCIA E LOGICA DI ACCESSO ---
st.markdown("<h1 class='poetic-title'>Poeticamente</h1>", unsafe_allow_html=True)

conteggio_reale = conta_opere_demo()

if conteggio_reale >= 3:
    st.markdown("<div class='welcome-club'>Il tuo tempo nell'Atelier gratuito è terminato. <br>Accedi al livello Premium per continuare a scrivere nel Registro.</div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Quota di mantenimento: 20€/mese</p>", unsafe_allow_html=True)
    if st.button("ATTIVA ABBONAMENTO PREMIUM", use_container_width=True):
        st.info("Reindirizzamento al sistema di pagamento Stripe...")
    st.stop()

st.markdown("<div class='welcome-club'>Benvenuto nel club dei poeti. Ti restano " + str(3 - conteggio_reale) + " pubblicazioni gratuite.</div>", unsafe_allow_html=True)

col_scrit, col_stat = st.columns([2, 1])

with col_scrit:
    tit_inp = st.text_input("Titolo dell'Opera")
    ver_inp = st.text_area("I tuoi versi", height=400)

with col_stat:
    st.markdown("### 📜 Archivio Storico")
    st.metric("Opere Demo Presenti", conteggio_reale)
    
    if st.button("🚀 PUBBLICA NELL'ALBO", use_container_width=True):
        if tit_inp and ver_inp:
            with st.spinner("Inchiostrazione in corso..."):
                if pubblica_opera(tit_inp, ver_inp):
                    st.success("Opera salvata permanentemente.")
                    time.sleep(1)
                    st.rerun()
        else:
            st.warning("Completa la tua opera prima di pubblicare.")