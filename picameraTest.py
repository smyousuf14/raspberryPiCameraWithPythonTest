#import the neccessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

#Initialize the camera 
camera = PiCamera()
rawCapture = PiRGBArray(camera)

# allow the camera to warmup
time.sleep(0.1)

#grab an image from the camera
camera.capture(rawCapture, format = "bgr")
image = rawCapture.array

#display the image on screen and wait fora keypress
cv2.imshow("Image",image)
cv2.waitKey(0)

