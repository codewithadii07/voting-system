import cv2
import os

# FULL PATH (IMPORTANT)
path = r"C:\xampp\htdocs\voting-system\dataset\user1"

# create folder if not exists
if not os.path.exists(path):
    os.makedirs(path)

cam = cv2.VideoCapture(0)
count = 0

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cam.read()

    if not ret:
        print("Camera not working")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1
        face = gray[y:y+h, x:x+w]

        file_name = os.path.join(path, f"{count}.jpg")
        cv2.imwrite(file_name, face)

        print("Saved:", file_name)

        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

    cv2.imshow("Capturing Faces", frame)

    # stop after 20 images (faster test)
    if count >= 20:
        print("Done capturing")
        break

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()