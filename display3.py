import cv2

# init camera
camera = cv2.VideoCapture(0)
camera.set(3, 640)  # set frame width
camera.set(4, 480)  # set frame height

# master frame
master = None

while 1:
    # grab a frame
    (ret, frame) = camera.read()
    # end of feed
    if not ret:
        break
    # gray frame
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # blur frame
    blur_frame = cv2.GaussianBlur(gray_frame, (15, 15), 0)

    # initialize master
    if master is None:
        master = blur_frame
        continue

    # delta frame
    delta_frame = cv2.absdiff(master, blur_frame)
    # threshold frame
    threshold_frame = cv2.threshold(delta_frame, 15, 255, cv2.THRESH_BINARY)[1]

    # display
    #cv2.imshow("Motion Video", delta_frame)
    cv2.imshow("Motion Video", threshold_frame)

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