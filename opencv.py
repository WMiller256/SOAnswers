import cv2
import numpy as np

im = cv2.imread('opencvtest.png')

# Find the average of each channel across the image
mean = [np.mean(im[:,:,i]) for i in range(im.shape[2])]

print(mean)

