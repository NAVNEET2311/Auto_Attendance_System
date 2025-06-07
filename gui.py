import tkinter as tk
from tkinter import messagebox, simpledialog
from database import save_new_user_face
from .utils import crop_face_from_frame
from .face_recognition import recognize_and_mark_attendance

def register_user():
    name = simpledialog.askstring("Register User", "Enter Name:")
    if not name or name.strip() == '':
        messagebox.showerror("Error", "Name cannot be empty.")
        return
    id_ = simpledialog.askstring("Register User", "Enter ID Number:")
    if not id_ or id_.strip() == '':
        messagebox.showerror("Error", "ID Number cannot be empty.")
        return
    save_new_user_face(id_.strip(), name.strip(), crop_face_from_frame, messagebox, __import__('cv2'), simpledialog)

def mark_attendance_gui():
    recognize_and_mark_attendance(messagebox)

def main_gui():
    root = tk.Tk()
    root.title("Real-time Attendance System")
    tk.Label(root, text="Real-time Attendance System", font=("Helvetica", 16)).pack(pady=20)
    btn_register = tk.Button(root, text="Register New User", width=25, command=register_user)
    btn_register.pack(pady=10)
    btn_attendance = tk.Button(root, text="Mark Attendance", width=25, command=mark_attendance_gui)
    btn_attendance.pack(pady=10)
    root.geometry("350x200")
    root.mainloop()
