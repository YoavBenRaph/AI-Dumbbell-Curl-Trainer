import cv2
import numpy as np
import time
import PoseModule as pm

# Use the webcam (device 0)
cap = cv2.VideoCapture(0)

# Check if the camera was opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0

# Define the target width and height from your video
wT, hT = 1280, 720

while True:
    success, img = cap.read()

    # If the camera feed is interrupted, break the loop
    if not success or img is None:
        print("Camera feed interrupted or frame could not be read.")
        break

    # Resize the camera frame to match the original video size
    img = cv2.resize(img, (wT, hT))

    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)

    if len(lmList) != 0:
        # Left Arm
        angle = detector.findAngle(img, 11, 13, 15)
        per = np.interp(angle, (210, 310), (0, 100))
        bar = np.interp(angle, (220, 310), (650, 100))

        # Check for dumbbell curls
        colour = (255, 0, 255)
        if per == 100:
            colour = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        elif per == 0:
            colour = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0

        # Draw Bar
        cv2.rectangle(img, (1110, 100,), (1175, 650), colour, 3)
        cv2.rectangle(img, (1110, int(bar)), (1175, 650), colour, cv2.FILLED)
        cv2.putText(img, f'{int(per)}%', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4, colour, 4)

        # Draw Curl Count
        cv2.rectangle(img, (0, 450,), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15, (255, 0, 0), 25)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
    cv2.imshow("Image", img)

    cv2.waitKey(1)