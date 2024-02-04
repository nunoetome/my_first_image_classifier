import streamlit as st
from transformers import pipeline
from PIL import Image



MODEL_1 = "google/vit-base-patch16-224"
MIN_ACEPTABLE_SCORE = 0.1
MAX_N_LABELS = 5
MODEL_2 = "nateraw/vit-age-classifier"
MODELS = [
            "google/vit-base-patch16-224", #Classifição geral
            "nateraw/vit-age-classifier", #Classifição de idade
            "microsoft/resnet-50", #Classifição geral
            #NOT OK "microsoft/beit-base-patch16-224-pt22k-ft22k", #Classifição geral
            "Falconsai/nsfw_image_detection", #Classifição NSFW
            "cafeai/cafe_aesthetic", #Classifição de estética
            "timm/vit_large_patch14_clip_224.openai_ft_in12k_in1k", #Classifição geral
            "timm/vit_base_patch16_224_in21k", #Classifição geral escolhida pelo copilot 
            "microsoft/resnet-18", #Classifição geral
            "microsoft/resnet-34", #Classifição geral escolhida pelo copilot 
            "microsoft/resnet-101", #Classifição geral escolhida pelo copilot 
            "microsoft/resnet-152", #Classifição geral escolhida pelo copilot
            "microsoft/resnet-50-kinetics-400", #Classifição geral escolhida pelo copilot
            "microsoft/swin-tiny-patch4-window7-224",#Classifição geral
            ""

        ]

def classify(image, model):
    classifier = pipeline("image-classification", model=model)
    result= classifier(image)
    return result

def save_result(result):
    st.write("In the future, this function will save the result in a database.")

def print_result(result):

    comulative_discarded_score = 0
    for i in range(len(result)):
        if result[i]['score'] < MIN_ACEPTABLE_SCORE:
            comulative_discarded_score += result[i]['score']
        else:
            st.write(result[i]['label'])
            st.progress(result[i]['score'])
            st.write(result[i]['score'])

    st.write(f"comulative_discarded_score:")
    st.progress(comulative_discarded_score)
    st.write(comulative_discarded_score)
    


def main():
    st.title("Image Classification")
    input_image = st.file_uploader("Upload Image")
    shosen_model = st.selectbox("Select the model to use",  MODELS)
    
    if input_image is not None:
        image_to_classify = Image.open(input_image)
        st.image(image_to_classify, caption="Uploaded Image", use_column_width=True)

        if st.button("Classify"):
            image_to_classify = Image.open(input_image)
            classification_obj1 =[]
            avable_models = st.selectbox
            
            classification_result = classify(image_to_classify, shosen_model)
            classification_obj1.append(classification_result)
            print_result(classification_result)
            save_result(classification_result)


if __name__ == "__main__":
    main()