import cv2
import numpy as np

# load trained model
model = cv2.face.LBPHFaceRecognizer_create()
model.read("face_model.yml")

# load labels
label_map = np.load("labels.npy", allow_pickle=True).item()

# face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# start camera
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    
    if not ret:
        print("Camera error")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]

        # resize same as training
        face = cv2.resize(face, (200, 200))

        label, confidence = model.predict(face)

        # confidence check (lower = better)
        if confidence < 80:
            name = label_map[label]
        else:
            name = "Unknown"

        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(frame, f"{name} ({int(confidence)})",
                    (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0,255,0),
                    2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()