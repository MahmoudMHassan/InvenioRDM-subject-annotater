import streamlit as st
import io
import os

EXAMPLE_FILE_PATH = os.path.join("data", "exem_data", "example_record.json")

def clean_annif_output_with_labels(raw_output):
    result = {}
    for record_id, output in raw_output.items():
        cleaned = []
        for line in output.split('\n'):
            parts = line.split('\t')
            if len(parts) >= 2:
                descriptor = parts[0]
                label = parts[1]
                score = parts[2]
                cleaned.append(f"descriptor: {descriptor}, label: {label}, similarity score: {score}")
        result[record_id] = cleaned
    return result

# --- Define the Help Guide Content ---
def show_help_guide():
    """A function to display the help guide in its own container."""
    with st.container(border=True): 
        st.subheader("ℹ️ How to Use This App")
        st.markdown(
            """
            **How to get your JSON file:**

            1.  **Navigate to a record:** Go to your InvenioRDM instance 
                (like [Zenodo](https://zenodo.org) or [BERD](https://berd-platform.de)).
            2.  **Find the "Export" section:** On the record's page, scroll down 
                to the "Formats" or "Export" box.
            3.  **Download the JSON:** Click on the **"JSON"** or **"DataCite JSON"** link.
            4.  **Save the file:** Right-click and "Save As..." to save it as a `.json` file.
            5.  **Upload:** Drag and drop that `.json` file into the file 
                uploader on the left!
            
            ---
            **Try it out:**
            
            Don't have a file? Click below to load an example record.
            """
        )
        st.button("Load Example Data", on_click=set_load_example, use_container_width=True)
    
def set_load_example():
    """
    Called when the 'Load Example' button is clicked.
    1. Reads the content from the external JSON file.
    2. INCREMENTS the uploader_key to force the file uploader widget to reset.
    """
    if not os.path.exists(EXAMPLE_FILE_PATH):
        # This error is the most common issue in deployment
        st.error(f"Error: Example file not found at {EXAMPLE_FILE_PATH}.")
        return

    try:
        with open(EXAMPLE_FILE_PATH, 'r') as f:
            json_string = f.read()
        
        st.session_state.example_file = io.StringIO(json_string)
        st.session_state.example_file.name = os.path.basename(EXAMPLE_FILE_PATH)
        st.session_state.load_example = True
        st.session_state.uploader_key += 1
        
    except Exception as e:
        st.error(f"Failed to load example file: {e}")

def clear_load_example():
    """
    Called when a new file is uploaded (via on_change).
    Clears the example data flag.
    """
    st.session_state.load_example = False
    if 'example_file' in st.session_state:
        del st.session_state.example_file
