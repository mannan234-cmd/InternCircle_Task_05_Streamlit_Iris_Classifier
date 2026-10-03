# InternCircle Task 05: Streamlit Interactive ML Web App

## Iris Flower Classification

This project converts a trained Machine Learning classification model into an interactive web application using Streamlit.

The application allows users to enter Iris flower measurements through interactive sliders and receive a real-time prediction of the flower species.

## Objectives

The main objectives of this project are to:

* Train a Decision Tree Classification model.
* Save the trained model using Joblib.
* Build an interactive Streamlit web application.
* Allow users to enter flower measurements using sliders.
* Generate real-time predictions.
* Display the predicted Iris flower species.
* Display prediction confidence.
* Prepare the application for online deployment.

## Technologies Used

* Python
* Scikit-learn
* Streamlit
* Joblib
* NumPy
* Pandas
* Google Colab
* GitHub

## Dataset

The project uses the built-in Iris dataset provided by Scikit-learn.

The dataset contains four flower measurements:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

The model predicts one of three Iris species:

* Setosa
* Versicolor
* Virginica

## Machine Learning Model

A Decision Tree Classifier is used for flower classification.

The dataset is divided into training and testing sets. The model is trained using the training data and evaluated using the testing data.

The trained model is saved as:

`iris_model.pkl`

Joblib is used to save and load the trained model.

## Streamlit Application

The Streamlit application provides four interactive sliders for entering flower measurements.

After entering the measurements, the user clicks the **Predict Flower Species** button.

The application then:

1. Collects the user's input.
2. Converts the input into the required numerical format.
3. Sends the input to the trained Decision Tree model.
4. Generates a prediction.
5. Calculates prediction confidence.
6. Displays the predicted Iris species.
7. Displays the entered input values.

## Project Files

```text
InternCircle_Task_02_Streamlit_Iris_Classifier/
│
├── app.py
├── iris_model.pkl
├── requirements.txt
└── README.md
```

### `app.py`

Contains the Streamlit application and prediction logic.

### `iris_model.pkl`

Contains the trained Decision Tree Machine Learning model.

### `requirements.txt`

Contains the Python libraries required to run the application.

### `README.md`

Contains the project documentation and instructions.

## Testing

The application was tested using different Iris flower measurements.

### Test 1 — Setosa

Input:

```text
Sepal Length: 5.1
Sepal Width: 3.5
Petal Length: 1.4
Petal Width: 0.2
```

Result:

```text
Predicted Flower: Setosa
Prediction Confidence: 100.00%
```

### Test 2 — Versicolor

Input:

```text
Sepal Length: 6.0
Sepal Width: 2.9
Petal Length: 4.5
Petal Width: 1.5
```

Result:

```text
Predicted Flower: Versicolor
Prediction Confidence: 100.00%
```

## Conclusion

This project demonstrates how a trained Machine Learning model can be converted into an interactive web application using Streamlit.

The application successfully accepts user input, loads the saved Machine Learning model, generates predictions, and displays the predicted Iris flower species with prediction confidence.

The project provides an end-to-end example of taking a Machine Learning model from training to an interactive web application suitable for deployment.
