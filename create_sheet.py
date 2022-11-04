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
        col  =  np.random.randint(1, 2**8, size = (n_obj, 1))   # lower bound 1 to remove bg colour
        size    = np.random.randint(min_size, max_size, size = n_obj)
        n_shapes = np.random.choice(shapes, n_obj)

        blank_image = np.zeros((height, width, 1), np.uint16)

        # Create all objects and place them on the image
        for i in range(0, n_obj):
            colour = (int(col[i,0]), int(col[i,0]), int(col[i,0]))

            if n_shapes[i] == 'circle':
                blank_image = cv2.circle(blank_image, (x[i],y[i]), size[i]//2, colour, -1)

            elif n_shapes[i] == 'square':
                start = (int(x[i]-size[i]/2), int(y[i]-size[i]/2))
                end = (int(x[i]+size[i]/2), int(y[i]+size[i]/2))
                blank_image = cv2.rectangle(blank_image, start, end, colour, -1)

        gt_image = np.where(blank_image>1,2**8, 0)  # ground truth is just binarized

        # Nasty way of making unique file names yuck, need to comment out one of these pairs 
        dir_name = 'C:/School/Masters/Project/Code/Toy-Problem/Sheets/Train Sheets/'
        gt_dir_name = 'C:/School/Masters/Project/Code/Toy-Problem/Sheets/Train Sheets Ground Truth/'

        # dir_name = 'C:/School/Masters/Project/Code/Toy-Problem/Sheets/Test Sheets/'
        # gt_dir_name = 'C:/School/Masters/Project/Code/Toy-Problem/Sheets/Test Sheets Ground Truth/'

        j = 0
        img_name = dir_name + \
            ''.join(shapes) + str(n_obj) + '_' + str(j)+ '.jpg'
        gt_img_name = gt_dir_name + \
            ''.join(shapes) + str(n_obj) + '_' + str(j)+ '.jpg'

        while os.path.exists(img_name):
            j = j + 1
            img_name = dir_name + \
            ''.join(shapes) + str(n_obj) + '_' + str(j)+ '.jpg'
            gt_img_name = gt_dir_name + \
            ''.join(shapes) + str(n_obj) + '_' + str(j)+ '.jpg' # This will overwrite other images which is ok, since it must match the above
            
        print(img_name)

        cv2.imwrite(img_name, blank_image)
        cv2.imwrite(gt_img_name, gt_image)
        plot_2D_image_pdf(img_name)             # Plot the PDF for fun


if __name__ == '__main__':
    import cv2
    import numpy as np
    import random as rand
    import os
    from helper_functions import plot_2D_image_pdf
    main()

