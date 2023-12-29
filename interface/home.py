
import joblib
import streamlit as st
import requests
import matplotlib as plt
import shap
import pandas as pd
from data import *
import json
from io import StringIO



st.set_page_config(
            page_title="Voice Anthenticator", # => Quick reference - Streamlit
            page_icon="🐍",
            layout="centered", # wide
            initial_sidebar_state="auto") # collapsed

st.set_option('deprecation.showPyplotGlobalUse', False)


with open('./files/wave.css') as f:
    css = f.read()




st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)





# st.image('files/sound.webp')


st.markdown("<h2 style='text-align: left; color: #CCA43B; font-size:100px '> <br/>Voice</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: right; color: #CCA43B; font-size:100px '> Authenticator</h2>", unsafe_allow_html=True)
