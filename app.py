import streamlit as st
from model import annotation_method
from utils import clean_annif_output_with_labels

st.set_page_config(page_title="Subject Annotator")
st.title("InvenioRDM Subject Annotator")
st.write("This is a subject annotator for research data that are hosted on invenioRDM based instances.")


uploaded_file = st.sidebar.file_uploader("Upload the json file of the research dataset ..", type=["json"])

selected = st.sidebar.selectbox(
    "Pick a machine learning method to generate subject recommendations:",
    ["TF-IDF", "STWFSA", "MLLM"]
)

def process_selection(choice):
    results = {}
    if uploaded_file is not None:
        with st.spinner('Processing... Please wait.'):
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
        if num_of_suggestions == 0:
            st.warning("No subject recommendations were generated. Please try with a different method or dataset.")
        
        else:
            st.subheader(f"Top {num_of_suggestions} subjects recommended")
            for value in values_list:
                st.write(f"**subject:**")
                st.write(value)


results = process_selection(selected)