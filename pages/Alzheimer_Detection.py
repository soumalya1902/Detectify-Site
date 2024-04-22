import streamlit as st
import imagerec
import pandas as pd
import random
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Detectify",
    initial_sidebar_state="auto",
)


st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
components.html(
    """
    <style>
        #effect{
            margin:0px;
            padding:0px;
            font-family: "Source Sans Pro", sans-serif;
            font-size: max(8vw, 20px);
            font-weight: 700;
            top: 0px;
            right: 25%;
            position: fixed;
            background: -webkit-linear-gradient(0.25turn,#FF4C4B, #FFFB80);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        p{
            font-size: 2rem;
        }
   
    """,
    height=10,
)
uploaded_file = None

st.title("Alzheimer Disease Detection")

uploaded_file = st.file_uploader("Upload your Medical Scan Image", type=['jpg','png','jpeg'])


if uploaded_file!=None:
    st.image(uploaded_file)
x = st.button("Detect")
if x:
    with st.spinner("Detecting..."):
        y,conf = imagerec.imagerecognise(uploaded_file,"Models/alzheimer.h5","Models/alzheimer.txt")
    if y.strip() == "normal":
        components.html(
            """
            <style>
            h1{
                
                background: -webkit-linear-gradient(0.25turn,#FF4C4B, #F70000);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: "Source Sans Pro", sans-serif;
            }
            </style>
            <h1>No Dementia Detected</h1>
            """
        )
    elif y.strip() == "moderate_dementia":
        components.html(
            """
            <style>
            h1{
                background: -webkit-linear-gradient(0.25turn,#FF4C4B, #F70000);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: "Source Sans Pro", sans-serif;
            }
            </style>
            <h1>Moderate Dementia Detected</h1>
            """
        )
    elif y.strip() == "mild_dementia":
        components.html(
            """
            <style>
            h1{
                background: -webkit-linear-gradient(0.25turn,#FF4C4B, #F70000);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: "Source Sans Pro", sans-serif;
            }
            </style>
            <h1>Mild Dementia Detected</h1>
            """
        )
    else:
        components.html(
            """
            <style>
            h1{
                background: -webkit-linear-gradient(0.25turn,#FF4C4B, #F70000);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: "Source Sans Pro", sans-serif;
            }
            </style>
            <h1>Very Mild Dementia Detected</h1>
            """
        )
