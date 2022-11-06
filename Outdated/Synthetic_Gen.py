#Outdated, no point using this, waste of everyones time

# Numpy dependency

class SynthData:

    width = None
    height = None
    img = None      # Image created
    gt = None       # Ground Truth of image. Pixels for phase_i have integer "phase_num" in them

    def __init__(self, width, height):
        self.width = width
        self.ny = height
        self.img = np.zeros((height,width, 1), np.uint16)
        self.gt = np.zeros((height,width,1), np.uint8)

    def __init__(self, image, ground_truth):
        self.img = image
        self.gt = ground_truth
        self.height, self.width = image.shape

    def add_phase(self, phase, phase_num):
        # if phase num already exists throw error
        pass # TODO

    def place_phase(self, indices, phase_num):
        # if phase num doesn't exist throw error
        pass # TODO

    def return_img(self):
        return self.img

    def return_gt(self):
        #Note that the ground truth is 8 bit 
        return self.gt

    def reset_img_gt(self):
        self.img = np.zeros((self.height,self.width, 1), np.uint16)
        self.gt = np.zeros((self.height,self.width,1), np.uint8)


class Phase:
    phase_num = None
    resolution = None

    def __init__(self, phase_num, resolution):
        self.phase_num, = phase_num
        self.resolution = resolution

    def return_resolution(self):
        return self.resolution

    

if __name__ == '__main__':
    import numpy as np
    