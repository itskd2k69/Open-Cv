import cv2

image = cv2.imread("D:\computer vision -Open Cv\download.jpeg")

if image is not None:
    cv2.imshow("Showing Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image is not loaded")


