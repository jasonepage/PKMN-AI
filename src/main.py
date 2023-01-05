from menu import Ui_MainWindow as MainWindow
from utils import initializePyAutoGUI

import sys
from PyQt5.QtWidgets import QApplication


def main():
    initializePyAutoGUI() 
    print('FAIL-SAFE turned on... Main processes starting!')

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    # pyautogui.displayMousePosition()
