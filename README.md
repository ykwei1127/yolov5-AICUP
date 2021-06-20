# yolov5-AICUP

## 環境設置
1. 安裝pytorch
2. 安裝需要的套件
```
pip install -U -r requirements.txt
```

## 資料前處理
3. 將下載的訓練資料放到datasets資料夾，使用json.py將比賽的給的json檔取出我們要的部分，並轉換成ground truth label的txt檔
4. 執行datasets資料夾下的move_file.py，把資料分成訓練集和驗證集
```
python json.py
cd datasets
python move_file.py
```
5. 執行datasets資料夾下的convert_large.py將比賽方提供的label轉成yolov5讀取的格式
```
python convert_large.py
```
## 訓練模型
6. 訓練yolov5x模型
```
cd ..
python train.py --img-size 640 --batch-size 8 --epoch 500 --data ./data/AICUP.yaml --cfg ./models/yolov5x.yaml --weight weights/yolov5x.pt --device 1

```
如果在linux terminal，可改執行train.sh
```
source train.sh
```
## 測試結果
7. 訓練好之後會產生run資料夾，底下會有train/exp/資料夾放訓練好的模型
8. 利用訓練好的模型判斷圖片文字框，--source後面接的參數為測試圖片的目錄，--weight後面參數則為訓練好的模型位置runs/train/exp/weight/best.pt
```
python detect.py --source ../PrivateTestDataset/img --weights runs/train/exp/weights/best.pt --conf 0.5 --save-txt --save-conf
```
如果在linux terminal，可改執行test.sh
```
source test.sh
```
9. 偵測完的結果會放在run/detect/資料夾底下，利用transform.py將抓出來的結果轉換成繳交用的csv檔格式，
```
python transform.py
```
## reference from official yolov5 github
```
https://github.com/ultralytics/yolov5
```
