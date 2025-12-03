import os
import cv2


class str_video:
    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)
        

        #frame_width = int(self.video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        #frame_height = int(self.video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        if not self.video_capture.isOpened():
            print("Failed to open video.")
            exit()
        self.frame = None
        self.frame2 = None
        self.is_running = False
        
    def start(self):
        self.is_running = True
    def get_frame(self):
        return self.frame
    def get_frame_xml(self):
        return self.frame2
    def Stop(self):
        self.is_running = False
    def _update_frame(self):
            
            if self.is_running:
                ret, framer = self.video_capture.read()          
                self.frame = framer
   