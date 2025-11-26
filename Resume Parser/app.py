import streamlit as st
from utils import extract_text_from_pdf, parse_resume
import time

# 1. Page Configuration
st.set_page_config(
    page_title="AI Resume Parser",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS for Styling
st.markdown("""
    <style>
    /* Main Background and Text */
    .main {
        background-color: #f8f9fa;
    }
    h1, h2, h3 {
        color: #2c3e50;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* Custom Header/Logo Area */
    .header-container {
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
        text-align: center;
    }
    .header-title {
        font-size: 3rem;
        font-weight: bold;
        margin: 0;
    }
    .header-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
        margin-top: 0.5rem;
    }

    /* Metric Cards */
    .metric-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        border-left: 5px solid #4b6cb7;
    }
    .metric-label {
        color: #7f8c8d;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .metric-value {
        color: #2c3e50;
        font-size: 2rem;
        font-weight: bold;
    }

    /* Result Sections */
    .info-box {
        background-color: white;
        padding: 1.5rem;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        margin-bottom: 1rem;
    }
    .success-message {
        padding: 1rem;
        background-color: #d4edda;
        color: #155724;
        border-radius: 5px;
        margin-bottom: 1rem;
        border: 1px solid #c3e6cb;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar with App Info
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135679.png", width=80)
    st.title("Resume Parser AI")
    st.info("This tool uses Google Gemini to extract structured data from resumes.")
    
    st.markdown("---")
    st.markdown("### ⚙️ Capabilities")
    st.markdown("""
    - 📄 Extracts Personal Info
    - 🎓 Parses Education
    - 💼 Analyzes Work History
    - 🛠️ Identifies Skills
    - 📊 Scores Resume Quality
    """)
    
    st.markdown("---")
    st.write("Built with ❤️ using Streamlit & Gemini")

# 4. Main Content Area
# Custom HTML Header
st.markdown("""
    <div class="header-container">
        <div class="header-title">📄 Smart Resume Parser</div>
        <div class="header-subtitle">Transform PDF Resumes into Structured Data Instantly</div>
    </div>
""", unsafe_allow_html=True)

# File Uploader Section
uploaded_file = st.file_uploader("📂 Upload a Resume (PDF)", type="pdf")

if uploaded_file is not None:
    # Processing Section
    with st.spinner("🤖 AI is reading the resume..."):
        try:
            # Simulate progress bar for better UX
            progress_bar = st.progress(0)
            
            # Step A: Extract Text
            raw_text = extract_text_from_pdf(uploaded_file)
            progress_bar.progress(50)
            
            # Step B: Send to Gemini AI
            data = parse_resume(raw_text)
            progress_bar.progress(100)
            time.sleep(0.5) # Small delay for visual effect
            progress_bar.empty()
            
            # Success Banner
            st.markdown('<div class="success-message">✅ Analysis Complete! Resume successfully parsed.</div>', unsafe_allow_html=True)
            
            # --- DISPLAY RESULTS ---
            
            # 1. Top Metrics Row
            score = data.get('resume_score', 0)
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">Resume Score</div>
                    <div class="metric-value">{score}/100</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="metric-card" style="border-left-color: #27ae60;">
                    <div class="metric-label">Experience Entries</div>
                    <div class="metric-value">{len(data.get('work_experience', []))}</div>
                </div>
                """, unsafe_allow_html=True)
                
            with col3:
                st.markdown(f"""
                <div class="metric-card" style="border-left-color: #e67e22;">
                    <div class="metric-label">Skills Identified</div>
                    <div class="metric-value">{len(data.get('skills', []))}</div>
                </div>
                """, unsafe_allow_html=True)

            st.write("") # Spacer
            st.write("")

            # 2. Detailed Analysis Layout
            col_main, col_side = st.columns([2, 1])
            
            with col_main:
                st.subheader("💼 Work Experience")
                if data.get('work_experience'):
                    for job in data.get('work_experience'):
                        with st.expander(f"{job.get('role', 'Role')} at {job.get('company', 'Company')}", expanded=True):
                            st.markdown(f"**📅 Duration:** {job.get('years', 'N/A')}")
                            st.markdown(f"**📝 Description:** {job.get('description', 'N/A')}")
                else:
                    st.info("No work experience found.")

                st.subheader("🎓 Education")
                if data.get('education'):
                    for edu in data.get('education', []):
                        st.markdown(f"- 🎓 {edu}")
                else:
                    st.info("No education found.")

            with col_side:
                st.subheader("👤 Candidate Details")
                with st.container():
                    st.markdown(f"**Name:** {data.get('full_name', 'N/A')}")
                    st.markdown(f"**Email:** {data.get('email', 'N/A')}")
                    st.markdown(f"**Phone:** {data.get('phone', 'N/A')}")
                
                st.markdown("---")
                
                st.subheader("🛠 Skills")
                st.markdown(
                    " ".join([f"`{skill}`" for skill in data.get('skills', [])])
                )
                
                st.markdown("---")
                
                st.subheader("💡 AI Tips")
                for tip in data.get('improvement_tips', []):
                    st.warning(f"• {tip}")

            # 3. Raw Data Toggle
            with st.expander("🔍 View Raw JSON Data"):
                st.json(data)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")