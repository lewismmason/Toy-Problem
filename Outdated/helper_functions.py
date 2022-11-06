# dependencies (yuch)
import json
import numpy as np
import os
from PIL import Image
import matplotlib. pyplot as plt
from skimage import io


# This is used for training over a full sheet of a singular shape
def data_label_pair(data_dir):
   # Parameters from the JSON file
    with open('params.json', 'r') as jf:
                params = json.load(jf)
    dx = params['dx']
    dy = params['dy']
    class_names = params['classes']

    ii = 1
    num_imgs = 0

    voxels = []
    labels = []

    dir = os.fsencode(data_dir)
    for jpg in os.listdir(dir):
        filename = os.fsdecode(jpg)
        if filename.endswith('.jpg'):
            jpg_path = os.path.join(dir, jpg)
            img = np.asarray(Image.open(jpg_path))

            # Now iterate through every dx by dy by dz subset and classify them
            ny = img.shape[0]//dy
            nx = img.shape[1]//dx
            num_imgs = num_imgs + ny*nx

            for j in range(0, ny):
                for i in range(0,nx):
                    sub_img = img[j*dy:(j+1)*dy, i*dx:(i+1)*dx]

                    # Label
                    if np.sum(sub_img) == 0:
                        label = class_names.index('none')  # none
                    elif np.all(sub_img == sub_img[0]):
                        label = class_names.index('unknown')  # unknown
                    elif 'circle' in filename:
                        label = class_names.index('circle')
                    elif 'square' in filename:
                        label = class_names.index('square')
                    labels.append(label)
                    voxels.append(sub_img)
        else:
            continue
        
        print('Done sheet ' + str(ii))
        ii = ii + 1

    print('Total of ' + str(num_imgs) + ' total images')
    return voxels, labels

# This is used to break a full sheet into chunks for evaluation, while keeping coordinates of the sections
def data_coord_pair(jpg_path):
   # Parameters from the JSON file
    with open('params.json', 'r') as jf:
                params = json.load(jf)
    dx = params['dx']
    dy = params['dy']

    ii = 1
    num_imgs = 0

    voxels = []
    coords = [] # List of length 2 lists representing top left coordinate of each voxel [x, y]

    img = np.asarray(Image.open(jpg_path))

    # Now iterate through every dx by dy by dz voxel and get their origin coords
    ny = img.shape[0]//dy
    nx = img.shape[1]//dx
    num_imgs = num_imgs + ny*nx

    for j in range(0, ny):
        for i in range(0,nx):
            sub_img = img[j*dy:(j+1)*dy, i*dx:(i+1)*dx]
            coords.append([i*dx, j*dy])
            voxels.append(sub_img)

        ii = ii + 1

    print('Total of ' + str(num_imgs) + ' sub images were generated')
    return voxels, coords

def plot_2D_image_pdf(jpg_path):
    img = io.imread(jpg_path)
    img = np.asarray(img, dtype=np.uint16)
    num_slice = img.shape[0]    # First dimension is slice, second is height, third width

    # 2. Get PDF of TIF file
    counts, bins = np.histogram(img[:,:], bins=2**8)    # Only supports 8 bit for now, 16 bit is way too slow
    counts[0] = 0   # Remove the pure black from the histogram
    plt.figure()

    # plt.imshow(img[1,:,:], cmap = 'gray')
    # plt.plot(bin_edges[0:-1], histogram)
    plt.hist(bins[:-1],bins, weights=counts)
    plt.show()

