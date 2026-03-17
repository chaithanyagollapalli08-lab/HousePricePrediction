<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>House Price Prediction</title>
</head>
<body>

    <h1>🏠 House Price Prediction Web App</h1>

    <h2>📌 Project Overview</h2>
    <p>
        This project is an end-to-end Machine Learning web application that predicts house prices 
        based on various property features. The model is trained on real-world housing data and 
        deployed using Flask, enabling users to get real-time predictions through a simple and 
        interactive web interface.
    </p>

    <h2>📊 Dataset Information</h2>
    <ul>
        <li><strong>Dataset:</strong> House Sales in King County, USA</li>
        <li><strong>Total Records:</strong> 21,613</li>
        <li><strong>Time Period:</strong> May 2014 – May 2015</li>
    </ul>

    <h3>🔑 Features Used</h3>
    <ul>
        <li>Bedrooms, Bathrooms</li>
        <li>Sqft Living, Sqft Lot</li>
        <li>Floors, Waterfront, View</li>
        <li>Condition</li>
        <li>Sqft Above, Sqft Basement</li>
        <li>Year Built, Year Renovated</li>
        <li>City (Encoded), Country (Encoded)</li>
        <li>Year, Month, Day</li>
    </ul>

    <h2>⚙️ Tech Stack</h2>
    <ul>
        <li><strong>Backend:</strong> Python, Flask</li>
        <li><strong>Machine Learning:</strong> Scikit-learn, NumPy, Pandas</li>
        <li><strong>Frontend:</strong> HTML, CSS</li>
        <li><strong>Deployment:</strong> Render</li>
        <li><strong>Version Control:</strong> GitHub</li>
    </ul>

    <h2>🔄 Project Workflow</h2>

    <h3>1. Data Preprocessing</h3>
    <ul>
        <li>Handled missing values</li>
        <li>Extracted date features (year, month, day)</li>
        <li>Encoded categorical variables</li>
        <li>Split dataset into training (80%) and testing (20%)</li>
    </ul>

    <h3>2. Model Training</h3>
    <ul>
        <li>Used Linear Regression algorithm</li>
        <li>Evaluation Metrics:
            <ul>
                <li>R² Score</li>
                <li>Mean Squared Error (MSE)</li>
                <li>Root Mean Squared Error (RMSE)</li>
            </ul>
        </li>
    </ul>

    <h3>3. Model Saving</h3>
    <ul>
        <li>Saved the trained model using pickle (.pkl)</li>
    </ul>

    <h3>4. Web Application</h3>
    <ul>
        <li>User inputs house details through UI</li>
        <li>Flask processes input data</li>
        <li>Model predicts and returns price</li>
    </ul>

    <h2>🚀 Deployment</h2>
    <p><strong>Platform:</strong> Render</p>

    <h3>Run Locally</h3>
    <pre>
pip install -r requirements.txt
python app.py
    </pre>

    <h3>Production Command</h3>
    <pre>
gunicorn app:app
    </pre>

    <h2>🔍 Sample Prediction</h2>

    <h3>Input:</h3>
    <ul>
        <li>Bedrooms: 2</li>
        <li>Bathrooms: 2</li>
        <li>Sqft Living: 300</li>
        <li>Sqft Lot: 500</li>
        <li>Floors: 3</li>
        <li>Waterfront: 0</li>
        <li>View: 2</li>
        <li>Condition: 4</li>
        <li>Sqft Above: 250</li>
        <li>Sqft Basement: 50</li>
        <li>Year Built: 2000</li>
        <li>Year Renovated: 0</li>
        <li>Day: 15</li>
        <li>Month: 6</li>
        <li>Year: 2014</li>
        <li>City (Encoded): 3</li>
        <li>Country (Encoded): 1</li>
    </ul>

    <h3>Output:</h3>
    <p><strong>➡️ Estimated Price: 417,322.15</strong></p>

    <h2>⚠️ Challenges Faced</h2>
    <ul>
        <li>Encoding categorical variables</li>
        <li>Handling frontend form inputs</li>
        <li>Model serialization using pickle</li>
        <li>Deployment issues</li>
    </ul>

    <h2>🔮 Future Enhancements</h2>
    <ul>
        <li>Implement advanced models (Random Forest, XGBoost)</li>
        <li>Add data visualization dashboard</li>
        <li>Store prediction history</li>
        <li>Docker deployment</li>
    </ul>

    <h2>📌 Conclusion</h2>
    <p>
        This project demonstrates a complete Machine Learning pipeline, from data preprocessing 
        and model building to deployment. It shows how ML models can be integrated into web 
        applications for real-time predictions.
    </p>

</body>
</html>

 
