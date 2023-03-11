import numpy as np
import cv2 as cv


def LaplaceN(img):
    k = [[0,1,0],[1,-4,1],[0,1,0]]
    return Convolution(img, k) 

img = cv2.imread('example.png', 0)

cv.imwrite('FILTROLAPLACIANON.png', LaplaceN(img)) 

cv2.waitKey(0)
cv.destroyAllWindows()
