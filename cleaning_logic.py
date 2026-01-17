import re
import nltk
from nltk.corpus import stopwords

# Download the list of stop words (only needs to be done once)
nltk.download('stopwords')
nltk.download('punkt')

def clean_resume(resume_text):
    # 1. Convert to lowercase
    text = resume_text.lower()
    
    # 2. Remove URLs
    text = re.sub(r'http\S+\s*', ' ', text)
    
    # 3. Remove hashtags and mentions
    text = re.sub(r'#\S+', '', text)
    text = re.sub(r'@\S+', '', text)
    
    # 4. Remove special characters and punctuation
    text = re.sub(r'[^\w\s]', ' ', text)
    
    # 5. Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # 6. Remove Stopwords (common words that don't add meaning)
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [w for w in words if w not in stop_words]
    
    return " ".join(filtered_words)

# Test the function
sample = "Check out my portfolio at http://myweb.com! #DataScience @Hiring"
print(f"Original: {sample}")
print(f"Cleaned: {clean_resume(sample)}")
