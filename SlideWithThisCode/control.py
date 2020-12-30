from cv2 import cv2                     #jangan lupa install dulu librarynya :)
import numpy as np
import pyautogui     

cam = cv2.VideoCapture(0)               # 0 jika menggunakan webcam bawaan, 1 jika memakai webcam eskternal
lower = np.array([22, 93, 0])           #tracking object warna kuning
upper = np.array([45, 255, 255])
prev_y = 0

while True : 
    ret, frame = cam.read()
    cv2.imshow('frame', frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  
    mask = cv2.inRange(hsv, lower, upper)
    contours, h = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in contours:                     
            area = cv2.contourArea(c)
            print (area)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) #bikin frame
            if area > 2000:                         #atur sendiri aja kalo kurang sensitif :)
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                if y < prev_y:
                    pyautogui.press('space')
                prev_y = y      
                
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == ord('q') :
        break

cam.release()
cv2.destroyAllWindows()
