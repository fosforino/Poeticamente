# pages/Premio.py
import streamlit as st

def show():
    # Titolo della pagina
    st.markdown("<h1 style='text-align: center; color: #3e2723; font-family: \"Playfair Display\";'>Il Tuo Riconoscimento Poetetico</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # --- IL MOTORE DEL MEDAGLIONE FRONTE-RETRO ---
    # Questa struttura HTML crea il "sandwich 3D" controllato dal CSS
    st.markdown("""
        <div class="medaglione-3d-container">
            <div class="card-3d">
                
                <div class="faccia fronte">
                    <img src="https://raw.githubusercontent.com/fosforino/Poeticamente/main/Poeticamente.png">
                </div>
                
                <div class="faccia retro">
                    <div class="testo-retro">by fosforino</div>
                </div>
                
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- LA PERGAMENA DELLA DEDICA ---
    st.markdown("""
        <div class="pergamena-dedica">
            <p style="font-size: 1.3rem; line-height: 1.8; color: #5d4037;">
                <i>"A chi ha saputo trasformare il silenzio in inchiostro,<br>
                e il pensiero in un'opera senza tempo."</i>
            </p>
            <p style="font-size: 1.1rem; color: #795548; margin-top: 20px;">
                Con stima e ammirazione,<br>
                la Comunità di Poeticamente.
            </p>
            <div class="firma-fosforino">by fosforino</div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    show()