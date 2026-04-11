🛡️ AI-Powered Email Spam Classifier

A modern, context-aware web application that classifies emails as **Spam** or **Not Spam** using the latest **Gemini 3 Flash** Large Language Model.

**Objective**: To help users detect phishing and email scams like
- Lottery/cash wins
- mails asking for important information like DOB, Phone number, Credit card details, etc.
- Responding to a social media or friend request
- Unknown links which direct users to a fake website or downloads a virus unknowingly on user device

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](ai-spam-classifier-ceqkrdomyfjzszkcktbadu.streamlit.app)

🚀 Overview
Unlike traditional spam filters that rely on simple keyword matching, this tool uses Generative AI to understand the intent and context of an email. It acts as a cybersecurity assistant, identifying sophisticated phishing attempts while reducing false positives for legitimate automated notifications (like GitHub or LinkedIn alerts).

✨ Key Features
- Contextual Analysis: Powered by Google Gemini 3 Flash to detect complex spam patterns.
- Cybersecurity Logic: Uses custom-engineered prompts to act like a security analyst.
- Secure Architecture: Implements industry-standard secret management (Streamlit Secrets & `.env`).
- Modern UI: Built with a clean, responsive interface using Streamlit.

**System Architecture**:
User sends prompt (email content) ---> LLM analyses it ---> A concise response appears on the screen, stating whether the email is legitimate or spam, with suitable explanation

🛠️ Tech Stack
- Language: Python 3.10+
- AI Model: Gemini 3 Flash (via Google GenAI SDK)
- Web Framework: Streamlit
- Deployment: Streamlit Community Cloud

**Debugging Log**:
- In the initial development stage the app was simply stating whether the entered email was legitimate or spam, without any explanation. This was vague and unprofessional so I implemented a percentage system (%spam or %not spam) with supportive facts.
- The prompt: "I would like to improve my web application to let the users know why and how the email is spam or not spam, as a simple classification with no facts is useless."
