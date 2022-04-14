from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QImage, QPixmap
import cv2
from PyQt5.QtWidgets import QFileDialog
from UI123 import Ui_MainWindow
import numpy as np
import os
import matplotlib.pyplot as plt
#pyuic5 -x ui2.ui -o UI123.py
class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.file_path = ''
        self.ui.read_img.triggered.connect(self.open_file)
        self.ui.save_img.triggered.connect(self.save_file)
        self.ui.ROI.triggered.connect(self.select_roi)
        self.ui.Histogram.triggered.connect(self.histogram)
        self.ui.Color_space.triggered.connect(self.color_space)
        self.ui.Thresholding.triggered.connect(self.threshold)
        self.ui.Histogram_equalization.triggered.connect(self.histogram_equalization)
        self.ui.horizontalSlider.valueChanged.connect(self.getslidervalue)
        self.ui.Canny.triggered.connect(self.canny)
        self.ui.GaussianBlur_3.triggered.connect(self.GaussianBlur)
        self.ui.medianblur.triggered.connect(self.medianblur)
        self.ui.horizontal_displacement.valueChanged.connect(self.horizontal_displacement)
        self.ui.Vertical_displacement.valueChanged.connect(self.Vertical_displacement)
        self.ui.displacement.triggered.connect(self.displacement)
        self.ui.rotate_horizontalSlider.valueChanged.connect(self.rotate_slider)
        self.ui.rotate.triggered.connect(self.rotate)
        self.ui.scale_horizontalSlider.valueChanged.connect(self.Affine_Transformation_slider)
        self.ui.affine_transform.triggered.connect(self.Affine_Transformation)
        self.ui.perspective_transform.triggered.connect(self.Perspective_transform)
    def Perspective_transform(self):
        self.ui.image_label.mousePressEvent=self.mouse_event
        self.ui.image_label.mouseReleaseEvent=self.mouse_ReleaseEvent
        self.setPerapective=True
        self.point=[]
    def mouse_event(self,event):
        self.x,self.y=event.x(),event.y()
        if self.setPerapective:
            if len(self.point) < 4:
                self.point.append([event.x(),event.y()])
    def mouse_ReleaseEvent(self,event):
        if len(self.point)==4:
            w,h=self.img.shape[:2]
            p1=np.float32(self.point)
            p2=np.float32([[0,0],[w,0],[0,h],[w,h]])
            n=cv2.getPerspectiveTransform(p1,p2)
            img=cv2.warpPerspective(self.img,n,(w,h),cv2.INTER_LINEAR)
            cv2.imshow('Perspective_transform',img)
            self.point=[]
            self.setPerapective=False
    def Affine_Transformation_slider(self):
        self.ui.scale_label.setText(f"{self.ui.scale_horizontalSlider.value()/10}")
    def Affine_Transformation(self):
        h,w=self.img.shape[:2]
        x=self.ui.horizontal_displacement.value()
        y=self.ui.Vertical_displacement.value()
        scale=self.ui.scale_horizontalSlider.value()/10
        if x and y !=0:
            n=np.float32([[1,scale,x],[scale,1,y]])
            img=cv2.warpAffine(self.img,n,(w,h))
            cv2.imshow('Affine_Transformation',img)
    def rotate(self):
        (h, w, d) = self.img.shape
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, self.ui.rotate_horizontalSlider.value(), 1.0)
        rotate_img = cv2.warpAffine(self.img, M, (w, h))
        cv2.imshow('rotate',rotate_img)
    def rotate_slider(self):
        self.ui.rotate_label.setText(f"{self.ui.rotate_horizontalSlider.value()}")
    def displacement(self):
        img = self.img
        h, w = img.shape[:2]
        mat_shift = np.float32([[1, 0, self.ui.horizontal_displacement.value()], [0, 1, self.ui.Vertical_displacement.value()]])
        dst = cv2.warpAffine(img, mat_shift, (w, h))
        cv2.imshow('displacement', dst)
    def horizontal_displacement(self):
        self.ui.horizontal_label.setText(f"{self.ui.horizontal_displacement.value()}")
    def Vertical_displacement(self):
        self.ui.Vertical_label.setText(f"{self.ui.Vertical_displacement.value()}")
    def canny(self):
        blur = cv2.GaussianBlur(self.img, (11,11), 0)
        canny = cv2.Canny(blur, 30, 150)
        cv2.imshow("blur", canny)
    def GaussianBlur(self):
        blur = cv2.GaussianBlur(self.img, (5, 5), 0)
        cv2.imshow("blur", blur)
    def medianblur(self):
        dst = cv2.medianBlur(self.img, 5)
        cv2.imshow("median_blur", dst)
    def getslidervalue(self):
        self.ui.label.setText(f"二質化閥值:{self.ui.horizontalSlider.value()}")
    def color_space(self):
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)  # RGB轉換為GRAY 這裡的GRAY是單通道的
        cv2.imshow("gray", gray)
        hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)  # 轉到HSV顏色空間
        cv2.imshow('hsv.', hsv)
        Ycrcb = cv2.cvtColor(self.img, cv2.COLOR_RGB2YCrCb)
        cv2.imshow("Ycrcb", Ycrcb)
        cv2.waitKey(0)
    def histogram_equalization(self):
        gray_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        equalize_img = cv2.equalizeHist(gray_img)
        cv2.imshow("equal_image", equalize_img)
        cv2.waitKey(0)
    def threshold(self):
        ret, th1 = cv2.threshold(self.img, self.ui.horizontalSlider.value(), 255, cv2.THRESH_BINARY)
        images = th1
        cv2.imshow('BINARY',images)
        cv2.waitKey(0)
    def histogram(self):
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            histr = cv2.calcHist([self.img], [i], None, [255], [0, 255])
            plt.plot(histr, color=col)
            plt.xlim([0, 255])
        plt.show()
    def select_roi(self):
        r=cv2.selectROI('roi',self.img,False,False)
        img_roi=self.img[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]
        cv2.imshow("hhh",img_roi)
    def open_file(self):
        filename, filetype = QFileDialog.getOpenFileName(self,"Open file","./")
        self.img = cv2.imdecode(np.fromfile(filename,dtype=np.uint8),-1)
        self.ui.img_inf.setText(f"影像尺寸:{self.img.shape}\n影像路徑:\n{filename}")
        height, width, channel = self.img.shape
        bytesPerline = 3 * width
        self.qimg = QImage(self.img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.ui.image_label.setPixmap(QPixmap.fromImage(self.qimg))
        self.ui.image_label.adjustSize()
    def save_file(self):
        filename ,filetype = QFileDialog.getSaveFileName(self,"Save file",'./')
        file=os.path.splitext(filename)[1]
        cv2.imencode(file,self.img)[1].tofile(filename)
