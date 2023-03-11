import numpy as np
import cv2 as cv


def LaplaceC(img):
    k = [[1,1,1],[1,-8,1],[1,1,1]]
    return Convolution(img, k)
img = cv2.imread('example.png', 0)

cv.imwrite('FILTROLAPLACIANOC.png', LaplaceC(img))

cv2.waitKey(0)
cv.destroyAllWindows()