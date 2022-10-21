# This script takes any image in "Sheets" dir and turns it into training data in "Training Data"
# This is unfortunately a manual process, thus I no longer use it, I'm lazy and will automate this

sheet_path = 'C:/School/Masters/Project/Code/Test Network/Sheets/'
save_path = 'C:/School/Masters/Project/Code/Test Network/Training Data/'

def main():

    classes = ['circle', 'square', 'none','unknown']

    # Load the model params for image sizing
    with open('params.json', 'r') as jf:
                params = json.load(jf)

    dx = params['dx']
    dy = params['dy']

    image = cv2.imread(sheet_path + '150.jpg')

    # This loses information if dx not integer multiple of im_width
    num_xcell = image.shape[1]//dx
    num_ycell = image.shape[0]//dy
    
    num_images = num_xcell * num_ycell

    for i in range(0,num_xcell):
        for j in range(0,num_ycell):
            sub_img = image[i*dx:(i+1)*dx, j*dy:(j+1)*dy]

            cv2.imshow('Press c, s, or n to label', sub_img)
            
            key = cv2.waitKey(0)

            if key == ord('c'):
                class_i = 0
            elif key == ord('s'):
                class_i = 1
            elif key == ord('n'):
                class_i = 2
            elif key == ord('u'):
                class_i = 3

            label = classes[class_i]

            # Prompt the user to label the data
            now = datetime.datetime.now()
            name = now.strftime('%m%d%H%M%S')
            cv2.imwrite(save_path + label + name + '.jpg', sub_img)


if __name__ == '__main__':
    import cv2
    import numpy as np
    import os
    import json
    import keyboard
    import datetime

    # temp, remove later
    import time
    main()