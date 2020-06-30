import cv2

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

    # display
    cv2.imshow("Raw Video", frame)

    # key delay and action
    # Press key 'q' to quit the webcam
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key != 255:
        print('key:', [chr(key)])

# release camera
camera.release()
# close all windows
cv2.destroyAllWindows()