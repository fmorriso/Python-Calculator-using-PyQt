import sys

from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtWidgets import *


class OutputUtils(QDialog):


    @staticmethod
    def display_message(msg: str, title: str, parent=None) -> None:
        app = QApplication(sys.argv)
        buttons = QMessageBox.StandardButton.Ok
        QMessageBox.information(parent, title, msg, buttons)
        app.closeAllWindows()
        app.exit()
