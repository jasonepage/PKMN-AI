import sys
import pyautogui
from events import BotActions
from huntmethods import singles_hunt, hordes_hunt, fishing_hunt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi('threads.ui', self)
        self.resize(800, 600)
        # add icon

        self.thread = {}
        self.pushButton.clicked.connect(self.start_worker_1)
        self.pushButton_2.clicked.connect(self.start_worker_2)
        
        self.pushButton_3.clicked.connect(self.stop_worker_1)
        self.pushButton_4.clicked.connect(self.stop_worker_2)

    def start_worker_1(self):
        self.thread[1] = ThreadClass(parent=None, index=1)
        self.thread[1].start()
        self.thread[1].any_signal.connect(self.checkForEncounter('singles', 'petalburg_woods'))
        self.pushButton.setEnabled(False)

    def start_worker_2(self):
        self.thread[2] = ThreadClass(parent=None, index=2)
        self.thread[2].start()
        self.thread[2].any_signal.connect(self.checkForWarnings)
        self.pushButton_2.setEnabled(False)

    def stop_worker_1(self):
        self.thread[1].stop()
        self.pushButton.setEnabled(True)

    def stop_worker_2(self):
        self.thread[2].stop()
        self.pushButton_2.setEnabled(True)

    def checkForWarnings(self):
        """
        Checks for any warnings that appear on the screen. Ex: Shiny, Disconnect, Captcha
        """  
        while True:
            captcha_warning = pyautogui.locateCenterOnScreen('images/Events/captcha_warning.PNG', confidence=0.8)
            disconnect_warning = pyautogui.locateCenterOnScreen('images/Events/disconnect_warning.PNG', confidence=0.8)
            shiny_warning = pyautogui.locateCenterOnScreen('images/Events/shiny_warning.PNG', confidence=0.8)

            # Send an alert
            print('Checking for warnings...')
            if captcha_warning or disconnect_warning or shiny_warning is not None:
                print("Warning Detected.")
                BotActions.warning()

    def checkForEncounter(self, method: str, hunt: str):
        """
        Performs BOT actions.
        """
        valid_methods = ['singles', 'hordes', 'fishing' ]
        if method not in valid_methods:
            raise ValueError("Invalid Method.")

        valid_hunts = ['petalburg_woods', 'route230', 'route119', 'driftveil_city', ]
        if hunt not in valid_hunts:
            raise ValueError("Invalid Hunt.")

        if method == 'singles':
            singles_hunt(hunt)

        elif method == 'hordes':
            hordes_hunt(hunt)

        elif method == 'fishing': 
            fishing_hunt(hunt)
       


class ThreadClass(QtCore.QThread):
    any_signal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None, index=0):
        super(ThreadClass, self).__init__(parent)
        self.index = index
        self.is_running = True

    def run(self):
        print("Thread {} started".format(self.index))
        # self.checkForEncounter('singles', 'petalburg_woods')
        #self.checkForWarnings()

    def stop(self):
        self.is_running = False
        print("Thread {} stopped".format(self.index))
        self.terminate()

    def checkForWarnings(self):
        """
        Checks for any warnings that appear on the screen. Ex: Shiny, Disconnect, Captcha
        """  
        while True:
            captcha_warning = pyautogui.locateCenterOnScreen('images/Events/captcha_warning.PNG', confidence=0.8)
            disconnect_warning = pyautogui.locateCenterOnScreen('images/Events/disconnect_warning.PNG', confidence=0.8)
            shiny_warning = pyautogui.locateCenterOnScreen('images/Events/shiny_warning.PNG', confidence=0.8)

            # Send an alert
            print('Checking for warnings...')
            if captcha_warning or disconnect_warning or shiny_warning is not None:
                print("Warning Detected.")
                BotActions.warning()

    def checkForEncounter(self, method: str, hunt: str):
        """
        Performs BOT actions.
        """
        valid_methods = ['singles', 'hordes', 'fishing' ]
        if method not in valid_methods:
            raise ValueError("Invalid Method.")

        valid_hunts = ['petalburg_woods', 'route230', 'route119', 'driftveil_city', ]
        if hunt not in valid_hunts:
            raise ValueError("Invalid Hunt.")

        if method == 'singles':
            singles_hunt(hunt)

        elif method == 'hordes':
            hordes_hunt(hunt)

        elif method == 'fishing': 
            fishing_hunt(hunt)
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
