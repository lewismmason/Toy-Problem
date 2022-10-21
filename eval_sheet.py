import tensorflow as tf
import pathlib
import PIL
import json
import helper_functions
import numpy as np
from PIL import Image, ImageOps
import cv2 
import time

# The sheet to evaluate
sheet_name = 'circlesquare200_0.jpg'
model_name = 'modelv3'

# Load JSON params
with open('params.json', 'r') as jf:
  params = json.load(jf)
dx = params['dx']
dy = params['dy']
class_names = params['classes']

model = tf.keras.models.load_model(model_name)
model.summary()

jpg_path = 'C:/School/Masters/Project/Code/Toy-Problem/Run Sheets/' + sheet_name

voxels, coords = helper_functions.data_coord_pair(jpg_path)
num = len(coords)
voxels = np.asarray(voxels)
coords = np.asarray(coords)

predicted_labels = []
out = model.predict(voxels)

# narly way of doing this, whatever sue me
for i in range(0,num):
    predicted_labels.append(class_names[np.argmax(out[i])])

# Show full image and tint sections based on predictions
img = Image.open(jpg_path)
img = ImageOps.grayscale(img)
img = np.array(img)
img = np.stack((img,)*3, axis=-1) # make single channel grayscale into three channel to annotate
for i in range(0, num):
    x_0 = coords[i,0]
    y_0 = coords[i,1]
    if np.argmax(out[i]) == 0:
      img[y_0:y_0+dy,x_0:x_0+dx, 0] = 255
    elif np.argmax(out[i]) == 1:
      img[y_0:y_0+dy,x_0:x_0+dx, 1] = 255
    elif np.argmax(out[i]) == 2:
      img[y_0:y_0+dy,x_0:x_0+dx, 2] = 255
    elif np.argmax(out[i]) == 3:
      img[y_0:y_0+dy,x_0:x_0+dx, 0] = 255
      img[y_0:y_0+dy,x_0:x_0+dx, 1] = 255
    

img = Image.fromarray(img)
img.show()



# now we have predicted stuff
# for i in range(0,100):
#     img = Image.fromarray(voxels[i])
#     print(predicted_labels[i])
#     img.show()
#     time.sleep(1)
#     img.close()