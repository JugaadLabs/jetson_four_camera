import multiprocessing
from multiprocessing import Process, Queue
import cv2

def safe_put(send_quene, put_object):
    if not send_quene.full():
        try:
            send_quene.put_nowait(put_object)
        except:
            print('quene full')

def gstreamer_pipeline(
        device_id=0,
        capture_width=4032,
        capture_height=3040,
        display_width=1280,
        display_height=480,
        framerate=10,
        flip_method=0,
    ):
    return (
        "nvarguscamerasrc sensor-id=%d wbmode=1 ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            device_id,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

class cameraProcess():
    def __init__(self, img_queue, sensor_id):
        self.cap = cv2.VideoCapture(gstreamer_pipeline(device_id=sensor_id), cv2.CAP_GSTREAMER)
        self.img_queue = img_queue
        ret = True
        if self.cap.isOpened():
            while ret:
                ret, img = self.cap.read()
                safe_put(self.img_queue, img)
        

   

