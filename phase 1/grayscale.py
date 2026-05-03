import cv2

image = cv2.imread("D:\computer vision -Open Cv\download.jpeg")

if image is not None:
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    saved = cv2.imwrite("Saved_image.png",gray)
else:
    print("Sorry")