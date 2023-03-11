import numpy as np
import cv2 as cv

def LaplaceR(img):
    k = [[1,0,1],[0,-4,0],[1,0,1]]
    return Convolution(img, k)

img = cv2.imread('example.png', 0)

cv.imwrite('FILTROLAPLACIANOR.png', LaplaceR(img)) 

cv2.waitKey(0)
cv.destroyAllWindows()
