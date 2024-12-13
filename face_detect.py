#pip install opencv-python
import cv2
#CascadeClassifier is used to identify the body parts like eyes,mouth ...
face_cap=cv2.CascadeClassifier("C:/Users/likit/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
#to capture through camera
video_cap=cv2.VideoCapture(0)
while True:
    ret , video_data=video_cap.read()
    #to give color
    col=cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
    #to captre face components
    face=face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for(x,y,w,h) in face:
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)
        #to show the image ,let video_live be frame name
    cv2.imshow("video_live",video_data)
    if cv2.waitKey(10) == ord("a"):
        break
video_cap.release()