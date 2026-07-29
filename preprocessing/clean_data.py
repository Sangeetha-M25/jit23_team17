import pandas as pd

# Read files
con = pd.read_csv("Dataset/CON1/CON1.csv")
rel = pd.read_csv("Dataset/RELAXED1/RELAXED1.csv")

# Columns we need
features = [
    "Delta_TP9","Delta_AF7","Delta_AF8","Delta_TP10",
    "Theta_TP9","Theta_AF7","Theta_AF8","Theta_TP10",
    "Alpha_TP9","Alpha_AF7","Alpha_AF8","Alpha_TP10",
    "Beta_TP9","Beta_AF7","Beta_AF8","Beta_TP10",
    "Gamma_TP9","Gamma_AF7","Gamma_AF8","Gamma_TP10"
]

# Keep only EEG band features
con = con[features]
rel = rel[features]

# Add labels
con["Label"] = 1      # Concentration
rel["Label"] = 0      # Relaxed

# Combine
data = pd.concat([con, rel], ignore_index=True)

# Remove rows with missing values
data = data.dropna()

print("Final Dataset Shape:", data.shape)
print(data.head())

# Save
data.to_csv("Dataset/eeg_dataset.csv", index=False)

print("Dataset saved successfully!")