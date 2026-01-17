import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier # Switched from KNN
import pickle
import bz2

# --- 1. LOAD DATASETS (Same as before) ---
df1 = pd.read_csv('Dataset/Resume.zip')
df2 = pd.read_csv('Dataset/AI_Resume_Screening.zip')
df3 = pd.read_csv('Dataset/UpdatedResumeDataSet.zip')

df1 = df1.rename(columns={'Resume_str': 'Resume'})[['Category', 'Resume']]
df2 = df2.rename(columns={'Job Role': 'Category', 'Skills': 'Resume'})[['Category', 'Resume']]
df3 = df3[['Category', 'Resume']]
df_master = pd.concat([df1, df2, df3], ignore_index=True).dropna().drop_duplicates()

# --- 2. OPTIMIZED TRAINING ---
# We use 2000 features for a good balance of accuracy and size
tfidf = TfidfVectorizer(stop_words='english', max_features=2000) 
X = tfidf.fit_transform(df_master['Resume'])
y = df_master['Category']

# Random Forest is much smaller than KNN
model = RandomForestClassifier(n_estimators=100, max_depth=20, random_state=42)
model.fit(X, y)

# --- 3. SAVE ASSETS ---
with bz2.BZ2File('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('tfidf.pkl', 'wb') as f:
    pickle.dump(tfidf, f)

df_master.to_csv('Dataset/Master_Merged_Dataset.zip', index=False, compression='zip')
print("Success! Model is now ultra-lightweight.")