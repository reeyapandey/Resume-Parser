import os
import json
from utils import parse_resume # Import your actual AI function
import time

DATA_DIR = "data/benchmark"

def calculate_f1(true_list, pred_list):
    """
    Helper to calculate F1 for lists of items (like Skills).
    We treat this as a set overlap problem.
    """
    true_set = set([x.lower().strip() for x in true_list])
    pred_set = set([x.lower().strip() for x in pred_list])
    
    if len(true_set) == 0: return 0.0
    
    # Find matches (simple substring match for robustness)
    matches = 0
    for p in pred_set:
        for t in true_set:
            if p in t or t in p: # Flexible matching
                matches += 1
                break
    
    precision = matches / len(pred_set) if len(pred_set) > 0 else 0
    recall = matches / len(true_set) if len(true_set) > 0 else 0
    
    if precision + recall == 0: return 0.0
    return 2 * (precision * recall) / (precision + recall)

def run_evaluation():
    print("🚀 Starting Evaluation on 30 Resumes...")
    
    files = [f for f in os.listdir(DATA_DIR) if f.endswith(".txt")]
    
    total_f1_skills = 0
    total_f1_name = 0
    total_files = len(files)
    
    results = []

    for filename in files:
        base_name = filename.replace(".txt", "")
        print(f"Processing {base_name}...", end="\r")
        
        # 1. Read Input Text
        with open(f"{DATA_DIR}/{filename}", "r", encoding="utf-8") as f:
            text = f.read()
            
        # 2. Read Ground Truth
        with open(f"{DATA_DIR}/{base_name}.json", "r", encoding="utf-8") as f:
            ground_truth = json.load(f)
            
        # 3. Run Your Model (The AI)
        try:
            # Note: We add a small sleep to avoid hitting API rate limits
            time.sleep(1) 
            prediction = parse_resume(text)
            
            # 4. Calculate Scores
            
            # Metric A: Skills F1
            f1_skills = calculate_f1(ground_truth['skills'], prediction.get('skills', []))
            
            # Metric B: Name Match (Binary 1.0 or 0.0)
            gt_name = ground_truth['full_name'].lower()
            pred_name = prediction.get('full_name', '').lower()
            score_name = 1.0 if (gt_name in pred_name or pred_name in gt_name) else 0.0
            
            total_f1_skills += f1_skills
            total_f1_name += score_name
            
        except Exception as e:
            print(f"\n❌ Error on {filename}: {e}")
            total_files -= 1

    # Final Report
    print("\n\n" + "="*30)
    print("📊 EVALUATION REPORT")
    print("="*30)
    
    # Safety Check: Prevent division by zero if no files were processed
    if total_files > 0:
        avg_f1_skills = total_f1_skills / total_files
        avg_name_acc = total_f1_name / total_files
        
        print(f"✅ Files Processed: {total_files}")
        print(f"Overall Accuracy (Name): {avg_name_acc*100:.2f}%")
        print(f"F1-Score (Skills Extraction): {avg_f1_skills:.4f}")
    else:
        print("❌ No resumes were processed successfully.")
        print("Check your API Key, Internet Connection, or Model Name.")
        
    print("="*30)

if __name__ == "__main__":
    run_evaluation()