import cv2
import numpy as np

#.Read an image

image = cv2.imread('Ronaldo.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


img_blur = cv2.GaussianBlur(gray, (5,5),0)



Kx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
Ky = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])

#Do filtering


sobel_GX = cv2.filter2D(src = img_blur, ddepth=-1, kernel=Kx)
sobel_GY = cv2.filter2D(src = img_blur, ddepth=-1, kernel=Ky)


sobel_XY = cv2.addWeighted(sobel_GX, 0.5, sobel_GY, 0.5,0)

# Show the result

cv2.imshow('GX', sobel_GX)


cv2.imshow('GY', sobel_GY)
cv2.imshow('XY', sobel_XY)

cv2.waitKey(0)
cv2.destroyAllWindow()
