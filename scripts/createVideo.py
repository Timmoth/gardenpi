import cv2
import os

image_folder = './'
video_name = 'video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 15, (width,height))
frameCount = images.count
print(f"frames: '{frameCount}'")

frameIndex = 0
for image in images.sort():
    print(f"stitching frame: '{image}' '{frameIndex}'")
    frameIndex += 1
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()