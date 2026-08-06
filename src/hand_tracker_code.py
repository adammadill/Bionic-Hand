import cv2 
import serial
import time
import numpy as np
from cvzone.HandTrackingModule import HandDetector

try:
    arduino = serial.Serial(port='COM3', baudrate=9600, timeout=0.1) # check its COM3 i did it through Device Manager
    time.sleep(2)
    print("Arduino connected")
except Exception as e:
    print(f"Error: {e}")
    exit()

cap = cv2.VideoCapture(0) # main cam
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cap.read() # takes image, returns success (True if working), and image img
    if not success:
        continue # accounts for cam failing

    hands, img = detector.findHands(img) # finds hands in image and draws, returning list hands
    if hands:
        hand = hands[0] # only 1 hand
        lmList = hand["lmList"] # list of 21 landmarks, xyz

        # calculate 3d interior joint angle

        # thumb, 0 is wrist, 2 is MCP joint, 4 is tip
        angle_thumb, img = detector.findAngle(lmList[0][0:2], lmList[2][0:2], lmList[4][0:2], img=img) # replace img with _ if you want angles in image, [0:2] takes XY, try 1 vs 0, 0 makes a bigger angle

        # index, 5 is MCP joint, 6 is PIP joint, 8 is tip
        angle_index, img = detector.findAngle(lmList[5][0:2], lmList[6][0:2], lmList[8][0:2], img=img) 

        # middle
        angle_middle, img = detector.findAngle(lmList[9][0:2], lmList[10][0:2], lmList[12][0:2], img=img)

        # ring
        angle_ring, img = detector.findAngle(lmList[13][0:2], lmList[14][0:2], lmList[16][0:2], img=img)

        # pinky
        angle_pinky, img = detector.findAngle(lmList[17][0:2], lmList[18][0:2], lmList[20][0:2], img=img) 

        # map to servo angles
        # servo 0 is open, 180 between fingers is open
        
        servo_thumb = int(np.interp(angle_thumb, [90,160], [180, 0])) # interpolates angle_index from range 60-170 to 0-180 for servo, test 90, 160 first angles
        servo_index = int(np.interp(angle_index, [60,170], [180, 0])) # test hand angles 60, 170
        servo_middle = int(np.interp(angle_middle, [60,170], [180, 0]))
        servo_ring = int(np.interp(angle_ring, [60,170], [180, 0]))
        servo_pinky = int(np.interp(angle_pinky, [60,170], [180, 0]))
        

        # format
        command = f"{servo_thumb}, {servo_index}, {servo_middle}, {servo_ring}, {servo_pinky}!" # send as string because the numbers have to be telled apart eg. cant send as 09045180
        arduino.write(command.encode('utf-8'))

    cv2.imshow("Hand Tracker Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()