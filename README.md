Real-time Face Recognition Attendance System
===========================================

This project is a real-time attendance system using face recognition, built with Python, OpenCV, and Tkinter. The system allows users to register their faces and mark attendance via a webcam. Attendance data is stored in CSV format.

------------------------------------------------------------
Features
------------------------------------------------------------
- Register new users by capturing their face via webcam.
- Mark attendance in real-time using face recognition.
- Attendance is recorded with date and time, avoiding duplicate entries for the same day.
- Simple graphical interface using Tkinter.
- Modular codebase organized into separate files for maintainability.

------------------------------------------------------------
File Structure
------------------------------------------------------------
- main.py
    Entry point; launches the main GUI window.
- gui.py
    Contains all Tkinter GUI logic and user interaction functions.
- database.py
    Handles saving/loading user face images and attendance records.
- utils.py
    Utility functions for folder management, face cropping, and feature matching.
- face_recognition.py
    Handles face recognition and attendance marking logic.
- dataset/
    Stores registered user face images.
- attendance/
    Stores the attendance CSV log.

------------------------------------------------------------
Requirements
------------------------------------------------------------
- Python 3.x
- OpenCV (opencv-python)
- Pandas
- Tkinter (usually included with Python)

Install dependencies with:
    pip install opencv-python pandas

------------------------------------------------------------
How to Use
------------------------------------------------------------
1. Run the application:
       python main.py

2. To register a user:
   - Click "Register New User" in the GUI.
   - Enter the name and ID when prompted.
   - Use the webcam to capture the face (press 'c' to capture).

3. To mark attendance:
   - Click "Mark Attendance".
   - The system will recognize faces in front of the webcam and log attendance.

------------------------------------------------------------
Notes
------------------------------------------------------------
- Ensure your webcam is connected and accessible.
- All images and attendance logs are saved locally in the `dataset` and `attendance` folders.
- You can adjust face recognition thresholds in the source code for improved accuracy.

------------------------------------------------------------
Author
------------------------------------------------------------
- NAVNEET
- Last updated: June 8, 2025

------------------------------------------------------------

