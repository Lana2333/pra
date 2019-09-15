# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget
# 导入 QtGui 中的QIcon 模块
from PyQt5.QtGui import QIcon

class AppIcon(QWidget):
    def __init__(self):
        super().__init__()
        # 界面绘制交给 initUI() 方法
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Icon')

        # setGeometry(x, y, width, height) 方法设置窗口位置和大小
        self.setGeometry(500, 300, 280, 200)

        # setWindowIcon(argv) 方法设置窗口图标；
        # QIcon(iconPath) 方法引用目标图片的路径
        self.setWindowIcon(QIcon('../imgs/tab.png'))

        self.show()

if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = AppIcon()
    sys.exit(app.exec_())

