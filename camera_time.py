# https://picamera.readthedocs.io/en/release-1.10/api_camera.html
# https://picamera.readthedocs.io/en/release-1.10/api_array.html

from picamera import PiCamera
import picamera.array
import time
import cv2

t1 = time.time()
camera = PiCamera()
camera.framerate = 30
stream = picamera.array.PiRGBArray(camera)  # Create the in-memory stream

t2 = time.time()
camera.capture('testing1.png')              # Take & save large image

t3 = time.time()
camera.resolution = (320, 208)
camera.capture('testing2.png')              # Take & save smaller image

t4 = time.time()
camera.capture(stream, format='bgr')        # Save a picture directly to memeory
image = stream.array
stream.truncate(0)                          # required to retake another pic

t5 = time.time()
cv2.imwrite('testing3.png', image)          # Save the image from memory
t6 = time.time()

print ("time to setup object PiCamera: %1.3f" % (t2-t1))
print ("time to take and save first picture: %1.3f" % (t3-t2))
print ("time to take and save smaller picture: %1.3f" % (t4-t3))
print ("time to take streamed image: %1.3f" % (t5-t4))
print ("time to save streamed image: %1.3f" % (t6-t5))
