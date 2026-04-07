import os
import face_recognition
import numpy as np
import pickle

DATASET_DIR = 'faces'
ENCODINGS_PATH = 'encodings.pkl'

def train_faces():
    known_encodings = []
    known_names = []
    if not os.path.exists(DATASET_DIR):
        print('No faces directory found. Please run capture_faces.py first.')
        return
    for person_name in os.listdir(DATASET_DIR):
        person_dir = os.path.join(DATASET_DIR, person_name)
        if not os.path.isdir(person_dir):
            continue
        for img_name in os.listdir(person_dir):
            img_path = os.path.join(person_dir, img_name)
            image = face_recognition.load_image_file(img_path)
            face_locations = face_recognition.face_locations(image)
            if len(face_locations) != 1:
                print(f"Skipping {img_path}: found {len(face_locations)} faces.")
                continue
            encoding = face_recognition.face_encodings(image, face_locations)[0]
            known_encodings.append(encoding)
            known_names.append(person_name)
            print(f"Encoded: {img_path}")
    if not known_encodings:
        print('No valid face encodings found.')
        return
    data = {'encodings': known_encodings, 'names': known_names}
    with open(ENCODINGS_PATH, 'wb') as f:
        pickle.dump(data, f)
    print(f"Training complete. Encodings saved to {ENCODINGS_PATH}.")

if __name__ == '__main__':
    train_faces()
