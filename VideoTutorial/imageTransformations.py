import cv2 as cv
import numpy as np

img=cv.imread("Photos/cat2.jpg")
cv.imshow("Cat 2",img)

#Translation
def translation(image,x,y):
    transMatrix=np.float32([[1,0,x],[0,1,y]])
    dimensions=(image.shape[1],image.shape[0])
    return cv.warpAffine(image,transMatrix,dimensions)


translated=translation(img,100,100)
cv.imshow("Translated Image",translated)

#Roatation
def rotation(image,angle,rotationPoint=None):
    width=image.shape[1]
    height=image.shape[0]

    if rotationPoint is None:
        rotationPoint=(width/2,height/2)

        rotMatrix=cv.getRotationMatrix2D(rotationPoint,angle,1.0)
        dimensions=(width,height)


    return cv.warpAffine(image,rotMatrix,dimensions)

rotatedImage=rotation(img,180)
cv.imshow("Rotated Image",rotatedImage)


#Resizing
def resize(image,scale=0.5):
    width=int(image.shape[1]*scale)
    height=int(image.shape[0]*scale)
    
    dimensions=(width,height)
    
    return cv.resize(image,dimensions,interpolation=cv.INTER_AREA)


#Flipping
flipped0=cv.flip(img,0)
flipped1=cv.flip(img,1)
flipped_1=cv.flip(img,-1)

cv.imshow("Flipped 0",flipped0)
cv.imshow("Flipped 1",flipped1)
cv.imshow("Flipped -1",flipped_1)


#Cropping
cropped=img[0:250,0:300]
cv.imshow("Cropped Image",cropped)






    


cv.waitKey(0)