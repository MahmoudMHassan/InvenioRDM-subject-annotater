
To create a virtual environment, activate and install the needed packages:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

To load stw vocab:

`annif load-vocab stw data/vocabs/stw/subjects.ttl`

Train the desired model: 
    To make the stwfsa works:
    ```
    pip install annif[stwfsa]
    annif train stw-stwfsa-en data-sets/stw-zbw/stw-econbiz.tsv.gz
    ```

    To make the tfidf works:

    `annif train stw-tfidf-en data-sets/stw-zbw/stw-econbiz.tsv.gz`
To train your model for ex here using the tfidf model: 

`annif train stw-tfidf-en data-sets/stw-zbw/stw-econbiz.tsv.gz`

run the app using:

`streamlit run app.py`# InvenioRDM-subject-annotater
