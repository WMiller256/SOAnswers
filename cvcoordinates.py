import cv2
import numpy as np

img = cv2.imread('./example.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
j = 1

c1 = np.zeros_like(contours[0])
c2 = np.zeros_like(contours[0])
c3 = np.zeros_like(contours[0])
c4 = np.zeros_like(contours[0])

if len(contours) > 0:
    for i in range(0, len(contours)):
        size = cv2.contourArea(contours[i])
        if 90 < size < 140:
            if j == 1:
                c1 = contours[i]
                j += 1
            elif j == 2:
                c2 = contours[i]
                j += 1
            elif j == 3:
                c3 = contours[i]
                j += 1
            elif j == 4:
                c4 = contours[i]
                break

Top = tuple(c1[c1[:, :, 1].argmin()][0])
Right = tuple(c2[c2[:, :, 0].argmax()][0])
Left = tuple(c3[c3[:, :, 0].argmin()][0])
Bottom = tuple(c4[c4[:, :, 1].argmax()][0])

cv2.circle(img, Top, 2, (0, 255, 0), -1)
cv2.circle(img, Right, 2, (0, 255, 0), -1)
cv2.circle(img, Left, 2, (0, 255, 0), -1)
cv2.circle(img, Bottom, 2, (0, 255, 0), -1)
