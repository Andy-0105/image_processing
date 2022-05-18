# image_processing-pyqt
使用Python圖形介面擴充套件庫之一的PyQt建立影像處理的圖形介面
# installation
```
pip install opencv-python
```
```
pip install pyqt
```
```
pip install numpy
```
```
pip install matplotlib
```
# Usage
```
python start.py
```
選取左上檔案->寫入圖片後

可經由選單中影像處理選項選擇需要項目

# function list
1.檔案
  + 寫入影像   
  + 儲存影像
 
2.設定
  + 設定ROI
  + 顯示直方圖
  + 色彩空間
  
3.影像處理
  + 影像二值化
  (可使用二值化閥值滑條調整)
  + 直方圖等化
  + 低通濾波
  + 高通濾波
  + 去除雜訊
  + 位移
  (可使用水平,垂直滑條調整)
  + 旋轉
  (可使用旋轉角度閥值滑條調整)
  + 仿射轉換
  (可使用水平,垂直,偏移倍率閥值滑條調整)
  + 透視投影轉換
  (可點選圖片四點顯示)
  + 角點檢測
  + 輪廓檢測
  + 侵蝕
  + 膨脹
