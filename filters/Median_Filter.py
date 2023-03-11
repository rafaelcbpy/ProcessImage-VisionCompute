import numpy as np
import cv2 as cv


def Median(img):
    s = np.zeros((img.shape[0], img.shape[1]), dtype=np.int)
    for i in range(1,img.shape[0]-1):    
        for j in range(1,img.shape[1]-1):
            lista = [img.item(i-1,j-1), img.item(i-1,j), img.item(i-1,j+1),img.item(i,j-1), img.item(i, j), img.item(i, j+1), img.item(i+1, j-1), img.item(i+1, j), img.item(i+1, j+1)] 
            lista.sort()
            valor = lista[4]
            s[i][j] = valor
    return s

img = cv.imread("example.png",0)

cv.imwrite('mediana.png', Median(img))

cv.waitKey(0)
cv.destroyAllWindows()