import re

#import nltk
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

def lemmatizer(texts, batchsize: int = 1):
    lemmatized = []
    batches = int(len(texts) / batchsize) + 1

    for batch in range(batches):

        # print(f"v2.4: Batch {batch + 1} of {batches}")
        to_lemmatize_batch = texts[20*batch:20*(batch+1)]

        cleaned_batch = [re.sub(r'[\W\d]', " ", text) for text in to_lemmatize_batch]
        docs = nlp.pipe(cleaned_batch)
        lemmatized += [[t.lemma_.replace("_", "").lower() for t in doc if t.lemma_.replace("_", "") not in stop_words_nl
                            and t.lemma_.replace("_", "") in en_words
                            and t.lemma_.replace("_", "") not in stop_words_en
                            and t.lemma_.replace("_", "").lower() not in overly_abundant
                            and t.lemma_.replace("_", "").lower() not in months
                            and len(t.lemma_.replace("_", "")) > 3] for doc in docs]

        # print(f"Batch {batch + 1} done!")

    lemmatized_joined = []

    [lemmatized_joined.append(" ".join(words)) for words in lemmatized]

    lemmatized_joined = [" ".join(article.split()) for article in lemmatized_joined]

    return lemmatized_joined


