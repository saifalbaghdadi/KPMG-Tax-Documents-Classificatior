import streamlit as st
#import numpy as np
#import os
import sklearn
from sklearn.neighbors import _dist_metrics
import pandas as pd
import json


# import functions
#sys.path.insert(0, '/preprocessing/lemmatization.py')
from input_handling.lemmatization_input import lemmatizer
from input_handling.translation_input import translate_doc
from input_handling.summarize_input import summarize

from model import juridIQ
from model.juridIQ import JuridIQ
model = JuridIQ()

st.header("JuridIQ")
st.subheader('Returns keywords and summary of the article.')
st.subheader('Recommends articles on the same topic')

# Input text
txt = st.text_area('Article to analyze', ''' ''')

# function that translates and lemmatizes text
def eng_lemmas(text):
    translated_text = translate_doc(txt)
    lemmatized_txt =  lemmatizer(translated_text)

    return lemmatized_txt


def find_topic(text):
    topic = model.get_topic(text)

    return topic


def find_articles(topic_prob):
    files_from_csv = pd.read_csv("KPMG_with_topics.csv").drop("Unnamed: 0", axis=1)

    topics_as_list = [json.loads(topic) for topic in files_from_csv["Topics"]]

    indexes = juridIQ.get_similar(topic_prob, topics_as_list)

    links_nl = []

    for index in indexes:
        links_nl.append(files_from_csv["Link NL"][index])
        
    return links_nl

def main():
    # Get the topic (for now - lemmas from translated text)
    if st.button('Analyze'):
        lemmas =  eng_lemmas(txt)
        topic_tuple = find_topic(lemmas)
        topic = model.model.get_topic(topic_tuple[0][0])

        prob = topic_tuple[1][0]

        articles = find_articles(prob)

        st.subheader('Keywords')
        st.write(topic)
        st.subheader('Similar articles')
        st.write(articles)
        st.subheader('Summary')
        summary = summarize(txt)
        st.write(summary)
        st.subheader('Summary translation')
        st.write(translate_doc(summary))
    else:
        st.write('') #displayed when the button is unclicked



main()

