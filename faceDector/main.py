import cv2
img = cv2.imread('./images/photo2.jpg')

if img is not None:
    resized_img = cv2.resize(img, (500, 500))

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Process the resized image
else:
    print('Failed to load the image')

