# This function creates a new sheet image that is saved in the "Sheets" directory. A sheet contains random shapes such as squares and circles which can be used for training or testing

def main():


    # Comment the types of shapes you would like to create 
    shapes = ['circle', 'square']
    # shapes = ['circle']
    # shapes = ['square']

    # User entered params
    width, height = 2000, 2000 # Arbitrary
    max_size =  200           # max size of objects (radius etc)
    min_size = 50              # min size of the objects
    n_obj = 200              # number of objects in the image
    num_images =   1       # number of images to generate
    
    for z in range(0, num_images):
        # Generate random origins, rotations, colours, and sizes
        x       = np.random.randint(0, width, size = n_obj)
        y       = np.random.randint(0, height, size = n_obj)
        angle   = np.random.randint(0, 360, size = n_obj) # not supported, sad
        col  =  np.random.randint(0, 255, size = (n_obj, 3))
        size    = np.random.randint(min_size, max_size, size = n_obj)
        n_shapes = np.random.choice(shapes, n_obj)

        blank_image = np.zeros((height, width, 3), np.uint8)

        # Create all objects and place them on the image
        for i in range(0, n_obj):
            colour = (int(col[i,0]), int(col[i,1]), int(col[i,2]))

            if n_shapes[i] == 'circle':
                blank_image = cv2.circle(blank_image, (x[i],y[i]), size[i]//2, colour, -1)

            elif n_shapes[i] == 'square':
                start = (int(x[i]-size[i]/2), int(y[i]-size[i]/2))
                end = (int(x[i]+size[i]/2), int(y[i]+size[i]/2))
                blank_image = cv2.rectangle(blank_image, start, end, colour, -1)

        # Nasty way of making unique file names
        j = 0
        img_name = 'C:/School/Masters/Project/Code/Test Network/Train Sheets/' + \
            ''.join(shapes) + str(n_obj) + '_' + str(j)+ '.jpg'

        print(img_name)

        while os.path.exists(img_name):
            j = j + 1
            img_name = 'C:/School/Masters/Project/Code/Test Network/Train Sheets/' + \
            ''.join(shapes) + str(n_obj) + '_' + str(j)+ '.jpg'
            
        cv2.imwrite(img_name, blank_image)


if __name__ == '__main__':
    import cv2
    import numpy as np
    import random as rand
    import os
    main()

