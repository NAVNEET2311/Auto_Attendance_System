import cv2
from .database import load_known_face_images, mark_attendance
from .utils import orb_feature_match

def recognize_and_mark_attendance(messagebox):
    known_images, known_ids, known_names = load_known_face_images()
    if len(known_images) == 0:
        messagebox.showerror("Error", "No registered users found! Please register first.")
        return

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    messagebox.showinfo("Info", "Attendance marking started. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            messagebox.showerror("Error", "Failed to open camera.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        label = "User unregistered"
        for (x, y, w, h) in faces:
            face_img = gray[y:y+h, x:x+w]
            best_match_count = 0
            best_match_index = -1
            for i, known_img in enumerate(known_images):
                matches_count = orb_feature_match(face_img, known_img)
                if matches_count > best_match_count:
                    best_match_count = matches_count
                    best_match_index = i
            if best_match_count > 15:
                name = known_names[best_match_index]
                id_ = known_ids[best_match_index]
                mark_attendance(id_, name)
                label = f"{name} - Present"
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.imshow('Mark Attendance - Press q to quit', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
