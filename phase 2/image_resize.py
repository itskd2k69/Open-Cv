import cv2

image_path = r"D:\computer vision -Open Cv\phase 2\p4.jpg"

image = cv2.imread(image_path)


if image is not None:
    print("image loaded")

resized_img = cv2.resize(image,dsize=(300,300))
cv2.imshow("image is been showing",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

resized_path = r"D:\computer vision -Open Cv\phase 2\resized_image.png"
resized_save = cv2.imwrite(resized_path,resized_img)

if resized_save is not None:
    print("image saved successfully")

shape = resized_img.shape

print(f"the shape of the image is : \n {shape}")
