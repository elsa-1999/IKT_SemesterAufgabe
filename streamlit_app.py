import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# Load the saved model
model = joblib.load('models/linear_model.pkl')

# Define a function to make predictions
def predict_likes(data, model):
# Assuming you already performed scaling on the dataset
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
# Make prediction using the loaded model
    prediction = model.predict(data_scaled)
    return prediction

# Streamlit App layout
st.title("Instagram Post Likes Prediction")
st.write("This app predicts the number of likes based on the post's features.")

# Input features for the prediction
post_type = st.selectbox("Post Type", options=['Image', 'Video'])
product_type = st.selectbox("Product Type",
                            options=['Beauty products', 'Content creation/Tourism', 'Entertainment', 'Housing', 'Logistics', 'blog', 'cloth', 'food', 'food/cakes'])
comments_count = st.number_input("Comments Count", min_value=0, max_value=12000, step=10)
hour = st.number_input("Hour of the day (0-23)", min_value=0, max_value=23, step=1)
day_of_week = st.number_input("Day of the week (0-6, where 0=Monday)", min_value=0, max_value=6, step=1)
video_view_count = st.number_input("Video View Count", min_value=0, max_value=1000000, step=100)
video_duration = st.number_input("Video Duration (seconds)", min_value=0, max_value=10000, step=1)

# Convert categorical values to numerical using the previously saved encodings
post_type_mapping = {'Image': 0, 'Video': 1}
product_type_mapping = {'Beauty products': 0, 'Content creation/Tourism': 1, 'Entertainment': 2, 'Housing': 3, 'Logistics': 4, 'blog': 5, 'cloth': 6, 'food': 7, 'food/cakes': 8}
product_type_encoded = product_type_mapping[product_type]
post_type_encoded = post_type_mapping[post_type]

# Prepare data for prediction
data_to_predict = pd.DataFrame({
    'videoViewCount': [video_view_count],
    'videoDuration': [video_duration],
    'commentsCount': [comments_count],
    'day_of_week': [day_of_week],
    'hour': [hour],
    'productType': [product_type_encoded],
    'type': [post_type_encoded]
})

# Button to make predictions
if st.button("Predict"):
    prediction = predict_likes(data_to_predict, model)
    st.write(f"The predicted number of likes is: {int(prediction[0])}")
