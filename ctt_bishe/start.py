from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys
import numpy as np
import matplotlib.pyplot as plt  # plt 用于显示图片
import matplotlib.image as mpimg  # mpimg 用于读取图片
import time
import socket
import os
import struct
from PIL import Image


# global x0, u, t, pic_name


class Ui_MainWindow(QMainWindow):
    def __init__(self, parrent=None):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 290, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 130, 72, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_account = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_account.setGeometry(QtCore.QRect(310, 130, 113, 21))
        self.lineEdit_account.setObjectName("lineEdit_account")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 200, 72, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(310, 200, 113, 21))
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.login_solt)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "登录"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.label.setText(_translate("MainWindow", "账号："))
        self.label_2.setText(_translate("MainWindow", "密码："))

    def login_solt(self):
        account = self.lineEdit_account.text()
        password = self.lineEdit_password.text()
        sign = ''
        if account != 'ctt':
            sign = '账号错误！'
            # 清除文本框并重置光标
            self.lineEdit_account.setText('')
            self.lineEdit_account.setFocus()
            return None
        if password != '001':
            sign = '密码错误！'
            self.lineEdit_password.setText('')
            self.lineEdit_password.setFocus()
            return None
        else:
        # if account == 'ctt' and password == '001':
            self.close()
        # app = QApplication(sys.argv)
            clientWindow.show()
        # sys.exit(app.exec_())


class Ui_Form_Client(QWidget):
    def __init__(self, parent=None):
        super(Ui_Form_Client, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(564, 458)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(200, 90, 161, 241))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logistic = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.logistic.setFont(font)
        self.logistic.setObjectName("logistic")
        self.verticalLayout.addWidget(self.logistic)
        self.arnold = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.arnold.setFont(font)
        self.arnold.setObjectName("arnold")
        self.verticalLayout.addWidget(self.arnold)
        self.mixed = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.mixed.setFont(font)
        self.mixed.setObjectName("mixed")
        self.verticalLayout.addWidget(self.mixed)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.logistic.clicked.connect(self.logistic_algo)
        self.arnold.clicked.connect(self.arnold_algo)
        self.mixed.clicked.connect(self.mixed_algo)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "client"))
        self.logistic.setText(_translate("Form", "Logistic算法"))
        self.arnold.setText(_translate("Form", "Arnold变换"))
        self.mixed.setText(_translate("Form", "混合算法"))

    def logistic_algo(self):
        self.close()
        logisticWindow.show()

    def arnold_algo(self):
        self.close()
        arnoldWindow.show()

    def mixed_algo(self):
        self.close()
        mixedWindow.show()


class Ui_Form_Logistic(QWidget):
    global x0, u, pic_name

    def __init__(self, parent=None):
        super(Ui_Form_Logistic, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.but_Lenter = QtWidgets.QPushButton(Form)
        self.but_Lenter.setGeometry(QtCore.QRect(140, 240, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.but_Lenter.setFont(font)
        self.but_Lenter.setObjectName("but_Lenter")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(60, 70, 265, 131))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.pic_name = QtWidgets.QLineEdit(self.widget)
        self.pic_name.setObjectName("pic_name")
        self.gridLayout.addWidget(self.pic_name, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.x0 = QtWidgets.QLineEdit(self.widget)
        self.x0.setObjectName("x0")
        self.gridLayout.addWidget(self.x0, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.u = QtWidgets.QLineEdit(self.widget)
        self.u.setObjectName("u")
        self.gridLayout.addWidget(self.u, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.but_Lenter.clicked.connect(self.logistic_data)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Logistic"))
        self.but_Lenter.setText(_translate("Form", "确认"))
        self.label_3.setText(_translate("Form", "图片名"))
        self.label.setText(_translate("Form", "X0(0-1)   "))
        self.label_2.setText(_translate("Form", "U(3.57-4)"))

    def logistic_data(self):
        x0 = float(self.x0.text())
        u = float(self.u.text())
        pic_name = self.pic_name.text()
        print(x0, u, pic_name)
        self.sock_client_image(x0, u, pic_name)
        self.close()


    def sock_client_image(self, x0, u, pic_name):
        im = Image.open(pic_name)
        # im = im.convert("L")

        plt.imshow(im)
        plt.show()
        self.img_hist(im)

        im_en = self.logic_encrypt(im, x0, u)
        # im_de = logic_encrypt(im_en, x0, u)
        plt.imshow(im_en)
        plt.axis('off')
        # plt.savefig('im_en.jpg') #分辨率改变
        im_en.save('im_en.png')  # 分辨率不变
        plt.show()
        self.img_hist(im_en)
        # plt.imshow(im_de)
        # plt.show()

        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(('82.156.17.246', 8080))
            except socket.error as msg:
                print(msg)
                print(sys.exit(1))
            socket.setdefaulttimeout(20)
            file = 'im_en.png'  # 输入当前目录下的图片名
            # pack按照图片格式、图片名字、图片大小
            fhead = struct.pack(b'128sq',  # 图片打包的格式为128sq
                                bytes(os.path.basename(file), encoding='utf-8'),  # 返回图片文件名，编码字节化
                                os.stat(file).st_size)  # 返回读取文件的相关属性，然后得到其中st_size的数据(记录文件大小)
            s.send(fhead)
            key_tuple = 'x0' + str(x0) + 'u' + str(u)
            s.send(key_tuple.encode('utf-8'))

            fp = open(file, 'rb')  # 打开要传输的图片
            while True:
                data = fp.read(1024 * 1024)  # 读入图片数据,data是图片的数据字节流(由于图片字节很多，这里一次只读取1024个字节)
                if not data:  # 如果读到字节的数据没有了
                    print('{0} send over...'.format(file))
                    break
                time.sleep(1)
                s.send(data)  # 以二进制格式发送图片数据（每次发1024个字节）

            s.close()
            break  # 如果需要一直发送图片则需要在这里进行修改
    def logic_encrypt(self, im, x0, u):
        xsize, ysize = im.size
        im = np.array(im).flatten()
        num = len(im)

        for i in range(100):
            x0 = u * x0 * (1 - x0)

        E = np.zeros(num)
        E[0] = x0
        for i in range(0, num - 1):
            E[i + 1] = u * E[i] * (1 - E[i])
        E = np.round(E * 255).astype(np.uint8)

        im = np.bitwise_xor(E, im)
        im = im.reshape(xsize, ysize, -1)
        im = np.squeeze(im)
        im = Image.fromarray(im)

        return im

    def img_hist(self, im):
        im = np.array(im)
        plt.hist(im.flatten(), bins=256)
        plt.show()


class Ui_Form_Arnold(QWidget):
    def __init__(self, parent=None):
        super(Ui_Form_Arnold, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.but_Aenter = QtWidgets.QPushButton(Form)
        self.but_Aenter.setGeometry(QtCore.QRect(140, 190, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.but_Aenter.setFont(font)
        self.but_Aenter.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(60, 90, 286, 57))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.pic_name = QtWidgets.QLineEdit(self.widget)
        self.pic_name.setObjectName("pic_name")
        self.gridLayout.addWidget(self.pic_name, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.t = QtWidgets.QLineEdit(self.widget)
        self.t.setObjectName("t")
        self.gridLayout.addWidget(self.t, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.but_Aenter.clicked.connect(self.arnold_data)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Arnold"))
        self.but_Aenter.setText(_translate("Form", "确认"))
        self.label_2.setText(_translate("Form", "图片名称"))
        self.label.setText(_translate("Form", "T(范围随机)"))

    def arnold_data(self):
        t = self.t.text()
        pic_name = self.pic_name.text()
        print(t, pic_name)
        self.sock_client(t, pic_name)
        self.close()

    def sock_client(self, t, pic_name):
        img = mpimg.imread(pic_name)  # 读取和代码处于同一目录下的
        plt.imshow(img)  # 显示图片
        # plt.axis('off') # 不显示坐标轴
        plt.show()

        for i in range(int(t)):
            imgn = self.arnold(img)
            img = np.copy(imgn)

        plt.imshow(img)  # 显示图片
        # plt.axis('off') # 不显示坐标轴
        plt.show()
        mpimg.imsave('img.bmp', img)
        # plt.savefig('img')
        # img.save('img.bmp')
        self.img_hist(img)

        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(('82.156.17.246', 8080))
            except socket.error as msg:
                print(msg)
                print(sys.exit(1))
            socket.setdefaulttimeout(20)
            file = 'img.bmp'  # 输入当前目录下的图片名
            # pack按照图片格式、图片名字、图片大小
            fhead = struct.pack(b'128sq',  # 图片打包的格式为128sq
                                bytes(os.path.basename(file), encoding='utf-8'),  # 返回图片文件名，编码字节化
                                os.stat(file).st_size)  # 返回读取文件的相关属性，然后得到其中st_size的数据(记录文件大小)
            s.send(fhead)
            key_tuple = 't' + str(t)
            s.send(key_tuple.encode('utf-8'))

            fp = open(file, 'rb')  # 打开要传输的图片
            while True:
                data = fp.read(1024 * 1024)  # 读入图片数据,data是图片的数据字节流(由于图片字节很多，这里一次只读取1024个字节)
                if not data:  # 如果读到字节的数据没有了
                    print('{0} send over...'.format(file))
                    break
                time.sleep(1)
                s.send(data)  # 以二进制格式发送图片数据（每次发1024个字节）

            s.close()
            break  # 如果需要一直发送图片则需要在这里进行修改

    def arnold(self, img):
        r, c, s = img.shape
        p = np.zeros((r, c, s), np.uint8)
        a = 1
        b = 1
        for i in range(r):
            for j in range(c):
                x = (i + b * j) % r
                y = (a * i + (a * b + 1) * j) % c
                p[x, y] = img[i, j]
        return p

    def img_hist(self, img):
        im = np.array(img)
        plt.hist(im.flatten(), bins=256)
        plt.show()


class Ui_Form_Mixed(QWidget):
    def __init__(self, parent=None):
        super(Ui_Form_Mixed, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.but_Menter = QtWidgets.QPushButton(Form)
        self.but_Menter.setGeometry(QtCore.QRect(150, 240, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.but_Menter.setFont(font)
        self.but_Menter.setObjectName("but_Menter")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(60, 40, 286, 161))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.pic_name = QtWidgets.QLineEdit(self.widget)
        self.pic_name.setObjectName("pic_name")
        self.gridLayout.addWidget(self.pic_name, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.x0 = QtWidgets.QLineEdit(self.widget)
        self.x0.setObjectName("x0")
        self.gridLayout.addWidget(self.x0, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.u = QtWidgets.QLineEdit(self.widget)
        self.u.setObjectName("u")
        self.gridLayout.addWidget(self.u, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.t = QtWidgets.QLineEdit(self.widget)
        self.t.setObjectName("t")
        self.gridLayout.addWidget(self.t, 3, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.but_Menter.clicked.connect(self.mixed_data)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "mixed"))
        self.but_Menter.setText(_translate("Form", "确认"))
        self.label_4.setText(_translate("Form", "图片名称"))
        self.label.setText(_translate("Form", "X0(0-1)"))
        self.label_2.setText(_translate("Form", "U(3.57-4)"))
        self.label_3.setText(_translate("Form", "T(范围随机)"))

    def mixed_data(self):
        x0 = float(self.x0.text())
        u = float(self.u.text())
        t = self.t.text()
        pic_name = self.pic_name.text()
        print(x0, t, u, pic_name)
        self.sock_client_image(t,x0,u,pic_name)
        self.close()

    def sock_client_image(self, t, x0, u,pic_name):
        img = mpimg.imread(pic_name)  # 读取和代码处于同一目录下的
        plt.imshow(img)  # 显示图片
        # plt.axis('off') # 不显示坐标轴
        plt.show()

        for i in range(int(t)):
            imgn = self.arnold(img)
            img = np.copy(imgn)

        plt.imshow(img)  # 显示图片
        plt.axis('off')  # 不显示坐标轴
        plt.show()
        mpimg.imsave('img.bmp', img)
        # plt.savefig('img')
        self.img_hist(img)

        im = Image.open('img.bmp')
        # im = im.convert("L")

        im_en = self.logic_encrypt(im, x0, u)
        # im_de = logic_encrypt(im_en, x0, u)
        plt.imshow(im_en)
        plt.axis('off')
        # plt.savefig('im_en.jpg') #分辨率改变
        im_en.save('im_en.bmp')  # 分辨率不变
        plt.show()
        self.img_hist(im_en)

        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(('82.156.17.246', 8080))
            except socket.error as msg:
                print(msg)
                print(sys.exit(1))
            socket.setdefaulttimeout(20)
            file = 'im_en.bmp'  # 输入当前目录下的图片名
            # pack按照图片格式、图片名字、图片大小
            fhead = struct.pack(b'128sq',  # 图片打包的格式为128sq
                                bytes(os.path.basename(file), encoding='utf-8'),  # 返回图片文件名，编码字节化
                                os.stat(file).st_size)  # 返回读取文件的相关属性，然后得到其中st_size的数据(记录文件大小)
            s.send(fhead)
            key_tuple = 't' + str(t) + 'x0' + str(x0) + 'u' + str(u)
            s.send(key_tuple.encode('utf-8'))

            fp = open(file, 'rb')  # 打开要传输的图片
            while True:
                data = fp.read(1024 * 1024)  # 读入图片数据,data是图片的数据字节流(由于图片字节很多，这里一次只读取1024个字节)
                if not data:  # 如果读到字节的数据没有了
                    print('{0} send over...'.format(file))
                    break
                time.sleep(1)
                s.send(data)  # 以二进制格式发送图片数据（每次发1024个字节）

            s.close()
            break  # 如果需要一直发送图片则需要在这里进行修改

    def arnold(self,img):
        r, c, s = img.shape
        p = np.zeros((r, c, s), np.uint8)
        a = 1
        b = 1
        for i in range(r):
            for j in range(c):
                x = (i + b * j) % r
                y = (a * i + (a * b + 1) * j) % c
                p[x, y] = img[i, j]
        return p

    def img_hist(self,img):
        im = np.array(img)
        plt.hist(im.flatten(), bins=256)
        plt.show()

    def logic_encrypt(self,im, x0, u):
        xsize, ysize = im.size
        im = np.array(im).flatten()
        num = len(im)

        for i in range(100):
            x0 = u * x0 * (1 - x0)

        E = np.zeros(num)
        E[0] = x0
        for i in range(0, num - 1):
            E[i + 1] = u * E[i] * (1 - E[i])
        E = np.round(E * 255).astype(np.uint8)

        im = np.bitwise_xor(E, im)
        im = im.reshape(xsize, ysize, -1)
        im = np.squeeze(im)
        im = Image.fromarray(im)

        return im


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    clientWindow = Ui_Form_Client()
    logisticWindow = Ui_Form_Logistic()
    arnoldWindow = Ui_Form_Arnold()
    mixedWindow = Ui_Form_Mixed()
    sys.exit(app.exec_())
