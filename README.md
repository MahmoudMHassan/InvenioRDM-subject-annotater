# InvenioRDM-subject-annotater

A web client wrapped around [annif](https://github.com/NatLibFi/Annif) for automatic subject indexing for instances that are using invenioRDM. A demo could be accessed via https://inveniordm-subject-annotater.streamlit.app/ 

## Install locally

Create a virtual environment, activate and install the needed packages:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

To load stw and yso vocab:

```
annif load-vocab stw data/vocabs/stw/subjects.ttl
annif load-vocab yso data/vocabs/yso/subjects.ttl
```

### Train the desired model: 
    
To make the stwfsa works:

```
pip install annif[stwfsa]
annif train stw-stwfsa-en data-sets/stw-zbw/stw-econbiz.tsv.gz
```

To make the term frequency inverse document frequency (tfidf) method work for stw and yso vocabs:

```
annif train stw-tfidf-en data-sets/stw-zbw/stw-econbiz.tsv.gz
annif train yso-tfidf-en data-sets/yso-finna/yso-finna.tsv.gz
```

To make the Maui-like Lexical Matching (mllm) method work:

`annif train stw-mllm-en data-sets/stw-zbw/stw-econbiz.tsv.gz`

### To run the app using:

`streamlit run app.py`
