import cv2
import numpy as np

img_a = cv2.imread('snowden.jpg')
img_b = cv2.imread('flower.jpg')
[r, c, z] = img_a.shape
# img1 = np.resize(img_b, img_a.shape)
img1 = cv2.bitwise_not(img_a)
img2=cv2.bitwise_not(img_b)
cv2.imshow("snowden",img1)
cv2.imshow("flower",img2)
cv2.waitKey(0)
