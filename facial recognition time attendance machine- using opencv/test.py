import cv2, os
import numpy as np
import datetime
from image_driver import img
import requests
import datetime

file_path = 'file_timekeeing.txt'
with open(file_path, 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a sample text.')
file.close()


with open(file_path, 'r') as file:
    lines = file.readlines()

# Get the last line
last_line = lines[-1]

# Print the last line
print(last_line)
