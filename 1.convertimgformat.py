import os

import cv2

down_path = "downloads"
img_path = "images"
if not os.path.exists(img_path):
  os.makedirs(img_path)
for file in os.listdir(down_path):
  file_name = os.path.join(down_path, file)
  img = cv2.imread(file_name)
  
  dst_file = os.path.join(img_path,os.path.basename(file_name)+".bmp")
  cv2.imwrite(dst_file, img)