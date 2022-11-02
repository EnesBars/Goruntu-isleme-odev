# Enes Barsbay 02205076051
import cv2
import numpy as np

# orijinal resimi göstermek için olan kısım
img2 = cv2.imread('lena.jpg')
cv2.imshow('orijinal', img2)

# işlenicek resim
img = cv2.imread('lena.jpg', 0)
cv2.imshow('resim-0', img)

# shape ile resim boyutunda matris oluştur
# np.zeros ile 0 ile dolu dizi dönder
# dizide gezerek inverting işlemini gerçekleştir
[h, w] = img.shape
resim2 = np.zeros([h, w], dtype=np.uint8)
for i in range(h):
    for j in range(w):
        img2[i, j] = 255 - img[i, j]

# işlenen resmi göster
cv2.imshow("Ters resim", img2)
cv2.waitKey()
