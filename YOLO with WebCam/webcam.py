from ultralytics import YOLO
import cv2
import cvzone

cap =cv2.VideoCapture(0,cv2.CAP_DSHOW ) # cv2.VideoCapture(0) takes alot of time to start the cam
cap.set(3, 1280)
cap.set(4, 720)

while True:
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)
