"""
for flipping 
1 for horizontally -> left to right 
0 for vertically -> top to bottom
-1 for both 
"""




import cv2

image_path = r"D:\computer vision -Open Cv\phase 2\p4.jpg"

image = cv2.imread(image_path)


if image is not None:
    print("image loaded")

w,h,c = image.shape

center = w//2 , h//2

print(f"width : {w}\n height : {h} \n color : {c}")
print(f"center of the image is \n {center}")

M = cv2.getRotationMatrix2D(center,90,1.0)
rotated_img = cv2.warpAffine(image,M,(w,h))
flipped_image = cv2.flip(image,-1)

cv2.imshow("original image",image)
cv2.imshow("Rotated image",rotated_img)
cv2.imshow("flipped image",flipped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()