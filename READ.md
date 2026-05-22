# Swiggy’s Restaurant Recommendation System using Streamlit

## Project Title
Swiggy’s Restaurant Recommendation System using Streamlit

## Skills Takeaway
- Data Preprocessing
- One-Hot Encoding
- Clustering (K-Means, Cosine Similarity, or Similar Methods)
- Streamlit Application Development
- Python Programming

## Domain
Recommendation Systems and Data Analytics

## Problem Statement
The objective of this project is to build a **restaurant recommendation system** using Swiggy’s restaurant dataset (CSV format).  
The system recommends restaurants to users based on input features such as **city, rating, cost, and cuisine preferences**.  

The application leverages **clustering** and **similarity measures** to generate recommendations and displays results in a user-friendly **Streamlit interface**.

## Business Use Cases
- **Personalized Recommendations**: Help users discover restaurants tailored to their preferences.
- **Improved Customer Experience**: Provide suggestions that enhance decision-making.
- **Market Insights**: Understand customer preferences and behaviors for targeted marketing.
- **Operational Efficiency**: Enable businesses to optimize offerings based on popular demand.

## Approach

### Dataset Columns
`['id', 'name', 'city', 'rating', 'rating_count', 'cost', 'cuisine', 'lic_no', 'link', 'address', 'menu']`

- **Categorical**: name, city, cuisine  
- **Numerical**: rating, rating_count, cost  

### Steps
1. **Data Understanding and Cleaning**
   - Remove duplicates
   - Handle missing values
   - Save cleaned dataset → `cleaneddata.csv`

2. **Data Preprocessing**
   - Apply One-Hot Encoding to categorical features (`city`, `cuisine`)
   - Save encoder → `encoder.pkl`
   - Save encoded dataset → `encoder.csv`

3. **Recommendation Methodology**
   - Use **K-Means Clustering** or **Cosine Similarity**
   - Map results back to cleaned dataset for interpretation

4. **Streamlit Application**
   - User input: city, cuisine, rating, cost
   - Recommendation engine: filter + cluster
   - Output: top recommended restaurants

## Results
- **Cleaned Dataset**: duplicates/missing values removed  
- **Encoded Dataset**: categorical features encoded  
- **Encoder File**: reusable for future data  
- **Recommendation System**: clustering/similarity-based engine  
- **Streamlit App**: interactive UI for recommendations  

## Project Structure
