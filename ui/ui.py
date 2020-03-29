#!/usr/bin/python3
"""UI"""
__author__ = 'kasakun'
__verison__ = '1.0'

import random
import argparse
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
    QTextEdit, QGridLayout, QApplication)
from PyQt5.QtCore import pyqtSlot

from enigma.enigma import Enigma

class EngimaUI(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        seed = QLabel('Seed')
        source = QLabel('Source')
        output = QLabel('Output')

        self.seed_edit = QLineEdit()
        self.source_edit = QTextEdit()
        self.output_edit = QTextEdit()
        self.output_edit.setReadOnly(True)

        button = QPushButton('Start')
        button.clicked.connect(self.on_click)

        # Grid setting
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(seed, 0, 0)
        grid.addWidget(self.seed_edit, 0, 1, 1, 5)

        grid.addWidget(source, 1, 0)
        grid.addWidget(self.source_edit, 1, 1, 4, 5)

        grid.addWidget(output, 5, 0)
        grid.addWidget(self.output_edit, 5, 1, 4, 5)

        grid.addWidget(button, 9, 0, 1, 1)

        self.setLayout(grid)

        self.setGeometry(200, 200, 600, 400)
        self.setWindowTitle('Enigma')
        self.show()

    @pyqtSlot()
    def on_click(self):
        random.seed(self.seed_edit.text())
        # Create a random size enigma
        enigma = Enigma(random.randint(5, 15))

        plain = self.source_edit.toPlainText()
        output = enigma.encrypt(plain)
        self.output_edit.setPlainText(output)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = EngimaUI()
    sys.exit(app.exec_())

