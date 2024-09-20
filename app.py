from flask import Flask, request, jsonify, render_template
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn

app = Flask(__name__)

model = mlflow.sklearn.load_model(f"runs:/45b5223bc3c645daaf71a3c21765ca3c/model")

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        
        data = request.json
        
        
        input_df = pd.DataFrame([data])
        
        input_df = input_df[['age', 'sex', 'race', 'total_juvenile_offenses', 'detention_period', 'prior_offense_count', 'current_charge_degree']]
        print(input_df)
        
        input_df['age'] = input_df['age'].astype(int)
        input_df['sex'] = input_df['sex'].astype(int)
        input_df['race'] = input_df['race'].astype(int)
        input_df['total_juvenile_offenses'] = input_df['total_juvenile_offenses'].astype(int)
        input_df['detention_period'] = input_df['detention_period'].astype(int)
        input_df['prior_offense_count'] = input_df['prior_offense_count'].astype(int)
        input_df['current_charge_degree'] = input_df['current_charge_degree'].astype(int)
        prediction = model.predict(input_df)
        print(model)  
        print(prediction)
        
        response = {
            'prediction': int(prediction[0]), 
            'message': 'Success'
        }
        print(response)
        return jsonify(response)
        
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
