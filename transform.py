import pandas as pd
import os

def extract_digit(s):
    numbers = ""
    for c in s:
        if c.isdigit():
            numbers+=c
    return numbers

base = "./runs/detect/exp10/labels/"
file_names = os.listdir(base)
# print(file_names)

final = pd.DataFrame()
for file_name in file_names:
    numbers = extract_digit(file_name)
    origin_txt_path = base + file_name
    print(origin_txt_path)
    with open(origin_txt_path, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            line = line.split('\n')
            line = line[0]
            r = line.split(' ')
            # print(r)
            answer = {
                "號碼": [numbers],
                "x1": [r[0]],
                "y1": [r[1]],
                "x2": [r[2]],
                "y2": [r[1]],
                "x3": [r[2]],
                "y3": [r[3]],
                "x4": [r[0]],
                "y4": [r[3]],
                "conf": [r[4]]
            }
            answer_df = pd.DataFrame(answer)
            final = final.append(answer_df, ignore_index=True)
final.to_csv("private_500e_yolov5x_trainexp10_largegt_c050_detectexp10.csv", index=False)