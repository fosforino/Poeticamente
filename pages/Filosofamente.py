import streamlit as st
import os
import base64

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

def apply_sacred_style():
    path_icona = "Poeticamente.png"
    img_base64 = get_base64_image(path_icona)
    img_html = f'<img src="data:image/png;base64,{img_base64}" class="bg-watermark-filosofia">' if img_base64 else ""

    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=EB+Garamond:ital,wght@0,400;1,400&display=swap');

        .stApp {{
            background-color: #fdf5e6;
            background-image: 
                url("https://www.transparenttextures.com/patterns/marble-similar.png"),
                url("https://www.transparenttextures.com/patterns/handmade-paper.png");
        }}

        /* Colonne Greche fisse ai bordi */
        .stApp::before, .stApp::after {{
            content: "";
            position: fixed;
            top: 0;
            width: 120px;
            height: 100%;
            background-image: url("https://www.transparenttextures.com/patterns/columns.png");
            background-size: contain;
            opacity: 0.08;
            z-index: 0;
            pointer-events: none;
        }}
        .stApp::before {{ left: 0; }}
        .stApp::after {{ right: 0; }}

        .titolo-filosofamente {{
            font-family: 'Cinzel', serif;
            text-align: center;
            color: #1a1a1a;
            font-size: 3.5rem;
            letter-spacing: 8px;
            margin-top: 20px;
            text-transform: uppercase;
        }}

        .marmo-focus {{
            background: rgba(255, 255, 255, 0.5);
            border: 1px solid rgba(0,0,0,0.1);
            padding: 50px;
            border-radius: 4px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.05);
            text-align: center;
            margin-top: 30px;
            min-height: 350px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            position: relative;
            z-index: 1;
        }}

        .nome-autore {{
            font-family: 'Cinzel', serif;
            font-size: 2rem;
            color: #5d4037;
            margin-bottom: 5px;
            letter-spacing: 3px;
        }}

        .opera-unica {{
            font-family: 'Cinzel', serif;
            font-size: 0.9rem;
            color: #8d6e63;
            margin-bottom: 25px;
            letter-spacing: 2px;
            text-transform: uppercase;
        }}

        .testo-stimolo {{
            font-family: 'EB Garamond', serif;
            font-size: 1.8rem;
            line-height: 1.6;
            font-style: italic;
            color: #1a1a1a;
        }}
        </style>
        {img_html}
    """, unsafe_allow_html=True)

def show():
    apply_sacred_style()
    
    st.markdown("<div class='titolo-filosofamente'>Filosofamente</div>", unsafe_allow_html=True)

    filosofi = {
        "Socrate": {"opera": "Apologia", "testo": "L'unica vera sapienza è sapere di non sapere. Una vita senza ricerca non è degna di essere vissuta."},
        "Eraclito": {"opera": "Frammenti", "testo": "Tutto scorre. Nessun uomo attraversa lo stesso fiume due volte, perché non è lo stesso fiume e lui non è lo stesso uomo."},
        "Platone": {"opera": "Simposio", "testo": "Al tocco dell'amore, ognuno diventa poeta."},
        "Immanuel Kant": {"opera": "Critica della ragion pura", "testo": "Il cielo stellato sopra di me, la legge morale dentro di me. Due cose riempiono l'animo di ammirazione sempre nuova."},
        "Karl Marx": {"opera": "Manoscritti del 1844", "testo": "L'uomo è l'essere che deve realizzare se stesso."},
        "Friedrich Nietzsche": {"opera": "Così parlò Zarathustra", "testo": "Bisogna avere ancora un caos dentro di sé per partorire una stella danzante."},
        "Martin Heidegger": {"opera": "Essere e tempo", "testo": "Il linguaggio è la casa dell'essere. I pensatori e i poeti sono i custodi di tale dimora."},
        "Umberto Eco": {"opera": "Il nome della rosa", "testo": "Stat rosa pristina nomine, nomina nuda tenemus."}
    }

    with st.sidebar:
        st.markdown("### 🏛️ Suggerimento d'uso")
        st.info("""
            Prenditi un istante. Seleziona un maestro. 
            Leggi la sua parola e lascia che risuoni. 
            Usa quel riflesso come scintilla per la tua prossima opera.
        """)

    col_l, col_c, col_r = st.columns([0.15, 1, 0.15])
    
    with col_c:
        nomi = ["Scegli una Scintilla..."] + list(filosofi.keys())
        selezione = st.selectbox("Quale anima vuoi consultare?", options=nomi)

        if selezione != "Scegli una Scintilla...":
            dati = filosofi[selezione]
            st.markdown(f"""
                <div class="marmo-focus">
                    <div class="nome-autore">{selezione}</div>
                    <div class="opera-unica">{dati['opera']}</div>
                    <div class="testo-stimolo">"{dati['testo']}"</div>
                </div>
            """, unsafe_allow_html=True)
            
            st.write("")
            if st.button("Vai allo Scrittoio"):
                # Assicurati che il nome della pagina nel comando sia esatto
                st.switch_page("pages/Scrittoio.py")
        else:
            st.markdown("<div style='text-align: center; margin-top: 80px; opacity: 0.4; font-family: \"EB Garamond\"; font-size: 1.5rem;'>Il silenzio è l'inizio di ogni grande opera. Seleziona un pensiero.</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    show()