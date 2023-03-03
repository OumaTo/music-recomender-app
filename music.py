import streamlit as st
import joblib
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np

col1, col2 = st.columns([2,1])

model = joblib.load("music-recommender.joblib")
col1.image('img/icon1.png')
col1.title("Music Recommender")

background = """
<style>
.css-fg4pbf {
    position: absolute;
    background: rgb(63,94,251);
    background-color: #D9AFD9;
    background-image: linear-gradient(0deg, #D9AFD9 0%, #97D9E1 100%);

    inset: 0px;
    overflow: hidden;
}</style>
"""
st.markdown(background, unsafe_allow_html = True)
side = st.sidebar.selectbox("Explore or Satisfied", ("predict", "Explore Data", "Author"))

with col1.container():
    col1.write("""### some info is taken to give the output""")

    name = col1.text_input("**Enter Your Name**", "eg. Ouma Tonny")
    genders = {
        0 : "Female",
        1 : "Male",
    }

    gender = st.selectbox("Gender  0.Female   1.Male", genders)
    age = col1.slider("Age",1,100)
    button = col1.button("Send")
    

    with col1.container():
        if button:

            predictions = model.predict([[age, gender]])
            col1.success(f"**Hello {name} we recommended  **{ predictions[0]}** music for you**")
            col1.write(f"[click here for your { predictions[0]} music collection](https://www.youtube.com/results?search_query={predictions[0]}+music)")


if side == "Author":
    st.sidebar.markdown("""Made by: **Ouma Tonny**
               oumatonny8@gmail.com\n
               """)
    st.sidebar.write('Reach me on Whatsapp')
    st.sidebar.success('[Whatsapp](https://wa.link/8g14e8)')
    st.sidebar.write('or scan the below QR code')
    st.sidebar.image('img/link.png')

if side == "Explore Data":
    data = pd.read_csv('music.csv')
    col2.subheader("Music recommender data set")
    col2.write(data)
