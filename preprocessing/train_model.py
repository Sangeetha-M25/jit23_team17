import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load Dataset
data = pd.read_csv("Dataset/eeg_dataset.csv")

# Features
X = data.drop("Label", axis=1)

# Labels
y = data["Label"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("="*40)
print("Accuracy :", accuracy)
print("="*40)

print(classification_report(y_test, y_pred))

# Save Model
joblib.dump(model, "models/eeg_model.pkl")

print("\nModel Saved Successfully!")