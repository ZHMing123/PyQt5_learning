# _*_ coding:utf-8 _*_
#文件作者: ZHMing123
#开发时间：2020/1/1 10:41
#文件名称：1.pyqt5_test.py
#开发工具：PyCharm


import sys
from PyQt5.QtWidgets import QApplication, QLabel


if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel('<h1><font color="red">Hello World !</h1>')
    label.show()
    sys.exit(app.exec_())

