import time
import numpy as np
import cv2
import multiprocessing
from multiprocessing import Process, Queue

from src.cameraProcess import cameraProcess

def safe_get(queue):
    if not queue.empty():
        return queue.get_nowait()
    else:
        pass

if __name__=='__main__':
    try:
        multiprocessing.set_start_method('spawn')
    except RuntimeError:
        pass
    img_queue0 = Queue(maxsize=1)
    img_queue1 = Queue(maxsize=1)
    camera_process0 = Process(target=cameraProcess, args=(img_queue0, 0))
    camera_process1 = Process(target=cameraProcess, args=(img_queue1, 1))
    camera_process0.start()
    camera_process1.start()

    while 1:
        if not img_queue0.empty():
            img = img_queue0.get_nowait()
            img0 = img[:, 0:640, :]
            img1 = img[:, 640:, :]
            cv2.imshow("CSI Camera0", img0)
            cv2.imshow("CSI Camera1", img1)
        if not img_queue1.empty():
            img = img_queue1.get_nowait()
            img2 = img[:, 0:640, :]
            img3 = img[:, 640:, :]
            cv2.imshow("CSI Camera2", img2)
            cv2.imshow("CSI Camera3", img3)

        # This also acts as
        keyCode = cv2.waitKey(1) & 0xFF
        # Stop the program on the ESC key
        if keyCode == 27:
            break