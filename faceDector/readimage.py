# import cv2
from tkinter import *

root = Tk()
canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
img = PhotoImage(file="ball.ppm")
canvas.create_image(20,20, anchor=NW, image=img)
mainloop()

# img = cv2.imread(img_from_file)
#
# if img is not None:
#     resized_img = cv2.resize(img, (500, 500))
#
#     cv2.imshow('image', img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#     # Process the resized image
# else:
#     print('Failed to load the image')
#
