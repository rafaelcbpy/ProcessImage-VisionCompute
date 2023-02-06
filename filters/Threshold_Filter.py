import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img1 = cv.imread('exampĺe.jpg', 0) #change path for your image
cv.imshow('example.jpg', img1)

limiar = 70

for i in range (0, 800):
    for j in range (0, 800):
        # 1, se f(x, y) >= L
        # 0, se f(x, y) <= l
        if(img1[i][j] >= limiar):
            img1[i][j] = 255
            if(img1[i][j] <= limiar):
                img1[i][j] = 0
                
cv.imshow('example_result.png', img1)

cv.waitKey(0)
cv.destroyAllWindows() #press any key to close the window
