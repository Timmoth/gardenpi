import cv2
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--dir", action="store_true",
                    help="image dir")
args = parser.parse_args()
imageDir = args.imageDir

video_name = 'video.mp4'

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