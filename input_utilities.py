import decimal
import sys
from decimal import Decimal

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMessageBox


class InputUtils:
    @staticmethod
    def get_whole_number(title: str, msg: str, parent=None) -> int:
        """get a whole number as directed by the specified message"""
        app = QApplication(sys.argv)
        waiting_for_valid_input = True
        response: tuple[int, bool] = (0, False)
        # trap user in dialog until they enter a valid value and click OK
        while waiting_for_valid_input:
            # response will be a tuple of the form (value, True/False} where True
            # means the OK button was preseed and False means the Cancel button was pressed
            response = QtWidgets.QInputDialog.getInt(parent, msg, title)
            # print(f'{response}=')
            if response[1]:
                waiting_for_valid_input = False

        n: int = response[0]
        app.closeAllWindows()
        app.exit()

        return n

    @staticmethod
    def get_decimal_number(title: str, msg: str, parent=None) -> Decimal:
        """return a decimal number as directed by the message"""
        app = QApplication(sys.argv)
        waiting_for_valid_input = True
        # trap user in dialog until they enter a valid value and click OK
        while waiting_for_valid_input:
            # response will be a tuple of the form (value, True/False} where True
            # means the OK button was pressed and False means the Cancel button was pressed
            min = 0
            max = decimal.MAX_EMAX
            decimals = sys.float_info.dig
            response = QtWidgets.QInputDialog.getDouble(parent, msg, title, 0, min, max,
                                                        decimals)  # print(f'{response}=')
            if response[1]:
                waiting_for_valid_input = False

        n: decimal = Decimal(response[0])
        app.closeAllWindows()
        app.exit()
        return n

    @staticmethod
    def get_floating_point_number(title: str, msg: str, parent=None) -> float:
        """return a floating-point number as directed by the message"""
        app = QApplication(sys.argv)
        waiting_for_valid_input = True
        # trap user in dialog until they enter a valid value and click OK
        while waiting_for_valid_input:
            # response will be a tuple of the form (value, True/False} where True
            # means the OK button was preseed and False means the Cancel button was pressed
            min = 0
            max = decimal.MAX_EMAX
            decimals = sys.float_info.dig
            response = QtWidgets.QInputDialog.getDouble(parent, msg, title, 0, min, max,
                                                        decimals)
            # print(f'{response}=')
            if response[1]:
                waiting_for_valid_input = False

        n: float = float(response[0])
        app.closeAllWindows()
        app.exit()
        return n

    @staticmethod
    def get_yesno_response(title: str, question: str, parent=None) -> bool:
        """get a yes/no (True/False) response to a question"""
        app = QApplication(sys.argv)

        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setInformativeText(question)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msgBox.setDefaultButton(QMessageBox.StandardButton.Yes)
        msgBox.setIcon(QMessageBox.Icon.Question)
        ret = msgBox.exec()

        app.closeAllWindows()
        app.exit()
        return ret == QMessageBox.StandardButton.Yes

    @staticmethod
    def get_single_choice(title: str, msg: str, choices: list[str], parent=None):
        """get a single choide from a list of choices"""
        app = QApplication(sys.argv)
        # flags
        # force user to choose one of the available choices before returning
        waiting_for_choice: bool = True
        while waiting_for_choice:
            item, resp = QtWidgets.QInputDialog.getItem(parent, title, msg, choices, 0, False, )
            # print(f'item={item}, resp={resp}')
            waiting_for_choice = not resp

        app.closeAllWindows()
        app.exit()
        app = None
        return item
