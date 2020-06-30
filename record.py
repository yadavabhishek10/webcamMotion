import cv2
import numpy as np
import  os
BASE_DIR = os.path.dirname(__file__)+"/recording/outputVideo"
# Create a VideoCapture object
capture = cv2.VideoCapture(0)
# Check if camera opened successfully
if (capture.isOpened() == False):
    print("Unable to read camera feed")

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(capture.get(3))
frame_height = int(capture.get(4))

# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
video = cv2.VideoWriter(BASE_DIR+'.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 20, (frame_width, frame_height))
while True:
    ret, frame = capture.read()
    if ret == True:
        # Write the frame into the file 'output.avi'
        video.write(frame)
        # Display the resulting frame
        cv2.imshow('Display Frame', frame)
        # Press Q on keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Break the loop
    else:
        break

# When everything done, release the video capture and video write objects
capture.release()
video.release()
# Closes all the frames
cv2.destroyAllWindows()

