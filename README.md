# 🏠 House Price Prediction using Linear Regression

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-green)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---

## 📌 Abstract

House price prediction is an important application of machine learning that helps buyers, sellers, and real estate professionals make informed decisions. Property prices depend on various factors such as location, area, number of bedrooms, number of bathrooms, and construction year.

This project develops a **House Price Prediction System using Linear Regression implemented from scratch**.

The project includes:

- Data Collection  
- Data Preprocessing  
- Feature Engineering  
- Manual Linear Regression Implementation  
- Model Evaluation  
- Flask Web Deployment  

The model is evaluated using:

- Mean Absolute Error (MAE)  
- Mean Squared Error (MSE)  
- Root Mean Squared Error (RMSE)  
- R² Score  

The trained model is deployed using a **Flask-based web application** for real-time house price prediction.

---

# 📖 Table of Contents

1. Introduction  
2. Problem Statement  
3. Objectives  
4. Scope  
5. System Requirements  
6. Dataset Description  
7. Methodology  
8. System Architecture  
9. Implementation  
10. Results and Analysis  
11. Output  
12. Advantages  
13. Limitations  
14. Future Enhancements  
15. Conclusion  
16. References  

---

# 1. Introduction

The real estate industry requires accurate house price estimation systems. Manual price estimation methods are:

- ❌ Time-consuming  
- ❌ Inconsistent  
- ❌ Error-prone  

Machine learning enables automated price prediction by analyzing historical housing data.

This project builds a **Multiple Linear Regression model manually using NumPy and SVD**, and deploys it using Flask.

---

# 2. Problem Statement

Determining house prices manually is complex due to multiple influencing factors:

- Location  
- Property size  
- Number of bedrooms  
- Bathrooms  
- Construction year  
- Market trends  

There is a need for an automated system that:

- Learns from historical data  
- Predicts prices accurately  
- Provides real-time predictions  
- Is simple and interpretable  

---

# 3. Objectives

- Analyze historical housing data  
- Perform data preprocessing  
- Implement Linear Regression from scratch  
- Evaluate model using regression metrics  
- Develop a Flask web application  
- Provide real-time house price predictions  

---

# 4. Scope of the Project

✔ Predict house prices using Linear Regression  
✔ Use structural and location-based features  
✔ Implement full ML workflow  
✔ Deploy using Flask  

Limitations:

- Assumes linear relationship  
- Does not include real-time market data  
- Designed mainly for educational purposes  

---

# 5. System Requirements

##  Hardware

- Processor: Intel i3 or higher  
- RAM: Minimum 4GB (8GB recommended)  
- Storage: 10GB free space  
- 64-bit architecture  

##  Software

- Python 3.10+
- Flask
- NumPy
- Pandas
- Scikit-learn (for train-test split)
- Pickle / Joblib
- Gunicorn (deployment)
- HTML, CSS (Frontend)

---

# 6. Dataset Description

- 📊 4600 Rows  
- 📈 18 Columns  
- 🎯 Target Variable: `price`  

## Important Features:

- bedrooms  
- bathrooms  
- sqft_living  
- sqft_lot  
- floors  
- waterfront  
- view  
- condition  
- sqft_above  
- sqft_basement  
- yr_built  
- yr_renovated  
- city (encoded)  
- country (encoded)  
- year, month, day  

Dataset split:

- 80% Training  
- 20% Testing  

---

# 7. Methodology

## 7.1 Data Collection

Housing dataset collected in CSV format containing historical sales records.

---

## 7.2 Data Preprocessing

- Removed unnecessary columns (`street`, `statezip`)
- Converted `date` column into:
  - year
  - month
  - day
- Encoded categorical variables:
  - country → USA = 1, others = 0
  - city → Manual label encoding
- Separated:
  - X → Features
  - y → Target (price)
- Train-test split (80:20)

---

## 7.3 Feature Selection

Selected meaningful attributes affecting house price to:

- Reduce model complexity
- Improve interpretability
- Enhance computational efficiency

---

## 7.4 Model Development (Linear Regression using SVD)

Model implemented manually using NumPy.

### Steps:

1. Convert data to NumPy arrays  
2. Mean centering  
3. Apply Singular Value Decomposition  
4. Compute pseudo-inverse  
5. Calculate regression coefficients  
6. Compute intercept  

---

## 7.5 Evaluation Metrics

### 📌 Mean Squared Error (MSE)

```math
MSE = (1/n) Σ (yi - ŷi)²
```

### 📌 Root Mean Squared Error (RMSE)

```math
RMSE = √MSE
```

### 📌 Mean Absolute Error (MAE)

```math
MAE = (1/n) Σ |yi - ŷi|
```

### 📌 R² Score

```math
R² = 1 - (SS_res / SS_total)
```

---

# 8. System Architecture

### 🔹 Dataset Layer  
Raw housing dataset (CSV)

### 🔹 Preprocessing Layer  
Cleaning, encoding, feature engineering

### 🔹 Model Training Layer  
Manual Linear Regression using SVD

### 🔹 Model Storage Layer  
Model saved as `.pkl` file

### 🔹 Web Application Layer  
Flask backend + HTML frontend

### 🔹 Prediction Output Layer  
Predicted price displayed to user

---

# 9. Implementation

## 🔹 Model Training

- Load dataset
- Preprocess data
- Train regression model
- Save model using Pickle

## 🔹 Model Testing

- Predict on unseen test data
- Calculate MSE, RMSE, MAE, R²

## 🔹 Flask Integration

- User enters house details
- Backend preprocesses input
- Model predicts price
- Result displayed instantly

---

# 10. Results and Analysis

## 📊 Training Results

- Low MSE
- Acceptable RMSE
- Good MAE
- R² ≈ 0.55  

Model explains ~55% of variance in training data.

---

## 📊 Testing Results

- Metrics close to training results  
- No significant overfitting  
- Good generalization ability  

---

# 11. Output

### ✔ Dataset Overview
- 4600 rows
- 18 columns

### ✔ Training Metrics
Model successfully learned relationships between features and prices.

### ✔ Testing Metrics
Model performs well on unseen data.

### ✔ Sample Prediction
System predicts house price for new inputs.

### ✔ Flask Web Application
- User-friendly interface
- Real-time prediction
- Integrated trained model

---

# 12. Advantages

- Automated price prediction  
- Simple & interpretable model  
- Low computational cost  
- Fast predictions  
- End-to-end ML pipeline  
- Easy to maintain  

---

# 13. Limitations

- Assumes linear relationship  
- Cannot capture complex nonlinear patterns  
- Sensitive to outliers  
- Limited scalability  
- Accuracy depends on dataset quality  

---

# 14. Future Enhancements

- Implement Random Forest  
- Implement Gradient Boosting  
- Add Neural Networks  
- Include Latitude & Longitude features  
- Deploy on AWS / Azure / GCP  
- Add Dashboard & Visualizations  
- Continuous model retraining  

---

# 15. Conclusion

The House Price Prediction System demonstrates the practical implementation of machine learning in the real estate domain.

The project includes:

- Complete data preprocessing  
- Manual regression implementation  
- Model evaluation  
- Flask-based deployment  

It serves as a strong foundation for understanding end-to-end machine learning workflows.

---

# 16. References

1. Kaggle – House Price Dataset  
   https://www.kaggle.com  

2. Scikit-learn Documentation  
   https://scikit-learn.org  

3. Python Documentation  
   https://docs.python.org  

4. Flask Documentation  
   https://flask.palletsprojects.com  

5. Tom M. Mitchell – *Machine Learning*, McGraw-Hill  

---

# 👩‍💻 Author

**G. Chaithanya**  


---

⭐ If you found this project useful, consider giving it a star!
