#Enes Barsbay 02205076051
import cv2
import numpy as np
#orjinal resimi al ve göster
resim2 = cv2.imread('lena.jpg')
cv2.imshow('resim', resim2)
#işlenicek resim 
resim = cv2.imread('lena.jpg',0)
cv2.imshow('resim-0', resim)
#resmi inverting et 
[h, w] = resim.shape
resim2 = np.zeros([h, w], dtype=np.uint8)
for i in range(h):
    for j in range(w):
        resim2[i, j] = 255 - resim[i, j]
#işlenen resmi göster
cv2.imshow("Ters resim", resim2)
cv2.waitKey()