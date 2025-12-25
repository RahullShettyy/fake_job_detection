import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import make_pipeline
from sklearn.calibration import CalibratedClassifierCV
import joblib
import os

print("⏳ Loading dataset from local file...")

# 1. LOAD LOCAL DATA
file_path = 'fake_job_postings.csv'

if not os.path.exists(file_path):
    print(f"❌ ERROR: Could not find '{file_path}' in this folder.")
    print("👉 Please download it manually and put it in D:\\fake_job_detection\\")
    exit()

df = pd.read_csv(file_path)
print(f"✅ Dataset loaded! Found {len(df)} job records.")

# 2. CLEANING & PREPARING
# Combine columns to get maximum context
df.fillna('', inplace=True)
df['text'] = df['title'] + " " + df['department'] + " " + df['company_profile'] + " " + df['description'] + " " + df['requirements'] + " " + df['benefits']

# 3. FEATURE ENGINEERING
# ngram_range=(1, 2): Look at single words AND pairs of words. 
vectorizer = TfidfVectorizer(stop_words='english', max_features=10000, ngram_range=(1, 2))

# 4. MODEL SETUP
# class_weight='balanced': This tells the model "Scams are rare, so treat them as very important."
base_model = SGDClassifier(loss='hinge', class_weight='balanced', max_iter=1000, random_state=42)
calibrated_model = CalibratedClassifierCV(base_model, method='sigmoid')

model = make_pipeline(vectorizer, calibrated_model)

# 5. TRAIN ON EVERYTHING
X = df['text']
y = df['fraudulent']

print(f"🧠 Training model... This might take 30 seconds.")
model.fit(X, y)

# 6. SAVE
joblib.dump(model, 'scam_model.pkl')
print("\n✅ SUCCESS! Model saved as 'scam_model.pkl'")