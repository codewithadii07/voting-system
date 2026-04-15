# AI-Based Voting System with Face Recognition

## 📌 Project Overview

This project is a **secure online voting system** that uses **face recognition** for user authentication.
Users can log in either using a username/password or through real-time face detection.

---

## 🚀 Technologies Used

* Frontend: HTML
* Backend: PHP
* Database: MySQL
* AI Module: Python, OpenCV
* API Integration: Flask

---

## ⚙️ Features

* User Registration & Login
* Face Recognition Login
* Secure Voting System (One vote per user)
* Admin Panel to view results
* Prevention of duplicate voting

---

## 🧠 How It Works

1. User registers on the system
2. Face images are captured and stored in dataset
3. Model is trained using OpenCV (LBPH algorithm)
4. During login, face is detected and matched
5. If matched, user is automatically logged in
6. User can cast vote (only once)

---

## 📁 Project Structure

```
voting-system/
│
├── register.php
├── login.php
├── vote.php
├── logout.php
├── admin_login.php
├── admin_panel.php
├── face_login.php
│
├── dataset/
│    └── user1/
│
├── face_model.yml
├── labels.npy
│
├── capture_faces.py
├── train_model.py
├── recognize_face.py
├── face_login_api.py
```

---

## 🛠️ Setup Instructions

### 1. Install XAMPP

Start Apache and MySQL

---

### 2. Setup Database

* Open: http://localhost/phpmyadmin
* Create database: `voting_db`
* Import SQL file (if provided)

---

### 3. Install Python Libraries

```
pip install opencv-contrib-python
pip install flask
pip install numpy
```

---

### 4. Capture Face Data

```
python capture_faces.py
```

---

### 5. Train Model

```
python train_model.py
```

---

### 6. Run Flask API

```
python face_login_api.py
```

---

### 7. Run Website

Open in browser:

```
http://localhost/voting-system/login.php
```

---

## 🔗 Important URLs

* Login Page:
  http://localhost/voting-system/login.php

* Register Page:
  http://localhost/voting-system/register.php

* Face Login API:
  http://127.0.0.1:8000/face-login

* Admin Panel:
  http://localhost/voting-system/admin_login.php

---

## 🎯 Key Highlights

* AI-based authentication using face recognition
* Secure and user-friendly system
* Prevents multiple voting
* Real-time webcam detection

---

## 🏆 Conclusion

This project demonstrates how **AI + Web Technologies** can be combined to build a **secure and intelligent voting system**.

---

## 👨‍💻 Author

Aditya Kanoujiya
