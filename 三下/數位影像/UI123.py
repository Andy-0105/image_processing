# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 791)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(190, 80, 720, 480))
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 80, 160, 22))
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 120, 111, 20))
        self.label.setText("")
        self.label.setObjectName("label")
        self.img_inf = QtWidgets.QLabel(self.centralwidget)
        self.img_inf.setGeometry(QtCore.QRect(190, 20, 341, 51))
        self.img_inf.setText("")
        self.img_inf.setObjectName("img_inf")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 170, 61, 16))
        self.label_3.setObjectName("label_3")
        self.horizontal_displacement = QtWidgets.QSlider(self.centralwidget)
        self.horizontal_displacement.setGeometry(QtCore.QRect(10, 200, 160, 22))
        self.horizontal_displacement.setMinimum(-800)
        self.horizontal_displacement.setMaximum(800)
        self.horizontal_displacement.setOrientation(QtCore.Qt.Horizontal)
        self.horizontal_displacement.setObjectName("horizontal_displacement")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 280, 61, 16))
        self.label_4.setObjectName("label_4")
        self.Vertical_displacement = QtWidgets.QSlider(self.centralwidget)
        self.Vertical_displacement.setGeometry(QtCore.QRect(10, 310, 160, 22))
        self.Vertical_displacement.setMinimum(-800)
        self.Vertical_displacement.setMaximum(800)
        self.Vertical_displacement.setOrientation(QtCore.Qt.Horizontal)
        self.Vertical_displacement.setObjectName("Vertical_displacement")
        self.horizontal_label = QtWidgets.QLabel(self.centralwidget)
        self.horizontal_label.setGeometry(QtCore.QRect(50, 230, 61, 21))
        self.horizontal_label.setText("")
        self.horizontal_label.setObjectName("horizontal_label")
        self.Vertical_label = QtWidgets.QLabel(self.centralwidget)
        self.Vertical_label.setGeometry(QtCore.QRect(50, 350, 61, 21))
        self.Vertical_label.setText("")
        self.Vertical_label.setObjectName("Vertical_label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 400, 71, 21))
        self.label_5.setObjectName("label_5")
        self.rotate_horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.rotate_horizontalSlider.setGeometry(QtCore.QRect(10, 440, 160, 22))
        self.rotate_horizontalSlider.setMinimum(-360)
        self.rotate_horizontalSlider.setMaximum(360)
        self.rotate_horizontalSlider.setSliderPosition(0)
        self.rotate_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rotate_horizontalSlider.setObjectName("rotate_horizontalSlider")
        self.rotate_label = QtWidgets.QLabel(self.centralwidget)
        self.rotate_label.setGeometry(QtCore.QRect(50, 470, 51, 16))
        self.rotate_label.setText("")
        self.rotate_label.setObjectName("rotate_label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 500, 81, 31))
        self.label_6.setObjectName("label_6")
        self.scale_horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.scale_horizontalSlider.setGeometry(QtCore.QRect(10, 540, 160, 22))
        self.scale_horizontalSlider.setMaximum(20)
        self.scale_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.scale_horizontalSlider.setObjectName("scale_horizontalSlider")
        self.scale_label = QtWidgets.QLabel(self.centralwidget)
        self.scale_label.setGeometry(QtCore.QRect(50, 580, 47, 12))
        self.scale_label.setText("")
        self.scale_label.setObjectName("scale_label")
        self.cornerharris_label = QtWidgets.QLabel(self.centralwidget)
        self.cornerharris_label.setGeometry(QtCore.QRect(50, 620, 71, 16))
        self.cornerharris_label.setObjectName("cornerharris_label")
        self.cornerharris_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.cornerharris_lineEdit.setGeometry(QtCore.QRect(20, 660, 113, 22))
        self.cornerharris_lineEdit.setObjectName("cornerharris_lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 25))
        self.menubar.setObjectName("menubar")
        self.file = QtWidgets.QMenu(self.menubar)
        self.file.setObjectName("file")
        self.setting = QtWidgets.QMenu(self.menubar)
        self.setting.setObjectName("setting")
        self.image_Preprocessing = QtWidgets.QMenu(self.menubar)
        self.image_Preprocessing.setObjectName("image_Preprocessing")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.read_img = QtWidgets.QAction(MainWindow)
        self.read_img.setObjectName("read_img")
        self.ROI = QtWidgets.QAction(MainWindow)
        self.ROI.setObjectName("ROI")
        self.Histogram = QtWidgets.QAction(MainWindow)
        self.Histogram.setObjectName("Histogram")
        self.Color_space = QtWidgets.QAction(MainWindow)
        self.Color_space.setObjectName("Color_space")
        self.Thresholding = QtWidgets.QAction(MainWindow)
        self.Thresholding.setObjectName("Thresholding")
        self.Histogram_equalization = QtWidgets.QAction(MainWindow)
        self.Histogram_equalization.setObjectName("Histogram_equalization")
        self.save_img = QtWidgets.QAction(MainWindow)
        self.save_img.setObjectName("save_img")
        self.actiondada = QtWidgets.QAction(MainWindow)
        self.actiondada.setObjectName("actiondada")
        self.GaussianBlur_2 = QtWidgets.QAction(MainWindow)
        self.GaussianBlur_2.setObjectName("GaussianBlur_2")
        self.GaussianBlur_3 = QtWidgets.QAction(MainWindow)
        self.GaussianBlur_3.setObjectName("GaussianBlur_3")
        self.Canny = QtWidgets.QAction(MainWindow)
        self.Canny.setObjectName("Canny")
        self.medianblur = QtWidgets.QAction(MainWindow)
        self.medianblur.setObjectName("medianblur")
        self.displacement = QtWidgets.QAction(MainWindow)
        self.displacement.setObjectName("displacement")
        self.rotate = QtWidgets.QAction(MainWindow)
        self.rotate.setObjectName("rotate")
        self.affine_transform = QtWidgets.QAction(MainWindow)
        self.affine_transform.setObjectName("affine_transform")
        self.perspective_transform = QtWidgets.QAction(MainWindow)
        self.perspective_transform.setObjectName("perspective_transform")
        self.cornerharris = QtWidgets.QAction(MainWindow)
        self.cornerharris.setObjectName("cornerharris")
        self.file.addAction(self.read_img)
        self.file.addAction(self.save_img)
        self.setting.addAction(self.ROI)
        self.setting.addAction(self.Histogram)
        self.setting.addAction(self.Color_space)
        self.image_Preprocessing.addAction(self.Thresholding)
        self.image_Preprocessing.addAction(self.Histogram_equalization)
        self.image_Preprocessing.addAction(self.GaussianBlur_3)
        self.image_Preprocessing.addAction(self.Canny)
        self.image_Preprocessing.addAction(self.medianblur)
        self.image_Preprocessing.addAction(self.displacement)
        self.image_Preprocessing.addAction(self.rotate)
        self.image_Preprocessing.addAction(self.affine_transform)
        self.image_Preprocessing.addAction(self.perspective_transform)
        self.image_Preprocessing.addAction(self.cornerharris)
        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.setting.menuAction())
        self.menubar.addAction(self.image_Preprocessing.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "二值化閥值"))
        self.label_3.setText(_translate("MainWindow", "水平位移量"))
        self.label_4.setText(_translate("MainWindow", "垂直位移量"))
        self.label_5.setText(_translate("MainWindow", "旋轉角度"))
        self.label_6.setText(_translate("MainWindow", "偏移倍率"))
        self.cornerharris_label.setText(_translate("MainWindow", "角點偵測"))
        self.file.setTitle(_translate("MainWindow", "檔案"))
        self.setting.setTitle(_translate("MainWindow", "設定"))
        self.image_Preprocessing.setTitle(_translate("MainWindow", "影像處理"))
        self.read_img.setText(_translate("MainWindow", "寫入影像"))
        self.ROI.setText(_translate("MainWindow", "設定ROI"))
        self.Histogram.setText(_translate("MainWindow", "顯示影像直方圖"))
        self.Color_space.setText(_translate("MainWindow", "顯示或改變色彩空間"))
        self.Thresholding.setText(_translate("MainWindow", "影像二值化"))
        self.Histogram_equalization.setText(_translate("MainWindow", "直方圖等化"))
        self.save_img.setText(_translate("MainWindow", "儲存圖片"))
        self.actiondada.setText(_translate("MainWindow", "dada"))
        self.GaussianBlur_2.setText(_translate("MainWindow", "453453"))
        self.GaussianBlur_3.setText(_translate("MainWindow", "低通濾波"))
        self.Canny.setText(_translate("MainWindow", "高通濾波"))
        self.medianblur.setText(_translate("MainWindow", "去除雜訊"))
        self.displacement.setText(_translate("MainWindow", "位移"))
        self.rotate.setText(_translate("MainWindow", "旋轉"))
        self.affine_transform.setText(_translate("MainWindow", "仿射轉換"))
        self.perspective_transform.setText(_translate("MainWindow", "透視投影轉換"))
        self.cornerharris.setText(_translate("MainWindow", " 角點檢測"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
