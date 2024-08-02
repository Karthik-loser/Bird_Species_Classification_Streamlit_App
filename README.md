# 🐦 Bird Species Classification Streamlit App
Welcome to the Bird Species Identification project! This project aims to classify and identify bird species from images using Convolutional Neural Networks (CNNs). The application is built using Python, TensorFlow, and Streamlit, allowing for an interactive and user-friendly experience.

## Project Overview
The goal of this project is to develop a machine learning model that can accurately identify bird species from images. We use Convolutional Neural Networks (CNNs) due to their effectiveness in image classification tasks. The web application built with Streamlit provides an easy-to-use interface for users to upload images and receive predictions about the bird species.
Live Demo
You can access the live application here: https://github.com/Karthik-loser/Bird_Species_Classification_Streamlit_App

## Features
Image Upload: Users can upload images of birds for classification.
Real-time Predictions: The model provides predictions on the bird species in real-time.
User Interface: Built with Streamlit to offer a clean and intuitive user experience.
Technologies Used
Python: Programming language used for implementing the model and application.
TensorFlow: Framework used to build and train the Convolutional Neural Network (CNN).
Streamlit: Framework used to create the interactive web application.
OpenCV: Used for image processing tasks.
## Getting Started
To run the Bird Species Identification application locally, follow these steps:

## Prerequisites
Python 3.8 or higher
Pip (Python package installer)
Installation
Clone the Repository
## Usage

git clone https://github.com/Karthik-loser/Bird_Species_Classification_Streamlit_App.git
cd Bird_Species_Classification_Streamlit_App
Create and Activate a Virtual Environment


python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Required Packages

pip install -r requirements.txt
Run the Streamlit Application

streamlit run app.py
Open Your Browser

After running the application, open your browser and go to http://localhost:8501 to interact with the Bird Species Identification app.

## Project Structure
- `app.py` is the main Python file of Streamlit Application. 
- `birds-classification.ipynb` is the Notebook file of the Training
- Dataset that I have used is [275 Bird Species]
- Dataset folder consists of test, train and valid folders along with birds.csv file  (https://www.kaggle.com/gpiosenka/100-bird-species).
- Model folder consists of BC.h5 file that is created from the birds-classification.ipynb file 
- To run app, write following command in CMD. or use any IDE.
To train the model on your own dataset, follow these steps:

Prepare your dataset and organize it into training and validation sets.
Update the model.py script with the appropriate dataset paths.
Run the training script to train the CNN model.
## Usage
Upload an image of a bird through the Streamlit app, and the model will provide a prediction of the bird species along with the confidence score.

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## Acknowledgments
TensorFlow for the machine learning framework.
Streamlit for the interactive web app framework.
