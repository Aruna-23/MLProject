                                               🧠Fashion Attribute Classification using Machine Learning

This project performs data preprocessing, visualization, and machine learning model comparison to classify fashion attributes from the dataset Attribute_DataSet.csv.
The models implemented include:

1) K-Nearest Neighbors (KNN)

2) Support Vector Machine (SVM)

3) Logistic Regression

4) Decision Tree

Each model is evaluated before and after hyperparameter tuning, and results are visualized using accuracy plots and confusion matrices.

🧩 Features

✅ Data Cleaning and Imputation

Handles missing values using the most frequent category for each feature

Visualizes missing data using MissingNo (bar, matrix, heatmap)

✅ Feature Encoding and Scaling

Encodes categorical variables using LabelEncoder

Standardizes features with StandardScaler

✅ Model Training and Evaluation

Implements multiple ML algorithms (KNN, SVM, Logistic Regression, Decision Tree)

Evaluates models using accuracy, confusion matrix, F1 score, and classification report

✅ Hyperparameter Tuning

Uses GridSearchCV to find optimal parameters

Compares model performance before and after tuning

✅ Visualization

Confusion matrices plotted with Seaborn heatmaps

Accuracy comparison line graphs before and after tuning
