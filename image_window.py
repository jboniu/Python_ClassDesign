import os

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QMainWindow

from image_mark import Ui_MainWindow
from PIL import Image, ImageDraw, ImageFont


class ImageWindow(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(ImageWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setupUi(self)  # 初始化

    # 判断图片
    def isImg(self, file):

        file = file.lower()
        if os.path.splitext(file)[-1] == '.jpg' or os.path.splitext(file)[-1] == '.png' or os.path.splitext(file)[
            -1] == '.jpeg' or os.path.splitext(file)[-1] == '.webp':
            return True
        else:
            return False

    # 获取所有文件
    def getFiles(self):

        self.img_path = QFileDialog.getExistingDirectory(None, "选择图片文件夹路径", "D:/")
        self.list = os.listdir(self.img_path)
        num = 0
        self.listWidget.clear()
        for i in range(0, len(self.list)):
            filepath = os.path.join(self.img_path, self.list[i])
            if os.path.isfile(filepath):
                if self.isImg(filepath) == True:
                    num = num + 1  # 数量加1
                    self.item = QtWidgets.QListWidgetItem(self.listWidget)
                    self.item.setText(self.list[i])
        self.statusBar.showMessage('共有图片 ' + str(num) + ' 张')

    # 选择保存路径
    def msg(self):
        self.dir_path = QFileDialog.getExistingDirectory(None, "选择路径", "D:/")
        self.lineEdit_3.setText(self.dir_path)

    # 文字水印
    def textMark(self, img, newImgPath):
        newImg=Image.open(img).copy()
        font = ImageFont.truetype(r"C:\Windows\Boot\Fonts\msjh_boot.ttf", size=40)
        imagedraw = ImageDraw.Draw(newImg)  # 创建绘制对象
        position = (0, 0)
        imagedraw.text(position, self.lineEdit.text(), fill="red", font=font)
        newImg.save(newImgPath)

    # 添加水印
    def addMark(self):
        if self.lineEdit_3.text() == '':  # 判断是否选择了保存路径
            QMessageBox.warning(None, '警告', '请选择保存路径', QMessageBox.Ok)
            return
        else:
            try:
                num = 0  # 记录处理图片数量
                for i in range(0, self.listWidget.count()):  # 遍历图片列表
                    # 设置原始图片路径（包括文件名）
                    filepath = os.path.join(self.img_path, self.listWidget.item(i).text())
                    # 设置水印图片保存路径（包括文件名）
                    newfilepath = os.path.join(self.lineEdit_3.text(), self.listWidget.item(i).text())
                    if self.lineEdit.text() == '':  # 判断是否输入了水印文字
                        QMessageBox.warning(None, '警告', '请输入水印文字', QMessageBox.Ok)
                        return
                    else:
                        self.textMark(filepath, newfilepath)
                        num += 1  # 处理图片数量加1

                statusBar_info = '任务完成，此次共处理 ' + str(num) + ' 张图片'
                self.statusBar.showMessage(statusBar_info)  # 显示处理图片总数
                QMessageBox.warning(None, '完成', statusBar_info, QMessageBox.Ok)
            except Exception:
                QMessageBox.warning(None, '错误', '图片格式有误，请重新选择……', QMessageBox.Ok)
