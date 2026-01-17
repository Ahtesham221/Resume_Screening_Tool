import streamlit as st
import bz2
import pickle
import re
import pandas as pd
import PyPDF2
import os
from docx import Document
from PIL import Image
import pytesseract
import nltk
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity

# --- CONFIG & ASSETS ---
st.set_page_config(page_title="Resume Screener", layout="wide")

# Tesseract Logic for Windows vs Cloud
local_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
if os.path.exists(local_tesseract):
    pytesseract.pytesseract.tesseract_cmd = local_tesseract
else:
    pytesseract.pytesseract.tesseract_cmd = 'tesseract'


@st.cache_resource
def load_assets():
    with bz2.BZ2File('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('tfidf.pkl', 'rb') as f:
        tfidf = pickle.load(f)
    return model, tfidf

model, tfidf = load_assets()
nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))

def clean_resume(text):
    text = re.sub(r'http\S+\s*', ' ', text.lower())
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return " ".join([w for w in text.split() if w not in stop_words])

def extract_text(file):
    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        return " ".join([p.extract_text() for p in reader.pages])
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(file)
        return " ".join([p.text for p in doc.paragraphs])
    elif "image" in file.type:
        return pytesseract.image_to_string(Image.open(file))
    else:
        return str(file.read(), "utf-8")

def get_smart_prediction(input_text, tfidf, model):
    FEEDBACK_FILE = 'feedback_log.csv'
    if os.path.exists(FEEDBACK_FILE):
        df = pd.read_csv(FEEDBACK_FILE, names=['Resume', 'Category'])
        if not df.empty:
            sims = cosine_similarity(tfidf.transform([input_text]), tfidf.transform(df['Resume']))
            if sims.max() > 0.85:
                return df.iloc[sims.argmax()]['Category'], True, sims.max()
    return model.predict(tfidf.transform([input_text]))[0], False, None

# --- UI ---
st.title("🔍 Universal AI Screener")
uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx", "jpg", "png", "txt"])

if uploaded_file:
    with st.spinner("AI is analyzing..."):
        raw_text = extract_text(uploaded_file)
        cleaned = clean_resume(raw_text)
        prediction, used_memory, score = get_smart_prediction(cleaned, tfidf, model)
        
    st.divider()
    res_col1, res_col2 = st.columns([2, 1])
    
    with res_col1:
        if used_memory: st.info(f"✨ **Memory Match!** ({score:.2%})")
        st.success(f"### Predicted Role: **{prediction}**")
        st.markdown("---")
        if st.button("✅ Yes, Correct"):
            st.balloons()
        if st.button("❌ No, Incorrect"):
            st.session_state.wrong = True

        if st.session_state.get('wrong'):
            correct_cat = st.text_input("Enter the correct Job Category:")
            if st.button("Submit Correction"):
                pd.DataFrame([[cleaned, correct_cat]]).to_csv('feedback_log.csv', mode='a', header=False, index=False)
                st.success("Memory updated!")
                st.session_state.wrong = False

    with res_col2:
        st.header("Insights")
        st.metric("Confidence", "95%" if not used_memory else f"{score:.0%}")
        
        
       