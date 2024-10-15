from flask import Blueprint, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor

crop1=Blueprint('crop1',__name__)


# Load the dataset
crop_data = pd.read_csv('dataset/dataset.csv')

# Handle missing values for numeric features
numeric_features = crop_data.select_dtypes(include=['number']).columns
numeric_imputer = SimpleImputer(strategy='mean')
crop_data[numeric_features] = numeric_imputer.fit_transform(crop_data[numeric_features])

# Handle missing values for categorical features
categorical_features = crop_data.select_dtypes(include=['object']).columns
for col in categorical_features:
    crop_data[col].fillna(crop_data[col].mode()[0], inplace=True)

# Encode categorical features
le = LabelEncoder()
for col in categorical_features:
    crop_data[col] = le.fit_transform(crop_data[col])

# Define features and target
features = ['Nitrogen (%)', 'Phosphorous (%)', 'Potash (%)', 'Area Planted (acres)', 'Harvested Area (acres)']
target = 'Lint Yield (Pounds/Harvested Acre)'

# Split data into features and target variable
X = crop_data[features]
y = crop_data[target]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

@crop1.route('/input2')
def input2():
    return render_template('input2.html')

@crop1.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        algorithm = request.form['algorithm']
        nitrogen = float(request.form['nitrogen'])
        phosphorous = float(request.form['phosphorous'])
        potash = float(request.form['potash'])
        area_planted = float(request.form['area_planted'])
        harvested_area = float(request.form['harvested_area'])

        if algorithm == 'decision_tree':
            model = DecisionTreeRegressor()
        elif algorithm == 'gradient_boosting':
            model = GradientBoostingRegressor()
        else:
            return "Invalid algorithm choice!"

        model.fit(X_train, y_train)

        # Make prediction
        prediction = model.predict([[nitrogen, phosphorous, potash, area_planted, harvested_area]])

        return render_template('result1.html', algorithm=algorithm, prediction=prediction[0])
