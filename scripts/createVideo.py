import cv2
import os
from datetime import date, timedelta
import argparse

def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

parser = argparse.ArgumentParser()
parser.add_argument("--dir", type=dir_path,
                    help="image dir")

args = parser.parse_args()
if args.dir is not None:
    dir = args.dir
else:
    yesterday = date.today() - timedelta(days=1)
    dir = os.path.join(os.path.expanduser('~'), yesterday.strftime("%Y-%m-%d"))

if(not os.path.exists(dir)):
    print(f"dir '{dir}' does not exist.")
    quit()

video_name = os.path.join(dir, 'video.mp4')
print(f"creating video '{video_name}'.")

images = [img for img in os.listdir(dir) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(dir, images[0]))
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'X264')
video = cv2.VideoWriter(video_name, fourcc, 15, (width,height))
frameCount = images.count
print(f"frames: '{frameCount}'")

frameIndex = 0
sortedFrames = sorted(images)
for image in sortedFrames:
    imagePath = os.path.join(dir, image)
    print(f"stitching frame: '{imagePath}' '{frameIndex}'")
    frameIndex += 1
    video.write(cv2.imread(imagePath))

cv2.destroyAllWindows()
video.release()