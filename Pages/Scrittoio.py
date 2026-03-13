import streamlit as st
from supabase import create_client

def show():
    # Stile per i bottoni colorati
    st.markdown("""
        <style>
        div.stButton > button[key="btn_salva"] { background-color: #708238 !important; color: white !important; border-radius: 20px !important; }
        div.stButton > button[key="btn_stampa"] { background-color: #3498db !important; color: white !important; border-radius: 20px !important; }
        div.stButton > button[key="btn_cancella"] { background-color: #e74c3c !important; color: white !important; border-radius: 20px !important; }
        </style>
        """, unsafe_allow_html=True)

    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    supabase = create_client(url, key)

    if "utente" in st.session_state:
        nome_poeta = st.session_state.utente
        st.title("✒️ Lo Scrittoio")

        # Recupero opere dell'utente
        try:
            res = supabase.table("Opere").select("*").eq("autore_email", nome_poeta).order("creato_il", desc=True).execute()
            opere = res.data
        except:
            opere = []

        scelta = st.sidebar.selectbox("Carica opera:", ["Nuova Opera"] + [o['titolo'] for o in opere])
        opera_corrente = next((o for o in opere if o['titolo'] == scelta), None)
        
        v_titolo = opera_corrente['titolo'] if opera_corrente else ""
        v_testo = opera_corrente['contenuto'] if opera_corrente else ""
        v_cat = opera_corrente.get('categoria', "Poesia") if opera_corrente else "Poesia"

        col_t, col_c = st.columns([2, 1])
        with col_t:
            titolo = st.text_input("Titolo", value=v_titolo)
        with col_c:
            cats = ["Poesia", "Romanzo", "Filastrocca", "Narrazione", "Opera Teatrale", "Canzone"]
            idx = cats.index(v_cat) if v_cat in cats else 0
            categoria = st.selectbox("Categoria", cats, index=idx)

        contenuto = st.text_area("Versi", value=v_testo, height=400)

        # Riga dei Bottoni
        st.write("---")
        b1, b2, b3, b4 = st.columns([1, 1, 1, 1])

        with b1:
            if st.button("💾 Salva", key="btn_salva"):
                if titolo:
                    dati = {"titolo": titolo, "contenuto": contenuto, "categoria": categoria, "autore_email": nome_poeta}
                    if opera_corrente:
                        supabase.table("Opere").update(dati).eq("id", opera_corrente['id']).execute()
                    else:
                        supabase.table("Opere").insert(dati).execute()
                    st.success("Salvato!")
                    st.rerun()
                else:
                    st.warning("Manca il titolo.")

        with b2:
            if st.button("🖨️ Stampa", key="btn_stampa"):
                st.markdown("<script>window.print();</script>", unsafe_allow_html=True)

        with b3:
            if opera_corrente:
                if st.button("🗑️ Elimina", key="btn_cancella"):
                    supabase.table("Opere").delete().eq("id", opera_corrente['id']).execute()
                    st.rerun()
    else:
        st.warning("Identificati nella Home.")