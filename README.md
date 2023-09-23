# **Liver Cirrhosis Prediction Web App**

This repository contains code for a web application that predicts the likelihood of a patient suffering from **liver cirrhosis** based on various health parameters. The application uses a machine learning model (K-Nearest Neighbors) trained on a dataset of health records.

## **Contents**

- `app.py`: The Flask web application script.
- `knn_model.pkl`: The trained K-Nearest Neighbors model for liver cirrhosis prediction.
- `scaler.pkl`: A pickled StandardScaler used to preprocess input data.
- `templates/`: HTML templates for the web pages.
- `static/`: Static files (e.g., CSS, JavaScript).
- `requirements.txt`: List of Python packages required to run the application.
- `README.md`: This readme file.

## **How to Use**

1. **Clone** this repository to your local machine.

2. Create a **virtual environment** and install the required packages from `requirements.txt`:

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
   pip install -r requirements.txt



Certainly! Here's the README.md content with some sections in bold:

markdown
Copy code
# **Liver Cirrhosis Prediction Web App**

This repository contains code for a web application that predicts the likelihood of a patient suffering from **liver cirrhosis** based on various health parameters. The application uses a machine learning model (K-Nearest Neighbors) trained on a dataset of health records.

## **Contents**

- `app.py`: The Flask web application script.
- `knn_model.pkl`: The trained K-Nearest Neighbors model for liver cirrhosis prediction.
- `scaler.pkl`: A pickled StandardScaler used to preprocess input data.
- `templates/`: HTML templates for the web pages.
- `static/`: Static files (e.g., CSS, JavaScript).
- `requirements.txt`: List of Python packages required to run the application.
- `README.md`: This readme file.

## **How to Use**

1. **Clone** this repository to your local machine.

2. Create a **virtual environment** and install the required packages from `requirements.txt`:

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
   pip install -r requirements.txt
Run the Flask application:

bash
Copy code
python app.py
Access the application in your web browser by going to http://localhost:5000.

Enter the patient's health parameters and click the "Predict" button to see the prediction.

About the Model
The model used in this application is a K-Nearest Neighbors (KNN) classifier trained on a dataset of health records. It predicts whether a patient is suffering from liver cirrhosis based on features such as duration of alcohol consumption, diabetes status, obesity, and various blood test results.

Credits
The dataset used for training the model is not included in this repository. It should be obtained separately.
