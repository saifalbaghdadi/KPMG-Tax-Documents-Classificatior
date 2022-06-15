import streamlit as st
import numpy as np
import os
#import sys

# import functions
#sys.path.insert(0, '/preprocessing/lemmatization.py')
from input_handling.lemmatization_input import lemmatizer
from input_handling.translation_input import translate_doc

st.header("JuridIQ")

# Input text
txt = st.text_area('Article to analyze', ''' ''')

# function that translates and lemmatizes text
def eng_lemmas(text):
    translated_text = translate_doc(txt)
    lemmatized_txt =  lemmatizer(translated_text)
    return lemmatized_txt


# Get the topic (for now - lemmas from translated text)
if st.button('Get the topic'):
    st.write('Lemmas:', eng_lemmas(txt)) #displayed when the button is clicked
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

