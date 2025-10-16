# format output with labelling
def clean_annif_output_with_labels(raw_output):
    result = {}
    for record_id, output in raw_output.items():
        cleaned = []
        # Split output by newline to get each line
        for line in output.split('\n'):
            parts = line.split('\t')
            if len(parts) >= 2:
                descriptor = parts[0]
                label = parts[1]
                score = parts[2]
                cleaned.append(f"descriptor: {descriptor}, label: {label}, similarity score: {score}")
        result[record_id] = cleaned
    return result