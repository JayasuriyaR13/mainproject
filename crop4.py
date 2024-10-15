from flask import Blueprint, request, jsonify, render_template
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

crop4 = Blueprint('crop4', __name__)

# Load dataset
dataset = pd.read_csv("dataset/SMART.csv")

# Remove any leading/trailing spaces from column names
dataset.columns = dataset.columns.str.strip()

# Separate features (X) and target variable (y)
X = dataset.drop('label', axis=1)
y = dataset['label']

# Define preprocessing steps
numeric_features = ['pH Level', 'Organic Matter (%)', 'Nitrogen Content (kg/ha)', 'Phosphorus Content (kg/ha)', 'Potassium Content (kg/ha)']
numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

categorical_features = ['Soil Type', 'Irrigation Method']
categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Append classifier to preprocessing pipeline
clf = Pipeline(steps=[('preprocessor', preprocessor),
                      ('classifier', RandomForestClassifier(random_state=42))])

# Split dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit model
clf.fit(X_train, y_train)

@crop4.route('/input4')
def input4():
    return render_template('input4.html')

@crop4.route('/predicting', methods=['POST'])
def predicting():
    data = request.form.to_dict()
    data_df = pd.DataFrame([data])
    
    # Convert columns to appropriate types
    data_df = data_df.rename(columns={
        "ph_level": "pH Level",
        "organic_matter": "Organic Matter (%)",
        "nitrogen_content": "Nitrogen Content (kg/ha)",
        "phosphorus_content": "Phosphorus Content (kg/ha)",
        "potassium_content": "Potassium Content (kg/ha)",
        "soil_type": "Soil Type",
        "irrigation_method": "Irrigation Method"
    })

    for col in numeric_features:
        data_df[col] = data_df[col].astype(float)
    
    prediction = clf.predict(data_df)
    return render_template('result2.html', prediction=prediction[0])
