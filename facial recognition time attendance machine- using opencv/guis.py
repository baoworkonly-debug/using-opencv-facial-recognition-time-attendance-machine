import os
import cv2
import tkinter as tk
from PIL import ImageTk, Image
from create_img import create_
from xml import make_xmt
from open_xml import data_detect
from strea_frame import str_video
import shutil
from image_driver import img
import requests
import datetime




_get_name = ""
_name = False







def search_files_xml():
    
    #keyword = entry_search.get()
    file_list_xml.delete(0, tk.END)  # Xóa danh sách hiện tại trong Listbox
    
    # Tìm kiếm các file trong thư mục hiện tại và các thư mục con
    for root, dirs, files in os.walk("D:\CODEEEEE\cham_cong\data_xml"):
        for file in files:
            #if keyword in file:
                file_list_xml.insert(tk.END, file)
def search_files_img():
    
    #keyword = entry_search.get()
    file_list_img.delete(0, tk.END)  # Xóa danh sách hiện tại trong Listbox
    
    # Tìm kiếm các file trong thư mục hiện tại và các thư mục con
    for root, dirs, files in os.walk("D:\CODEEEEE\cham_cong\data_img"):
        for file in dirs:
            #if keyword in file:
                file_list_img.insert(tk.END, file)
def button_click():
    
    data = entry_input.get()
    if data != "" :
        print("ds ")
        label_input.config(text="Dữ liệu đã nhập: " + data)
        create_(str_video.get_frame(),data)
    search_files_img()
    
def bt_xml():
    make_xmt()
    search_files_xml()



def check_name_get(check,name):
    time_day = now.strftime("%d")
    output_dir = "D:\CODEEEEE\cham_cong\check_in\day_" + time_day 
    os.makedirs(output_dir, exist_ok=True)


    now = datetime.datetime.now()
    time_str = now.strftime(" %Hh:%Mp-%Y/%m/%d")

    image_path = os.path.join(output_dir, f"face_{time_str}.jpeg")
    frame = str_video.get_frame()
    cv2.imwrite(image_path, frame)
    img(image_path)

    
    a = time_str.split("-")
    
    meth_get(name,check,a[0],a[1])
    print("input ok")


def name_T():
        _name = True
def name_F():
        _name = False
def up_name(name):
    if _name == True:
            _get_name = name
            time_hour = now.strftime("%H")
            if(int(time_hour)> 6 and int(time_hour) < 14):
                chi = "In"
                print(chi)
                check_name_get(chi,_get_name )
            elif ( int(time_hour)> 12 and int(time_hour) < 22):
                cho = "Out"
                print(cho)
                check_name_get(cho, _get_name)



def bt_input():
    check = "In"
    check_name(check)
def bt_output():

    check = "Out"
    check_name(check)


def meth_get( check_in, time_in, day_in, mon_in):
    ur = 'https://script.google.com/macros/s/AKfycbxhkrvPTWbasv4ix9TaRZFbg0E2bPmqdUWr8gnsvUrwXOvWL7B9vAco62U4ReO0Y5Qw/exec?'
    
    
    url = ur + 'value1=' + str(check_in) + '&value2=' + str(time_in) +'&value3=' + str(day_in) +'&value4=' + str(mon_in)

    
    x = requests.get(url)
    print(url)
    print(x.status_code) 

def bt_delete():
    
    fd_fl = entry_de.get()
       
    result = fd_fl.split(",")
    path = result[0]
    file_foder = result[1]
    if path == "D":
        folder_path = 'D:\CODEEEEE\cham_cong\data_img\data_' + file_foder
        if os.path.exists(folder_path):
    # Xóa thư mục và toàn bộ nội dung bên trong nó
            shutil.rmtree(folder_path)
            label_de.config(text="đã xóa folder: " + file_foder)
            
        else:
            label_de.config(text="không tìm thấy folder: " + file_foder)

    if path == "F":
        file_path = 'D:\CODEEEEE\cham_cong\data_xml\face_' + file_foder


        if os.path.exists(file_path):
    
            os.remove(file_path)

            label_de.config(text="đã xóa file: " + file_foder)
        else:
            label_de.config(text="không tìm thấy file: " + file_foder)


def vd_frame():

        cascade_path = 'haarcascade_frontalface_default.xml'

        face_cascade = cv2.CascadeClassifier(cascade_path)
        return  face_cascade

name_arr = []

def note_time_day():
    now = datetime.datetime.now()
    time_day = now.strftime("%d")
    file_path = 'file_timekeeing.txt'
    with open(file_path, 'w') as file:
        file.write(time_day)
    file.close()
def read_time_day():

    with open(file_path, 'r') as file:
        lines = file.readlines()
    last_line = lines[-1]
    return last_line

face_cascade = vd_frame()
                

str_video = str_video()
str_video.start()


data_detect_ = data_detect()



window = tk.Tk()
label1 = tk.Label(window)
label1.pack()



def update_frame():
    now_ = datetime.datetime.now()
    time_day_now = now_.strftime("%d")
    
    if int(time_day_now) != name_arr[0]:
        name_arr = []
        name_arr[0] = int(time_day_now)
    #_,frame = video_capture.read()
    str_video._update_frame()
    frame = str_video.get_frame()
    
    #cv2.imshow("frame",frame)           
    
    
    if frame is not None:
        # Chuyển đổi khung hình từ BGR sang RGB

        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
        faced = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faced:
                cv2.rectangle(frame, pt1 = (x,y),pt2 = (x+w, y+h), color = (255,0,0),thickness =  3)
                roi_gray = gray[y:y+h,x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                face = []
                face = data_detect_.get_xml()
                for faces in face:

                    fac = faces.split('$')
           
                    recognizer = cv2.face.LBPHFaceRecognizer_create()
                    recognizer.read(fac[0])
                    print("faces")
                    print(fac[1])
                    # Viết chữ lên frame
                    
                    label, confidence = recognizer.predict(roi_gray)
                    font = cv2.FONT_HERSHEY_SIMPLEX  # Kiểu font
                    font_scale = 1.0  # Tỷ lệ font
                    color = (0, 255, 0)  # Màu chữ (xanh lá cây)
                    thickness = 2  # Độ dày chữ

                    
                    if round(confidence) < 43:
                         # Viết chữ lên frame                       
                        cv2.putText(frame, fac[1], (x, y), font, font_scale, color, thickness)
                        name_frame = fac[1]
                        name_face = name_frame.split(".")

                        name_T()  

                        for Name_ is name_arr:
                            if name_ == name_face[0]:
                                name_F()
                                break
                         
                        
                        
                        up_name(name_face[0])
                        name_F()
                        name_arr.append(name_face[0])
                           

                    else:
                        txt = '.....!'
                        cv2.putText(frame, txt, (x, y), font, font_scale, color, thickness)

# In ra nhãn và độ tin cậy

                    
                    print('Confidence:', confidence)
                    print('Confidence:', round(confidence*100, 2))


        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Chuyển đổi khung hình thành đối tượng PIL Image
        pil_image = Image.fromarray(rgb_frame)
        # Chuyển đổi PIL Image thành đối tượng ImageTk
        image = ImageTk.PhotoImage(pil_image)
        # Cập nhật hình ảnh trong nhãn Tkinter
        label1.place(x = 0, y= 0)
        label1.configure(image=image)
        label1.configure(width=800, height=600)
        label1.image = image
        
        
    
      
    
    # Lặp lại việc cập nhật khung hình
    window.after(1, update_frame)

# Bắt đầu cập nhật khung hình đầu tiên

label_input = tk.Label(window, text="Nhập tên file:...")
label_input.place(x = 810, y= 100)

entry_input = tk.Entry(window)
entry_input.place(x = 810, y= 120)
update_frame()

button1 = tk.Button(window, text="creat img:", command=button_click)
button1.place(x = 810, y= 140)
button2 = tk.Button(window, text="make xml :", command=bt_xml)
button2.place(x = 900, y= 140)


button_search_img = tk.Button(window, text="hiện danh sách img:", command=search_files_img)
button_search_img.place(x= 950, y = 170)
file_list_img = tk.Listbox(window)
file_list_img.place(x= 950, y = 190)

button_search_xml = tk.Button(window, text="hiện danh sách xml:", command=search_files_xml)
button_search_xml.place(x= 810, y = 170)
file_list_xml = tk.Listbox(window)
file_list_xml.place(x= 810, y = 190)

button_de = tk.Button(window, text="delete fil&fod/ F:D,name file :", command=bt_delete)
button_de.place(x = 810, y= 480)
label_de = tk.Label(window, text="Nhập tên file:")
label_de.place(x = 810, y= 440)
entry_de = tk.Entry(window)
entry_de.place(x = 810, y= 460)

button_input = tk.Button(window, text="input  :", command=bt_input)
button_input.place(x = 300, y= 570)
label_input = tk.Label(window, text=".....:")
label_input.place(x = 300, y= 550)

button_output = tk.Button(window, text="out put :", command=bt_output)
button_output.place(x = 360, y= 570)
label_output = tk.Label(window, text=".....:")
label_output.place(x = 360, y= 550)

window.mainloop()

cv2.destroyAllWindows()


