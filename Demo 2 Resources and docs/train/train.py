# File to run MNIST digit classification using Tensorflow
# It downloads the MNIST data and trains the model. Finally it pushes the saved model to the predefined git directory
# Uses custom pull and push python files which contain code to run git shell commands
# Dependencies: Tensorflow, keras and custom 'push.py' and 'pull.py' files. These 2 files should be in the same location where train.py is located
# Usage: python train.py 

from __future__ import absolute_import, division, print_function, unicode_literals

import os
import tensorflow as tf
from tensorflow import keras
from datetime import datetime
import subprocess
from push import upload_model # To push model to Github
from pull import download_model # To fetch model from Github
from subprocess import Popen, PIPE, STDOUT

print(tf.version.VERSION)
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

# Create a basic model instance
model = create_model()

# Display the model's architecture
model.summary()

checkpoint_path = "/t/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Create a callback that saves the model's weights
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)

# Train the model with the new callback
model.fit(train_images, 
          train_labels,  
          epochs=10,
          validation_data=(test_images,test_labels),
          callbacks=[cp_callback])  # Pass callback to training

# This may generate warnings related to saving the state of the optimizer.
# These warnings (and similar warnings throughout this notebook)
# are in place to discourage outdated usage, and can be ignored.

# Create a basic model instance
model = create_model()

# Evaluate the model
loss, acc = model.evaluate(test_images,  test_labels, verbose=2)
print("Untrained model, accuracy: {:5.2f}%".format(100*acc))

# Loads the weights
model.load_weights(checkpoint_path)

# Re-evaluate the model
loss,acc = model.evaluate(test_images,  test_labels, verbose=2)
print("Trained model accuracy: {:5.2f}%".format(100*acc))

# Save the entire model to a HDF5 file.
# The '.h5' extension indicates that the model shuold be saved to HDF5
model.save('my_model.h5') 

print("Model SAVED! Trying to upload...")

upload_model()

