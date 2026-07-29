import pandas as pd
import joblib
import time

# Load model
model = joblib.load("models/eeg_model.pkl")

# Load EEG dataset
data = pd.read_csv("Dataset/eeg_dataset.csv")

X = data.drop("Label", axis=1)

print("Starting Brain Simulation...\n")

for i in range(len(X)):
    sample = X.iloc[[i]]

    prediction = model.predict(sample)[0]

    if prediction == 1:
        state = "Concentration"
    else:
        state = "Relaxed"

    print(f"Sample {i+1} : {state}")

    time.sleep(2)