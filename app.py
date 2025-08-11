from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import sys
import os
import webbrowser
from threading import Timer

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.pipeline.predict_pipeline import PredictPipeline, CustomData
from sklearn.preprocessing import LabelEncoder
from src.utils import load_object
from src.logger import setup_logger

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    logger = setup_logger(__name__)
    logger.info("Predict route accessed")
    if request.method == 'GET':
        logger.info("GET request received, rendering home.html")
        return render_template('home.html')
        
    else:
        try:
            # Match the form field names from your HTML
            data = CustomData(
                Time_spent_Alone=float(request.form.get('time_alone')),  # Fixed field name
                Stage_fear=float(request.form.get('stage_fear')),        # Fixed field name
                Social_event_attendance=float(request.form.get('social_events')),  # Fixed field name
                Going_outside=float(request.form.get('going_outside')),
                Drained_after_socializing=1.0 if request.form.get('drained_after_socializing') == 'Yes' else 0.0,
                Friends_circle_size=float(request.form.get('friends_circle')),
                Post_frequency=int(request.form.get('post_frequency'))  # Fixed field names
            )
            logger.info("Data received from form: %s", data)
            
            
            pred_df = data.get_data_as_dataframe()
            predict_pipeline = PredictPipeline()
            results_01 = predict_pipeline.predict(pred_df)
            logger.info("Prediction results: %s", results_01)
            
            label_encoder = load_object('artifacts/label_encoder.pkl')
            results = label_encoder.inverse_transform(results_01)
            logger.info("Decoded prediction results: %s", results)
            
            return render_template('home.html', results=results[0])
            
        except Exception as e:
            print(f"Error during prediction: {e}")  # For debugging
            return render_template('home.html', error=str(e))

if __name__ == "__main__":  # Fixed the syntax error
    print("Starting Flask app...")
    print("Navigate to: http://localhost:8080/predictdata")
    Timer(1, lambda: webbrowser.open("http://localhost:8080/predictdata")).start()
    app.run(host="0.0.0.0", port=8080, debug=True)
