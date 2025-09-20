import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
import os

HAARCASCADE_PATH = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
if not os.path.exists(HAARCASCADE_PATH):
    HAARCASCADE_PATH = 'haarcascade_frontalface_default.xml'

try:
    FACE_CASCADE = cv2.CascadeClassifier(HAARCASCADE_PATH)
    if FACE_CASCADE.empty():
        raise IOError("Could not load the Haar Cascade XML file.")
except IOError as e:
    print(f"Error: {e}")
    print("Please make sure 'haarcascade_frontalface_default.xml' is in the same directory as this script.")
    FACE_CASCADE = None 
class FaceDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Detection Tool")
        self.root.geometry("800x600")
        self.root.configure(bg="#0D0014")

        self.main_frame = tk.Frame(self.root, bg="#0D0014", bd=2, relief="solid", highlightbackground="#8A2BE2", highlightcolor="#8A2BE2", highlightthickness=3)
        self.main_frame.pack(expand=True, padx=20, pady=20, fill="both")

        self.title_label = tk.Label(self.main_frame, text="Face Detector", font=("Inter", 24, "bold"), fg="#DDA0DD", bg="#0D0014")
        self.title_label.pack(pady=20)

        self.canvas = tk.Canvas(self.main_frame, bg="#1E002B", bd=0, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, padx=20, pady=10)

        self.result_label = tk.Label(self.main_frame, text="No image loaded", font=("Inter", 16), fg="#DDA0DD", bg="#0D0014")
        self.result_label.pack(pady=10)

        self.button_frame = tk.Frame(self.main_frame, bg="#0D0014")
        self.button_frame.pack(pady=20)

        self.upload_button = tk.Button(self.button_frame, text="Upload Image", font=("Inter", 12, "bold"), fg="#FFFFFF", bg="#8A2BE2", activebackground="#9B30F5", activeforeground="#FFFFFF", relief="flat", bd=0, command=self.upload_image, padx=20, pady=10)
        self.upload_button.pack(side="left", padx=10, ipady=5)

       
        if FACE_CASCADE is None:
            self.detect_button = tk.Button(self.button_frame, text="Detect Faces", font=("Inter", 12, "bold"), fg="#FFFFFF", bg="#5E208A", relief="flat", bd=0, padx=20, pady=10, state=tk.DISABLED)
        else:
            self.detect_button = tk.Button(self.button_frame, text="Detect Faces", font=("Inter", 12, "bold"), fg="#FFFFFF", bg="#5E208A", activebackground="#6F289E", activeforeground="#FFFFFF", relief="flat", bd=0, command=self.detect_faces, padx=20, pady=10, state=tk.DISABLED)
        self.detect_button.pack(side="left", padx=10, ipady=5)

        self.original_image = None
        self.display_photo = None

        if FACE_CASCADE is None:
            self.result_label.config(text="Error: Haar Cascade file not found. Please place it in the script directory.")

    def upload_image(self):
        """
        Opens a file dialog to allow the user to select an image file.
        Loads the selected image and displays it on the canvas.
        """
        if FACE_CASCADE is None:
            self.result_label.config(text="Error: Face detection not available.")
            return

        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )
        if file_path:
            self.original_image = cv2.imread(file_path)
            self.original_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)
            self.display_image(self.original_image)
            self.detect_button.config(state=tk.NORMAL, bg="#8A2BE2")
            self.result_label.config(text="Image loaded. Click 'Detect Faces' to proceed.")

    def display_image(self, image):
        """
        Resizes and displays the given image on the canvas while maintaining aspect ratio.
        """
        if image is None:
            return

        h, w, _ = image.shape
        canvas_w = self.canvas.winfo_width()
        canvas_h = self.canvas.winfo_height()

        if h > canvas_h or w > canvas_w:
            aspect_ratio = w / h
            if aspect_ratio > (canvas_w / canvas_h):
                new_w = canvas_w
                new_h = int(new_w / aspect_ratio)
            else:
                new_h = canvas_h
                new_w = int(new_h * aspect_ratio)
            
            resized_image = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)
        else:
            resized_image = image

        pil_image = Image.fromarray(resized_image)
        self.display_photo = ImageTk.PhotoImage(pil_image)
        
        self.canvas.delete("all")
        self.canvas.create_image(self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2, image=self.display_photo, anchor="center")
        self.canvas.image = self.display_photo 
    def detect_faces(self):
        """
        Detects faces in the loaded image using the Haar Cascade Classifier.
        Draws rectangles around the detected faces and updates the count.
        """
        if self.original_image is not None and FACE_CASCADE is not None:
            
            detected_image = self.original_image.copy()
            
            gray_image = cv2.cvtColor(detected_image, cv2.COLOR_RGB2GRAY)
            
            faces = FACE_CASCADE.detectMultiScale(
                gray_image,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )

            for (x, y, w, h) in faces:
                cv2.rectangle(detected_image, (x, y), (x+w, y+h), (255, 255, 0), 2)
            
            face_count = len(faces)
            self.result_label.config(text=f"Faces Detected: {face_count}")

            self.display_image(detected_image)
        else:
            self.result_label.config(text="Please upload an image first or fix the Haar Cascade issue.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceDetectionApp(root)
    root.bind("<Configure>", lambda event: app.display_image(app.original_image) if app.original_image is not None else None)
    root.mainloop()
