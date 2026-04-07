import cv2
import face_recognition
import numpy as np
import pandas as pd
import os
import pickle
from datetime import datetime

ENCODINGS_PATH = 'encodings.pkl'
ATTENDANCE_CSV = 'attendance.csv'

# Load known face encodings
def load_encodings():
    if not os.path.exists(ENCODINGS_PATH):
        print('No encodings found. Please run train_faces.py first.')
        exit()
    with open(ENCODINGS_PATH, 'rb') as f:
        data = pickle.load(f)
    return data['encodings'], data['names']

# Mark attendance in CSV
def mark_attendance(name):
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%H:%M:%S')
    if os.path.exists(ATTENDANCE_CSV):
        df = pd.read_csv(ATTENDANCE_CSV)
    else:
        df = pd.DataFrame(columns=['Name', 'Date', 'Time'])
    # Prevent duplicate attendance for same day
    if not ((df['Name'] == name) & (df['Date'] == date_str)).any():
        df = pd.concat([df, pd.DataFrame([[name, date_str, time_str]], columns=['Name', 'Date', 'Time'])], ignore_index=True)
        df.to_csv(ATTENDANCE_CSV, index=False)
        print(f"Attendance marked for {name} at {time_str}")
    else:
        print(f"Attendance already marked for {name} today.")

def main():
    known_encodings, known_names = load_encodings()
    cap = cv2.VideoCapture(0)
    print("Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print('Failed to access camera.')
            break
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.5)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            if len(face_distances) > 0:
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_names[best_match_index]
                    mark_attendance(name)
            # Draw rectangle and label
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.7, (255, 255, 255), 2)
        cv2.imshow('Face Attendance', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
