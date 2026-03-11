import streamlit as st
from supabase import create_client, Client

# --- CONNESSIONE SUPABASE ---
url: str = st.secrets["SUPABASE_URL"]
key: str = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(url, key)

def apply_aesthetic_style():
    """Applica l'estetica 'Cervello-Pergamena-Stilografica' allo Scrittoio."""
    st.markdown(
        """
        <style>
        /* Sfondo generale coordinato con App.py */
        .stApp {
            background-color: #fdf5e6 !important;
        }

        /* Il 'Foglio' dello Scrittoio */
        .stTextArea textarea, .stTextInput input {
            background-color: #fffaf0 !important;
            border: 1px solid #d7ccc8 !important;
            font-family: 'EB Garamond', serif !important;
            font-size: 1.2rem !important;
            color: #3e2723 !important;
            line-height: 1.6 !important;
            border-radius: 4px !important;
            box-shadow: inset 1px 1px 5px rgba(0,0,0,0.02) !important;
        }

        /* Focus sugli input: colore bronzo come la stilografica */
        .stTextArea textarea:focus, .stTextInput input:focus {
            border-color: #c19a6b !important;
            box-shadow: 0 0 5px #c19a6b !important;
        }

        /* Titoli e Testi */
        h1, h2, h3, h4 {
            font-family: 'Playfair Display', serif !important;
            color: #3e2723 !important;
        }

        /* I contenitori delle opere salvate (Effetto pergamena singola) */
        .stContainer {
            background-color: #f5f1e8 !important;
            padding: 25px !important;
            border-radius: 2px !important;
            border-left: 3px solid #c19a6b !important;
            margin-bottom: 25px !important;
            box-shadow: 3px 3px 10px rgba(0,0,0,0.05) !important;
        }

        /* Pulsanti stile Inchiostro */
        div.stButton > button {
            background-color: #3e2723 !important;
            color: #fdf5e6 !important;
            border: 1px solid #c19a6b !important;
            font-family: 'Playfair Display', serif !important;
            border-radius: 5px !important;
            transition: 0.3s all ease !important;
        }

        div.stButton > button:hover {
            background-color: #c19a6b !important;
            color: #3e2723 !important;
        }

        /* Divider elegante */
        hr {
            border: 0;
            height: 1px;
            background-image: linear-gradient(to right, rgba(193, 154, 107, 0), rgba(193, 154, 107, 0.75), rgba(193, 154, 107, 0));
            margin: 30px 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def show():
    apply_aesthetic_style()
    
    # Titolo con richiamo grafico
    st.markdown("<h1 style='text-align: center;'>Lo Scrittoio di Poeticamente ✒️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-style: italic; color: #8d6e63; font-family: EB Garamond;'>Intingi la piuma nel tuo pensiero e lascia che il verso scorra sulla carta.</p>", unsafe_allow_html=True)
    
    # --- CREAZIONE OPERA ---
    # Usiamo un layout pulito senza expander pesante se possibile, o personalizziamolo
    with st.container():
        st.markdown("### 📝 Componi una nuova Opera")
        titolo = st.text_input("Titolo dell'Opera:", key="new_titolo", placeholder="Es: Il Risveglio del Pensiero")
        testo = st.text_area("Versi:", height=250, key="new_testo", placeholder="Scrivi qui i tuoi versi...")
        url_immagine = st.text_input("URL Immagine Ispirazionale (Opzionale):", placeholder="https://link-immagine.jpg")
        
        col_btn_1, col_btn_2, col_btn_3 = st.columns([1, 1, 1])
        with col_btn_2:
            if st.button("Imprimi l'Opera", use_container_width=True):
                if titolo and testo:
                    data = {
                        "autore": st.session_state.utente,
                        "titolo": titolo,
                        "testo": testo,
                        "immagine_url": url_immagine if url_immagine else None
                    }
                    try:
                        supabase.table("opere").insert(data).execute()
                        st.success("L'opera è stata impressa nel registro eterno.")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Errore nel salvataggio: {e}")
                else:
                    st.warning("Un'opera senza titolo o versi è come un soffio senza voce.")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("### 📜 Il Tuo Registro Poetico")

    # --- RECUPERO DATI ---
    response = supabase.table("opere").select("*").eq("autore", st.session_state.utente).order("created_at", desc=True).execute()
    opere = response.data

    if not opere:
        st.info("Le tue pagine sono ancora bianche. Comincia a scrivere!")
    else:
        for opera in opere:
            with st.container():
                col_testo, col_azioni = st.columns([3, 1])
                
                with col_testo:
                    st.markdown(f"<h4 style='margin-top: 0; color: #3e2723;'>{opera['titolo']}</h4>", unsafe_allow_html=True)
                    st.markdown(f"<div style='white-space: pre-wrap; font-family: \"EB Garamond\", serif; font-size: 1.15rem; padding: 10px 0; color: #3e2723;'>{opera['testo']}</div>", unsafe_allow_html=True)
                    
                    if opera.get('immagine_url'):
                        st.image(opera['immagine_url'], width=300)
                
                with col_azioni:
                    # Pulsanti piccoli e discreti per la gestione
                    if st.button("Modifica ✏️", key=f"btn_edit_{opera['id']}", use_container_width=True):
                        st.session_state[f"editing_{opera['id']}"] = True
                    
                    if st.button("Elimina 🗑️", key=f"btn_del_{opera['id']}", use_container_width=True):
                        supabase.table("opere").delete().eq("id", opera['id']).execute()
                        st.rerun()

                # --- FORM DI MODIFICA INLINE ---
                if st.session_state.get(f"editing_{opera['id']}", False):
                    st.markdown("---")
                    with st.form(key=f"edit_form_{opera['id']}"):
                        edit_titolo = st.text_input("Correggi Titolo", value=opera['titolo'])
                        edit_testo = st.text_area("Rifinisci Versi", value=opera['testo'], height=200)
                        edit_img = st.text_input("Aggiorna Immagine", value=opera.get('immagine_url', ''))
                        
                        c1, c2 = st.columns(2)
                        if c1.form_submit_button("Salva Modifiche"):
                            supabase.table("opere").update({
                                "titolo": edit_titolo,
                                "testo": edit_testo,
                                "immagine_url": edit_img if edit_img else None
                            }).eq("id", opera['id']).execute()
                            st.session_state[f"editing_{opera['id']}"] = False
                            st.rerun()
                        
                        if c2.form_submit_button("Annulla"):
                            st.session_state[f"editing_{opera['id']}"] = False
                            st.rerun()