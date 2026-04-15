from flask import Flask, redirect
import cv2
import numpy as np
import os

app = Flask(__name__)

BASE_PATH = r"C:\xampp\htdocs\voting-system"

model = cv2.face.LBPHFaceRecognizer_create()
model.read(os.path.join(BASE_PATH, "face_model.yml"))

label_map = np.load(os.path.join(BASE_PATH, "labels.npy"), allow_pickle=True).item()

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

@app.route('/face-login')
def face_login():
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        return "Camera not working"

    while True:
        ret, frame = cam.read()
        if not ret:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face = cv2.resize(gray[y:y+h, x:x+w], (200, 200))
            label, confidence = model.predict(face)

            if confidence < 70:
                user = label_map[label]
                cam.release()
                cv2.destroyAllWindows()

                return redirect("http://localhost/voting-system/face_login.php?user=" + user)

        cv2.imshow("Face Login", frame)

        # press ESC to cancel
        if cv2.waitKey(1) == 27:
            break

    cam.release()
    cv2.destroyAllWindows()

    return "Face not recognized"

if __name__ == "__main__":
    app.run(port=8000)