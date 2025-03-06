import streamlit as st
import joblib
import pandas as pd
import re
import nltk
nltk.download('stopwords')
stop_words=nltk.corpus.stopwords.words('english')
stop_words.remove('no')
stop_words.remove('not')
stop_words.remove('but')
ps=nltk.porter.PorterStemmer()
import numpy as np
import matplotlib.pyplot as plt

def simple_text_preprocessor(document):
    # lower case
    document=str(document).lower()
    # remove unnecessary characters
    document=re.sub(r'[^a-zA-Z]',r' ',document)
    document=re.sub(r'nbsp',r'',document)
    document=re.sub(' +',' ',document)
    # simple porter stemming
    document=' '.join([ps.stem(word) for word in document.split()])
    # stopwords removal
    document=' '.join([word for word in document.split() if word not in stop_words])

    return document

model = joblib.load(open('lr.pkl','rb'))
st.title("Twitter Sentiment Analysis")
tweet= st.text_input("Enter your tweet: ")

if st.button("Predict"):
    prediction = model.predict([simple_text_preprocessor(tweet)])
    sentiment = 'Positive' if prediction[0] == 1 else 'Negative'
    st.subheader(f"The above tweet is {sentiment}")

