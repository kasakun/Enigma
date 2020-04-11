#!/usr/bin/python3
"""UI"""
__author__ = 'kasakun'
__verison__ = '1.0'

import random
import argparse
import sys
import time
from PyQt5.QtWidgets import (QWidget, QDialog, QLabel, QLineEdit, QPushButton,
    QTextEdit, QGridLayout, QApplication, QProgressBar)
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread, Qt

from enigma.enigma import Enigma

class Runthread(QThread):
    """Work thread processing engima"""
    sig_finish_to_main = pyqtSignal(str)

    def __init__(self, seed, source):
        super(Runthread, self).__init__()

        self.seed = seed
        self.source = source

    def __del__(self):
        self.wait()

    def run(self):
        # Create a random size enigma
        random.seed(self.seed)
        enigma = Enigma(random.randint(5, 15))
        output = enigma.encrypt(self.source)

        self.sig_finish_to_main.emit(output)

class Loading(QDialog):
    """
    Loading window for processing engmia.
    Cancel button to close the window and terminate the workload.
    """
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.button = QPushButton('Cancel')
        self.button.clicked.connect(self.close)

        self.pbar = QProgressBar(self)
        self.pbar.setValue(0)

        # Grid setting
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.pbar, 0, 0, 1, 5)
        grid.addWidget(self.button, 1, 2, 1, 1)

        self.setLayout(grid)
        self.setGeometry(300, 300, 400, 100)
        self.setWindowTitle('Loading')
        self.setWindowFlag(Qt.FramelessWindowHint)

class EngimaUI(QWidget):
    """Main window"""
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        seed = QLabel('Seed')
        source = QLabel('Source')
        output = QLabel('Output')

        self.seed_edit = QLineEdit()
        self.source_edit = QTextEdit()
        self.output_edit = QTextEdit()
        self.output_edit.setReadOnly(True)

        button = QPushButton('Start')
        button.clicked.connect(self.create_thread_and_run)

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
    def create_thread_and_run(self):
        # create thread and loading window
        self.loading = Loading()
        self.thread = Runthread(self.seed_edit.text(),
            self.source_edit.toPlainText())

        # cancel button to terminate the thread
        self.loading.button.clicked.connect(self.thread.terminate)

        # show/close the loading window when the thread start/end
        self.thread.started.connect(self.loading.show)
        self.thread.finished.connect(self.loading.close)

        # print the result in the output when thread returns
        self.thread.sig_finish_to_main.connect(self.print_result)

        # start the thread
        self.thread.start()

    @pyqtSlot(str)
    def print_result(self, output):
        self.output_edit.setPlainText(output)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = EngimaUI()
    sys.exit(app.exec_())

