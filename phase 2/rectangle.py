import cv2

image_path = r"D:\computer vision -Open Cv\phase 2\p4.jpg"

image = cv2.imread(image_path)


if image is not None:
    print("image loaded")


w,h,c = image.shape

print(f"width : {w}\n height : {h} \n color : {c}")

pt1 = (50,50)
pt2 = (280,280)
color = (0,255,0)
thickness = 2

rec_image = cv2.rectangle(image,pt1,pt2,color,thickness)

cv2.imshow("rectangle",rec_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
