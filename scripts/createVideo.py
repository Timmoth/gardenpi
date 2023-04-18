import cv2
import os
import argparse
import time

def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

parser = argparse.ArgumentParser()
parser.add_argument("--dir", type=dir_path,
                    help="image dir")

args = parser.parse_args()
imageDir = args.dir

timestamp = time.time()
video_name = f'{timestamp}.mp4'

images = [img for img in os.listdir(imageDir) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(imageDir, images[0]))
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
    video.write(cv2.imread(os.path.join(imageDir, image)))

cv2.destroyAllWindows()
video.release()