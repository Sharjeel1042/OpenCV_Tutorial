#Drawing shape and putting text on images
import cv2 as cv
import numpy as np

img=cv.imread("Photos/cat2.jpg")
cv.imshow("Cat Image",img)

#1.Paint the image a certain color
img[:]=0,255,0 #Painting the entire image green
cv.imshow("Green Paint",img)

#2.Draw a rectangle
rect=cv.rectangle(img,(0,0),(300,200),(0,0,255),thickness=2)
#img=The image on which we want the rectangle to be drawn
#(0,0)=Staring point of the rectangle. (Origin in this case)
#(300,200)=Ending point of the rectangle
#thickness=Thickness of the borders of the rectangle
#If thickness=cv.FILLED
cv.imshow("Rectangle Drawn on Image",rect)


#3.Draw a Circle
circle=cv.circle(img,(300,200),40,(255,0,0),thickness=3)
#img=The image on which we want the circle to be drawn
#(0,0)=Midpoint of the Circle.
#40=Radius of the circle
#thickness=Thickness of the borders of the Circle
cv.imshow("Circle Drawn on image",circle)

#4.Draw a Line on the image
line=cv.line(img,(0,0),(300,200),(0,100,155),thickness=2)
cv.imshow("Line drawn on an image",line)

#5.Write text on an image
textImage=cv.putText(img,"Hello there!!",(300,200),cv.FONT_HERSHEY_TRIPLEX,1.0,(100,100,55),thickness=2)
cv.imshow("Putting Text on an image",textImage)



cv.waitKey(0)
