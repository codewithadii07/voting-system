import cv2
import os
import numpy as np

# dataset path
dataset_path = r"C:\xampp\htdocs\voting-system\dataset"

faces = []
labels = []
label_map = {}
current_label = 0

# loop through each user folder
for user in os.listdir(dataset_path):
    user_path = os.path.join(dataset_path, user)

    # skip if not a folder
    if not os.path.isdir(user_path):
        continue

    label_map[current_label] = user

    # loop through images
    for img_name in os.listdir(user_path):
        img_path = os.path.join(user_path, img_name)

        # read image
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        # skip if image not loaded
        if img is None:
            continue

        # resize to fixed size (IMPORTANT)
        img = cv2.resize(img, (200, 200))

        faces.append(img)
        labels.append(current_label)

    current_label += 1

# convert labels to numpy array
labels = np.array(labels)

# create LBPH model
model = cv2.face.LBPHFaceRecognizer_create()

# train model
model.train(faces, labels)

# save model
model.save("face_model.yml")

# save label map
np.save("labels.npy", label_map)

print("Training complete!")