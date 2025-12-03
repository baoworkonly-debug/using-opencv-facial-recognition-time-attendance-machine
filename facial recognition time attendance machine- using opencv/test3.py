import cv2
import requests
import numpy as np


import urllib.request

# URL của hình ảnh

path_1 = 'frame_1.jpg'
image = cv2.imread(path_1)
cv2.imshow("face",image)

# Đọc ảnh từ mảng numpy
#image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
image_array = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Tải bộ phân loại đã huấn luyện từ tệp
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('face_0.xml')


label, confidence = recognizer.predict(image_array)

# In ra nhãn và độ tin cậy

key = cv2.waitKey(0)
print('Label:', label)
print('Confidence:', confidence)
print('Confidence:', round(confidence*100, 2))

cv2.destroyAllWindows()