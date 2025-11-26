🚀 AI Resume Parser with Custom NER
An end-to-end Resume Parser built using Python, Streamlit, and Google Gemini 2.0 Flash. It leverages Large Language Models (LLMs) to extract structured data (JSON) from PDF resumes with high accuracy,       replacing brittle regex-based parsers.

<img width="1909" height="905" alt="Screenshot 2025-11-26 201439" src="https://github.com/user-attachments/assets/5a627b61-67e4-42bf-8d46-745004a98a97" />
<img width="1913" height="909" alt="Screenshot 2025-11-26 201556" src="https://github.com/user-attachments/assets/9673e34d-dd3a-430a-9c96-e2099f54dfff" />


📊 Benchmarks & Accuracy
We evaluated the model against a "Ground Truth" dataset of 30 diverse resumes derived from the Kaggle Resume Entities for NER dataset.

* Evaluation Results:

✅ Name Extraction Accuracy: 100%

✅ Skills Extraction F1-Score: 0.83 (High precision/recall)

Processing Time: ~1.5 seconds per resume

<img width="915" height="241" alt="Screenshot 2025-11-26 193454" src="https://github.com/user-attachments/assets/5e42e5c3-f984-4bd9-a978-efab2f7288ad" />


🛠️ Tech Stack
> Frontend: Streamlit (for a responsive, interactive UI)
> AI Model: Google Gemini 2.0 Flash (via google-generativeai SDK)
> Parsing: PDFPlumber (for reliable text extraction from PDFs)
> Logic: Python 3.x

🌟 Features
> Structured Extraction: Converts unstructured PDF text into strict JSON format.
> Entity Recognition: Identifies Name, Email, Phone, Education, Work Experience, and Skills.
> Smart Scoring: AI analyzes the resume content to provide a "Resume Score" (0-100).
> Actionable Feedback: Generates improvement tips for the candidate.
> Robust Evaluation: Includes a standalone script to benchmark accuracy against a labeled dataset.

🚀 How to Run Locally

> Clone the repository
git clone [https://github.com/reeyapandey/Resume-Parser](https://github.com/reeyapandey/Resume-Parser)

> Install dependencies
pip install -r requirements.txt

> Set up API Key
Create a file named .env in the root folder.

> Add your Google Gemini API key:
GOOGLE_API_KEY=AIzaSy...YourKeyHere

> Run the App
streamlit run app.py

> The app will open in your browser at http://localhost:8501/.

🧪 How to Run the Benchmark

~ To reproduce the accuracy scores:
~ Ensure the data/ folder contains the source JSON dataset (Entity Recognition in Resumes.json).
~ Run the preparation script to generate the benchmark files:
~ python prepare_dataset.py
~ Run the evaluation script to calculate scores:
~ python evaluate.py
