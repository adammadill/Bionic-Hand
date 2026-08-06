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

def findAngle(p1, p2, p3, img=None): # img=None is the default
    """
    Calculates the interior angle between three (x, y) points.
    p2 is the vertex/joint point.
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    # Calculate angle
    angle = np.degrees(np.arctan2(y3 - y2, x3 - x2) - np.arctan2(y1 - y2, x1 - x2))
    
    # Keep angle positive and within 0-180 degrees
    angle = abs(angle)
    if angle > 180:
        angle = 360 - angle

    # Optional
    if img is not None:
        cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 2)
        cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 2)
        cv2.circle(img, (x2, y2), 6, (0, 0, 255), cv2.FILLED)

    return angle, img

while True:

    print('Menu:')
    print('1. Open hand')
    print('2. Close hand')
    print('3. Cam detect')
    print('q. Quit')

    choice = input('Enter your choice (1, 2, or 3): ')

    if choice == '1':
        open_cmd = f"{0}, {0}, {0}, {0}, {0}!"
        arduino.write(open_cmd.encode('utf-8'))
    elif choice == '2':
        close_cmd = f"{180}, {180}, {180}, {180}, {180}!"
        arduino.write(close_cmd.encode('utf-8'))
    elif choice == '3':
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
                angle_thumb, img = findAngle(lmList[0][0:2], lmList[2][0:2], lmList[4][0:2], img=img) # replace img with _ if you want angles in image, [0:2] takes XY, try 1 vs 0, 0 makes a bigger angle

                # index, 5 is MCP joint, 6 is PIP joint, 8 is tip
                angle_index, img = findAngle(lmList[5][0:2], lmList[6][0:2], lmList[8][0:2], img=img) 

                # middle
                angle_middle, img = findAngle(lmList[9][0:2], lmList[10][0:2], lmList[12][0:2], img=img)

                # ring
                angle_ring, img = findAngle(lmList[13][0:2], lmList[14][0:2], lmList[16][0:2], img=img)

                # pinky
                angle_pinky, img = findAngle(lmList[17][0:2], lmList[18][0:2], lmList[20][0:2], img=img) 

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
            if cv2.waitKey(1) & 0xFF == ord('q'): # press q on window
                break

        cap.release()
        cv2.destroyAllWindows()
        #arduino.close()

    elif choice == 'q':
        break