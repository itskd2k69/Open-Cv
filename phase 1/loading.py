import cv2

image = cv2.imread("D:\computer vision -Open Cv\download.jpeg")

if image is None:
    print("Error image not Found")
else:
    print("Image Loaded Successfully")


