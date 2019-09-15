# -*- coding:utf-8 -*-
import sys

# 引用pyqt5.qtwidgets模块中的基本控件
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 每一个pyqt5应用程序必须创建一个应用程序对象。 sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)
    # QWidgets部件是pyqt5所有用户界面对象的基类。它为QWidget提供默认构造函数。默认构造函数没有父类。
    w = QWidget()
    # resize(width, height) 方法调整窗口的大小
    w.resize(250, 150)
    # move(x, y) 方法移动窗口在屏幕上的位置
    w.move(300, 300)
    # setWindowTitle(string) 设置窗口标题
    w.setWindowTitle('Simple')
    # show() 显示在屏幕上
    w.show()

    # sys.exit() 方法确保应用程序干净的退出
    sys.exit(app.exec_())