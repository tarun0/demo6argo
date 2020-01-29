# File to run MNIST digit classification prediction using Tensorflow
# It will first fetch the model from git directory defines in 'pull.py' file.
# Then, it downloads the MNIST data and runs the prediction code. 
# Uses custom 'pull.py' python fil which contain code to run git shell commands
# Dependencies: Tensorflow, keras and custom 'pull.py' file. This file should be in the same location where predict.py is located
# Usage: python predict.py 

from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow import keras
import os
from datetime import datetime
import subprocess
from subprocess import Popen, PIPE, STDOUT
from pull import download_model # To fetch model from Github

fileName = 'my_model.h5'

# Download the model from Git
download_model()

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

train_labels = train_labels[:1000]
test_labels = test_labels[:1000]

train_images = train_images[:1000].reshape(-1, 28 * 28) / 255.0
test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0

# Define a simple sequential model
def create_model():
  model = tf.keras.models.Sequential([
    keras.layers.Dense(512, activation='relu', input_shape=(784,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation='softmax')
  ])

  model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

  return model


new_model = tf.keras.models.load_model(fileName)
# Show the model architecture
new_model.summary()

loss, acc = new_model.evaluate(test_images,  test_labels, verbose=2)
print('Restored model accuracy: {:5.2f}%'.format(100*acc))



