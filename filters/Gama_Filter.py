import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread('example.jpg', 0) #change path for your image
cv.imshow('example.jpg', img) 

gamma = int(3) 
c = int(1)
for i in range (0, 769):
    for j in range (0, 765):
        # funcao = q(imagem/q)^gamma
        pixel = float((255*(img[i][j]/255)**gamma))
        img[i][j] = pixel
        
cv.imshow('img_result.png', img)


cv.waitKey(0)
cv.destroyAllWindows() #press any key to close the window
