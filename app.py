import streamlit as st
import random
import time
import streamlit.components.v1 as components

# --- 1. CONFIGURAZIONE ESTETICA "ATELIER" ---
st.set_page_config(page_title="Poeticamente", page_icon="🖋️", layout="wide", initial_sidebar_state="collapsed")

# CSS Avanzato per forzare l'eleganza del Club
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital@0;1&family=Lora:ital,wght@0,400;0,500;1,400&display=swap');
    
    /* Sfondo e Font Generale */
    .stApp {
        background-color: #fdfcfb !important;
        color: #1a1a1a !important;
        font-family: 'Lora', serif !important;
    }

    /* Titolo Centrale Elegante */
    .poetic-title {
        font-family: 'Playfair Display', serif;
        font-size: 4rem;
        text-align: center;
        color: #1a1a1a;
        margin-top: -50px;
        padding-bottom: 10px;
    }

    /* MESSAGGIO DI CORTESIA CLUB PREMIUM */
    .welcome-club {
        background-color: #ffffff;
        border: 1px solid #d4af37 !important;
        padding: 25px;
        border-radius: 2px; /* Linee più squadrate e professionali */
        text-align: center;
        font-family: 'Lora', serif !important;
        font-style: italic;
        font-size: 1.2rem;
        color: #1a1a1a;
        margin: 20px auto;
        max-width: 800px;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.1);
    }

    /* Personalizzazione Input e Bottoni */
    .stTextInput input, .stTextArea textarea {
        background-color: #ffffff !important;
        border: 1px solid #e0e0e0 !important;
        font-family: 'Lora', serif !important;
        font-size: 1.1rem !important;
    }

    .stButton button {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
        border-radius: 0px !important;
        border: none !important;
        font-family: 'Playfair Display', serif !important;
        transition: all 0.3s ease;
    }

    .stButton button:hover {
        background-color: #d4af37 !important;
        color: #ffffff !important;
    }

    /* Nascondi elementi Streamlit */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGICA DI STATO ---
if "conteggio_demo" not in st.session_state:
    st.session_state.conteggio_demo = 0
if "abbonato" not in st.session_state:
    st.session_state.abbonato = False

def contiene_linguaggio_vietato(testo):
    termini_vietati = ["anarchia", "insurrezione", "sovvertire", "abbasso lo stato", "disordine pubblico"]
    return any(term in testo.lower() for term in termini_vietati)

# --- 3. PAYWALL (BLOCCO DOPO 3 PROVE) ---
if st.session_state.conteggio_demo >= 3 and not st.session_state.abbonato:
    st.markdown("<h1 class='poetic-title'>Poeticamente</h1>", unsafe_allow_html=True)
    st.markdown("<div class='welcome-club'>Il tuo percorso demo nel Club è terminato. Per continuare a pubblicare e accedere alle funzioni esclusive, attiva il tuo profilo PREMIUM.</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        accetta = st.checkbox("Accetto i Termini di Servizio (Neutralità politica e tutela della proprietà)")
        if st.button("ACCEDI AL LIVELLO PREMIUM - 20€/MESE", use_container_width=True):
            if accetta:
                st.session_state.abbonato = True
                st.rerun()
    st.stop()

# --- 4. INTERFACCIA DESKTOP ---
st.markdown("<h1 class='poetic-title'>Poeticamente</h1>", unsafe_allow_html=True)

# Messaggio di cortesia visibile solo se non abbonato
if not st.session_state.abbonato:
    st.markdown("""
        <div class='welcome-club'>
            Benvenuto nel club dei poeti e scrittori, se il nostro sito ti affascina, accedi alle funzioni esclusive PREMIUM.
        </div>
    """, unsafe_allow_html=True)

col_scrittura, col_strumenti = st.columns([2, 1])

with col_scrittura:
    titolo = st.text_input("Titolo dell'opera", placeholder="Inserisci il titolo...")
    testo = st.text_area("Componi i tuoi versi", height=400, placeholder="L'ispirazione attende...")
    
    if contiene_linguaggio_vietato(testo):
        st.warning("⚠️ Nota del Club: Il linguaggio rilevato non rispetta la Policy di decoro e neutralità.")

with col_strumenti:
    st.markdown("### 🏛️ L'Atelier")
    if testo:
        sillabe = len(testo.split('\n')[-1].strip()) // 2
        st.metric("Metrica stimata", f"{sillabe} sillabe")
    
    st.divider()
    st.info(f"Prove demo effettuate: {st.session_state.conteggio_demo}/3")
    
    if st.button("🚀 PUBBLICA OPERA", use_container_width=True):
        if contiene_linguaggio_vietato(testo):
            st.error("Violazione Policy: Contenuto non compatibile con gli standard del Club.")
        elif not testo:
            st.warning("Inserisci del testo prima di pubblicare.")
        else:
            with st.spinner("Registrazione nel Registro dei Poeti..."):
                time.sleep(1.5)
                st.session_state.conteggio_demo += 1
                st.success(f"Opera n.{st.session_state.conteggio_demo} pubblicata!")
                time.sleep(1)
                st.rerun()

# --- 5. JS PER IL TOCCO DI CLASSE ---
components.html("""
<script>
    const area = window.parent.document.querySelectorAll('textarea')[0];
    area.style.border = 'none';
    area.style.borderBottom = '2px solid #d4af37';
    area.addEventListener('focus', () => {
        area.style.backgroundColor = '#fffaf0';
    });
</script>
""", height=0)