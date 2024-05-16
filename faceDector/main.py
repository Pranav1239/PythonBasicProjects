import tkinter as tk
import cv2

def close_window():
    root.destroy()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("No camera detected")
else:
    cap.set(3, 1280)
    cap.set(4, 720)

    root = tk.Tk()
    root.title("Face Detection")

    label = tk.Label(root, text="Face Detection using OpenCV")
    label.pack(pady=10)


    canvas = tk.Canvas(root, width=1280, height=720)
    canvas.pack()

    def update_video_feed():
        success, img = cap.read()
        if success:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (1280, 720))
            img = tk.PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())
            canvas.create_image(0, 0, anchor=tk.NW, image=img)
            root.img = img
            canvas.after(10, update_video_feed)

    update_video_feed()

    close_button = tk.Button(root, text="Close", command=close_window)
    close_button.pack()

    root.mainloop()

cap.release()
cv2.destroyAllWindows()
