import cv2 as cv


#Reading images
img=cv.imread("Photos/cat2.jpg")
#.imread() method is used in OpenCV to read images. It takes image as input and returns it as a matrix of the pixels


if img is None:
    print("Error. Image not found")
else:
    cv.imshow("Cat2", img)
    # Displays the image in a new window. 2 parameters passed:
    # 1-Name of the window("Cat_1" in this case)
    # 2-The matrix of pixels to display(Output of img)

    cv.waitKey(0)
    # A keyboard binding method. It waits for a specific delay or time in milliseconds for a key to be pressed
    # 0 means that it will wait indefinitely for you to press the key

#Reading videos

capture=cv.VideoCapture("Videos/dog1.mp4")
#If input(hyperparameter):effect/use case
#0:WebCam
#1:1st camera
#2:2nd camera

#For reading a video, we use a while loop and read the video frame-by-frame

while True:
    isTrue,frame=capture.read()#Read the video frame by frame and returns a boolean value telling whether the frame was successfully read or not
    cv.imshow("Dog1_Video",frame)#Display/show the video frame by frame

    if cv.waitKey(20) & 0xFF==ord('x'):
        break #If 'x' key is pressed the condition becomes true

capture.release()
cv.destroyAllWindows()