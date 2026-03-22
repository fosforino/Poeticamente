# pages/Premio.py - Versione Scrittoio Millenario con Pergamena Ruotata
import streamlit as st
import random

def genera_vortice_lettere(num_lettere=130):
    """Genera l'HTML per il vortice di lettere casuali (Latine, Greche e Simboli)."""
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZΩΨΦΣΠΛΔΓΘΞαβγδεζηθικλμνξοπρστυφχψω!?¿<>+=-*%"
    html_lettere = '<div class="vortex-container">'
    
    for _ in range(num_lettere):
        char = random.choice(alfabeto)
        pos_x = random.uniform(0, 100)
        pos_y = random.uniform(0, 100)
        classe_dim = random.choice(['piccola', 'media', 'grande'])
        durata_anim = random.uniform(20, 50) # Secondi per un'orbita completa

        html_lettere += f"""
            <div class="lettera-vortice {classe_dim}" 
                 style="left: {pos_x}vw; top: {pos_y}vh; animation-duration: {durata_anim}s;">
                {char}
            </div>
        """
    html_lettere += '</div>'
    return html_lettere

def show():
    # 1. INIETTIAMO IL VORTICE (Sfondo dinamico)
    st.markdown(genera_vortice_lettere(), unsafe_allow_html=True)

    # 2. TITOLO (Sopra il vortice)
    # Abbiamo stilizzato il titolo via CSS con .titolo-id
    st.markdown("<h1 class='titolo-id'>Il Tuo Riconoscimento</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # --- HTML FILIGRANA (MEDAGLIONE RETRO - STATICO E RUOTATO) ---
    st.markdown("""
        <div class="filigrana-retro">
            <img src="https://raw.githubusercontent.com/fosforino/Poeticamente/main/Poeticamente_retro.png">
        </div>
    """, unsafe_allow_html=True)

    # --- HTML MEDAGLIONE 3D (FULCRO FLOTTANTE - SOLO FRONTE) ---
    st.markdown("""
        <div class="medaglione-3d-container">
            <div class="card-3d">
                
                <div class="faccia fronte">
                    <img src="https://raw.githubusercontent.com/fosforino/Poeticamente/main/Poeticamente.png">
                </div>
                
                </div>
        </div>
    """, unsafe_allow_html=True)

    # --- HTML PERGAMENA DEDICA (Contenuto statico) ---
    st.markdown("""
        <div class="pergamena-dedica">
            <p style="font-size: 1.3rem; line-height: 1.8; color: #5d4037;">
                <i>"A chi ha saputo trasformare il silenzio in inchiostro,<br>
                e il pensiero in un'opera senza tempo."</i>
            </p>
            <p style="font-size: 1.1rem; color: #795548; margin-top: 25px;">
                Un riconoscimento da parte di chi crede nel valore<br>
                <b>dell'Alchimia tra il Pensiero e il Verso.</b>
            </p>
            <div class="firma-fosforino">
                fosforino
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    show()