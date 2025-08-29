import streamlit as st
import pandas as pd


#  Szöveg, címek: st.title(), st.header(), st.write()
#  Input mezők: st.text_input(), st.number_input(), st.selectbox(), st.multiselect()
#  Gomb: st.button()
#  Dátumválasztó: st.date_input()
#  Fájl feltöltés: st.file_uploader()

st.title('Adatlekérdező app')
st.header('Próba header')

user_input = st.text_input('Írd be a lekérdezésed:')
number_input = st.number_input('Válassz egy számot.')
select_box = st.select_s


st.write('Próba write')

if st.button('Futtatás'):
    st.write(f"Ezt írtad: {user_input}")
    st.write(f"A szám amit válaszottál: {number_input}")


#  futtatás: streamlit run --filename--