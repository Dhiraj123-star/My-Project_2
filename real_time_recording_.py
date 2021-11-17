# real time recording using python

import cv2

ip4_url ="http://10.8.197.17:8080"

# read video

cam= f"{ip4_url}/video"

cap = cv2.VideoCapture(cam)

while True:
    # read each frame from video
    ret,frame= cap.read()
    # resize frames
    frame= cv2.resize(frame,(600,600))
    # display frame
    cv2.imshow("Mobile Camera: ",frame)

    # press q to break the loop

    if cv2.waitKey(1)==ord('q'):
        break

# release camera
cap.release()

# destroy windows

cv2.destroyAllWindows()

