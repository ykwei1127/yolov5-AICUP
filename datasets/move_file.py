import os
import random
import shutil

## 移動訓練和驗證資料到使用的資料路徑 ###
image_list = os.listdir("train_images")
for i in range(len(image_list)):
    source = "train_images/" + image_list[i]
    destination= "AICUP/images/train/" + image_list[i]
    shutil.move(source, destination)
image_list = os.listdir("val_images")
for i in range(len(image_list)):
    source = "val_images/" + image_list[i]
    destination= "AICUP/images/val/" + image_list[i]
    shutil.move(source, destination)

## 切訓練和驗證資料 ###
image_list = os.listdir("train_images")
print(image_list)
image_list = random.sample(image_list,len(image_list))
print(image_list)
for i in range(400):
    source = "train_images/" + image_list[i]
    destination= "val_images/" + image_list[i]
    print(source)
    print(destination)
    shutil.move(source, destination)