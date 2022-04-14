from time import sleep
from picamera import PiCamera
from io import BytesIO
from Focuser import Focuser

# Create an in-memory stream
# my_stream = BytesIO()
# camera = PiCamera()
# camera.start_preview()
# camera.rotation = 90
# # Camera warm-up time
# sleep(5)
# camera.capture(my_stream, 'jpg')
x =200
print((int(1.33 * x), x))

width = 320
#frame_height = int(cap.get(4))
height= 240

print((2 * height, 2 * width, 3))