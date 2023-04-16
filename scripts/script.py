import cv2
import base64
import imutils
import requests

cap = cv2.VideoCapture(0)  # video capture source camera (Here webcam of laptop)
ret, frame = cap.read()  # return a single frame in variable `frame`

for x in range(50):
  (grabbed, frame) = cap.read()
  
(grabbed, frame) = cap.read()
frame = imutils.resize(frame, width=200)
retval, buffer = cv2.imencode('.png', frame)
jpg_as_text = base64.b64encode(buffer).decode("utf-8")
cap.release()

url = 'https://7kc2vxit8l.execute-api.eu-west-1.amazonaws.com/dev/image'
myobj = {'imageData': jpg_as_text}

x = requests.post(url, json = myobj)
print(x.status_code)