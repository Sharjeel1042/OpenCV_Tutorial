import cv2 as cv

img=cv.imread("Photos/cat2.jpg")
cv.imshow("Cat Original",img)

#BGR->Greyscale
greyscale=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("GreyScale",greyscale)

#BGR->HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)

#BGR->LAB
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)

#BGR->RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)

#Greyscale->BGR
bgr1=cv.cvtColor(greyscale,cv.COLOR_GRAY2BGR)
cv.imshow("From GreyScale",bgr1)

#HSV->BGR
bgr2=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow("From HSV",bgr2)

#LAB->BGR
bgr3=cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow("From LAB",bgr3)

#RGB->BGR
bgr4=cv.cvtColor(rgb,cv.COLOR_RGB2BGR)
cv.imshow("From RGB",bgr4)

cv.waitKey(0)