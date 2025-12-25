import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

# 1. Load Secrets
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. Initialize the New Client
if api_key:
    client = genai.Client(api_key=api_key)
else:
    st.error("Missing API Key! Please add it to your .env file.")
    st.stop()

# 3. UI Setup
st.set_page_config(page_title="AI Spam Filter", page_icon="🛡️")
st.title("🛡️ Email Spam Classifier")
st.write("Using Gemini 3 Flash to detect complex phishing and spam.")

email_input = st.text_area("Paste the email text here:", height=250)

if st.button("Classify Email"):
    if not email_input.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Analyzing with Security Logic..."):
            try:
                # 4. Structured Prompting Logic
                prompt = f"""
                You are an expert Cybersecurity Analyst. Classify the email below as 'SPAM' or 'NOT SPAM'.
                
                CRITERIA FOR 'NOT SPAM':
                - Legitimate automated notifications (GitHub, Google, LinkedIn).
                - Personalized details (specific project names, correct usernames).
                - Links lead to official domains (e.g., github.com).
                
                CRITERIA FOR 'SPAM':
                - Phishing, unsolicited marketing, or suspicious 'look-alike' links.
                - Requests for passwords, urgent financial action, or unusual attachments.
                
                Provide the result in this format:
                VERDICT: [SPAM/NOT SPAM]
                CONFIDENCE: [0-100%]
                REASON: [One clear sentence]
                
                EMAIL CONTENT:
                {email_input}
                """
                
                # Using gemini-3-flash-preview for the best 2025 performance
                response = client.models.generate_content(
                    model="gemini-3-flash-preview",
                    contents=prompt
                )
                
                # 5. Result Display
                result_text = response.text
                if "VERDICT: SPAM" in result_text.upper():
                    st.error(result_text)
                else:
                    st.success(result_text)
                    
            except Exception as e:
                st.error(f"Analysis Error: {e}")

st.divider()
st.caption("Secured by Gemini 3 Flash • Google GenAI SDK v1.56")