import streamlit as st

# import functions
from input_handling.lemmatization_input import lemmatizer
from input_handling.translation_input import translate_doc
from input_handling.summarize_input import summarize
from input_handling.modeling import modeling

# function that translates and lemmatizes text
def eng_lemmas(text):
    translated_text = translate_doc(text)
    lemmatized_txt =  lemmatizer(translated_text)

    return lemmatized_txt

def main():
    st.header("JuridIQ")

    # Input text
    txt = st.text_area('Article to analyze', ''' ''')


    # Get the topic
    topic_btn = st.button('Get the topic')
    if topic_btn:
        with st.spinner('Topic identification...'):            
            lemmas = eng_lemmas(txt)
            model = modeling(lemmas)
            st.subheader("output")
            st.write(model)



    sum_btn = st.button('Summarize')

    # Get summary
    if sum_btn:
        with st.spinner('Preparing summary...'):
            summary = summarize(txt)
            st.subheader("Summary:")
            st.write(summarize(txt)) #displayed when the button is clicked
            # Translate summary
            st.subheader("Summary translation:")
            st.write(translate_doc(summary))


    # Find similar articles
    recommend_btn = st.button('Recommend similar articles')

    if recommend_btn:
        st.subheader("Similar articles")
        st.write('Articles:') #displayed when the button is clicked    

if __name__ == '__main__':
    main()