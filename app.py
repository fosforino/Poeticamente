import streamlit as st
import random
import time
import streamlit.components.v1 as components

# --- 1. CONFIGURAZIONE ESTETICA "PERGAMENA" ---
st.set_page_config(page_title="Poeticamente", page_icon="🖋️", layout="wide", initial_sidebar_state="collapsed")

# CSS per trasformare l'app in un Atelier di lusso
st.markdown("""
    <style>
    /* Importazione Font Letterari */
    @import url('https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Playfair+Display:ital,wght@0,600;1,600&display=swap');
    
    /* Sfondo Effetto Carta Antica */
    .stApp {
        background-color: #fdf5e6 !important; /* Avorio invecchiato */
        background-image: radial-gradient(#f4e4bc 1px, transparent 1px) !important;
        background-size: 20px 20px !important;
        color: #2b1d0e !important; /* Inchiostro Seppia */
        font-family: 'EB Garamond', serif !important;
    }

    /* Titolo Monumentale */
    .poetic-title {
        font-family: 'Playfair Display', serif;
        font-size: 4.5rem;
        text-align: center;
        color: #1a1a1a;
        margin-top: -40px;
        letter-spacing: -1px;
    }

    /* Messaggio di Cortesia Premium */
    .welcome-club {
        background-color: rgba(255, 255, 255, 0.5);
        border: 1px solid #d4af37 !important; /* Bordo Oro Antico */
        padding: 30px;
        text-align: center;
        font-family: 'EB Garamond', serif !important;
        font-style: italic;
        font-size: 1.4rem;
        color: #2b1d0e;
        margin: 25px auto;
        max-width: 850px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    }

    /* Input e Area di Scrittura (Stile Manoscritto) */
    .stTextInput input, .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.3) !important;
        border: none !important;
        border-bottom: 1px solid #d4af37 !important;
        font-family: 'EB Garamond', serif !important;
        font-size: 1.3rem !important;
        color: #2b1d0e !important;
    }

    /* Bottone Istituzionale */
    .stButton button {
        background-color: #2b1d0e !important;
        color: #fdf5e6 !important;
        border-radius: 0px !important;
        border: 1px solid #d4af37 !important;
        font-family: 'Playfair Display', serif !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        padding: 10px 25px !important;
        transition: all 0.4s ease;
    }

    .stButton button:hover {
        background-color: #d4af37 !important;
        color: #2b1d0e !important;
    }

    /* Nascondi Interfaccia Standard */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGICA DI STATO E POLICY ---
if "conteggio_demo" not in st.session_state:
    st.session_state.conteggio_demo = 0
if "abbonato" not in st.session_state:
    st.session_state.abbonato = False

def contiene_linguaggio_vietato(testo):
    # Policy di decoro e neutralità concordata
    termini_vietati = ["anarchia", "insurrezione", "sovvertire", "abbasso lo stato", "disordine pubblico"]
    return any(term in testo.lower() for term in termini_vietati)

# --- 3. PAYWALL PREMIUM (20€/MESE) ---
if st.session_state.conteggio_demo >= 3 and not st.session_state.abbonato:
    st.markdown("<h1 class='poetic-title'>Poeticamente</h1>", unsafe_allow_html=True)
    st.markdown("<div class='welcome-club'>Il tuo tempo nell'Atelier gratuito è terminato. <br>Accedi al livello Premium per continuare a pubblicare nel registro del Club.</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("<p style='text-align:center;'>Quota di mantenimento: 20€/mese</p>", unsafe_allow_html=True)
        if st.button("ATTIVA ABBONAMENTO PREMIUM", use_container_width=True):
            st.session_state.abbonato = True
            st.rerun()
    st.stop()

# --- 4. INTERFACCIA PRINCIPALE ---
st.markdown("<h1 class='poetic-title'>Poeticamente</h1>", unsafe_allow_html=True)

if not st.session_state.abbonato:
    st.markdown("<div class='welcome-club'>Benvenuto nel club dei poeti e scrittori, se il nostro sito ti affascina, accedi alle funzioni esclusive PREMIUM.</div>", unsafe_allow_html=True)

col_scrittura, col_info = st.columns([2, 1])

with col_scrittura:
    st.text_input("Titolo dell'Opera", placeholder="Inserisci il titolo...")
    testo_poesia = st.text_area("I tuoi versi", height=450, placeholder="Inizia a comporre...")
    
    if contiene_linguaggio_vietato(testo_poesia):
        st.warning("⚠️ Nota del Club: Il linguaggio rilevato non rispetta la Policy di decoro e neutralità.")

with col_info:
    st.markdown("### 📜 L'Atelier")
    st.write("Ogni parola è un solco nella pergamena del tempo.")
    st.divider()
    st.metric("Pubblicazioni Demo", f"{st.session_state.conteggio_demo}/3")
    
    if st.button("🚀 PUBBLICA OPERA", use_container_width=True):
        if contiene_linguaggio_vietato(testo_poesia):
            st.error("Violazione Policy: Contenuto non compatibile con gli standard del Club.")
        elif not testo_poesia:
            st.warning("La pergamena è ancora vuota.")
        else:
            with st.spinner("Inchiostrazione in corso..."):
                time.sleep(2)
                st.session_state.conteggio_demo += 1
                st.rerun()