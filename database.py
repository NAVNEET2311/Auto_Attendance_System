import os
import cv2
import pandas as pd
from datetime import datetime
from .utils import ensure_folder_exists

def save_new_user_face(id_, name, crop_face_func, messagebox, cv2, simpledialog):
    ensure_folder_exists('dataset')
    cap = cv2.VideoCapture(0)
    messagebox.showinfo("Info", "Camera will open now. Press 'c' to capture your face photo.")
    while True:
        ret, frame = cap.read()
        if not ret:
            messagebox.showerror("Error", "Failed to open camera.")
            break
        cv2.imshow('Register - Press c to capture', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):
            face_img = crop_face_func(frame)
            if face_img is None:
                messagebox.showwarning("Warning", "No face detected, try again.")
            else:
                filename = f"dataset/{id_}_{name}.jpg"
                cv2.imwrite(filename, face_img)
                messagebox.showinfo("Success", f"Face image saved as {filename}")
                break
        elif key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def load_known_face_images():
    known_images = []
    known_names = []
    known_ids = []
    dataset_folder = 'dataset'
    ensure_folder_exists(dataset_folder)
    for filename in os.listdir(dataset_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            path = os.path.join(dataset_folder, filename)
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            if img is not None:
                known_images.append(img)
                base = os.path.splitext(filename)[0]
                id_, name = base.split('_', 1)
                known_ids.append(id_)
                known_names.append(name)
    return known_images, known_ids, known_names

def mark_attendance(id_, name):
    attendance_folder = 'attendance'
    ensure_folder_exists(attendance_folder)
    attendance_file = os.path.join(attendance_folder, 'attendance_log.csv')
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%H:%M:%S')
    if os.path.exists(attendance_file):
        df = pd.read_csv(attendance_file)
    else:
        df = pd.DataFrame(columns=['ID', 'Name', 'Date', 'Time'])
    already_marked = ((df['ID'] == id_) & (df['Date'] == date_str)).any()
    if not already_marked:
        new_entry = {'ID': id_, 'Name': name, 'Date': date_str, 'Time': time_str}
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_csv(attendance_file, index=False)
        print(f"Attendance marked for {name} at {time_str}")
