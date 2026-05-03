import cv2

image_path = r"D:\computer vision -Open Cv\phase 2\p4.jpg"

image = cv2.imread(image_path)


if image is not None:
    print("image loaded")

cropped_img = image[100:200, 50:150]
cropped_path = r"D:\computer vision -Open Cv\phase 2\cropped_one.jpg"
cropped_save = cv2.imwrite(cropped_path,cropped_img)

if cropped_save:
    print("cropped image")

cv2.imshow("cropped image",cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()