import streamlit as st
from model import annotation_method
from utils import clean_annif_output_with_labels, show_help_guide, clear_load_example

st.set_page_config(page_title="Subject Annotator", layout="wide")

# Initialize the uploader key and example load state
if 'uploader_key' not in st.session_state:
    st.session_state.uploader_key = 0
if 'load_example' not in st.session_state:
    st.session_state.load_example = False

# --- Sidebar Controls 
# CHANGE: File uploader now uses a dynamic key.
# When uploader_key changes (via set_load_example), this widget is destroyed and recreated, 
# effectively clearing its display and internal state.
uploaded_file = st.sidebar.file_uploader(
    "Upload the json file of the research data ..",
    type=["json"],
    key=f"uploader_{st.session_state.uploader_key}",
    on_change=clear_load_example 
)

vocab = st.sidebar.selectbox(
    "Select a vocabulary to annotate your data:",
    ["YSO", "STW"]
)

# Dynamically define options
if vocab == "YSO":
    ml_methods = ["TF-IDF"]
elif vocab == "STW":
    ml_methods = ["TF-IDF", "STWFSA", "MLLM"]

selected = st.sidebar.selectbox(
    "Pick a machine learning method to generate subject recommendations:",
    ml_methods
)


def run_main_app():
    st.title("InvenioRDM Subject Annotator")
    st.write("This is a subject annotator for research data that are hosted on invenioRDM based instances.")
    st.divider()

    # 1. Determine which file to process
    data_to_process = None
    is_example_loaded = st.session_state.get('load_example', False)

    if is_example_loaded:
        data_to_process = st.session_state.example_file
        st.info(f"✅ Using exemplary record")
    elif uploaded_file is not None:
        data_to_process = uploaded_file

    # 2. Run processing only if data is available
    results = {}
    if data_to_process is not None:
        # Reset file pointer for processing functions (crucial for both uploads and StringIO)
        data_to_process.seek(0) 
        
        with st.spinner('Processing... Please wait.'):
            if vocab == "YSO" and selected == "TF-IDF":
                results = clean_annif_output_with_labels(annotation_method(data_to_process, "yso-tfidf-en"))
            elif vocab == "STW" and selected == "TF-IDF":
                results = clean_annif_output_with_labels(annotation_method(data_to_process, "stw-tfidf-en"))
            elif selected == "STWFSA":
                results = clean_annif_output_with_labels(annotation_method(data_to_process,"stw-stwfsa-en"))
            elif selected == "MLLM":
                results = clean_annif_output_with_labels(annotation_method(data_to_process, "stw-mllm-en"))
    else:
        st.info("Upload a JSON file or load the example to begin.")


    # 3. Display results
    if results:
        values_list = next(iter(results.values()))
        num_of_suggestions = len(values_list)
        
        if num_of_suggestions == 0:
            st.warning("No subject recommendations were generated. Please try with a different vocabulary or method")
        else:
            st.subheader(f"Top {num_of_suggestions} subjects recommended")
            for value in values_list:
                st.write(f"**subject:**")
                st.write(value)

main_col, info_col = st.columns([0.7, 0.3])

with main_col:
    run_main_app() 

with info_col:
    show_help_guide() 