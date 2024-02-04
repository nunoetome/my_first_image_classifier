import streamlit as st
from transformers import pipeline
from PIL import Image
from datasets import load_dataset, Image

MODEL_1 = "google/vit-base-patch16-224"
MIN_ACEPTABLE_SCORE = 0.1
MAX_N_LABELS = 5
MODELS = [
            "google/vit-base-patch16-224", #Classifição geral
            "nateraw/vit-age-classifier", #Classifição de idade
]

def main():

    st.title("Image Classification")
    input_image = st.file_uploader("Upload Image")
    shosen_model = st.selectbox("Select the model to use",  MODEL_1)
    
    main_data = load_dataset("leonardo", "single")
    st.write(main_data)

    
    
    if input_image is not None:
        image_to_classify = Image.open(input_image)
        st.image(image_to_classify, caption="Uploaded Image", use_column_width=True)

        if st.button("Classify"):
            image_to_classify = Image.open(input_image)



if __name__ == "__main__":
    main()