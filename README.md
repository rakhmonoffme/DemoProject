# 🧠 Personality Predictor – Extrovert vs Introvert

This project is a **machine learning classification model** that predicts whether a person is an **Extrovert** or **Introvert** based on behavioral and social interaction features.  
The model is deployed as an **interactive web app** for real-time predictions.

**🔗 Live App:** [https://personality-prediction-ten.vercel.app](https://personality-prediction-ten.vercel.app)

---

## 📊 Dataset Overview

- **Source**: Custom / collected dataset  
- **Size**: N entries × 7 columns  
- **Target Variable**: Personality type (Extrovert / Introvert)

### Features:

| Feature                     | Description                                         |
|-----------------------------|-----------------------------------------------------|
| 🕒 Time Spent Alone          | Average hours spent alone per day                   |
| 🎤 Stage Fear                | Level of public speaking anxiety                    |
| 🎉 Social Event Attendance   | Frequency of attending social gatherings            |
| 🚶 Going Outside             | How often the person goes outdoors                  |
| 😩 Drained After Socializing | Tendency to feel exhausted after socializing         |
| 👥 Friends Circle Size       | Number of close friends                             |
| 📱 Post Frequency            | Social media posting frequency                      |

---

## 🎯 Objective

Predict whether a person is more likely to be an **Extrovert** or **Introvert** using lifestyle and social activity indicators.

---

## ⚙️ Model Training

### Algorithms Explored:  
- Logistic Regression  
- Decision Tree Classifier  
- XGBoost  
- **RandomForestClassifier ✅ (Best)**

### ✅ Best Model: RandomForestClassifier  
- **Accuracy**: ~85%

---

## 📈 Evaluation

- Metrics: Accuracy, Precision, Recall, and F1-score  
- In the web app: Displays predicted personality along with model confidence score

---

## 🛠 Feature Engineering

- Encoding categorical variables  
- Scaling numerical features where needed  
- Dropping irrelevant fields

---

## 🚀 Deployment

- Trained RandomForestClassifier model saved as `.pkl` file  
- Integrated into a **Streamlit** / Vercel-hosted web app  
- Takes real-time inputs and instantly predicts personality type

---

## ✅ Model Strengths

- High classification accuracy  
- Interpretable model outputs  
- Fast inference speed

---

## 📬 Contact

If you have any questions, suggestions, or feedback, feel free to reach out:  

📧 **rakhmonovbb@gmail.com**
