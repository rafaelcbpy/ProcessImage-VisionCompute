import cv2 as cv
image = cv.imread("example.jpg",0) #change path for your image

for i in range (0, image.shape[0]):
    for j in range (0, image.shape[1]):
        bits = bin(image[i][j])[2:].zfill(8)
        if(bits[3] == "1"):
            image[i][j]= image[i][j]
        else:
            image [i][j] = 0     
                  
cv.imshow("example_result.png",image)

cv.waitKey(0)
cv.destroyAllWindows() #press any key to close the window
