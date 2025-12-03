import cv2
import numpy as np
import os


def make_xmt():
    dataset_path =  'D:\CODEEEEE\cham_cong\data_img'
    labels = []
    faces = []
    
    for root, dirs, files in os.walk(dataset_path):
    
      for dir in dirs: 
            print(dir)
            name = dir
            num_labels = 0
            url = os.path.join(root, dir)
            face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  # Sử dụng một bộ phân loại gương mặt có sẵn

            for ssa, dirs2, files2 in os.walk(url):
                for file in files2:
                    if file.endswith(".jpg") or file.endswith(".png"):
            # Tạo đường dẫn đầy đủ của tệp tin ảnh
                        image_path = os.path.join(ssa, file)
            # Đọc tệp tin ảnh
                        image = cv2.imread(image_path)
                # Chuyển đổi ảnh sang ảnh xám
                        
                          # Nhãn tương ứng với từng ảnh (0: không có gương mặt, 1: có gương mặt)

# Huấn luyện mô hình phân loại gương mặt
                       

                        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                        faced = face_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
                        for (x, y, w, h) in faced:
                            roi_gray = gray[y:y+h,x:x+w]
                            
            # Thêm ảnh xám vào danh sách faces
                        faces.append(roi_gray)
            # Thêm nhãn tương ứng vào danh sách labels
                        labels.append(num_labels)
                num_labels += 1


            face_recognizer = cv2.face.LBPHFaceRecognizer_create()
            
            face_recognizer.train(faces, np.array(labels))
            
            folder_p = 'D:\CODEEEEE\cham_cong\data_xml' 
# Tên tệp tin
            file_name = 'face_'+ name +'.xml'
# Tạo đường dẫn đầy đủ
            file_p = os.path.join(folder_p, file_name)
# Lưu bộ nhận dạng vào đường dẫn đầy đủ
            face_recognizer.save(file_p)



print("as")
a =  make_xmt()