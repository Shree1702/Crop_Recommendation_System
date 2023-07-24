# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 16:58:20 2023

@author: SHRIKANT D DHARMAL
"""

import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np

# Load the dataset
df = pd.read_csv('C:/Users/SHRIKANT D DHARMAL/Documents/Crop_recommendation.csv')
x = df.iloc[:, 0:7]
y = df.iloc[:, 7]  # Assuming the target variable is in the 8th column

# Perform one-hot encoding on the target variable
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

onehot_encoder = OneHotEncoder(sparse=False)
y_encoded = y_encoded.reshape(-1, 1)
y_onehot = onehot_encoder.fit_transform(y_encoded)

x_train, x_test, y_train, y_test = train_test_split(x, y_onehot, test_size=0.2)
lsr = LinearRegression()
lsr.fit(x_train, y_train)

# Create the Tkinter GUI
window = tk.Tk()
window.title("Crop Yield Prediction")
window.geometry("400x300")
window.bgcolor="orange"


# Create input labels and entry fields
labels = ["Nitrogen content:", "Phosphorous content:", "Potassium content:",
          "Temperature (°C):", "Humidity (%):", "pH value:", "Rainfall (mm):"]
entries = []
for i in range(len(labels)):
    label = tk.Label(window, text=labels[i])
    label.pack()
    entry = tk.Entry(window)
    entry.pack()
    entries.append(entry)

# Define the prediction function
def predict_yield():
    try:
        # Get user inputs
        values = [float(entry.get()) for entry in entries]
        val = np.array(values).reshape(1, -1)

        # Ensure the input data has the same column names as training data
        val = pd.DataFrame(val, columns=x_train.columns)

        # Make the prediction
        pred = lsr.predict(val)
        pred_label_encoded = np.argmax(pred)
        pred_label = label_encoder.inverse_transform([pred_label_encoded])

        # Display the prediction in a message box
        messagebox.showinfo("Crop Yield Prediction", f"The predicted crop is: {pred_label[0]}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")

# Create the predict button
predict_button = tk.Button(window, text="Predict", command=predict_yield)
predict_button.pack()

window.mainloop()
