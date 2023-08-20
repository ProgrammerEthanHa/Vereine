import streamlit as st
import pandas as pd
import altair as alt

st.header("Allgemeine Aktivität in Verbanden und Vereinen")
st.subheader("Wie viele Jugendliche treiben Sport in Vereine?")

source = pd.DataFrame({
        'Anteil(%)': [60, 40],
        ' ': ['ja', 'nein']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x=' :O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Jugendlichen; 2014; Landeshauptstadt Erfurt
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: erfurt.de")