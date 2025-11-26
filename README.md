🚀 AI Resume Parser with Custom NER

An end-to-end Resume Parser built using Python, Streamlit, and Google Gemini 2.0 Flash. It leverages Large Language Models (LLMs) to extract structured data (JSON) from PDF resumes with high accuracy, replacing brittle regex-based parsers.

(Replace this link with a screenshot of your running app)

📊 Benchmarks & Accuracy

We evaluated the model against a "Ground Truth" dataset of 30 diverse resumes derived from the Kaggle Resume Entities for NER dataset.

Evaluation Results:

✅ Name Extraction Accuracy: 100%

✅ Skills Extraction F1-Score: 0.83 (High precision/recall)

Processing Time: ~1.5 seconds per resume

(Replace this link with the screenshot of your terminal output)

🛠️ Tech Stack

Frontend: Streamlit (for a responsive, interactive UI)

AI Model: Google Gemini 2.0 Flash (via google-generativeai SDK)

Parsing: PDFPlumber (for reliable text extraction from PDFs)

Logic: Python 3.x

🌟 Features

Structured Extraction: Converts unstructured PDF text into strict JSON format.

Entity Recognition: Identifies Name, Email, Phone, Education, Work Experience, and Skills.

Smart Scoring: AI analyzes the resume content to provide a "Resume Score" (0-100).

Actionable Feedback: Generates improvement tips for the candidate.

Robust Evaluation: Includes a standalone script to benchmark accuracy against a labeled dataset.

🚀 How to Run Locally

Clone the repository

git clone [https://github.com/yourusername/ai-resume-parser.git](https://github.com/yourusername/ai-resume-parser.git)
cd ai-resume-parser


Install dependencies

pip install -r requirements.txt


Set up API Key

Create a file named .env in the root folder.

Add your Google Gemini API key:

GOOGLE_API_KEY=AIzaSy...YourKeyHere


Run the App

streamlit run app.py


The app will open in your browser at http://localhost:8501.

📂 Project Structure

ResumeParser/
├── .env                                # API Keys (Not committed to Git)
├── app.py                              # Streamlit Frontend Application
├── utils.py                            # Backend Logic (AI & PDF parsing)
├── requirements.txt                    # Python Dependencies
├── evaluate.py                         # Accuracy Benchmarking Script
├── prepare_dataset.py                  # Dataset Preparation Script
└── data/                               # Data Folder
    ├── Entity Recognition in Resumes.json  # Source Kaggle Dataset
    └── benchmark/                      # Generated Ground Truth Files (txt/json)


🧪 How to Run the Benchmark

To reproduce the accuracy scores:

Ensure the data/ folder contains the source JSON dataset (Entity Recognition in Resumes.json).

Run the preparation script to generate the benchmark files:

python prepare_dataset.py


Run the evaluation script to calculate scores:

python evaluate.py


📜 License

This project is licensed under the MIT License.
