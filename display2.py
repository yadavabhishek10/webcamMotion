import cv2
from datetime import datetime

# init camera
camera = cv2.VideoCapture(0)
camera.set(3, 1280)  # set frame width
camera.set(4, 720)  # set frame height


while 1:
    # grab a frame
    (ret, frame) = camera.read()
    # end of feed
    if not ret:
        break

    # gray frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,str(datetime.now()),(10,30), font, 1,(255,255,255),2,cv2.LINE_AA)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    


    # display
    cv2.imshow("B/W Video", gray_frame)

    # key delay and action
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key != 255:
        print('key:', [chr(key)])

# release camera
camera.release()
# close all windows
cv2.destroyAllWindows()
