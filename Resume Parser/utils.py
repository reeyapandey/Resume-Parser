import google.generativeai as genai
import pdfplumber
import os
import json
import typing_extensions as typing
from dotenv import load_dotenv

# 1. Load Environment Variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    # Fallback if .env fails (only for testing, remove in production)
    # api_key = "AIzaSy...PasteKeyHereIfEnvFails" 
    raise ValueError("Google API Key not found. Please check your .env file.")

genai.configure(api_key=api_key)

# 2. Define the exact structure we want the AI to return
class WorkExperience(typing.TypedDict):
    company: str
    role: str
    years: str
    description: str

class ResumeEntities(typing.TypedDict):
    full_name: str
    email: str
    phone: str
    skills: list[str]
    education: list[str]
    work_experience: list[WorkExperience]
    # A score from 0-100 on how well the resume is written
    resume_score: int 
    # Quick tips to improve the resume
    improvement_tips: list[str] 

# 3. Helper function to extract text from PDF
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# 4. Main function to call Gemini API
def parse_resume(text):
    # We use gemini-1.5-flash because it's fast and free
    model = genai.GenerativeModel("models/gemini-2.0-flash")
    
    prompt = f"""
    You are an expert HR and Resume Parser. 
    Analyze the resume text below and extract the entities strictly as JSON.
    Also provide a 'resume_score' (0-100) and 'improvement_tips'.
    
    Resume Text:
    {text}
    """
    
    # This configuration forces Gemini to return ONLY valid JSON matching our schema
    result = model.generate_content(
        prompt,
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json",
            response_schema=ResumeEntities
        )
    )
    
    # Parse the text response into a Python dictionary
    return json.loads(result.text)