# Face-Based Attendance System

A beginner-friendly Python project to automate attendance using face recognition. This system captures face samples, trains a model, and marks attendance automatically via webcam.

---

## What is this project about?
This project is a complete solution for marking attendance using facial recognition. It allows you to:
- Capture face images for each person
- Train a face recognition model
- Mark attendance automatically when a face is recognized via webcam
- Store attendance in a CSV file (Name, Date, Time)
- Prevent duplicate attendance for the same person on the same day
- Display a live camera feed with name labels

---

## Technologies Used
- Python
- OpenCV
- face_recognition
- numpy
- pandas

---

## File Structure
- `capture_faces.py` - Capture face images for each person
- `train_faces.py` - Train the face recognition model
- `main.py` - Run the attendance system
- `attendance.csv` - Attendance records
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation

---

## How to Fork This Project
1. Click the **Fork** button at the top right of this repository on GitHub.
2. Clone your forked repository to your local machine:
	```
	git clone https://github.com/your-username/face-based-attendance-system.git
	```
3. Navigate to the project directory:
	```
	cd face-based-attendance-system
	```

---

## Setup Instructions

### 1. Install Dependencies
Open a terminal in the project folder and run:

```
pip install -r requirements.txt
```

---

## How to Use

### 1. Capture Face Images
Run the following command to capture face images for a new person:

```
python capture_faces.py
```
- Enter the person's name when prompted.
- The webcam will open. Position the face in front of the camera.
- Press the spacebar to capture an image. Capture at least 10 images.
- Press 'q' to quit when done.

### 2. Train the Model
After capturing faces, train the recognition model:

```
python train_faces.py
```
- This will process all captured faces and create encodings for recognition.

### 3. Run the Attendance System
Start the main attendance system:

```
python main.py
```
- The webcam will open and recognize faces in real-time.
- Attendance will be marked in `attendance.csv`.
- Each person is marked only once per day.

---

## Notes
- Make sure your webcam is connected and accessible.
- For best results, capture images in good lighting.

---

## Developer
**dev = tubakhxn**

---

## Footer
Built by tubakhxn
