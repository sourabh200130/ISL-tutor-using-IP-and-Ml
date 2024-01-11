import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap

class ImageWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Viewer')
        self.setGeometry(100, 100, 400, 400)
        self.current_image_index = 0
        self.image_filenames = sorted([f for f in os.listdir('images') if f.endswith('.jpg')])

        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap(f'images/{self.image_filenames[self.current_image_index]}'))
        self.image_label.setGeometry(0, 0, 400, 300)

        self.next_button = QPushButton('Next', self)
        self.next_button.setGeometry(150, 320, 100, 50)
        self.next_button.clicked.connect(self.next_image)

    def next_image(self):
        self.current_image_index += 1
        if self.current_image_index >= len(self.image_filenames):
            self.current_image_index = 0
        self.image_label.setPixmap(QPixmap(f'images/{self.image_filenames[self.current_image_index]}'))

if __name__ == '__main__':
    app = QApplication([])
    window = ImageWindow()
    window.show()
    app.exec_()
