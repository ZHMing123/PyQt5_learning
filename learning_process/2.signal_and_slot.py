# _*_ coding:utf-8 _*_
#文件作者: ZHMing123
#开发时间：2020/1/1 16:47
#文件名称：2.signal_and_slot.py
#开发工具：PyCharm

import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class Demo(QWidget):
    # 自定义信号
    my_signal = pyqtSignal()

    def __init__(self):
        super(Demo, self).__init__()
        # self.button = QPushButton('Start', self)

        # 一个信号连接一个槽
        # self.button.clicked.connect(self.change_text)

        # 多个信号连接同一个槽
        # self.button.pressed.connect(self.change_text)
        # self.button.released.connect(self.change_text)

        # 一个信号与另外一个信号连接
        # self.button.pressed.connect(self.button.released)
        # self.button.released.connect(self.change_text)

        # 一个信号连接多个槽,信号都为clicked
        # self.resize(300, 300)
        # self.setWindowTitle('demo')
        # self.button = QPushButton('Start', self)
        # self.button.clicked.connect(self.change_text)
        # self.button.clicked.connect(self.change_window_size)
        # self.button.clicked.connect(self.change_window_title)

        # 自定义信号
        self.label = QLabel('Hello World', self)
        self.my_signal.connect(self.change_text)

    def change_text(self):
        # 一个信号连接一个槽
        # print('change text')
        # self.button.setText('Stop')
        # self.button.clicked.disconnect(self.change_text)

        # 多个信号连接同一个槽
        # 一个信号连接多个槽,信号都为clicked
        # # 若当前按钮文本为‘Start’，则将文本改为‘Stop’；若为‘Stop’，则改为‘Start’。
        # if self.button.text() == 'Start':
        #     self.button.setText('Stop')
        # else:
        #     self.button.setText('Start')

        # 自定义信号
        if self.label.text() == 'Hello World':
            self.label.setText('Hello PyQt5')
        else:
            self.label.setText('Hello World')

    def change_window_size(self):
        print('change window size')
        self.resize(500, 500)
        self.button.clicked.disconnect(self.change_window_size)

    def change_window_title(self):
        print('change window title')
        self.setWindowTitle('window title changed')
        self.button.clicked.disconnect(self.change_window_title)

    # 自定义信号
    # mousePressEvent()方法是许多控件自带的，这里来自于QWidget。
    # 该方法用来监测鼠标是否有按下。现在鼠标若被按下，则会发出自定义的信号。
    def mousePressEvent(self, QMouseEvent):
        self.my_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())