import streamlit as st
import pandas as pd

st.title("🍽️ Swiggy Restaurant Recommendation System")
st.markdown("Find the best restaurants based on your preferences")

cleaned_df = pd.read_csv(r"C:/Users/shenbagam/Downloads/swiggy/cleaneddata.csv")
cleaned_df['city'] = cleaned_df['city'].astype(str).str.strip().str.lower()
cleaned_df['cuisine'] = cleaned_df['cuisine'].astype(str).str.strip().str.lower()

city_options = sorted(cleaned_df['city'].dropna().unique().tolist())
cuisine_series = cleaned_df['cuisine'].dropna().astype(str).str.split(',')
cuisine_options = sorted(set(c.strip() for sublist in cuisine_series for c in sublist))

st.subheader("🔍 Select Your Preferences")
city = st.selectbox("Select City", city_options)
cuisine = st.selectbox("Select Cuisine", cuisine_options)

rating_min, rating_max = cleaned_df['rating'].min(), cleaned_df['rating'].max()
cost_min, cost_max = cleaned_df['cost'].min(), cleaned_df['cost'].max()

rating = st.slider("Minimum Rating", float(rating_min), float(rating_max), float(rating_min))
cost = st.slider("Maximum Cost", float(cost_min), float(cost_max), float(cost_max))

def recommend_top(city, cuisine, rating, cost, top_n=10):
   
    filtered_df = cleaned_df[
        (cleaned_df['city'] == city.lower()) &
        (cleaned_df['cuisine'].str.contains(cuisine.lower(), na=False)) &
        (cleaned_df['rating'] >= rating) &
        (cleaned_df['cost'] <= cost)
    ]
    if filtered_df.empty:
        return None
    
    filtered_df = filtered_df.sort_values(['rating','cost'], ascending=[False, True])
    
    return filtered_df[['id','name','city','cuisine','rating','cost']].head(top_n)

if st.button("Get Recommendations"):
    results = recommend_top(city, cuisine, rating, cost, top_n=10)

    if results is None or results.empty:
        st.warning("⚠️ No restaurants match your filters.")
    else:
        st.subheader("🍴 Top Recommended Restaurants")
        st.dataframe(results)
