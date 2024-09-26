# 📦 Streamlit App Starter Kit 
```
⬆️ popularity of Instagram posts
```
## Demo App

[![Streamlit App]((https://iktsemesteraufgabe-j4djtx24cp8hbadehnzzapp.streamlit.app/))

## GitHub Codespaces

Open in GitHub Codespaces:(https://github.com/elsa-1999/IKT_SemesterAufgabe.git))

## Section Heading

-Some installations needed for the Project:
-anaconda--> to Access jupyter noteBook
-pyCharm --> use to create the streamlite app


Instagram Post Popularity Prediction

Table of Contents
1. Introduction
2. Business Problem
3. Data Understanding
4. Data Preparation
5. Modeling
6. Model Evaluation
7. Model Deployment
8. Conclusion
9. Future Work


1.Introduction
In this project, the goal is to predict the popularity of Instagram posts based on various attributes of the post, 
such as video views, post type, and other features. This prediction can help marketers and content creators better 
understand the elements that make a post successful in terms of engagement (likes).

2.Business Problem
In today’s social media-driven world, the success of a post on platforms like Instagram can be a significant driver of 
business growth. Predicting post popularity can help businesses, influencers, and marketing teams optimize content 
creation strategies. The business needs are:
- To determine which features most impact post engagement (likes).
- To build a predictive model to estimate the number of likes a new post will receive


3.Data Understanding

3.1. Data Collection
The dataset used in this project contains information about Instagram posts, including:
- videoViewCount: The number of views on the video.
- likesCount: The target variable that represents the number of likes.
- productType: Categorical feature that describes the type of product in the post.
- type: Categorical feature that describes the content type (e.g., video, image).

3.2. Initial Data Exploration
Key statistics about the data were collected, including distributions, missing values, and basic visualizations.

- Data Shape: The dataset contains X records and Y columns.
- Missing Values: No missing values were detected in this dataset.

3.3. Data Visualization

- Distribution of Likes: The likesCount is right-skewed, indicating that most posts receive a lower number of likes, while only a few posts go viral.
  
- Correlation Matrix:
  A correlation analysis revealed a high correlation (> 0.90) between videoViewCount and videoPlayCount, indicating a strong linear relationship between these two features.
  
  
4.Data Preparation

4.1. Data Cleaning
The initial dataset was cleaned by handling categorical variables and scaling the numerical features:
- Encoding Categorical Variables: The productType and type columns were encoded using LabelEncoder to convert categorical values into numerical representations.
- Feature Scaling: The StandardScaler was used to standardize the numerical features (videoViewCount) to ensure all features are on the same scale.

4.2. Splitting Data
The dataset was split into training (80%) and testing (20%) sets using train_test_split.


5. Modeling

5.1. Model Selection
Several models were tested on the dataset:
- Random Forest:
- Linear Regression: A simple regression model that assumes a linear relationship between the features and the target.
- Ridge Regression: A regularized version of linear regression that reduces overfitting.
- Lasso Regression: Similar to Ridge but with L1 regularization, which also helps with feature selection.

5.2. Model Training
The models were trained on the scaled training data (X_train and y_train). 
Hyperparameter tuning was performed using Grid Search for the regularization models.


6.Model Evaluation

6.1. Performance Metrics
Models were evaluated using the R-squared score and RMSE (Root Mean Squared Error):
- Random Forest: R²= 0.5761910878925839
- Linear Regression: R² = 0.8901797240242584
- Ridge Regression: R² = 0.8017012859106458 
- Lasso Regression: R² = 0.8754304440551823

Based on the results, Linear Regression provided the best performance with an R² of 0.8901797240242584.

6.2. Model Tuning
Hyperparameter tuning was performed for Ridge and Lasso regressions, but neither surpassed the performance of the 
linear regression model.


7. Model Deployment

The chosen model (Linear Regression) was saved for deployment in a Streamlit app. The StandardScaler and LabelEncoders used during preprocessing 
were also saved to ensure consistency when processing new data.

A Streamlit app was created to allow users to upload new Instagram post data and predict the number of likes.


8. Conclusion

The linear regression model was the best-performing model for predicting Instagram post popularity, with an R² of 0.8901797240242584. This shows a good ability to generalize on new data but leaves room for improvement.

8.1. Key Insights:
- Video View Count: Strong predictor of likes.
- Post Type: Categorical variable that impacts engagement, with certain product types receiving more likes.
- Hour 


9. Future Work

Further improvements can be made by:
1. Data Collection: Collect more data in others to extends use cases of our projects
1. Feature Engineering: Creating new features such as engagement rate (likes to views ratio) could improve model performance.
2. Exploring More Complex Models: Testing advanced models like Neural Networks could enhance prediction accuracy.
3. Hyperparameter Optimization: More exhaustive hyperparameter tuning might improve the regularized models (Ridge/Lasso).


## Sources

- Die Vorlesung
- Chatgpt
- https://youtu.be/xBDdZTBDhgk?si=LOrh8N18Yn8FC0lx
- Udemy: Machine Learning
