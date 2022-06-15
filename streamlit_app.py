import streamlit as st
import numpy as np
import os
#import sys

# import functions
#sys.path.insert(0, '/preprocessing/lemmatization.py')
from preprocessing.lemmatization_input import lemmatizer

st.header("JuridIQ")

# Input text
txt = st.text_area('Article to analyze', ''' ''')
preprocessed_txt =  lemmatizer(txt)


# Get the topic
if st.button('Get the topic'):
    st.write('Lemmas:', preprocessed_txt) #displayed when the button is clicked
else:
    st.write('') #displayed when the button is unclicked


# Get summary
if st.button('Summarize'):
    st.write('Summary:') #displayed when the button is clicked
else:
    st.write('') #displayed when the button is unclicked

# Translate summary
agree = st.checkbox('Translate to English')
if agree:
     st.write('Translating...')

# Get summary
if st.button('Recommend similar articles'):
    st.write('Articles:') #displayed when the button is clicked
else:
    st.write('') #displayed when the button is unclicked     

