import cv2
import winsound
from playsound import playsound
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()

    mot_detec = cv2.absdiff(frame1,frame2)

    grayscale = cv2.cvtColor(mot_detec, cv2.COLOR_RGB2GRAY)

    blur = cv2.GaussianBlur(grayscale,(5,5),0)
    _, thresh = cv2.threshold(blur,20,255, cv2.THRESH_BINARY)
    dilated= cv2.dilate(thresh,None, iterations=3)
    boundary, _ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    # cv2.drawContours(frame1, boundary, -1, (0,255,0), 2)
    
    for i in boundary:
        if cv2.contourArea(i) < 3000:
            continue
        x,y,w,h = cv2.boundingRect(i)
        cv2.rectangle(frame1, (x,y),(x+w, y+h), (0,255,0), 2)
        winsound.Beep(800 , 400)

    if cv2.waitKey(10) == ord('z'):
        break
    cv2.imshow('Surveillance Camera', frame1)

