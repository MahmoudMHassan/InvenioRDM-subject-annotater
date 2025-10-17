import json
import subprocess

def stw_tfidf_a_file(uploaded_file):
    results = {}
    record = json.load(uploaded_file)
    record_id = record.get("id")
    description = record.get("metadata").get("description")  

    if record_id and description:
        # Run annif on the description and capture output
        process = subprocess.Popen(
            ["annif", "suggest", "stw-tfidf-en", "--limit", "5"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=description)
        if process.returncode == 0:
            results[record_id] = stdout.strip()
        else:
            results[record_id] = f"Error: {stderr.strip()}"
    return results

def stwfsa_a_file(uploaded_file):
    results = {}
    record = json.load(uploaded_file)
    record_id = record.get("id")
    description = record.get("metadata").get("description")  

    if record_id and description:
        # Run annif on the description and capture output
        process = subprocess.Popen(
            ["annif", "suggest", "stw-stwfsa-en", "--limit", "5"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=description)
        if process.returncode == 0:
            results[record_id] = stdout.strip()
        else:
            results[record_id] = f"Error: {stderr.strip()}"
    return results

def mllm_a_file(uploaded_file):
    results = {}
    record = json.load(uploaded_file)
    record_id = record.get("id")
    description = record.get("metadata").get("description")  

    if record_id and description:
        # Run annif on the description and capture output
        process = subprocess.Popen(
            ["annif", "suggest", "stw-mllm-en", "--limit", "5"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=description)
        if process.returncode == 0:
            results[record_id] = stdout.strip()
        else:
            results[record_id] = f"Error: {stderr.strip()}"
    return results