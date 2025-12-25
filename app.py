from flask import Flask, render_template, request, jsonify
import joblib

# --- 1. SETUP THE APP ---
app = Flask(__name__)

# --- 2. LOAD THE AI MODEL ---
# We wrap this in a try-except block so the app doesn't crash if the model is missing
try:
    model = joblib.load('scam_model.pkl')
    print("✅ Model loaded successfully!")
except Exception as e:
    print("❌ Error loading model: ", e)
    print("👉 Make sure you ran 'python train_model.py' first!")
    model = None

# --- 3. THE HOME PAGE ---
@app.route('/')
def home():
    return render_template('index.html')

# --- 4. THE PREDICTION LOGIC ---
@app.route('/predict', methods=['POST'])
def predict():
    # Check if model exists
    if model is None:
        return jsonify({'error': 'Model not found. Please run train_model.py first.'}), 500

    try:
        data = request.json
        email_text = data.get('content', '')
        
        # Check text length
        if not email_text or len(email_text) < 20:
            return jsonify({'error': 'Text is too short. Please paste the full job description.'}), 400

        # Predict using the loaded model
        # The model returns [Probability of Real, Probability of Fake]
        probs = model.predict_proba([email_text])[0]
        scam_probability = probs[1] * 100 

        # --- STRICTER LOGIC ---
        if scam_probability > 70:
            status_class = "danger"
            message = "⚠️ DANGER: High Risk of Scam"
        elif scam_probability > 30:
            status_class = "warning"
            message = "⚠️ CAUTION: Suspicious elements detected."
        else:
            status_class = "safe"
            message = "✅ LOOKS GENUINE: Standard corporate pattern."

        return jsonify({
            'status_class': status_class,
            'message': message,
            'confidence': round(scam_probability, 2)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# --- 5. START THE SERVER ---
if __name__ == '__main__':
    app.run(debug=True)