import os
import cv2

class data_detect:
    def __init__(self):
        self.xml = False
        self.arr = []
    def get_xml(self):
        if self.xml == False:
            arr2 = []
            for root, dirs, files in os.walk('D:\CODEEEEE\cham_cong\data_xml'):
                    for file in files: 
                       
                        #face_data = cv2.CascadeClassifier(xml_path)
                        xml_path = os.path.join(root, file)
                        a =str( xml_path) + "$"+ str(files)
                        arr2.append(a)
                        
            self.arr = arr2
            self.xml = True
        #print(len(self.arr))
        return self.arr
    def update_xml(self):
        self.xml = False