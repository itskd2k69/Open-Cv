import cv2
import mediapipe as mp

# ---------------- FACE CASCADE ----------------
face_cascade = cv2.CascadeClassifier(r"D:\computer vision -Open Cv\Face & Object Detection\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"D:\computer vision -Open Cv\Face & Object Detection\haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier(r"D:\computer vision -Open Cv\Face & Object Detection\haarcascade_smile.xml")

if face_cascade.empty() or eye_cascade.empty() or smile_cascade.empty():
    raise IOError("Error loading cascade files. Check paths.")

# ---------------- MEDIAPIPE HAND SETUP ----------------
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# ---------------- CAMERA ----------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot open webcam")

cv2.namedWindow("Smart Face Detector", cv2.WINDOW_NORMAL)

# ---------------- FINGER COUNT FUNCTION ----------------
def count_fingers(hand_landmarks):
    tips = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb (simple heuristic)
    if hand_landmarks.landmark[tips[0]].x < hand_landmarks.landmark[tips[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other 4 fingers
    for i in range(1, 5):
        if hand_landmarks.landmark[tips[i]].y < hand_landmarks.landmark[tips[i] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return sum(fingers)

# ---------------- MAIN LOOP ----------------
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # -------- FACE DETECTION --------
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # -------- EYE DETECTION --------
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        if len(eyes) > 0:
            cv2.putText(frame, "Eyes Detected", (x, y - 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        # -------- SMILE DETECTION --------
        h_half = int(h / 2)
        roi_gray_lower = roi_gray[h_half:h, :]
        roi_color_lower = roi_color[h_half:h, :]

        roi_gray_lower = cv2.GaussianBlur(roi_gray_lower, (5, 5), 0)

        smiles = smile_cascade.detectMultiScale(
            roi_gray_lower,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(25, 25)
        )

        if len(smiles) > 0:
            cv2.putText(frame, "Smiling", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(roi_color_lower, (sx, sy),
                              (sx + sw, sy + sh), (255, 0, 0), 2)

    # -------- HAND DETECTION --------
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Count fingers
            fingers = count_fingers(hand_landmarks)

            cv2.putText(frame, f'Fingers: {fingers}',
                        (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (255, 0, 0),
                        2)

    # -------- DISPLAY --------
    cv2.imshow("Smart Face Detector", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()