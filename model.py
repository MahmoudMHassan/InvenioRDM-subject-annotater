import json
import subprocess

def annotation_method(uploaded_file, choice):
    results = {}
    record = json.load(uploaded_file)
    record_id = record.get("id")
    description = record.get("metadata").get("description")  
    
    if record_id and description and choice:
        # Run annif on the description and capture output
        process = subprocess.Popen(
            ["annif", "suggest", choice, "--limit", "5"],
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