from decision_engine import DecisionEngine

engine = DecisionEngine()

predictions = [

    "Concentration",
    "Concentration",
    "Concentration",
    "Concentration",
    "Concentration",

    "Relaxed",
    "Relaxed",
    "Relaxed",
    "Relaxed",
    "Relaxed",

    "Concentration",
    "Concentration",
    "Concentration",
    "Concentration",
    "Concentration",
]

for p in predictions:

    result = engine.process_prediction(p)

    if result:
        print(result)

print("\nCart")

for item in engine.cart:
    print(item)