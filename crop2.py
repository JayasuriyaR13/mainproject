from flask import Blueprint,render_template,request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor


crop2=Blueprint('crop2',__name__)




# Load the dataset
crop_data = pd.read_csv('dataset/SMARTFARM.csv')

# Data preprocessing
le = LabelEncoder()
crop_data['Soil Type'] = le.fit_transform(crop_data['Soil Type'])
crop_data['Crop'] = le.fit_transform(crop_data['Crop'])
crop_data['Irrigation Method'] = le.fit_transform(crop_data['Irrigation Method'])

# Define features and target
features = ['Soil Type', 'pH Level', 'Organic Matter (%)', 'Nitrogen Content (kg/ha)', 'Phosphorus Content (kg/ha)', 'Potassium Content (kg/ha)', 'Crop', 'Irrigation Method', 'Water Availability (liters/hectare)']
target = 'Water Consumption (liters/hectare)'

# Split data into features and target variable
X = crop_data[features]
y = crop_data[target]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

@crop2.route('/input3')
def input3():
    return render_template('input3.html')

@crop2.route('/crop', methods=['POST'])
def crop():
    if request.method == 'POST':
        algorithm = request.form['algorithm']
        soil_type = int(request.form['soil_type'])
        ph_level = float(request.form['ph_level'])
        organic_matter = float(request.form['organic_matter'])
        nitrogen_content = float(request.form['nitrogen_content'])
        phosphorus_content = float(request.form['phosphorus_content'])
        potassium_content = float(request.form['potassium_content'])
        crop = int(request.form['crop'])
        irrigation_method = int(request.form['irrigation_method'])
        water_availability = float(request.form['water_availability'])

        # Choose algorithm based on user selection
        if algorithm == 'knn':
            model = KNeighborsRegressor(n_neighbors=5)
        elif algorithm == 'random':
            model = RandomForestRegressor(n_estimators=100, random_state=42)
        else:
            return "Invalid algorithm choice!"

        model.fit(X_train, y_train)

        # Make prediction
        prediction = model.predict([[soil_type, ph_level, organic_matter, nitrogen_content, phosphorus_content, potassium_content, crop, irrigation_method, water_availability]])

        return render_template('result.html', algorithm=algorithm, prediction=prediction[0])


