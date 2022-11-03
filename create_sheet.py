# This function creates a new sheet image that is saved in the "Sheets" directory. A sheet contains random shapes such as squares and circles which can be used for training or testing

def main():
    # Comment the types of shapes you would like to create 
    # shapes = ['circle', 'square']
    shapes = ['circle']
    # shapes = ['square']

    # User entered params, I could do in the console but I'm lazy
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

        blank_image = np.zeros((height, width, 1), np.uint16)

        # Create all objects and place them on the image
        for i in range(0, n_obj):
            colour = (int(col[i,0]), int(col[i,1]), int(col[i,2]))

            if n_shapes[i] == 'circle':
                blank_image = cv2.circle(blank_image, (x[i],y[i]), size[i]//2, colour, -1)

            elif n_shapes[i] == 'square':
                start = (int(x[i]-size[i]/2), int(y[i]-size[i]/2))
                end = (int(x[i]+size[i]/2), int(y[i]+size[i]/2))
                blank_image = cv2.rectangle(blank_image, start, end, colour, -1)

        # Nasty way of making unique file names yuck
        j = 0
        dir_name = 'C:/School/Masters/Project/Code/Toy-Problem/Train Sheets/'

        img_name = dir_name + \
            ''.join(shapes) + str(n_obj) + '_' + str(j)+ '.jpg'

        print(img_name)

        while os.path.exists(img_name):
            j = j + 1
            img_name = dir_name + \
            ''.join(shapes) + str(n_obj) + '_' + str(j)+ '.jpg'
            
        cv2.imwrite(img_name, blank_image)
        plot_2D_image_pdf(img_name)             # Plot the PDF for fun


if __name__ == '__main__':
    import cv2
    import numpy as np
    import random as rand
    import os
    from helper_functions import plot_2D_image_pdf
    main()

