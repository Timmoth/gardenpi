import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)  # video capture source camera (Here webcam of laptop)

ret, frame1 = cap.read()

oldFrame = frame1

while(True):
    ret, frame2 = cap.read()
  
    diff = cv2.absdiff(oldFrame, frame2)
    diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    diff_blur = cv2.GaussianBlur(diff_gray, (5,5), 0)
    _, thresh_bin = cv2.threshold(diff_blur, 20, 255, cv2.THRESH_BINARY)
    oldFrame = frame2

    number_of_white_pix = np.sum(thresh_bin == 255)
    print(number_of_white_pix)
    # Display the resulting frame
    if(number_of_white_pix > 2000):
      timestr = time.strftime("%Y%m%d-%H%M%S")
      cv2.imwrite(f"{timestr}.jpg", frame2)   
      time.sleep(0.5)
      print(f"Write: {timestr}")
