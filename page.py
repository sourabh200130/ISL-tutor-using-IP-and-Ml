import os
# Form implementation generated from reading ui file 'page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import string
import cv2
import numpy as np
from PyQt5.QtGui import QImage, QPixmap, QFont
from PyQt5.QtCore import QThread, Qt , QSize
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QPushButton
import mediapipe as mp
import joblib
import time

import page

mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
clf = joblib.load('indian_last.pkl')


class Ui_ThirdWindow(object):
    def openWindow4(self):
        self.window=QtWidgets.QMainWindow()
        from welcm2 import Ui_SecondWindow
        self.ui=Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, ThirdWindow):
        ThirdWindow.setObjectName("MainWindow")
        ThirdWindow.resize(1193, 757)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ThirdWindow.sizePolicy().hasHeightForWidth())
        ThirdWindow.setSizePolicy(sizePolicy)
        ThirdWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        ThirdWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(ThirdWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.nextbutton = QtWidgets.QPushButton(self.centralwidget)
        self.nextbutton.setObjectName("nextbutton")
        self.gridLayout.addWidget(self.nextbutton, 18, 6, 1, 1)
        self.prevbutton = QtWidgets.QPushButton(self.centralwidget)
        self.prevbutton.setObjectName("prevbutton")
        self.gridLayout.addWidget(self.prevbutton, 18, 3, 1, 1)

        self.backbtn = QPushButton(self.centralwidget, clicked=lambda: self.openWindow4())
        self.backbtn.setObjectName("backbtn")
        self.backbtn.setMaximumSize(QSize(50, 16777215))
        self.gridLayout.addWidget(self.backbtn, 0, 0, 1, 1)
        self.backbtn.clicked.connect(ThirdWindow.close)
        self.backbtn.clicked.connect(self.closeEvent)

        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setMinimumSize(QSize(256, 220))
        self.image_label.setMaximumSize(QtCore.QSize(680, 478))
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.gridLayout.addWidget(self.image_label, 9, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 17, 12, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 5, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 9, 5, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 8, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setToolTip("")
        self.label_6.setStyleSheet(
            "<html><head/><body><p><span style=\" font-size:18pt;\">1. Make sure webcam is turned on and Working.\\n2.Look at the current letter and its equivalent handsign.\\n3.Replicate the handsign infront of the camera.\\n4.Make sure the handsign is in the frame and it is being recognized.\\n5.If it shows an error try correcting the mistake and do it again.</span></p></body></html>")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 1, QtCore.Qt.AlignTop)
        #self.showbutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.showbutton.sizePolicy().hasHeightForWidth())
        # self.showbutton.setSizePolicy(sizePolicy)
        # self.showbutton.setMaximumSize(QtCore.QSize(660, 498))
        # self.showbutton.setObjectName("showbutton")
        # self.gridLayout.addWidget(self.showbutton, 17, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 21, 12, 1, 1)

        #To display the hint(images)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 5, 5, 2, 1)
        self.current_image_index = 0
        self.image_filenames = sorted([f for f in os.listdir('images') if f.endswith('.jpg')])
        self.nextbutton.clicked.connect(self.next_image)
        self.prevbutton.clicked.connect(self.prev_image)
        image = QPixmap("images/a.jpg")
        self.label_14.setPixmap(image)


        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 18, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 8, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 11, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 10, 1, 1)
        self.alphabet_label = QtWidgets.QLabel(self.centralwidget)
        self.alphabet_label.setMinimumSize(QtCore.QSize(240, 45))
        self.alphabet_label.setMaximumSize(QtCore.QSize(800, 60))
        self.alphabet_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alphabet_label.setText("")
        self.alphabet_label.setObjectName("alphabet_label")
        self.gridLayout.addWidget(self.alphabet_label, 5, 0, 1, 1, QtCore.Qt.AlignTop)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 11, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 6, 1, 1, 1)
        ThirdWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ThirdWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1193, 26))
        self.menubar.setObjectName("menubar")
        ThirdWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ThirdWindow)
        self.statusbar.setObjectName("statusbar")
        ThirdWindow.setStatusBar(self.statusbar)
        self.retranslateUi(ThirdWindow)
        QtCore.QMetaObject.connectSlotsByName(ThirdWindow)

        # button connection
        #self.showbutton.clicked.connect(self.start_camera)
        self.alphabet_label.setFont(QFont("Times NewRoman", 30))
        self.alphabet_label.setText('A')
        self.alphabets = list(string.ascii_uppercase)
        self.current_index = 0
        self.alphabet_label.setText(self.alphabets[self.current_index])
        self.nextbutton.clicked.connect(self.next_alphabet)
        self.prevbutton.clicked.connect(self.prev_alphabet)
        self.camera_thread = None
        self.cap = None
        self.start_camera()
        global obj
        obj=self

    def retranslateUi(self, ThirdWindow):
        _translate = QtCore.QCoreApplication.translate
        ThirdWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nextbutton.setText(_translate("MainWindow", "NEXT"))
        self.backbtn.setText(_translate("MainWindow", "BACK"))
        self.label_11.setText(_translate("MainWindow", "HINT:"))
        self.label_10.setText(_translate("MainWindow", "ALPHABET:"))
        self.label_12.setText(_translate("MainWindow", "LIVE CAMERA:"))
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:11pt;\">1. Make sure webcam is turned on and Working.</span></p><p><span style=\" font-size:11pt;\">2.Look at the current letter and its equivalent handsign.</span></p><p><span style=\" font-size:11pt;\">3.Replicate the handsign infront of the camera.</span></p><p><span style=\" font-size:11pt;\">4.Make sure the handsign is in the frame and it is being recognized.</span></p><p><span style=\" font-size:11pt;\">5.If it shows an error try correcting the mistake and do it again.</span></p></body></html>"))
        #self.showbutton.setText(_translate("MainWindow", "show"))
        self.label_5.setText(_translate("MainWindow", "LEARNING PHASE"))
        self.label_13.setText(_translate("MainWindow", "INSTRUCTIONS:"))
        self.prevbutton.setText(_translate("MainWindow", "PREV"))

    def start_camera(self):
        if self.camera_thread is None:
            self.cap = cv2.VideoCapture(0)
            self.camera_thread = CameraThread(self.cap, self.image_label)
            self.camera_thread.start()

    def closeEvent(self, event):
        self.camera_thread.stop()

     # To display next & prev image,alphabets
    def return_self(self):
        return obj
    def next_image(self):
        self.current_image_index += 1
        if self.current_image_index >= len(self.image_filenames):
            self.current_image_index = 0
        self.label_14.setPixmap(QPixmap(f'images/{self.image_filenames[self.current_image_index]}'))

    def prev_image(self):
        self.current_image_index -= 1
        self.label_14.setPixmap(QPixmap(f'images/{self.image_filenames[self.current_image_index]}'))


    def next_alphabet(self):
        self.current_index = (self.current_index + 1) % len(self.alphabets)
        self.alphabet_label.setText(self.alphabets[self.current_index])

    def prev_alphabet(self):
        self.current_index = (self.current_index - 1) % len(self.alphabets)
        self.alphabet_label.setText(self.alphabets[self.current_index])


class CameraThread(QThread):
    def __init__(self, cap, image_label):
        super().__init__()
        self.cap = cap
        self.image_label = image_label
        self.is_running = False



    def run(self):
        self.is_running = True
        with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
            while self.is_running and self.cap.isOpened():
                ret, image = self.cap.read()
                flag=0
                image.flags.writeable = False
                results = hands.process(image)
                image.flags.writeable = True
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    cleaned_landmark = self.data_clean(results.multi_hand_landmarks)
                    # print(cleaned_landmark)
                    if cleaned_landmark:
                        flag=0
                        y_pred = clf.predict(cleaned_landmark)
                        # print(y_pred[0])
                        image = cv2.putText(image, y_pred[0], (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255),2,cv2.LINE_AA)
                        try:
                            print(obj.alphabet_label.text())
                            if str(obj.alphabets[obj.current_index])==str(y_pred[0]) :
                                flag=1
                                obj.next_alphabet()
                                obj.next_image()
                        except Exception as error:
                            print(error)

                pixmap = self.convert_cvimage_to_pixmap(image)
                self.image_label.setPixmap(pixmap.scaled(
                    self.image_label.size(), Qt.KeepAspectRatio, Qt.FastTransformation))
                if flag:
                    time.sleep(1)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
        self.cap.release()
        cv2.destroyAllWindows()

    def stop(self):
        self.is_running = False

    @staticmethod
    def data_clean(landmark):
        data = landmark[0]

        try:
            data = str(data)

            data = data.strip().split('\n')

            garbage = ['landmark {', '  visibility: 0.0', '  presence: 0.0', '}']

            without_garbage = []

            for i in data:
                if i not in garbage:
                    without_garbage.append(i)

            clean = []

            for i in without_garbage:
                i = i.strip()
                clean.append(i[2:])

            return ([clean])

        except:
            return (np.zeros([1, 63], dtype=int)[0])
    @staticmethod
    def mediapipe_detection(image, model):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # COLOR CONVERSION BGR 2 RGB
        image.flags.writeable = False  # Image is no longer writeable
        results = model.process(image)  # Make prediction
        image.flags.writeable = True  # Image is now writeable
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # COLOR COVERSION RGB 2 BGR
        return image, results

    @staticmethod
    def draw_landmarks(image, results):
        mp_drawing.draw_landmarks(image,results.multi_hand_landmarks , mp_holistic.HAND_CONNECTIONS)
        # mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS)
        # mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
        # mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        # mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

    @staticmethod
    def convert_cvimage_to_pixmap(cvimage):
        rgb_image = cv2.cvtColor(cvimage, cv2.COLOR_BGR2RGB)
        height, width, channel = rgb_image.shape
        bytes_per_line = channel * width
        q_image = QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        return QPixmap.fromImage(q_image)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ThirdWindow = QtWidgets.QMainWindow()
    ui = Ui_ThirdWindow()
    ui.setupUi(ThirdWindow)
    ThirdWindow.show()
    sys.exit(app.exec_())