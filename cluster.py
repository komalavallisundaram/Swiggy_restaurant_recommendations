import pandas as pd
import joblib
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from scipy.sparse import csr_matrix
from geopy.distance import geodesic


print("🔄 Starting clustering process...")

# Load encoder data
try:
    encoder_path = r"C:/Users/shenbagam/Downloads/swiggy/encoder.pkl"
    print("📂 Loading encoder.pkl...")
    df = joblib.load(encoder_path)
except:
    encoder_path = r"C:/Users/shenbagam/Downloads/swiggy/encoder.csv"
    print("📂 Loading encoder.csv...")
    df = pd.read_csv(encoder_path)

print(f"✅ Loaded {df.shape[0]} rows and {df.shape[1]} columns.")

# Prepare features
features = df.drop(columns=['id','name','rating','cost','latitude','longitude'], errors='ignore').astype(float).fillna(0)
features_sparse = csr_matrix(features)

# Dimensionality reduction
print("⚙️ Training TruncatedSVD...")
svd = TruncatedSVD(n_components=50, random_state=42)
reduced_features = svd.fit_transform(features_sparse)
print(f"✅ Reduced to {reduced_features.shape[1]} dimensions")

# Clustering
print("🔢 Training KMeans...")
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
labels = kmeans.fit_predict(reduced_features)
df["Cluster"] = labels
print("✅ Clustering complete.")

# Save models for backend use
joblib.dump(svd, r"C:/Users/shenbagam/Downloads/swiggy/svd.pkl")
joblib.dump(kmeans, r"C:/Users/shenbagam/Downloads/swiggy/kmeans.pkl")
joblib.dump(features.columns.tolist(), r"C:/Users/shenbagam/Downloads/swiggy/feature_names.pkl")

print("🎉 Backend clustering ready!")

