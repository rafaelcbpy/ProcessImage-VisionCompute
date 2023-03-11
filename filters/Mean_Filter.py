import numpy as np
import cv2 as cv


def Mean(img):
    vetor = np.zeros((img.shape[0], img.shape[1]), dtype=np.int)
    for i in range(1,img.shape[0]-1):
        for j in range(1,img.shape[1]-1):
            v = float(img.item(i-1, j-1)+img.item(i-1, j)+img.item(i-1, j+1)+img.item(i,j-1)+img.item(i, j)+img.item(i,j+1)+img.item(i+1,j-1)+ img.item(i+1,j)+img.item(i+1, j+1))
            v = v/9.0
            vetor.itemset((i,j), int(v))
    return vetor


img = cv2.imread('example.png', 0)

cv.imwrite('FILTROMEDIA.png', Mean(img))

cv2.waitKey(0)
cv.destroyAllWindows()