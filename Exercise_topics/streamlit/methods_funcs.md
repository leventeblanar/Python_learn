#  -------------------------------
#  Szöveg & formázás
#  -------------------------------
st.title()          # nagy cím
st.header()         # alcím
st.subheader()      # kisebb alcím
st.text()           # sima szöveg
st.write()          # "okos" kiírás (szöveg, dataframe, dict, bármi)
st.markdown()       # markdown formátum
st.code()           # kód blokk
st.latex()          # LaTeX matematikai képletek
st.caption()        # halvány megjegyzés

#  -------------------------------
#  Input elemek (widgetek)
#  -------------------------------
st.text_input()     # szövegmező
st.number_input()   # számmező
st.text_area()      # több soros szöveg
st.date_input()     # dátum választó
st.time_input()     # idő választó
st.checkbox()       # checkbox
st.radio()          # rádió gombok
st.selectbox()      # legördülő
st.multiselect()    # több választásos legördülő
st.slider()         # slider
st.select_slider()  # slider előre megadott értékekkel
st.file_uploader()  # fájl feltöltés
st.color_picker()   # színválasztó

#  -------------------------------
#  Gombok
#  -------------------------------
st.button()         # egyszerű gomb
st.download_button()# fájl letöltés gomb

#  -------------------------------
#  Média
#  -------------------------------
st.image()          # kép
st.audio()          # audió
st.video()          # videó

#  -------------------------------
#  Adatok megjelenítése
#  -------------------------------
st.dataframe()      # interaktív pandas dataframe
st.table()          # statikus tábla
st.json()           # json szépen
st.metric()         # kiemelt mérőszám

#  -------------------------------
#  Grafikonok
#  -------------------------------
st.line_chart()     # vonaldiagram
st.area_chart()     # területdiagram
st.bar_chart()      # oszlopdiagram
st.map()            # térkép
st.pyplot()         # matplotlib plot
st.altair_chart()   # Altair chart
st.vega_lite_chart()# Vega Lite chart
st.plotly_chart()   # Plotly chart
st.bokeh_chart()    # Bokeh chart
st.pydeck_chart()   # PyDeck chart

#  -------------------------------
#  Layout
#  -------------------------------
st.sidebar           # oldalsáv (pl. st.sidebar.selectbox())
st.columns()         # több hasáb
st.tabs()            # tab-ok
st.expander()        # összecsukható doboz
st.container()       # konténer
st.empty()           # placeholder (pl. dinamikus frissítéshez)

#  -------------------------------
#  Állapot, üzenetek
#  -------------------------------
st.progress()       # progress bar
st.spinner()        # "Loading..." animáció
st.toast()          # felugró üzenet
st.error()          # hibaüzenet
st.warning()        # figyelmeztetés
st.info()           # infó
st.success()        # siker üzenet
st.exception()      # kivétel stack trace

#  -------------------------------
#  Egyéb
#  -------------------------------
st.form()           # űrlap
st.form_submit_button() # űrlap gomb
st.cache_data       # eredmények cache-elése
st.cache_resource   # resource cache
st.session_state    # session állapot tárolás
st.experimental_rerun() # újratöltés
