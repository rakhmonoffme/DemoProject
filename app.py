# backend/app.py
from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import sys
import os
from flask_cors import CORS
from threading import Timer
import webbrowser

# Import your own modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.pipeline.predict_pipeline import PredictPipeline, CustomData
from src.utils import load_object
from src.logger import setup_logger

application = Flask(__name__)
app = application

# Allow CORS for React frontend
CORS(app, resources={r"/predict": {"origins": "*"}})

@app.route('/')
def home():
    return jsonify({"message": "Flask backend is running"})

@app.route('/predict', methods=['POST'])
def predict_datapoint():
    logger = setup_logger(__name__)
    logger.info("Predict route accessed via POST")

    try:
        # Accept form data (React sends x-www-form-urlencoded)
        form_data = request.form

        data = CustomData(
            Time_spent_Alone=float(form_data.get('time_alone', 0)),
            Stage_fear=float(form_data.get('stage_fear', 0)),
            Social_event_attendance=float(form_data.get('social_events', 0)),
            Going_outside=float(form_data.get('going_outside', 0)),
            Drained_after_socializing=float(form_data.get('drained_after_socializing', 0)),
            Friends_circle_size=float(form_data.get('friends_circle', 0)),
            Post_frequency=int(form_data.get('post_frequency', 0))
        )

        pred_df = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        results_01 = predict_pipeline.predict(pred_df).astype(np.int64)

        label_encoder = load_object('artifacts/label_encoder.pkl')
        results = label_encoder.inverse_transform(results_01)

        logger.info(f"Prediction: {results[0]}")
        return jsonify({"prediction": results[0]})

    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    print("Starting Flask app...")
    print("Navigate to: http://localhost:8080")
    Timer(1, lambda: webbrowser.open("http://localhost:8080")).start()
    app.run(host="0.0.0.0", port=8080, debug=True)
