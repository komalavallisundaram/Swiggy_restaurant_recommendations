import pandas as pd

file_path = r"C:/Users/shenbagam/Downloads/swiggy/swiggy.csv"

df = pd.read_csv(file_path)

df = df[['id','name','city','cuisine','rating','cost']].copy()


df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['cost'] = df['cost'].astype(str).str.replace('₹','', regex=False).str.replace(',','', regex=False)
df['cost'] = pd.to_numeric(df['cost'], errors='coerce')

df['city'] = df['city'].astype(str).str.strip().str.lower()
df['cuisine'] = df['cuisine'].astype(str).str.strip().str.lower()

df = df.dropna(subset=['rating','cost']).drop_duplicates()

df.to_csv(r"C:/Users/shenbagam/Downloads/swiggy/cleaneddata.csv", index=False)
print("✅ Cleaned data saved")
