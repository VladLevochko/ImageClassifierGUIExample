import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFrame
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt

import random


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'First QT application'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 600

        self.image_label = None
        self.text_label = None

        self.initUi()

    def initUi(self):
        self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)

        layout = QVBoxLayout()

        pixmap = QPixmap("320x320.jpg")
        print(pixmap.size())
        self.image_label = QLabel()
        self.image_label.setPixmap(pixmap)
        self.image_label.setContentsMargins(0, 0, 0, 0)

        self.text_label = QLabel()
        self.text_label.setText("label1: 0.23525\nlabel2: 0.272\nlabel3: 0.26386")

        layout.addWidget(self.image_label)
        layout.addWidget(self.text_label)

        self.setLayout(layout)
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_Space:
            image, text = self.generate_random_values()
            self.set_labels(image, text)

    def set_labels(self, image, text):
        self.image_label.setPixmap(image)
        self.text_label.setText(text)

    def generate_random_values(self):
        image = QPixmap("320x320.jpg")
        text = ''
        for i in range(5):
            text += ('label %d: ' % i) + str(random.uniform(0, 1)) + '\n'

        return image, text


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
