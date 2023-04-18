import cv2
import os

image_folder = './'

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") and "." in img]
for image in images:
    os.remove(image)