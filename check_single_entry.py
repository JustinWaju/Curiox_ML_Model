import sys
import csv
import numpy as np
import keras
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D, Flatten, Dense
from keras.optimizers import Adam
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler

# Load the trained model
model = load_model("Testing_model.keras", custom_objects={'Adam': Adam})

# Load and preprocess the verification data for a single entry
file_path_single_entry = 'test.txt'

with open(file_path_single_entry, mode='r') as file:
    reader = csv.reader(file)
    data_single_entry = [row for row in reader]

# Convert string values to appropriate types if needed
data_single_entry = [[float(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5])] for row in data_single_entry]

# Convert the single entry to a NumPy array
x_single_entry = np.array(data_single_entry)

# Set numpy print options to display numbers with 2 decimal places
np.set_printoptions(suppress=True, precision=2)

# Make predictions for the single entry
predictions = model.predict(x_single_entry.reshape(1, -1))

# Print the predicted probabilities for each class
print("Predicted Probabilities:")
print(predictions)

# Get the predicted class (index with the highest probability)
predicted_class_index = np.argmax(predictions)
print(f"Predicted Class Index: {predicted_class_index}")


