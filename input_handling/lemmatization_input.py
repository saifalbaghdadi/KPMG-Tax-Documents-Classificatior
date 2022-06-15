import re

import nltk
nltk.download("stopwords")
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('words')

#stop-words
stop_words_nl=set(nltk.corpus.stopwords.words('dutch'))
stop_words_en=set(nltk.corpus.stopwords.words('english'))

import spacy
import en_core_web_sm

nlp = en_core_web_sm.load()
en_words = set(nltk.corpus.words.words())
overly_abundant = ["article", "decree", "publication"]
months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

def lemmatizer(text):

        cleaned_text = re.sub(r'[\W\d]', " ", text)
        cleaned_text = text.replace("\n", " ").strip().replace(";", " ").strip().replace(",", " ").strip().replace(".", " ").strip()
        doc = nlp(cleaned_text)
        cleaned_lemmas = [t.lemma_ for t in doc if t.lemma_ not in stop_words_nl 
                            and t.lemma_ in en_words
                            and t.lemma_ not in stop_words_en
                            and t.lemma_.lower() not in overly_abundant
                            and t.lemma_.lower() not in months
                            and not re.match(r".*\d.*", t.lemma_)]
        return cleaned_lemmas
