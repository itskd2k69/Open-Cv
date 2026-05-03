# """
# steps which i have to do in this

# first load the image 
# convert it into the gray scale
# show that image 
# as well save it too 
# """

# # Step 1 : Load the image 

# from cv2 import COLOR_RGB2GRAY
# import cv2

# image = cv2.imread(r"Assignment 1\p6.jpg")

# if image is not None:
#     # Step 2 : convert it into the gray scale
#     gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#     cv2.imshow("Showing the image",gray_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

#     #Step 3 : Save this Gray Image

#     saved_one = cv2.imwrite("output_saved_image.jpg",gray_image)
# else:
#     print("Error : There is a problem to load the image")

import cv2
import sys

image_path = r"D:\computer vision -Open Cv\Assignment 1\p6.jpg"

# Step 1: Load image
image = cv2.imread(image_path)

if image is None:
    print("Error: Image could not be loaded")
    sys.exit()

print("Image Loaded Successfully")

# Step 2: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Step 3: Save image (FIXED PATH)
output_path = r"D:\computer vision -Open Cv\Assignment 1\saving_image.jpg"

saved = cv2.imwrite(output_path, gray)

if saved:
    print(f"Image saved successfully at: {output_path}")
else:
    print("Error: Failed to save the image")

# Step 4: Show image

print("Before imshow")
cv2.imshow("Grayscale Image", gray)
print("After imshow") 

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Image shown")


