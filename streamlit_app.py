import streamlit as st
import pandas as pd
import joblib

# Load the saved model and encoders
model = joblib.load('models/linear_model.pkl')
product_type_encoder = joblib.load('models/label_encoder_product.pkl')
post_type_encoder = joblib.load('models/label_encoder_type.pkl')

# Define a function to make predictions
def predict_likes(data, model):
# Assuming you already performed scaling on the dataset
    scaler = joblib.load('models/scaler.pkl')
    data_scaled = scaler.transform(data)
# Make prediction using the loaded model
    prediction = model.predict(data_scaled)
    return prediction

# Streamlit App layout
st.title("Instagram Post Likes Prediction")
st.markdown("### Predict the number of likes based on the post's features")

# Input features for the prediction
st.sidebar.header("Input Features")
post_type = st.sidebar.selectbox("Post Type", options=['Image', 'Video'])
product_type = st.sidebar.selectbox("Product Type",
                            options=['Beauty products', 'Content creation/Tourism', 'Entertainment', 'Housing', 'Logistics', 'blog', 'cloth', 'food', 'food/cakes'])
comments_count = st.sidebar.number_input("Comments Count", min_value=0, max_value=1000000, step=10)
hour = st.sidebar.number_input("Hour of the day (0-23)", min_value=0, max_value=23, step=1)
day_of_week = st.sidebar.number_input("Day of the week (0-6, where 0=Monday)", min_value=0, max_value=6, step=1)
video_view_count = st.sidebar.number_input("Video View Count", min_value=0, max_value=1000000, step=100)
video_duration = st.sidebar.number_input("Video Duration (seconds)", min_value=0, max_value=10000, step=1)

# Convert categorical values to numerical using the loaded encoders
product_type_encoded = product_type_encoder.transform([product_type])[0]
post_type_encoded = post_type_encoder.transform([post_type])[0]

# Prepare data for prediction
data_to_predict = pd.DataFrame({
    'commentsCount': [comments_count],
    'productType': [product_type_encoded],
    'type': [post_type_encoded],
    'videoDuration': [video_duration],
    'videoViewCount': [video_view_count],
    'hour': [hour],
    'day_of_week': [day_of_week]
})

# Button to make predictions
if st.sidebar.button("Predict"):
    prediction = predict_likes(data_to_predict, model)
    st.write(f"The predicted number of likes is: {int(prediction[0])}")
