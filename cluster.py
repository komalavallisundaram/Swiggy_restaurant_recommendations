import pandas as pd
import joblib
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD

print("🔄 Starting encoding + clustering process...")

csv_path = r"C:/Users/shenbagam/Downloads/swiggy/swiggy.csv"
df = pd.read_csv(csv_path)

required_cols = ['id','name','city','cuisine','rating','cost']
df = df.dropna(subset=required_cols)
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['cost'] = df['cost'].astype(str).str.replace('₹','', regex=False).str.replace(',','', regex=False).str.strip()
df['cost'] = pd.to_numeric(df['cost'], errors='coerce')
df = df[(df['rating'] >= 0) & (df['rating'] <= 5)]
df = df[df['cost'] >= 0]

df['cuisine'] = df['cuisine'].astype(str).str.lower()
df = df.assign(cuisine=df['cuisine'].str.split(','))
df = df.explode('cuisine')
df['cuisine'] = df['cuisine'].str.strip()

categorical_cols = ['city','cuisine']
encoded_cats = pd.get_dummies(df[categorical_cols], drop_first=False, sparse=True)
encoded_df = pd.concat([df[['id','name']], encoded_cats, df[['rating','cost']]], axis=1)

features = encoded_df.drop(columns=['id','name'])
svd = TruncatedSVD(n_components=200, random_state=42)  
features_reduced = svd.fit_transform(features)

kmeans = KMeans(n_clusters=5, random_state=42)
encoded_df['cluster'] = kmeans.fit_predict(features_reduced)
print("✅ KMeans clustering completed")

cos_sim = cosine_similarity(features_reduced)

def recommend_restaurants(restaurant_name, top_n=5):
    if restaurant_name not in encoded_df['name'].values:
        return f"Restaurant '{restaurant_name}' not found."
    idx = encoded_df[encoded_df['name'] == restaurant_name].index[0]
    sim_scores = list(enumerate(cos_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices = [i for i, _ in sim_scores[1:top_n+1]]
    return encoded_df.iloc[top_indices][['id','name','rating','cost','cluster']]

print("\n🔎 Recommendations for a sample restaurant:")
print(recommend_restaurants("Domino's Pizza", top_n=5))
