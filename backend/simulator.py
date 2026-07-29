import pandas as pd
import joblib

from recommendation_engine import recommend_products

# Load model
model = joblib.load("models/eeg_model.pkl")

# Load EEG dataset
data = pd.read_csv("Dataset/eeg_dataset.csv")

X = data.drop("Label", axis=1)

current_index = 0

def get_next_prediction():

    global current_index

    sample = X.iloc[[current_index]]

    prediction = model.predict(sample)[0]

    state = "Concentration" if prediction == 1 else "Relaxed"

    recommendations = recommend_products(prediction, 3)

    current_index += 1

    if current_index >= len(X):
        current_index = 0

    return {
        "state": state,
        "recommendations": recommendations
    }