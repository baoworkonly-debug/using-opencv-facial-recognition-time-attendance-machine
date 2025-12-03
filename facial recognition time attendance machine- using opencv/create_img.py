import cv2 as cv
import os

dataset_path =  'D:\CODEEEEE\cham_cong\data_img'


def pes(x):
    pass
def create_(name, img):
    file_count =0
   
    for root, dirs, files in os.walk(dataset_path):
        file_count += len(files)
    
    cv.namedWindow('img')
    print(file_count)
    
    
    folder_path = 'D:\CODEEEEE\cham_cong\data_img\data_' + img

# Sử dụng os.mkdir() để tạo một thư mục mới
    try:
        os.mkdir(folder_path)
        print("Thư mục mới đã được tạo thành công.")
    except FileExistsError:
        print("Thư mục đã tồn tại.")

    cv.imshow('img',  name)
    file_count +=1
    
    output_path = os.path.join(folder_path , f"frame_{file_count}.jpg")
    cv.imwrite(output_path,  name)
   

  

