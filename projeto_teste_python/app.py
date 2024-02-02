import streamlit as st
from transformers import pipeline

st.title("Sumarização de Texto")

# prompt = st.text_input("Insira o texto para sumarizar1", "Insira o texto para sumarizar")
prompt = st.text_area("Insira o texto para sumarizar", "Insira o texto para sumarizar")


if st.button("Sumarizar"):
    summarizer = pipeline("summarization")
    summary = summarizer(prompt)
    st.write(summary[0]['summary_text'])



