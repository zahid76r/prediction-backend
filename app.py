from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow requests from WordPress

@app.route('/predict-manual', methods=['POST'])
def predict_manual():
    data = request.get_json()
    sequence = data.get('sequence', '')
    timeframe = data.get('timeframe', '5')

    if not sequence or not all(c in '01' for c in sequence):
        return jsonify({'error': 'Invalid input'}), 400

    # Simple dummy prediction logic
    ones = sequence.count('1')
    zeros = sequence.count('0')

    prediction = "UP" if ones >= zeros else "DOWN"
    confidence = round((ones / len(sequence)) * 100 if prediction == "UP" else (zeros / len(sequence)) * 100, 2)

    return jsonify({'prediction': prediction, 'confidence': confidence})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Get port from environment or default 5000
    app.run(host='0.0.0.0', port=port)
