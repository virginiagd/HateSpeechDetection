from flask import Flask, request, jsonify, render_template
import re 
import pickle
import numpy as np
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
with open("tokenizer.pkl", "rb") as file:
    tokenizer = pickle.load(file)

model = load_model("saved_model.keras")
maximum_features = 500000
maximum_length = 150

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\d+', '', text)  # Remove numbers
    return text
def generate_prediction(sentence):
    try:
        sentence_cleaned = clean_text(sentence)
        sequence = tokenizer.texts_to_sequences([sentence_cleaned])
        if not sequence[0]:
            print("Warning: Tokenizer generated an empty sequence. Check your tokenizer vocabulary.")
        padded_sequence = pad_sequences(sequence, maxlen=maximum_length)
        prediction_prob = model.predict(padded_sequence).flatten()[0]
        prediction = int(prediction_prob > 0.5)
        # Optional debug output
        print(f"Cleaned Sentence: {sentence_cleaned}")
        print(f"Prediction: {prediction}")
        print(f"Prediction Probability: {prediction_prob}")
        return {"label": prediction, "probability": float(prediction_prob)}
    except Exception as e:
        print(f"Error during prediction: {e}")
        return None, None

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    data = request.json
    if not data or "text" not in data:
        return jsonify({"error": "No text provided!"}), 400

    input_text = data["text"]
   
    result = generate_prediction(input_text)
    return jsonify({
        "input_text": input_text,
        "prediction": result["label"],  
        "probability": result["probability"]  
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
