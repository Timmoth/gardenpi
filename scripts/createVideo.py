import cv2
import os
import time
from datetime import date, timedelta

yesterday = date.today() - timedelta(days=1)
dir = os.path.join(os.path.expanduser('~'), yesterday.strftime("%Y-%m-%d"))

if(not os.path.exists(dir)):
    print(f"dir '{dir}' does not exist.")
    quit()

video_name = os.path.join(dir, 'video.mp4')

images = [img for img in os.listdir(dir) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(dir, images[0]))
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'h264')
video = cv2.VideoWriter(video_name, fourcc, 15, (width,height))
frameCount = images.count
print(f"frames: '{frameCount}'")

frameIndex = 0
sortedFrames = sorted(images)
for image in sortedFrames:
    print(f"stitching frame: '{image}' '{frameIndex}'")
    frameIndex += 1
    video.write(cv2.imread(os.path.join(dir, image)))

cv2.destroyAllWindows()
video.release()