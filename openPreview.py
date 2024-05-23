import os

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QMainWindow

from preview import Ui_MainWindow


class PreviewWindow(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(PreviewWindow,self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)  # 只显示关闭按钮
        self.setupUi(self)  # 初始化窗体设置

    # 是否为图片
    def isImg(self, file):
        file = file.lower()
        if os.path.splitext(file)[-1] == '.jpg' or os.path.splitext(file)[-1] == '.png' or os.path.splitext(file)[
            -1] == '.jpeg' or os.path.splitext(file)[-1] == '.webp':
            return True
        else:
            return False
    # 获取所有文件
    def getfile(self):
        # 选择图片文件夹路径
        self.img_path = QFileDialog.getExistingDirectory(None, "选择图片文件夹路径", "D:/")
        self.list = os.listdir(self.img_path)  # 遍历选择的文件夹
        num = 0  # 记录图片数量
        self.Pre_listWidget.clear()  # 清空列表项
        for i in range(0, len(self.list)):  # 遍历图片列表
            filepath = os.path.join(self.img_path, self.list[i])  # 记录遍历到的文件名
            if os.path.isfile(filepath):  # 判断是否为文件
                if self.isImg(filepath) == True:  # 判断是否为图片
                    num = num + 1  # 数量加1
                    self.item = QtWidgets.QListWidgetItem(self.Pre_listWidget)  # 创建子窗口列表项
                    self.item.setText(self.list[i])  # 显示图片列表

    # 预览图片
    def itemClick(self, item):
        os.startfile(self.img_path + '\\' + item.text())

