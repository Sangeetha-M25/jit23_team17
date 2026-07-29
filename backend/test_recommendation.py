from recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

print("\nConcentration Products\n")

for item in engine.recommend("Concentration"):

    print(item)

print("\nRelaxed Products\n")

for item in engine.recommend("Relaxed"):

    print(item)