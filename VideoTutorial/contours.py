import cv2 as cv
import numpy as np
#Contour: continuous curves that join all the points along the boundary
# of an object that have the same color or intensity.
#Useed for shape analysis, object detection, face recognition,etc

#Steps:
#1-Convert into greyscale
#2-Get the edges using Canny edge detector
#3-Find the contours using findContours() method. Returns contours and hierarchies
#4-Draw the contours on the image using .drawContours() method

img=cv.imread("Photos/cat2.jpg")
cv.imshow("Cat Original",img)

grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Greyscale",grey)

blur=cv.GaussianBlur(grey,(5,5),cv.BORDER_DEFAULT)
cv.imshow("Blurred",blur)


canny=cv.Canny(blur,125,175)
cv.imshow("Canny",canny)

contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print("Number of Contours: ",len(contours))


blank=np.zeros(img.shape,dtype='uint8')
cv.imshow("Blank",blank)

cv.drawContours(blank,contours,-1,(0,0,255),thickness=2)
cv.imshow("Contours Drawn",blank)


cv.waitKey(0)