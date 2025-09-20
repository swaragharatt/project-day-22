# project-day-22
# Face Detection Tool

A **Tkinter-based desktop application** that detects faces in uploaded images using **OpenCV Haar Cascade Classifier**.  
The tool allows users to upload images and automatically highlights detected faces with rectangles.  

---

## Features  

- Upload any image in `.jpg`, `.jpeg`, `.png`, `.bmp`, or `.gif` format  
- Detect faces using **OpenCV Haar Cascade Classifier**  
- Displays the **number of faces detected**  
- Modern dark-themed UI with **Tkinter Canvas**  
- Resizes images to fit the display while maintaining **aspect ratio**  
- Handles errors if Haar Cascade XML is missing  

---

## Technologies Used  

- **Python 3** – Core programming language  
- **Tkinter** – GUI interface  
- **OpenCV (cv2)** – Face detection using Haar cascades  
- **Pillow (PIL)** – Image handling in Tkinter  

---

## Project Structure  

face-detection-tool/  
│── app.py               # Main application script  
│── haarcascade_frontalface_default.xml  # Haar cascade XML (optional if OpenCV default path exists)  
│── README.md            # Project documentation  

---

## How to Run  

1. Clone the repository.  
2. Install dependencies:  
   ```bash
   pip install opencv-python pillow numpy
Make sure haarcascade_frontalface_default.xml is available either in the OpenCV data path or in the project directory.

Run the app:

bash
Copy code
python app.py
Use the Upload Image button to select an image.

Click Detect Faces to see faces highlighted and the count displayed.

Screenshots
Upload Image Interface – Dark-themed Tkinter canvas for displaying uploaded images.
Face Detection – Faces are highlighted with rectangles, and total count is displayed dynamically.

## Output 

<img width="981" height="772" alt="Screenshot 2025-09-20 232741" src="https://github.com/user-attachments/assets/646523ee-6c41-4f14-8148-af150d726e4c" />

Author
Swara Gharat

yaml
Copy code
