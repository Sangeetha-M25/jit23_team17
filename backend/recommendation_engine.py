import pandas as pd
import random

# Load grocery dataset
products = pd.read_csv("Dataset/groceries.csv")

def recommend_products(brain_state, n=3):
    """
    brain_state:
    1 -> Concentration
    0 -> Relaxed
    """

    if brain_state == 1:
        state = "Concentration"
    else:
        state = "Relaxed"

    filtered = products[products["BrainState"] == state]

    recommendations = filtered.sample(min(n, len(filtered)))

    return recommendations.to_dict(orient="records")