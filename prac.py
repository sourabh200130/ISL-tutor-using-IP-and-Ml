import sys
import cv2
import string
from PyQt5.QtCore import QThread, Qt
from PyQt5.QtGui import QImage, QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import mediapipe as mp
from page import Ui_ThirdWindow
from PyQt5 import QtCore, QtGui, QtWidgets

mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils


class ThirdWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_ThirdWindow()
        self.ui.setupUi(self)
        self.ui.showbutton.clicked.connect(self.start_camera)
        self.ui.alphabet_label.setFont(QFont("Times NewRoman", 30))
        self.ui.alphabet_label.setText('A')
        self.alphabets = list(string.ascii_uppercase)
        self.current_index = 0
        self.ui.alphabet_label.setText(self.alphabets[self.current_index])
        self.ui.nextbutton.clicked.connect(self.next_alphabet)
        self.ui.prevbutton.clicked.connect(self.prev_alphabet)
        self.camera_thread = None
        self.cap = None

    def start_camera(self):
        if self.camera_thread is None:
            self.cap = cv2.VideoCapture(0)
            self.camera_thread = CameraThread(self.cap, self.ui.image_label)
            self.camera_thread.start()

    def closeEvent(self, event):
        if self.camera_thread is not None:
            self.camera_thread.stop()
        if self.cap is not None:
            self.cap.release()
        event.accept()

    def next_alphabet(self):
        self.current_index = (self.current_index + 1) % len(self.alphabets)
        self.ui.alphabet_label.setText(self.alphabets[self.current_index])

    def prev_alphabet(self):
        self.current_index = (self.current_index - 1) % len(self.alphabets)
        self.ui.alphabet_label.setText(self.alphabets[self.current_index])



class CameraThread(QThread):
    def __init__(self, cap, image_label):
        super().__init__()
        self.cap = cap
        self.image_label = image_label
        self.is_running = False

    def run(self):
        self.is_running = True
        with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
            while self.is_running and self.cap.isOpened():
                ret, frame = self.cap.read()
                image, results = self.mediapipe_detection(frame, holistic)
                self.draw_landmarks(image, results)
                pixmap = self.convert_cvimage_to_pixmap(image)
                self.image_label.setPixmap(pixmap.scaled(
                    self.image_label.size(), Qt.KeepAspectRatio, Qt.FastTransformation))
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
        self.cap.release()
        cv2.destroyAllWindows()

    def stop(self):
        self.is_running = False

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
        # mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS)
        # mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
        mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

    @staticmethod
    def convert_cvimage_to_pixmap(cvimage):
        rgb_image = cv2.cvtColor(cvimage, cv2.COLOR_BGR2RGB)
        height, width, channel = rgb_image.shape
        bytes_per_line = channel * width
        q_image = QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        return QPixmap.fromImage(q_image)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = ThirdWindow()
    Window.show()
    sys.exit(app.exec_())

