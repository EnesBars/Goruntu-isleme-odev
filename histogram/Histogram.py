
import cv2
import numpy as np
import matplotlib.pyplot as plt

resim = cv2.imread("candy.jpg")
s = resim.shape
cv2.imshow('resim', resim)
resim_gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
cv2.imshow('resim gri', resim_gray)
H = np.zeros(shape=(256,1))
for i in range(s[0]):
    for j in range(s[1]):
        k = resim_gray[i,j]
        H[k,0] = H[k,0]+1
#print(H)
plt.plot(H)
plt.show()
cv2.waitKey(0)

