import streamlit as st
from model import annotation_method
from utils import clean_annif_output_with_labels

st.set_page_config(page_title="Subject Annotator")
st.title("InvenioRDM Subject Annotator")
st.write("Upload the json of the research dataset")


uploaded_file = st.file_uploader("Choose json file...", type=["json"])

def process_selection(choice):
    results = {}
    if uploaded_file is not None:
        if choice == "TF-IDF":
            results = clean_annif_output_with_labels(annotation_method(uploaded_file, "stw-tfidf-en"))

        elif choice == "STWFSA":
            results = clean_annif_output_with_labels(annotation_method(uploaded_file,"stw-stwfsa-en"))

        elif choice == "MLLM":
            results = clean_annif_output_with_labels(annotation_method(uploaded_file, "stw-mllm-en"))

    if results:
        values_list = next(iter(results.values()))
        num_of_suggestions = len(values_list)
        # Display results
        st.subheader(f"Top {num_of_suggestions} subjects recommended")
        for value in values_list:
            st.write(f"**subject:**")
            st.write(value)

selected = st.selectbox(
    "Pick a machine learning method to generate subject recommendations:",
    ["TF-IDF", "STWFSA", "MLLM"]
)
results = process_selection(selected)