import qrcode
from PIL import ImageTk, Image
import tkinter as tk

class QRGenerate:
    def __init__(self, master):
        self.master = master
        self.master.title("QR Code Generator")

        self.label = tk.Label(master, text="Enter the data to generate the QR code")
        self.label.pack(pady=10)

        self.input_entry = tk.Entry(master)
        self.input_entry.pack()

        self.label = tk.Label(master, text="Click the button to generate a QR code")
        self.label.pack(pady=10)

        self.generate_button = tk.Button(master, text="Generate QR Code", command=self.generate_qr)
        self.generate_button.pack(pady=5)

        self.canvas = tk.Canvas(master, width=300, height=300)
        self.canvas.pack(pady=10)

        def close_window():
            root.destroy()

        self.close_button = tk.Button(root, text="Close", command=close_window)
        self.close_button.pack()

    def generate_qr(self):
        data = self.input_entry.get()
        qr = qrcode.make(data)
        img = ImageTk.PhotoImage(qr)
        self.canvas.create_image(150, 150, image=img, anchor=tk.CENTER)
        self.canvas.img = img

if __name__ == "__main__":
    root = tk.Tk()
    qr_app = QRGenerate(root)
    root.mainloop()