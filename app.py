import streamlit as st
import requests

st.set_page_config(page_title="AI Marketing Tool", page_icon="✍️")
st.title("✍️ AI Marketing Tool")

nazwa = st.text_input("Nazwa produktu:")
opis = st.text_area("Opis produktu:")

if st.button("🚀 Generuj reklamę"):
    if not nazwa or not opis:
        st.warning("Uzupełnij pola!")
    else:
        with st.spinner("Llama 3 pracuje..."):
            try:
                # Wysyłka do FastAPI
                dane = {"nazwa": nazwa, "opis": opis}
                odpowiedz = requests.post("http://127.0.0.1:8000/generuj", json=dane)

                if odpowiedz.status_code == 200:
                    wynik_ai = odpowiedz.json()

                    # Jeśli to co przyszło to słownik, wyciągamy tekst
                    if isinstance(wynik_ai, dict) and "reklama" in wynik_ai:
                        st.success("Gotowe!")
                        st.write(wynik_ai["reklama"])
                    else:
                        # Jeśli to co przyszło to goły tekst (tak jak na Twoim screenie)
                        st.success("Gotowe (odebrano tekst bezpośredni):")
                        st.write(wynik_ai)
                else:
                    st.error("Błąd serwera!")
            except Exception as e:
                st.error(f"Błąd: {e}")