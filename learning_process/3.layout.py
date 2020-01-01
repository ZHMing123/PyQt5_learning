# _*_ coding:utf-8 _*_
#文件作者: ZHMing123
#开发时间：2020/1/1 20:03
#文件名称：3.layout.py
#开发工具：PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QFormLayout, QGridLayout

class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()
        self.user_label = QLabel('Username', self)
        self.pwd_label = QLabel('Password', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('Log in', self)
        self.signin_button = QPushButton('Sign in', self)

        # # 1.垂直布局
        # self.v_layout = QVBoxLayout()
        # self.v_layout.addWidget(self.user_label)
        # self.v_layout.addWidget(self.pwd_label)
        #
        # self.setLayout(self.v_layout)

        # # 2.水平布局
        # self.h_layout = QHBoxLayout()
        # self.h_layout.addWidget(self.user_label)
        # self.h_layout.addWidget(self.pwd_label)
        #
        # self.setLayout(self.h_layout)

        # 3.1将两个QLabel用垂直布局方式摆放，将两个QLineEdit也用垂直布局方式摆放，
        # 最后用一个水平布局管理来摆放着两个垂直布局管理器
        # self.label_v_layout = QVBoxLayout()
        # self.line_v_layout = QVBoxLayout()
        # self.button_h_layout = QHBoxLayout()
        # self.label_line_h_layout = QHBoxLayout()
        # self.all_v_layout = QVBoxLayout()
        #
        # self.label_v_layout.addWidget(self.user_label)
        # self.label_v_layout.addWidget(self.pwd_label)
        # self.line_v_layout.addWidget(self.user_line)
        # self.line_v_layout.addWidget(self.pwd_line)
        # self.button_h_layout.addWidget(self.login_button)
        # self.button_h_layout.addWidget(self.signin_button)
        # self.label_line_h_layout.addLayout(self.label_v_layout)
        # self.label_line_h_layout.addLayout(self.line_v_layout)
        # self.all_v_layout.addLayout(self.label_line_h_layout)
        # self.all_v_layout.addLayout(self.button_h_layout)
        #
        # self.setLayout(self.all_v_layout)

        # 3.2换种思路，可以把QLabel和QLineEdit用水平布局方式摆放：
        # self.user_h_layout = QHBoxLayout()
        # self.pwd_h_layout = QHBoxLayout()
        # self.button_h_layout = QHBoxLayout()
        # self.all_v_layout = QVBoxLayout()
        #
        # self.user_h_layout.addWidget(self.user_label)
        # self.user_h_layout.addWidget(self.user_line)
        # self.pwd_h_layout.addWidget(self.pwd_label)
        # self.pwd_h_layout.addWidget(self.pwd_line)
        # self.button_h_layout.addWidget(self.login_button)
        # self.button_h_layout.addWidget(self.signin_button)
        # self.all_v_layout.addLayout(self.user_h_layout)
        # self.all_v_layout.addLayout(self.pwd_h_layout)
        # self.all_v_layout.addLayout(self.button_h_layout)
        #
        # self.setLayout(self.all_v_layout)

        # 4.表单布局QFormLayout
        # self.f_layout = QFormLayout()
        # self.button_h_layout = QVBoxLayout()
        # self.all_v_layout = QVBoxLayout()
        #
        # self.f_layout.addRow(self.user_label, self.user_line)
        # self.f_layout.addRow(self.pwd_label, self.pwd_line)
        # self.button_h_layout.addWidget(self.login_button)
        # self.button_h_layout.addWidget(self.signin_button)
        # self.all_v_layout.addLayout(self.f_layout)
        # self.all_v_layout.addLayout(self.button_h_layout)
        #
        # self.setLayout(self.all_v_layout)

        # 5.网格布局QGridLayout
        # 把整个窗体想象成带有坐标的，然后只用把各个控件放在相应的坐标
        self.grid_layout = QGridLayout()
        self.button_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)
        self.button_h_layout.addWidget(self.login_button)
        self.button_h_layout.addWidget(self.signin_button)
        self.all_v_layout.addLayout(self.grid_layout)
        self.all_v_layout.addLayout(self.button_h_layout)

        self.setLayout(self.all_v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())