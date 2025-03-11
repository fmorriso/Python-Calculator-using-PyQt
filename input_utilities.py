import decimal
import sys
from decimal import Decimal

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMessageBox


class InputUtils:
    
    @staticmethod
    def get_whole_number(title: str, msg: str, parent=None) -> int:
        """get a whole number as directed by the specified message"""
        n: int = 0
        app = QApplication(sys.argv)
        waiting_for_valid_input = True
        response: tuple[int, bool] = (0, False)
        # trap user in dialog until they enter a valid value and click OK
        while waiting_for_valid_input:
            # response will be a tuple of the form (value, True/False} where True
            # means the OK button was pressed and False means the Cancel button was pressed
            n, response = QtWidgets.QInputDialog.getInt(parent, msg, title)
            # print(f'{response}=')
            if response:
                waiting_for_valid_input = False

        app.closeAllWindows()
        app.exit()

        return n

    @staticmethod
    def get_decimal_number(title: str, msg: str, parent=None) -> Decimal:
        """return a decimal number as directed by the message"""
        n: Decimal = Decimal(0)
        app = QApplication(sys.argv)
        waiting_for_valid_input = True
        # trap user in dialog until they enter a valid value and click OK
        while waiting_for_valid_input:
            # response will be a tuple of the form (value, True/False} where True
            # means the OK button was pressed and False means the Cancel button was pressed
            min = 0
            max = decimal.MAX_EMAX
            decimals = sys.float_info.dig
            n, response = QtWidgets.QInputDialog.getDouble(parent, msg, title, 0, min, max,
                                                        decimals)  # print(f'{response}=')
            if response:
                waiting_for_valid_input = False

        n: decimal = Decimal(n)
        app.closeAllWindows()
        app.exit()
        return n

    @staticmethod
    def get_floating_point_number(title: str, msg: str, parent=None) -> float:
        """return a floating-point number as directed by the message"""
        n: float = 0
        app = QApplication(sys.argv)
        waiting_for_valid_input = True
        # trap user in dialog until they enter a valid value and click OK
        while waiting_for_valid_input:
            # response will be a tuple of the form (value, True/False} where True
            # means the OK button was preseed and False means the Cancel button was pressed
            min_value = 0
            max_value = decimal.MAX_EMAX
            decimals = sys.float_info.dig
            n, response = QtWidgets.QInputDialog.getDouble(parent, msg, title, 0, min_value, max_value,
                                                           decimals)
            # print(f'{response}=')
            if response:
                waiting_for_valid_input = False

        n: float = float(n)
        app.closeAllWindows()
        app.exit()
        return n

    @staticmethod
    def get_yesno_response(title: str, question: str, parent=None) -> bool:
        """get a yes/no (True/False) response to a question"""
        app = QApplication(sys.argv)

        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setInformativeText(question)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Yes)
        msg_box.setIcon(QMessageBox.Icon.Question)
        ret: QMessageBox.StandardButton = msg_box.exec()

        app.closeAllWindows()
        app.exit()
        return ret == QMessageBox.StandardButton.Yes

    @staticmethod
    def get_single_choice(title: str, msg: str, choices: list[str], parent=None):
        """get a single choice from a list of choices"""
        item = ''
        app = QApplication(sys.argv)
        # flags
        # force user to choose one of the available choices before returning
        waiting_for_choice: bool = True
        while waiting_for_choice:
            item, resp = QtWidgets.QInputDialog.getItem(parent, title, msg, choices, 0, False, )
            # print(f'{item=}, {resp=}')
            waiting_for_choice = not resp

        app.closeAllWindows()
        app.exit()
        app = None
        return item
