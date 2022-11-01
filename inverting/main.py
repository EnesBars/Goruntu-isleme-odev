import cv2
import numpy as np

resim2 = cv2.imread('lena.jpg')
cv2.imshow('resim', resim2)

resim = cv2.imread('lena.jpg',0)
cv2.imshow('resim-0', resim)

[h, w] = resim.shape
resim2 = np.zeros([h, w], dtype=np.uint8)
for i in range(h):
    for j in range(w):
        resim2[i, j] = 255 - resim[i, j]

cv2.imshow("Ters resim", resim2)
cv2.waitKey()