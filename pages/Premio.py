import streamlit as st

def show():
    # Spazio superiore per centrare visivamente il premio
    st.write("##")
    
    # Titolo Principale in Pompa Magna
    st.markdown("<h1 style='text-align: center; color: #3e2723; font-family: \"Playfair Display\"; font-size: 3rem; margin-bottom: 0;'>Il Riconoscimento d'Onore</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-style: italic; color: #795548; font-size: 1.2rem; margin-top: -10px;'>Al Poeta che ha intrecciato Pensiero e Anima</p>", unsafe_allow_html=True)

    # Il Medaglione 3D che gira lentamente
    LOGO_URL = "https://raw.githubusercontent.com/fosforino/Poeticamente/main/Poeticamente.png"
    st.markdown(f"""
        <div class="medaglione-3d-container">
            <img src="{LOGO_URL}" class="medaglione-bronzo-3d" title="Medaglia al Valore Poetico">
        </div>
    """, unsafe_allow_html=True)

    # La Pergamena con la Dedica
    nome_poeta = st.session_state.get("utente", "Poeta Anonimo")
    st.markdown(f"""
        <div class="pergamena-dedica">
            <h2 style='font-family: "Playfair Display"; color: #5d4037; font-size: 2.2rem; margin-bottom: 20px;'>Al Poeta {nome_poeta}</h2>
            <p style='font-size: 1.5rem; font-style: italic; color: #795548; line-height: 1.6;'>
                "Che si è distinto Filosofamente nei versi,<br>
                intrecciando il pensiero con l'inchiostro dell'anima."
            </p>
            <p style='font-size: 1.1rem; color: #a1887f; margin-top: 25px; font-style: italic;'>
                Il Consiglio dei Saggi di Poeticamente, con immensa stima,<br>
                ti conferisce questo premio al valore del tuo operato.
            </p>
            <span class="firma-fosforino">by fosforino</span>
        </div>
    """, unsafe_allow_html=True)