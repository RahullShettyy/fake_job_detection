# 🛡️ JobGuard AI - Job Scam Detection System

**JobGuard AI** is a machine learning-powered web application designed to help job seekers identify fraudulent job postings. 
By analyzing job descriptions or email text, the system predicts whether a job offer is "Real" or a "Potential Scam" using Natural Language Processing (NLP).

---

## 🚀 Features
* **Real-Time Analysis:** Instantly analyzes job text to detect scam patterns.
* **Confidence Score:** Provides a percentage score indicating the likelihood of a scam.
* **Smart Classification:**
    * 🟢 **Green:** Likely Legitimate
    * 🟡 **Yellow:** Suspicious / Caution
    * 🔴 **Red:** High Risk / Scam
* **Modern UI:** Built with HTML5 and Tailwind CSS for a clean, responsive experience.
* **Professional Dataset:** Trained on the **EMSCAD** dataset (18,000+ real and fake job postings).

---

## 🛠️ Tech Stack
* **Frontend:** HTML, CSS,Tailwind CSS (CDN)
* **Backend:** Python, Flask
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Algorithm:** SGDClassifier (Support Vector Machine) with TF-IDF Vectorization

---

## 📂 Project Structure
```text
job-scam-detector/
│
├── static/
│   └── style.css          # Custom animations and styling
├── templates/
│   └── index.html         # Main user interface
├── app.py                 # Flask backend server
├── train_model.py         # Script to train the AI model
├── scam_model.pkl         # The trained model (generated after running script)
├── fake_job_postings.csv  # Dataset (18,000 records)
└── requirements.txt       # List of Python dependencies
⚡ How to Run Locally1.
PrerequisitesMake sure you have Python installed.
Then, create a requirements.txt file and install the necessary libraries:Bashpip install flask scikit-learn pandas numpy joblib
2. Download the DatasetDownload the fake_job_postings.csv dataset and place it in the root folder.Download Dataset Here
3. Train the AI ModelBefore running the website, you must train the model once.
Open your terminal
run:Bashpython train_model.py
Wait for the message: ✅ SUCCESS! Model saved as 'scam_model.pkl'4.
Start the ApplicationRun the Flask server:Bashpython app.py
5. Access the WebsiteOpen your browser and go to:http://127.0.0.1:5000(Note: Do not use VS Code "Live Server". You must open the localhost link shown in the terminal.)
🧪 Testing the Model
Here are some prompts to test the system:Try a Real Job: Copy a job description from LinkedIn (e.g., Microsoft, Google) or type:"We are looking for a Software Engineer with 3 years of experience in Python. Full benefits, health insurance, and 401k included.
Apply on our official website."Try a Scam:"URGENT! You are hired for a data entry job. Earn $2000/week. No interview needed.
 Kindly send $200 via Western Union for software. Reply immediately with bank details."🔧
TroubleshootingErrorSolutionFileNotFoundError: 'scam_model.pkl'You forgot to run python train_model.py.
Run that script first to generate the brain of the AI.NameError: name 'app' is not definedYour app.py is incomplete. Ensure you copied the full code including app = Flask(__name__).
Dataset Download ErrorIf the script fails to download the CSV automatically, download it manually from the link in Step 2 and place it in the project folder.Site not working (Port 5500)You are likely using "Live Server".
 Close that tab and use the http://127.0.0.1:5000 link from your Python terminal.
📜 License & CreditsDataset: EMSCAD (Employment Scam Aegean Dataset)
Developer: [Rahul Shetty]
