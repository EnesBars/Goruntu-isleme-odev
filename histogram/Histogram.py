# Enes Barsbay 02205076051
import cv2
import numpy as np
import matplotlib.pyplot as plt

# resim img at
# shape ile sınırları s değişkenine at
# resmi göster
img = cv2.imread("candy.jpg")
s = img.shape
cv2.imshow('resim normal', img)

# BGR den GRAY çevir renkleri
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gri hali', img_gray)

# histogram hesapla
H = np.zeros(shape=(256, 1))
# matris s değerinde
for i in range(s[0]):
    for j in range(s[1]):
        k = img_gray[i, j]
        H[k, 0] = H[k, 0] + 1

# histogram yazdir
plt.plot(H)
plt.show()
cv2.waitKey(0)
