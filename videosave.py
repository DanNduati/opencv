import numpy as np
import cv2
cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
#codec = cv.CV_FOURCC('M', 'J', 'P', 'G')fourcc = cv2.CV_FOURCC(*'MJPG')
out = cv2.VideoWriter('output.avi',-1, 20.0, (640,480))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)
        # write the flipped frame
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
