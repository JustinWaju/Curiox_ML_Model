# Import necessary libraries

import sys
import csv
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D, Flatten, Dense
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler

# Example data, should be gotten from file afterwards, sufficient for now
# keep in mind, it might be better to create a mapping first, e.g. (right-to-left-swing -> 0, left-to-right-swing -> 1 and so on, to keep consistent and write into the file accordingly)

file_path = 'generated_data_sorted.txt'

with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]

# Convert string values to appropriate types if needed
data = [[float(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), row[6]] for row in data]

# Extract features (X) and labels (y)
x_values = np.array([row[:6] for row in data])  # Convert to NumPy array
y_labels = [row[6] for row in data]

# Step 1: Use LabelEncoder to convert swing type labels to numerical values
label_encoder = LabelEncoder()
y_numerical = label_encoder.fit_transform(y_labels)

# Step 2: Use OneHotEncoder to perform one-hot encoding for y_numerical
onehot_encoder = OneHotEncoder(sparse_output=False)
y_onehot = onehot_encoder.fit_transform(y_numerical.reshape(-1, 1))

# Define your Sequential model
model = Sequential()

#DISCLAIMER: Experimenting with different activation functions and model architectures is often necessary to find the best configuration for your specific task and dataset.

# Add a 1D convolutional layer with suitable filters and kernel size
#kernelsize should equal number of inputs
#filters can be experimented with, is somewhat dependent on the size of the data
#tanh stands for hyperbolic tangent activation function, it accounts for both negative and positive values and squashes them into the range of [-1,1]
#input shape takes timesteps (number of steps in one second; can be experimented with, when we set it to 1 we got an error, so now trying with 10 for the moment)

model.add(Conv1D(filters=32, kernel_size=6, activation='tanh', input_shape=(6, 1)))

# Add a max pooling layer to down-sample the spatial dimensions
# poolSize keeps the biggest numbers of the features given, so it should be equal to kernel size and features, since we want to keep everything
model.add(MaxPooling1D(pool_size=1))

# Flatten the output to feed into a dense layer
model.add(Flatten())

# Add one or more dense layers for classification
model.add(Dense(64, activation='tanh'))
# num_classes should be the number of distinct classes in your data
# Change 10 to the actual number of classes in your data
model.add(Dense(12, activation='softmax')) 

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Print the model summary to see the architecture
model.summary()

# Start training the model with your data
# Note: You may need more data for effective training; adjust epochs and batch_size accordingly
 # Adjust epochs and batch_size as needed
 #input_data, targe_labels (one-hot encoded), number of times the model will iterate over the training set, number of samples that will be used with each iteration

model.fit(x_values, y_onehot, epochs=100, batch_size=100)

#after changing something, change this name
model.save("Testing_model.keras")