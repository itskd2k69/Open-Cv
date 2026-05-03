import cv2
image_input = input("Enter file location: ")
image = cv2.imread(image_input)
if image is None:
    print("Image does not exist")
    exit()
Choice = input("""Choose operation to perfrom: \n1. Draw line\n2. Draw Rectangle\n3. Draw Circle\n4. Write text\n""")

if(Choice=='1'):
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    thickness = int(input("Enter thickness: "))
    cv2.line(image, (x1,y1), (x2,y2), (0,0,255), thickness)

elif(Choice=='2'):
    x1 = int(input("Enter x1"))
    y1 = int(input("Enter y1"))
    x2 = int(input("Enter x2"))
    y2 = int(input("Enter y2"))
    thickness = int(input("Enter thickness: "))
    cv2.rectangle(image, (x1,y1), (x2,y2), (0,0,255), thickness)

elif(Choice=='3'):
    x, y = map(int, input("Enter center (x y): ").split())
    radius = int(input("Enter radius"))
    center = (x,y)
    thickness = int(input("Enter thickness: "))
    cv2.circle(image, center, radius, (0,0,255), thickness)

elif(Choice=='4'):
    text = input("Enter text: ")
    thickness = int(input("Enter thickness: "))
    cv2.putText(image, text, (50,300), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), thickness)

else:
    print("Please enter valid operation")

cv2.imshow("Output_image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

wish = input("Do you want to save this file?").lower()
if(wish == "yes"):
    success = cv2.imwrite("CATIEY.PNG", image)
    if(success):
        print("Image saved successfully!")
    else:
        print("Failed to save image!")