import os

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QMainWindow, QListWidgetItem

from rename import Ui_MainWindow



class openRename(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(openRename, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setupUi(self)  # 初始化

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
        self.img_path = QFileDialog.getExistingDirectory(None, "选择图片文件夹路径", "D:/")
        self.lineEdit.setText(self.img_path)
        self.list = os.listdir(self.img_path)  # 遍历文件夹中的文件
        num = 0
        self.Old_listWidget.clear()
        for i in range(0, len(self.list)):
            filepath = os.path.join(self.img_path, self.list[i])
            if os.path.isfile(filepath):
                if self.isImg(filepath) == True:
                    num = num + 1
                    self.item = QtWidgets.QListWidgetItem(self.Old_listWidget)
                    self.item.setText(self.list[i])

    def Rename(self):

        # oldpath=self.lineEdit.text()
        self.new_path = QFileDialog.getExistingDirectory(None, "选择图片文件夹路径", "D:/")

        for i in range(0, self.Old_listWidget.count()):
            item_ = self.Old_listWidget.item(i)
            itemtext = item_.text()

            x = itemtext.replace(itemtext.split(".")[0], ("rename" + str(i + 1)))
            self.item = QtWidgets.QListWidgetItem(self.listWidget_2)
            self.item.setText(x)
            newpath = os.path.join(self.new_path, x)
            oldpath = os.path.join(self.lineEdit.text(), itemtext)
            os.rename(oldpath, newpath)

    def Back(self):
        QMessageBox.warning(None, '完成', '重未名图片成功', QMessageBox.Ok)
