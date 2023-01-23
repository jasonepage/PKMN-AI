from utils import send_warning, add_encounter
from vision import Vision
from bot_actions import Bot

import cv2, time, json, pyautogui
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5 import uic


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi('PKMN-AI.ui', self)
        self.setWindowIcon(QtGui.QIcon('images\gui\icon.png'))
        self.setWindowTitle('PKMN-AI Bot')

        # Initialize start/stop buttons
        self.thread = {}
        self.start_bot.clicked.connect(self.start_worker_1)
        self.start_warnings.clicked.connect(self.start_worker_2)
        self.pause_bot.clicked.connect(self.stop_worker_1)
        self.pause_warnings.clicked.connect(self.stop_worker_2)

        # Set the initial encounters equal to encounters1.json
        with open('encounters/encounters1.json', 'r') as f:
            encounters = json.load(f)
        self.encounters.setText('Encounters: ' + str(encounters['encounters']))

        # Add available hunts to selection combobox
        for hunt in ['singles', 'hordes', 'fishing']: # TODO: read a file to get single encounter hunts
            self.hunts.addItem(hunt)

    def start_worker_1(self):
        hunt = self.hunts.currentText() # get hunt from hunts combobox
        self.thread[1] = ThreadClass(parent=None, index=1, hunt=hunt)
        self.thread[1].start()
        self.thread[1].any_signal.connect(self.my_function)
        self.start_bot.setEnabled(False)

    def start_worker_2(self):
        self.thread[2] = ThreadClass(parent=None, index=2)
        self.thread[2].start()
        self.thread[2].any_signal.connect(self.my_function)
        self.start_warnings.setEnabled(False)

    def stop_worker_1(self):
        self.thread[1].stop()
        self.start_bot.setEnabled(True)

    def stop_worker_2(self):
        self.thread[2].stop()
        self.start_warnings.setEnabled(True)

    def my_function(self):
        print('Starting threaded function.')
       

class ThreadClass(QtCore.QThread):
    any_signal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None, index=0, hunt=''):
        super(ThreadClass, self).__init__(parent)
        self.DEBUG = False
        self.index = index
        self.is_running = True
        self.hunt_method = hunt
        self.timer = 60
        self.battle_action = 'run'

    def run(self):
        print("Thread {} started".format(self.index))
        if self.index == 1:
            self.find_encounters()
        elif self.index == 2:
            self.checkForWarnings()
        
    def stop(self):
        self.is_running = False
        print("Thread {} stopped".format(self.index))
        self.terminate()

    def checkForWarnings(self):
        """
        Checks for any warnings that appear on the screen. Ex: Shiny, Disconnect, Captcha
        Ran on a separate thread to prevent the bot from stopping.
        """ 
        vision = Vision()

        while (True):
            screen = vision.get_screenshot()
            text = vision.find_text(screen).lower()

            # Send an alert
            if 'captcha' in text or 'shiny' in text or 'disconnected' in text:
                print("Warning Detected.")
                send_warning()
            else:
                print("No Warnings Detected.")

            # Displays the DEBUG Window
            if self.DEBUG: 
                cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    exit()

    def find_encounters(self):
        """
        Performs BOT actions.
        Ran on a separate thread to prevent the BOT from getting stuck.
        """
        bot = Bot()
        vision = Vision()
        start_time = time.time()
        last_run_button = time.time()
        BOT_STATE = 'HUNTING' # 'HUNTING' or 'IN_BATTLE'

        while (time.time() - start_time) < (self.timer * 60): # while the timer hasn't expired
            screen = vision.get_screenshot()
            screen = cv2.resize(screen, (0,0), fx=0.5, fy=0.5)
            text = vision.find_text(screen)

            if self.battle_action == 'run' and 'run' in text.lower():
                print('Running Away...')
                run_button = vision.find_word_coordinates(screen, 'run')
                pyautogui.click(run_button)
                add_encounter(1)
            if self.battle_action == 'fight' and 'fight' in text.lower():
                fight_button = vision.find_word_coordinates(screen, 'fight')
                pyautogui.click(fight_button)
                time.sleep(0.5)
                pyautogui.click(fight_button) # Click the first attacking move
            if 'nibble' in text.lower() or 'sweet scent' in text.lower() or 'pp' in text.lower() or 'replenish' in text.lower() or 'landed' in text.lower() or 'another' in text.lower():
                bot.skip_dialogue()


            if time.time() - last_run_button > 15:
                cv2.imwrite('error.PNG', screen)
                print(text)

            elapsed_time = time.time() - start_time
            screen = None
            if elapsed_time > 2 and BOT_STATE == 'HUNTING':
                if self.hunt_method == 'singles':
                    bot.find_single_encounters(0.5)
                elif self.hunt_method == 'hordes':
                    bot.sweet_scent()
                elif self.hunt_method == 'fishing':
                    bot.use_fishingrod()              
                elapsed_time = 0
                start_time = time.time()

        print("Timer Expired.")
            