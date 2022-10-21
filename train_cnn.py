import tensorflow as tf
import os
import PIL
from PIL import Image 
import numpy as np
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import json
import helper_functions
import random

model_name = 'modelv3'

# Parameters for training from the JSON file
with open('params.json', 'r') as jf:
  params = json.load(jf)
dx = params['dx']
dy = params['dy']
batch_size = params['batch_size']
v_split = params['validation_split']
class_names = params['classes']
num_epochs = params['num_epochs']

# Generate dataset and label pair
data_dir = 'C:/School/Masters/Project/Code/Test Network/Train Sheets'
voxels, labels  = helper_functions.data_label_pair(data_dir)
num = len(labels)
voxels = np.asarray(voxels)
labels = np.asarray(labels)

# for i in range(0, len):
#   img = Image.fromarray(voxels[i])
#   img.show()

AUTOTUNE = tf.data.AUTOTUNE

num_classes = len(class_names)

model = tf.keras.Sequential([
  tf.keras.layers.Rescaling(1./255),
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  # tf.keras.layers.Conv2D(32, 3, activation='relu'),
  # tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(num_classes)
])

model.compile(
  optimizer='adam',
  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy'])

history = model.fit(
  epochs = num_epochs,
  batch_size = batch_size,
  x = voxels,
  y = labels,
  validation_split = v_split
)

model.save(model_name)

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.1, 1])
plt.legend(loc='lower right')
plt.show()