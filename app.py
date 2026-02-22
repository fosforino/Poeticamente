import streamlit as st
import random
import time

# --- CONFIGURAZIONE FISCALE E BRAND ---
NOME_APP = "Poeticamente"
MODALITA_COMMERCIALE = False  # Cambiare in True solo dopo apertura P.IVA

# --- LOGICA DI SICUREZZA E TEST (DIETRO LE QUINTE) ---
def registra_interesse_nel_db(funzione, email):
    # Qui il codice simula il salvataggio. 
    # Quando collegheremo Supabase, i dati andranno nella tabella "Interesse_Premium"
    time.sleep(1) # Simula caricamento professionale
    return True

# --- INTERFACCIA UTENTE ---
st.set_page_config(page_title=NOME_APP, page_icon="🖋️", layout="wide")

# Sidebar
st.sidebar.title(f"✨ {NOME_APP}")
st.sidebar.info("Versione: 1.0.0-Beta (Sperimentale)")
profilo = st.sidebar.selectbox("Tipo Profilo", ["Curioso (Free)", "Ambizioso (Premium)"])

# Header
st.title(f"Benvenuto su {NOME_APP}")
st.subheader("La tua opera merita una firma eterna.")

# --- AREA EDITOR ---
st.divider()
col_scrittura, col_strumenti = st.columns([2, 1])

with col_scrittura:
    titolo_opera = st.text_input("Titolo della tua opera", placeholder="Es: Il risveglio dei versi")
    testo_opera = st.text_area("Componi qui", height=400, placeholder="Scrivi i tuoi versi...")

with col_strumenti:
    st.markdown("### 🛠️ Strumenti Professionali")
    
    # Feature Gating: mostriamo i servizi ma li blocchiamo per testare i clic
    st.button("🎨 Font Editoriali (Premium)", use_container_width=True, on_click=lambda: st.session_state.update({"click_premium": "Font Editoriali"}))
    
    st.button("🖋️ Firma Digitale Legale (Premium)", use_container_width=True, on_click=lambda: st.session_state.update({"click_premium": "Firma Digitale"}))
    
    st.button("📧 Certificato via Email (Premium)", use_container_width=True, on_click=lambda: st.session_state.update({"click_premium": "Invio Certificato"}))

# --- LOGICA SMOKE TEST (IL FILTRO) ---
if "click_premium" in st.session_state:
    st.divider()
    with st.container():
        st.warning(f"### 🚀 Funzione '{st.session_state.click_premium}' in fase di rilascio")
        st.write("""
            Per garantirti la massima **tutela legale e fiscale**, stiamo attivando le procedure di certificazione. 
            Non vogliamo passi falsi: il servizio sarà disponibile a breve con garanzia di valore giudiziario.
        """)
        
        # Il CAPTCHA Logico
        if 'n1' not in st.session_state:
            st.session_state.n1 = random.randint(1, 10)
            st.session_state.n2 = random.randint(1, 10)
            st.session_state.risultato_corretto = st.session_state.n1 + st.session_state.n2

        col_mail, col_captcha = st.columns(2)
        with col_mail:
            email_interessato = st.text_input("Tienimi informato (tua email):")
        with col_captcha:
            risposta_captcha = st.number_input(f"Sei umano? Quanto fa {st.session_state.n1} + {st.session_state.n2}?", step=1)

        if st.button("Inseriscimi nella lista d'attesa prioritaria"):
            if risposta_captcha == st.session_state.risultato_corretto:
                if email_interessato:
                    successo = registra_interesse_nel_db(st.session_state.click_premium, email_interessato)
                    if successo:
                        st.success("Ottimo! Ti abbiamo inserito tra i 'Poeti Fondatori'. Riceverai una notifica al lancio.")
                        # Reset per evitare spam
                        del st.session_state.click_premium
                        del st.session_state.n1
                else:
                    st.error("Inserisci un'email valida.")
            else:
                st.error("Errore di sicurezza. Il calcolo non è corretto.")

# --- FOOTER ---
st.divider()
st.caption(f"© 2026 {NOME_APP} | Ricerca di mercato attiva | Nessun dato fiscale richiesto in questa fase.")