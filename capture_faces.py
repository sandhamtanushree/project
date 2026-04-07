import cv2
import os

# Directory to save face images
DATASET_DIR = 'faces'
if not os.path.exists(DATASET_DIR):
    os.makedirs(DATASET_DIR)

def capture_faces():
    name = input('Enter the name of the person: ').strip()
    if not name:
        print('Name cannot be empty.')
        return
    person_dir = os.path.join(DATASET_DIR, name)
    if not os.path.exists(person_dir):
        os.makedirs(person_dir)
    else:
        print(f"Directory for {name} already exists. New images will be added.")

    cap = cv2.VideoCapture(0)
    count = 0
    print("Press SPACE to capture an image. Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print('Failed to access camera.')
            break
        cv2.imshow(f'Capturing faces for {name}', frame)
        key = cv2.waitKey(1)
        if key % 256 == 32:  # SPACE pressed
            img_name = os.path.join(person_dir, f"{name}_{count+1}.jpg")
            cv2.imwrite(img_name, frame)
            print(f"Saved: {img_name}")
            count += 1
        elif key & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    print(f"Total images captured for {name}: {count}")

if __name__ == '__main__':
    capture_faces()
