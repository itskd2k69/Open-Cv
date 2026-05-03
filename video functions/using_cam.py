import cv2

capture = cv2.VideoCapture(0)

while True:
    ret , frame = capture.read()

    if not ret:
        print("Could not read the fram")
        break

    cv2.imshow("Webcam Feed",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

capture.release()
cv2.destroyAllWindows()
