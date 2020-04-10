# Question: https://stackoverflow.com/questions/61131809/opencv-create-circle-out-of-bounds

import cv2
import numpy as np

image = cv2.imread("example.png")

def create_circle(image):
  color = (np.random.randint(low=0, high=255),
           np.random.randint(low=0, high=255),
           np.random.randint(low=0, high=255))
  while True:
    pos = (np.random.randint(low=0, high=image.shape[1]), np.random.randint(low=0, high=image.shape[0]))
    rad = np.random.randint(low=0, high=image.shape[0]//2)
    if rad + pos[0] < image.shape[0] and rad + pos[1] < image.shape[1] and pos[0] >= rad and pos[1] >= rad:
      break
  cv2.circle(image,pos,rad,color,-1)

for i in range(5):
	create_circle(image)

cv2.imwrite("circles.png", image)
