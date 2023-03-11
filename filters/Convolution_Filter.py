import numpy as np
import cv2 as cv


def Convolution(img, c):
    vetor = np.zeros((img.shape[0], img.shape[1]), dtype=np.int)
    for i in range(1,img.shape[0]-1):
        for j in range(1,img.shape[1]-1):
            v = img.item(i-1, j-1)*c[0][0]+img.item(i-1, j)*c[0][1]+img.item(i-1, j+1)*c[0][2]+img.item(i,j-1)*c[1][0]+img.item(i, j)*c[1][1]+img.item(i,j+1)*c[1][2]+img.item(i+1,j-1)*c[2][0]+ img.item(i+1,j)*c[2][1]+img.item(i+1, j+1)*c[2][2]
            if v > 255:
                v=255
            if v <= 0 :
                v = 0
            vetor.itemset((i,j), v)
    return vetor

img = cv.imread('example.png',0)

m = [[1,1,1], [1,-8,1], [1,1,1]]
p = Conv(img, m)
cv.imwrite('Ifiltro.png', p)

cv.waitKey(0)
cv.destroyAllWindows()