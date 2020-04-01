import cv2
import numpy as np

im = cv2.imread('./example.png')
im[:,450:][im[:,450:] > 180] = 255
cv2.imwrite('./check.png', im)
