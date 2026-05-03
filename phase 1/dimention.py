import cv2

image = cv2.imread("D:\computer vision -Open Cv\download.jpeg")

if image is not None:
    h,w,c = image.shape
    print(f"Image loaded config :\n Height : {h} \n Width : {w} \n & Channels : {c}")
else:
    print("Error :Can not load the image ")