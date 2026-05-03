import cv2

image = cv2.imread("D:\computer vision -Open Cv\download.jpeg")

if image is not None:
    success =cv2.imwrite("Outputimage.png",image)
    if success:
        print("Image is saved successfully")
    else:
        print("Image is not saved")
else:
    print("Error : Image could not load")