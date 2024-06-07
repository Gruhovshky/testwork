import os
import random
import shutil
img_path = "images"
test_path ="test"
val_path = "val"
train_path = "train"

for path in[test_path,val_path,train_path]:
  #如果目录存在就删除
  if os.path.exists(path):
    shutil.rmtree(path)
  #创建目录,保证是空目录
  if not os.path.exists(path):
    os.makedirs(path)

for img_file in os.listdir(img_path):
  if not img_file.endswith(".bmp"):
    continue
  img_file_name = os.path.join(img_path,img_file)
  txt_file = img_file[:-4]+".txt"
  txt_file_name = os.path.join(img_path,txt_file)
  if not os.path.exists(txt_file_name):
    continue

  rnd = random.random()
  if rnd < 0.1:
    dst_img_file = os.path.join(test_path,img_file)
    dst_txt_file = os.path.join(test_path,txt_file)
  elif rnd < 0.3:
    dst_img_file = os.path.join(val_path,img_file)
    dst_txt_file = os.path.join(val_path,txt_file)
    #shutil.copy(img_file_name, dst_file)
  else:
    dst_img_file = os.path.join(train_path,img_file)
    dst_txt_file = os.path.join(train_path,txt_file)
    #shutil.copy(img_file_name, dst_file)
  print( " {}=> {}".format(img_file_name,dst_img_file))
  print( " {}=> {}".format(txt_file_name,dst_txt_file))
  shutil.copy(img_file_name, dst_img_file)
  shutil.copy(txt_file_name, dst_txt_file)
