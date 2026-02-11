🩺 Multi-Disease Prediction Web Application using Machine Learning

A machine learning–based web application that predicts the likelihood of multiple diseases, including Diabetes, Breast Cancer, Heart Disease, and Parkinson’s Disease, using user-provided medical parameters. The system integrates trained ML models with a simple web interface to deliver real-time predictions.

This project demonstrates the end-to-end implementation of machine learning, from data preprocessing and model training to model deployment in a web application.

🚀 Features

Predicts Diabetes, Breast Cancer, Heart Disease, and Parkinson’s Disease

Uses supervised machine learning classification models

Real-time predictions through a web interface

Clean, modular, and scalable codebase

Easy to extend with new diseases or models

🧠 Machine Learning Models

Each disease prediction module is built using a separately trained ML model on standard healthcare datasets.

Diabetes Prediction – Based on clinical features such as glucose level, BMI, age, etc.

Breast Cancer Prediction – Classifies tumors as benign or malignant using diagnostic features.

Heart Disease Prediction – Predicts risk using cardiovascular health indicators.

Parkinson’s Disease Prediction – Uses biomedical voice measurements for prediction.

🛠️ Tech Stack

Programming Language: Python

Libraries: NumPy, Pandas, Scikit-learn

Web Framework: Streamlit / Flask

Model Storage: Pickle

IDE: VS Code / Spyder

📁 Project Structure
├── trained_models/
│   ├── diabetes_model.sav
│   ├── breast_cancer_model.sav
│   ├── heart_disease_model.sav
│   └── parkinsons_model.sav
│
├── datasets/
│   ├── diabetes.csv
│   ├── breast_cancer.csv
│   ├── heart.csv
│   └── parkinsons.csv
│
├── app.py / main.py
├── requirements.txt
└── README.md
⚙️ Installation & Setup

Clone the repository

git clone https://github.com/your-username/multi-disease-prediction-ml.git
cd multi-disease-prediction-ml

Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Run the application

For Streamlit

streamlit run app.py

For Flask

python app.py
📊 Datasets Used

Diabetes Dataset – PIMA Indians Diabetes Dataset

Breast Cancer Dataset – Wisconsin Breast Cancer Dataset

Heart Disease Dataset – UCI Heart Disease Dataset

Parkinson’s Dataset – UCI Parkinson’s Dataset

(All datasets are publicly available and used for educational purposes.)

⚠️ Disclaimer

This application is not a medical diagnostic tool.
It is intended only for educational and research purposes.
Always consult a qualified healthcare professional for medical advice or diagnosis.

🔮 Future Enhancements

Add more disease prediction modules

Improve model accuracy using advanced algorithms (XGBoost, Deep Learning)

Integrate database for user history

Deploy on cloud platforms (AWS / Heroku / Streamlit Cloud)

🤝 Contributing

Contributions are welcome!
Feel free to fork the repository, create a new branch, and submit a pull request.

⭐ Acknowledgments

UCI Machine Learning Repository

Scikit-learn Documentation

Open-source ML community

📬 Contact

If you find this project useful, consider giving it a ⭐ on GitHub!
