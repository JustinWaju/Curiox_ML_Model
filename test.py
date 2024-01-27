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

# Load and preprocess the verification data
file_path_verification = 'generated_data_sorted_verification.txt'

with open(file_path_verification, mode='r') as file:
    reader = csv.reader(file)
    data_verification = [row for row in reader]

# Convert string values to appropriate types if needed
data_verification = [[float(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), row[6]] for row in data_verification]

# Extract features (X) and labels (y) for verification
x_values_verification = np.array([row[:6] for row in data_verification])  # Convert to NumPy array
y_labels_verification = [row[6] for row in data_verification]

# Step 1: Use LabelEncoder to convert swing type labels to numerical values
label_encoder_verification = LabelEncoder()
y_numerical_verification = label_encoder_verification.fit_transform(y_labels_verification)

# Step 2: Use OneHotEncoder to perform one-hot encoding for y_numerical
onehot_encoder_verification = OneHotEncoder(sparse_output=False)
y_onehot_verification = onehot_encoder_verification.fit_transform(y_numerical_verification.reshape(-1, 1))

# Evaluate the model on the verification data
loss, accuracy = model.evaluate(x_values_verification, y_onehot_verification)
print(f'Accuracy on verification data: {accuracy * 100:.2f}%')
