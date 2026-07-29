import pandas as pd

data = pd.read_csv("Dataset/eeg_dataset.csv")

print(data.columns)
print(data.shape)