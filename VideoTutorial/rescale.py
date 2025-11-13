import cv2 as cv
#Reason behind resizing and rescaling images/videos: To reduce computational power/strain
def rescaleFrame(frame,scale=0.5):
    #Works for images,videos and live Videos
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[0] * scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #Only for Live VIdeo
    capture.set(3,width)
    capture.set(4,height)




capture=cv.VideoCapture("Videos/dog1.mp4")
while True:
    isTrue,frame=capture.read()
    frame_resized=rescaleFrame(frame)
    cv.imshow("Dog 1 Original",frame)
    cv.imshow("Dog 1 Rescaled",frame_resized)

    if cv.waitKey(20) & 0xFF==ord('x'):
        break
capture.release()
cv.destroyAllWindows()