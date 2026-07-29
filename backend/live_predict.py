import numpy as np
import pandas as pd
import joblib

from pylsl import StreamInlet, resolve_streams
from scipy.signal import welch

from recommendation_engine import recommend_products

# ==========================================
# Load Trained Model
# ==========================================

model = joblib.load("models/eeg_model.pkl")

# ==========================================
# Connect to Muse EEG
# ==========================================

print("Searching for Muse EEG...")

streams = resolve_streams()

eeg_stream = None

for stream in streams:
    if stream.type() == "EEG":
        eeg_stream = stream
        break

if eeg_stream is None:
    raise RuntimeError("No EEG stream found!")

inlet = StreamInlet(eeg_stream)

print("Muse Connected Successfully!")

# ==========================================
# Parameters
# ==========================================

FS = 256          # Sampling Rate
WINDOW = 256      # 1 second

# ==========================================
# Band Power Function
# ==========================================

def bandpower(signal, fs, low, high):

    freqs, psd = welch(signal, fs=fs)

    idx = np.logical_and(freqs >= low, freqs <= high)

    if np.sum(idx) == 0:
        return 0

    return np.mean(psd[idx])

# ==========================================
# Live Prediction
# ==========================================

def get_next_prediction():

    samples = []

    while len(samples) < WINDOW:

        sample, timestamp = inlet.pull_sample()

        # Use only EEG channels
        samples.append(sample[:4])

    samples = np.array(samples)

    # ======================================
    # Signal Quality Check
    # ======================================

    signal_std = np.std(samples)

    print("Signal STD :", signal_std)

    if signal_std < 5:

        return {

            "state": "Wear Headset",

            "recommendations": []

        }

    # ======================================
    # Feature Extraction
    # ======================================

    features = []

    bands = [

        (0.5,4),     # Delta

        (4,8),       # Theta

        (8,13),      # Alpha

        (13,30),     # Beta

        (30,45)      # Gamma

    ]

    for low, high in bands:

        for ch in range(4):

            bp = bandpower(

                samples[:, ch],

                FS,

                low,

                high

            )

            features.append(bp)

    feature_names = [

        "Delta_TP9",
        "Delta_AF7",
        "Delta_AF8",
        "Delta_TP10",

        "Theta_TP9",
        "Theta_AF7",
        "Theta_AF8",
        "Theta_TP10",

        "Alpha_TP9",
        "Alpha_AF7",
        "Alpha_AF8",
        "Alpha_TP10",

        "Beta_TP9",
        "Beta_AF7",
        "Beta_AF8",
        "Beta_TP10",

        "Gamma_TP9",
        "Gamma_AF7",
        "Gamma_AF8",
        "Gamma_TP10"

    ]

    X = pd.DataFrame(

        [features],

        columns=feature_names

    )

    prediction = model.predict(X)[0]

    if prediction == 1:

        state = "Concentration"

    else:

        state = "Relaxed"

    recommendations = recommend_products(

        prediction,

        3

    )

    return {

        "state": state,

        "recommendations": recommendations

    }