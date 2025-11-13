import cv2 as cv

img=cv.imread("Photos/cat2.jpg")
cv.imshow("Cat 2",img)

#Converting an image to Greyscale
grayscale=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale",grayscale)

#Blurring an image:Reducing unnecessary noise in the image caused by bad lighting, bad camera sensor,etc
blurImg=cv.GaussianBlur(img,(9,9),cv.BORDER_DEFAULT)
cv.imshow('Blurred Image',blurImg)

#Edge Cascade:Finding the edges that are present in the image
canny=cv.Canny(img,125,175)
cv.imshow('Canny',canny)

#Dilating the image
dilated=cv.dilate(canny,(3,3),iterations=1)
cv.imshow("Dilated Image",dilated)

#Eroding
eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow("Eroded Image",eroded)

#Resizing:Reducing image size
reduced=cv.resize(img,(250,250),interpolation=cv.INTER_AREA)
cv.imshow("Reduced Size",reduced)
#cv.INTER_AREA for reducing image size

#Resizing an image:Increasing the size
increased=cv.resize(img,(750,750),interpolation=cv.INTER_CUBIC)
cv.imshow("Increased Size",increased)
#INTER_CUBIC and INTER_LINEAR for increasing size
#INTER_CUBIC is slow but image of best quality

#Cropping"Considering that images are arrays
cropped=img[50:100,0:250]
cv.imshow("Cropped",cropped)

cv.waitKey(0)