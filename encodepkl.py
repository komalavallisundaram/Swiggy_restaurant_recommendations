import pandas as pd
import pickle

encoded_df = pd.read_csv(r"C:/Users/shenbagam/Downloads/swiggy/encoder.csv")

with open(r"C:/Users/shenbagam/Downloads/swiggy/encoder.pkl","wb") as f:
    pickle.dump(encoded_df, f)

print("✅ Encoder PKL saved")
