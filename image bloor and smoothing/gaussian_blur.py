import cv2
image_path = r"D:\computer vision -Open Cv\image bloor and smoothing\portfolio-details.jpg"

image = cv2.imread(image_path)

blured = cv2.GaussianBlur(image,(5,5),0)

cv2.imshow("original",image)
cv2.imshow("blured",blured)
cv2.waitKey(0)
cv2.destroyAllWindows()