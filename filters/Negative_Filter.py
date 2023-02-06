import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("example.jpg") #change path for your image

for i in range (0, image.shape[0]):
    for j in range (0, image.shape[1]):
            pixel = 255 - 1 -image[i][j]
            image[i][j] = pixel
            
cv.imwrite('image.png',image)

cv.imshow("example_result.png",image)
cv.waitKey(0)
cv.destroyAllWindows() #press any key to close the window
