import cv2
import  os
BASE_DIR = os.path.dirname(__file__)+"/Captured/image"
print(BASE_DIR)
capture = cv2.VideoCapture(0)

'''cap = True
while (cap):
    ret, frame = capture.read()
    cv2.imwrite("\cv_project\Captured\image.jpg", frame)
    cap = False

capture.release()
cv2.destroyAllWindows()
'''

fr = 0

while True:
    ret, frame = capture.read()
    cv2.imshow("Capture Frame", frame)
    if not ret:
        break
    key = cv2.waitKey(1)

    # Esc key
    if key % 256 == 27:
        print("Close")
        break
    # Space key
    elif key % 256 == 32:
        print("Image"+str(fr)+" captured")

        file = BASE_DIR+str(fr)+'.jpg'
        print(file)
        cv2.imwrite(file, frame)
        fr += 1

capture.release()
cv2.destroyAllWindows()
