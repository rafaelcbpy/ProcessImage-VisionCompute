import cv2 as cv
import numpy as np

    
image = cv.imread("example.jpg",0) #change path for your image

print(np.max(image))
c = (255/np.log(np.max(image)))
for i in range (0, image.shape[0]):
    for j in range (0, image.shape[1]):
            pixel = c*np.log(1+image[i][j])
            image[i][j] = pixel
            
cv.imshow("example_result.png",image) 

cv.waitKey(0)
cv.destroyAllWindows() #press any key to close the window
