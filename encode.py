import pandas as pd
import joblib

print("🔄 Starting encoding process...")

cleaned_path = r"C:/Users/shenbagam/Downloads/swiggy/cleaneddata.csv"
print("C:/Users/shenbagam/Downloads/swiggy/cleaneddata.csv")
cleaned_df = pd.read_csv(cleaned_path)

cleaned_df['cuisine'] = cleaned_df['cuisine'].astype(str).str.lower()
cleaned_df = cleaned_df.assign(cuisine=cleaned_df['cuisine'].str.split(','))
cleaned_df = cleaned_df.explode('cuisine')
cleaned_df['cuisine'] = cleaned_df['cuisine'].str.strip()

categorical_cols = ['city', 'cuisine']
encoded_cats = pd.get_dummies(cleaned_df[categorical_cols], drop_first=False)
encoded_df = pd.concat(
    [cleaned_df[['id', 'name']], encoded_cats, cleaned_df[['rating', 'cost']]],
    axis=1
)
encoded_csv_path = r"C:/Users/shenbagam/Downloads/swiggy/encoder.csv"
encoded_pkl_path = r"C:/Users/shenbagam/Downloads/swiggy/encoder.pkl"

encoded_df.to_csv(encoded_csv_path, index=False)
joblib.dump(encoded_df, encoded_pkl_path, compress=3)
print("✅ Encoder CSV + PKL saved successfully!")
