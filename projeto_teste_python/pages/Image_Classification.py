import streamlit as st
from transformers import pipeline
from PIL import Image

MODEL_GOOGLE_1 = "google/vit-base-patch16-224"
MODEL_GOOGLE_1_MIN_ACEPTABLE_SCORE = 0.003
MODEL_GOOGLE_1_MAX_NUMBER_OF_LABELS = 5



def print_result(result):
    min_aceptable_score = 0.003
    comulative_discarded_score = 0
    for i in range(len(result)):
        if result[i]['score'] < min_aceptable_score:
            comulative_discarded_score += result[i]['score']
        else:
            st.write(result[i]['label'])
            st.progress(result[i]['score'])
            st.write(result[i]['score'])
            break




st.title("Image Classification")

image = st.file_uploader("Upload Image")

if st.button("Classify"):
    image = Image.open(image)
    classifier = pipeline("image-classification", model=MODEL_GOOGLE_1)
    result = classifier(image)
    print(f"result: {result}")
    print_result(result[:5])
    st.image(image, caption="Uploaded Image", use_column_width=True)