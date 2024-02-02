import streamlit as st
from transformers import pipeline
from PIL import Image

MODEL_1 = "google/vit-base-patch16-224"
MODEL_1_MIN_ACEPTABLE_SCORE = 0.003
MODEL_1_MAX_N_LABELS = 5
MODEL_2 = "nateraw/vit-age-classifier"


def classify(image, model, min_aceptable_score, max_n_labels):
    classifier = pipeline("image-classification", model=model)
    result = classifier(image)
    #regista resultados
    print(f"result: {result}")
    print_result_tags(result[:max_n_labels])
    save_result(result)
    return result

def save_result(result):
    st.write(result)

def print_result_tags(result):
    min_aceptable_score = MODEL_1_MIN_ACEPTABLE_SCORE
    comulative_discarded_score = 0
    for i in range(len(result)):
        if result[i]['score'] < min_aceptable_score:
            st.write(f"Discarded: {result[i]['label']}")
            comulative_discarded_score += result[i]['score']
        else:
            st.write(result[i]['label'])
            st.progress(result[i]['score'])
            st.write(result[i]['score'])
            break
    st.write(f"comulative_discarded_score: {comulative_discarded_score}")


def main():
    st.title("Image Classification")
    input_image = st.file_uploader("Upload Image")

    if st.button("Classify"):
        image_to_classify = Image.open(input_image)

        classify(image_to_classify, MODEL_1, MODEL_1_MIN_ACEPTABLE_SCORE, MODEL_1_MAX_N_LABELS)
        classify(image_to_classify, MODEL_2, MODEL_1_MIN_ACEPTABLE_SCORE, MODEL_1_MAX_N_LABELS)

        #google/vit-base-patch16-224
        #classifier = pipeline("image-classification", model=MODEL_1)
        #result = classifier(image_to_classify)
        #print(f"result: {result}")
        #print_result(result[:MODEL_1_MAX_N_LABELS])
        st.image(image_to_classify, caption="Uploaded Image", use_column_width=True)



if __name__ == "__main__":
    main()