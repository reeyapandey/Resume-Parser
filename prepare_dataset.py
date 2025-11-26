import json
import random
import os

# 1. Setup paths
INPUT_FILE = "Data/Entity Recognition in Resumes.json"  # The file you downloaded
OUTPUT_DIR = "data/benchmark"         # Where we save the clean 30 resumes

os.makedirs(OUTPUT_DIR, exist_ok=True)

def convert_dataturks_to_schema(record):
    """
    Converts the Kaggle/DataTurks format to our simple Schema.
    """
    content = record['content']
    annotation = record['annotation']
    
    # Initialize our schema structure
    ground_truth = {
        "full_name": "",
        "email": "",
        "skills": [],
        "education": [],
        "work_experience": [] # The Kaggle dataset doesn't have structured work exp, so we skip strictly validation this
    }

    # Extract entities based on labels in the dataset
    for entity in annotation:
        label = entity['label'][0]
        points = entity['points']
        text_segment = ""
        
        # Get text from content using indices
        for point in points:
            start = point['start']
            end = point['end']
            text_segment = content[start:end + 1]

        text_segment = text_segment.replace("\n", " ").strip()

        # Map to our schema
        if label == "Name":
            ground_truth["full_name"] = text_segment
        elif label == "Email Address":
            ground_truth["email"] = text_segment
        elif label == "Skills":
            ground_truth["skills"].append(text_segment)
        elif label == "Degree" or label == "College Name":
            ground_truth["education"].append(text_segment)

    return content, ground_truth

# 2. Process the file
print("Loading dataset...")
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Select 30 random resumes
selected_lines = random.sample(lines, 30)

print(f"Converting {len(selected_lines)} resumes...")

for i, line in enumerate(selected_lines):
    record = json.loads(line)
    resume_text, ground_truth = convert_dataturks_to_schema(record)
    
    # Save as a pair: Text file (Input) and JSON file (Gold Standard)
    base_name = f"resume_{i}"
    
    # 1. Save Text
    with open(f"{OUTPUT_DIR}/{base_name}.txt", "w", encoding="utf-8") as f:
        f.write(resume_text)
        
    # 2. Save Ground Truth JSON
    with open(f"{OUTPUT_DIR}/{base_name}.json", "w", encoding="utf-8") as f:
        json.dump(ground_truth, f, indent=4)

print(f"✅ Success! Created 30 labeled resumes in '{OUTPUT_DIR}'")