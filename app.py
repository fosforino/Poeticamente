import streamlit as st
import random
import time
import streamlit.components.v1 as components

# --- CONFIGURAZIONE BRAND ---
NOME_APP = "Poeticamente"
PREZZO_MENSILE = "20€"
LIMITE_DEMO = 3

# --- 1. ESTETICA "STELLATA" (CSS & DESIGN) ---
st.set_page_config(page_title=NOME_APP, page_icon="🖋️", layout="wide", initial_sidebar_state="collapsed")

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital@0;1&family=Lora:wght@400;500&display=swap');
    
    .stApp {{ background-color: #fdfcfb; color: #2c3e50; font-family: 'Lora', serif; }}
    
    .poetic-title {{ 
        font-family: 'Playfair Display', serif; 
        font-size: 3.5rem; 
        text-align: center; 
        color: #1a1a1a; 
        margin-bottom: 0.5rem; 
    }}
    
    /* Messaggio di Cortesia Premium */
    .welcome-club {{
        background-color: #ffffff;
        border: 1px solid #d4af37;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        font-style: italic;
        color: #1a1a1a;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }}

    .premium-badge {{ 
        background-color: #d4af37; 
        color: white; 
        padding: 5px 15px; 
        border-radius: 20px; 
        font-size: 0.8rem; 
        font-weight: bold; 
        text-transform: uppercase; 
    }}

    .stTextArea textarea {{ 
        background-color: transparent !important; 
        border: 1px solid #e0e0e0 !important; 
        border-radius: 10px !important; 
        font-size: 1.2rem !important; 
    }}
    
    #MainMenu, footer, header {{visibility: hidden;}}
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

# --- 3. PAYWALL (DOPO 3 PROVE) ---
if st.session_state.conteggio_demo >= LIMITE_DEMO and not st.session_state.abbonato:
    st.markdown("<h1 class='poetic-title'>L'Esclusività ha un Valore</h1>", unsafe_allow_html=True)
    st.divider()
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("<div style='text-align: center; font-size: 5rem;'>🏛️</div>", unsafe_allow_html=True)
    with col2:
        st.subheader("Il tuo percorso demo è terminato.")
        st.write(f"Per continuare a far parte del nostro club e accedere alle funzioni editoriali avanzate, attiva il tuo abbonamento.")
        st.markdown(f"**Investimento: {PREZZO_MENSILE}/mese**")
        
        accetta = st.checkbox("Accetto i Termini di Servizio (Neutralità politica e tutela della proprietà)")
        if st.button("Sottoscrivi e Continua"):
            if accetta:
                st.session_state.abbonato = True
                st.rerun()
    st.stop()

# --- 4. DESKTOP DI SCRITTURA ---
st.markdown(f"<h1 class='poetic-title'>{NOME_APP}</h1>", unsafe_allow_html=True)

# MESSAGGIO DI CORTESIA (EVIDENZIATO SOLO PER I NON ANCORA ABBONATI)
if not st.session_state.abbonato:
    st.markdown("""
        <div class='welcome-club'>
            Benvenuto nel club dei poeti e scrittori, se il nostro sito ti affascina, accedi alle funzioni esclusive PREMIUM.
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("<p style='text-align: center;'><span class='premium-badge'>Membro del Club</span></p>", unsafe_allow_html=True)

col_scrittura, col_strumenti = st.columns([2, 1])

with col_scrittura:
    titolo = st.text_input("Titolo dell'opera", placeholder="Titolo...")
    testo = st.text_area("I tuoi versi", height=400, placeholder="Inizia a comporre...")
    
    if contiene_linguaggio_vietato(testo):
        st.warning("⚠️ Nota del Club: Il linguaggio rilevato non è conforme alla nostra Policy di decoro e neutralità.")

with col_strumenti:
    st.markdown("### 🏛️ Atelier")
    if testo:
        # Metrica semplificata per il test
        sillabe = len(testo.split('\n')[-1].strip()) // 2
        st.metric("Metrica Verso", f"{sillabe} sillabe")
    
    st.divider()
    if st.button("🚀 PUBBLICA OPERA", type="primary", use_container_width=True):
        if contiene_linguaggio_vietato(testo):
            st.error("Violazione Policy: Contenuto non pubblicabile.")
        elif not testo:
            st.warning("L'inchiostro è ancora nel calamaio...")
        else:
            with st.spinner("Registrazione opera nel Registro Fondatori..."):
                time.sleep(1.5)
                st.session_state.conteggio_demo += 1
                st.success("Opera registrata!")
                time.sleep(1)
                st.rerun()

# --- 5. JS TOCCo DI CLASSE ---
components.html("""
<script>
    const area = window.parent.document.querySelectorAll('textarea')[0];
    area.addEventListener('focus', () => {
        area.style.boxShadow = '0 0 15px rgba(212, 175, 55, 0.2)';
        area.style.borderColor = '#d4af37';
    });
</script>
""", height=0)