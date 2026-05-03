import cv2
image_path = r"D:\computer vision -Open Cv\image bloor and smoothing\portfolio-details.jpg"

image = cv2.imread(image_path)

median_blured = cv2.medianBlur(image,13 )


cv2.imshow("original",image)
cv2.imshow("blured",median_blured)
cv2.waitKey(0)
cv2.destroyAllWindows()