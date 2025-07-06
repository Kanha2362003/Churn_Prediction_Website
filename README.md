# Churn_Prediction_Website
This project focuses on predicting customer churn — that is, identifying which customers are likely to stop using a company’s service — using exploratory data analysis (EDA), machine learning models, and an interactive web application built with Streamlit.

✅ 📌 Key Components
1️⃣ Data Analysis
Perform Exploratory Data Analysis (EDA) to understand the dataset.

Visualize trends, correlations, and key features affecting churn.

Handle missing values, outliers, and feature encoding.

Balance the dataset if it’s imbalanced (e.g., with SMOTE or resampling).

2️⃣ Machine Learning Models
Train multiple classification models:

Logistic Regression

Decision Tree

Random Forest

Gradient Boosting (e.g., XGBoost)

Evaluate models using:

Accuracy, Precision, Recall, F1-Score, ROC-AUC

Select the best model based on performance metrics.

Save the trained model with pickle or joblib.

3️⃣ Streamlit Web App
Build an interactive web app using Streamlit.

Key features:

Upload customer data or input customer details manually.

Display predictions: Churn or Not Churn.

Show probability scores.

Include EDA visuals for business understanding.

Deploy locally or to Streamlit Cloud / Heroku for public access.

✅ 📌 Folder Structure
Example:

bash
Copy
Edit
Customer-Churn-Prediction/
│
├── data/                  # Raw and processed data
├── notebooks/             # Jupyter notebooks for EDA & modeling
├── app_churn.py           # Streamlit app
├── model.pkl              # Saved ML model
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
└── images/                # EDA plots or screenshots
✅ 📌 How to Run the App
1️⃣ Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
2️⃣ Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the app

bash
Copy
Edit
streamlit run app_churn.py
✅ 📌 Tools & Technologies
Python

Pandas, NumPy, Matplotlib, Seaborn — for data analysis & visualization.

Scikit-learn, XGBoost — for ML modeling.

Streamlit — for building the web app.

Pickle/Joblib — for model serialization.

✅ 📌 Features
📊 Interactive EDA dashboards.

🔍 Multiple ML models with evaluation metrics.

⚙️ Predict churn for new customer data.

🌐 Simple user-friendly web interface.

🚀 Easy deployment to Streamlit Cloud / Heroku.
