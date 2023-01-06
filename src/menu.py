from utils import send_warning
from huntmethods import singles_hunt, hordes_hunt, fishing_hunt
from vision import Vision

import cv2, time
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5 import uic


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi('threads.ui', self)
        # self.resize(600, 300)
        # add icon
        self.setWindowIcon(QtGui.QIcon('images\gui\icon.png'))
        # set title
        self.setWindowTitle('PKMN-AI Bot')

        # Initialize start/stop buttons
        self.thread = {}
        self.start_bot.clicked.connect(self.start_worker_1)
        self.start_warnings.clicked.connect(self.start_worker_2)
        self.pause_bot.clicked.connect(self.stop_worker_1)
        self.pause_warnings.clicked.connect(self.stop_worker_2)

        # Add available locations to combobox
        for location in ['driftveil_city', 'petalburg_woods', 'route230', 'route119']: # TODO: read a file to get locations
            self.locations.addItem(location)

    def start_worker_1(self):
        location = self.locations.currentText() # get location from locations combobox
        self.thread[1] = ThreadClass(parent=None, index=1, location=location)
        self.thread[1].start()
        self.thread[1].any_signal.connect(self.my_funciton)
        self.start_bot.setEnabled(False)

    def start_worker_2(self):
        self.thread[2] = ThreadClass(parent=None, index=2)
        self.thread[2].start()
        self.thread[2].any_signal.connect(self.my_funciton)
        self.start_warnings.setEnabled(False)

    def stop_worker_1(self):
        self.thread[1].stop()
        self.start_bot.setEnabled(True)

    def stop_worker_2(self):
        self.thread[2].stop()
        self.start_warnings.setEnabled(True)

    def my_funciton(self):
        print('Starting my function')
       

class ThreadClass(QtCore.QThread):
    any_signal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None, index=0, location=''):
        super(ThreadClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        self.location = location

    def run(self):
        print("Thread {} started".format(self.index))
        if self.index == 1:
            self.checkForEncounter(self.location)
        elif self.index == 2:
            self.checkForWarnings()
        
    def stop(self):
        self.is_running = False
        print("Thread {} stopped".format(self.index))
        self.terminate()

    def checkForWarnings(self):
        """
        Checks for any warnings that appear on the screen. Ex: Shiny, Disconnect, Captcha
        """ 
        vision = Vision()
        while (True):
            screen = vision.CaptureImage((0, 40, 800, 640)) # TODO: make this dynamic
            text = vision.TextFinder(screen).lower()
            time.sleep(0.5)

            # Send an alert
            if 'captcha' in text or 'shiny' in text or 'disconnected' in text:
                print("Warning Detected.")
                send_warning()
            print("No Warnings Detected.")

            if (True): 
                continue
                cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    exit()

    def checkForEncounter(self, location: str):
        """
        Performs BOT actions.
        """
        singles_locations = ['petalburg_woods', 'route230', 'route119']

        hordes_locations = ['driftveil_city']

        fishing_locations = []

        if location in singles_locations:
            singles_hunt(location)

        elif location in hordes_locations:
            hordes_hunt(location)

        elif location in fishing_locations: 
            fishing_hunt(location)

        else:
            raise ValueError("Invalid Hunt. Please select a hunt.")
