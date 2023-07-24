# Crop_Recommendation_System
Description
This project is a Crop Recommendation System implemented in Python using Simple Linear Regression. The goal of the system is to assist farmers in making informed decisions about which crops are most suitable for their agricultural land based on certain environmental and soil parameters.

Dependencies
Before running the project, make sure you have the following dependencies installed:

Python 3.x
Pandas
NumPy
Scikit-learn
Tkinter
You can install the required dependencies using pip:
pip install pandas numpy scikit-learn tkinter

Dataset
The project uses a dataset containing historical data of various crops and their corresponding characteristics, such as temperature, humidity, rainfall, soil pH, etc. The dataset is stored in a CSV file named crop_data.csv.

Usage
Clone the repository or download the project files to your local machine.

Ensure that the required dependencies are installed as mentioned in the "Dependencies" section.

Place the crop_data.csv file in the same directory as the Python script.

Run the crop_recommendation.py script using the following command:

bash
Copy code
python crop_recommendation.py
The script will process the dataset, train the Simple Linear Regression model, and prompt you to input environmental and soil parameters for prediction.

Enter the values for parameters when prompted and press Enter.

The system will predict the most suitable crop based on the input parameters using the trained model and display the recommendation.

How it works
The Crop Recommendation System utilizes Simple Linear Regression to find relationships between various environmental and soil factors and crop suitability. The model is trained on historical data to make accurate predictions.

The core steps involved are:

Data Loading: The script reads the crop_data.csv file and loads it into a Pandas DataFrame for further processing.

Data Preprocessing: The dataset is preprocessed to handle any missing values, outliers, or inconsistencies.

Feature Selection: The relevant features (independent variables) are selected to train the Simple Linear Regression model.

Model Training: The Simple Linear Regression model is trained on the selected features and their corresponding crop labels.

User Input: The user provides environmental and soil parameters as input to the system.

Prediction: The model uses the provided input to predict the most suitable crop.

Recommendation: The system displays the recommended crop based on the prediction.

Acknowledgments
Special thanks to the authors of the dataset used in this project for providing valuable agricultural data.

Contact
If you have any questions, suggestions, or feedback, feel free to contact me at shrikantdipakdharmal@gmail.com.




