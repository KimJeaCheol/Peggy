import tkinter as tk 
import picamera 
from Focuser import Focuser

pic_number = 0 

camera = picamera.PiCamera()
focuser = Focuser(1)

def camera_start(): 
    camera.resolution=(640, 480) 
    camera.start_preview(fullscreen=False, window=(200, 200, 640, 480))

def camera_stop(): 
    camera.stop_preview() 
    
def close_window(): 
    root.destroy 
    camera.stop_preview() 
    camera.close() 
    quit() 

def camera_capture(): 
    global pic_number 
    pic_number += 1 
    camera.capture('/home/pi/Desktop/image_' + str(pic_number) + '.jpg') 

def camera_ir(): 
    focuser.set(Focuser.OPT_IRCUT,focuser.get(Focuser.OPT_IRCUT)^0x0001)

root = tk.Tk() 
root.title("Camera Test") 
root.geometry("250x250+1000+50") 

frame = tk.Frame(root) 
frame.pack(pady = 0, padx = 0) 

button1 = tk.Button(frame, text = "카메라 시작", width=20, padx = 20, pady = 10, command = camera_start) 
button1.grid(row = 0, column = 0, padx = 1, pady = 3) 

button2 = tk.Button(frame, text = "카메라 중지", width=20, padx = 20, pady = 10, command = camera_stop) 
button2.grid(row = 1, column = 0, padx = 1, pady = 3) 

button3 = tk.Button(frame, text = "카메라 캡쳐", width=20, padx = 20, pady = 10, command = camera_capture) 
button3.grid(row = 2, column = 0, padx = 1, pady = 3) 

button3 = tk.Button(frame, text = "카메라 IR", width=20, padx = 20, pady = 10, command = camera_ir) 
button3.grid(row = 3, column = 0, padx = 1, pady = 3) 

root.protocol("WM_DELETE_WINDOW", close_window) 
root.mainloop()