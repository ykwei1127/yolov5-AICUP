import os
from PIL import Image

### 驗證資料 ###
val_img_list = os.listdir("AICUP/images/val")
for img in val_img_list:
    img_path = "AICUP/images/val/" + img
    image = Image.open(img_path)
    W = image.width
    H = image.height

    gt_path = "train_gts/" + img + ".txt"
    with open(gt_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    txt_path = "AICUP/labels/val/" + img[:-4] + ".txt"
    with open(txt_path,'a',encoding="utf-8") as f:
        for line in lines:
            result = list()
            line = line.split(',')
            line = line[:-2]
            x1 = min([int(line[0]), int(line[6])])
            x2 = max([int(line[2]), int(line[4])])
            x = round((x2+x1)/2)
            w = x2-x1
            y1 = min([int(line[1]), int(line[3])])
            y2 = max([int(line[5]), int(line[7])])
            y = round((y2+y1)/2)
            h = y2-y1
            f.write('0 '+str(x/W)+' '+str(y/H)+' '+str(w/W)+' '+str(h/H)+'\n')

## 訓練資料 ###
train_img_list = os.listdir("AICUP/images/train")
for img in train_img_list:
    img_path = "AICUP/images/train/" + img
    image = Image.open(img_path)
    W = image.width
    H = image.height

    gt_path = "train_gts/" + img + ".txt"
    with open(gt_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    txt_path = "AICUP/labels/train/" + img[:-4] + ".txt"
    with open(txt_path,'a',encoding="utf-8") as f:
        for line in lines:
            result = list()
            line = line.split(',')
            line = line[:-2]
            x1 = min([int(line[0]), int(line[6])])
            x2 = max([int(line[2]), int(line[4])])
            x = round((x2+x1)/2)
            w = x2-x1
            y1 = min([int(line[1]), int(line[3])])
            y2 = max([int(line[5]), int(line[7])])
            y = round((y2+y1)/2)
            h = y2-y1
            f.write('0 '+str(x/W)+' '+str(y/H)+' '+str(w/W)+' '+str(h/H)+'\n') 


### 1張圖片測試 ###
# img = "img_1.jpg"
# img_path = "AICUP/images/train/" + img
# image = Image.open(img_path)
# W = image.width
# H = image.height
# print(W)
# print(H)

# gt_path = "train_gts/" + img + ".txt"
# with open(gt_path, "r", encoding="utf-8") as f:
#     lines = f.readlines()
    
# with open("test.txt",'a',encoding="utf-8") as f:
#     for line in lines:
#         result = list()
#         line = line.split(',')
#         line = line[:-2]
#         print(line)
#         x1 = min([int(line[0]), int(line[6])])
#         x2 = max([int(line[2]), int(line[4])])
#         x = round((x2+x1)/2)
#         w = x2-x1
#         y1 = min([int(line[1]), int(line[3])])
#         y2 = max([int(line[5]), int(line[7])])
#         y = round((y2+y1)/2)
#         h = y2-y1
#         print(x,y)
#         print(w,h)
#         result.append('0')
#         result.append(str(x/W))
#         result.append(str(y/H))
#         result.append(str(w/W))
#         result.append(str(h/H))
#         print(result)
#         print("\n")

#         f.write('0 '+str(x/W)+' '+str(y/H)+' '+str(w/W)+' '+str(h/H)+'\n')  