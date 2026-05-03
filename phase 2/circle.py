import cv2

image_path = r"D:\computer vision -Open Cv\phase 2\p4.jpg"

image = cv2.imread(image_path)


if image is not None:
    print("image loaded")

w,h = image.shape[:2]

center = w//2 , h//2
color = (255,0,0)
thickness = 5

circle_img = cv2.circle(image,center,130,color,thickness)

cv2.imshow("circle in the image",circle_img)
cv2.waitKey(0)
cv2.destroyAllWindows()