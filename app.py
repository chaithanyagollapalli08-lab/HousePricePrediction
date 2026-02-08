import pickle
import numpy as np
from flask import Flask, render_template, request

# Load model dictionary
with open('house_pricepredicts.pkl', 'rb') as f:
    model_dict = pickle.load(f)

intercept = model_dict['intercept']
coefficients = model_dict['coefficients']

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form inputs as floats
        input_values = [float(i) for i in request.form.values()]
        input_array = np.array(input_values)

        # Compute prediction manually: y = intercept + sum(coeff_i * x_i)
        prediction = intercept + np.dot(coefficients, input_array)

        return render_template('index.html', prediction_text=f"Predicted Price: ${prediction:,.2f}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
