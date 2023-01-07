from types import NoneType
import pyautogui
import pyscreeze
from replay.playback import playActions
from time import sleep


class BotState:
    def __init__(self):
        pass


class Bot:
    def __init__(self):
        pass

    def run_away(self, button: tuple):
        """
        Receives Run Button Coordinates and clicks the coordinates.
        Moves the user's cursor to the run button coordinates for a split seconds and moves it back.
        """
        print('Running Away...')
        current_posiiton = pyautogui.position()
        pyautogui.click(button)
        sleep(0.5)
        pyautogui.moveTo(current_posiiton)


    #### SINGLES ACTIONS ####
    def find_encounter(self, img_left: NoneType or pyscreeze.Point, img_right: NoneType or pyscreeze.Point):
        """
        Moves the player to the left or right depending on their position in game.
        """
        if img_left is not None:
            pyautogui.keyDown('d') # Start moving right if user has reached furthest left point

        if img_right is not None: 
            pyautogui.keyUp('d') # Start moving left if user has reached furthest right point
            pyautogui.keyDown('a')


    #### HORDES ACTIONS ####
    def teleport(self):
        print('Teleporting...')
        pyautogui.press('z')
        sleep(2)


    def sweet_scent(self):
        print('Using Sweet Scent...')
        pyautogui.press('x')


    def replenish_leppa(self):
        print('Replenishing Leppa Berries...')
        pyautogui.press('e')


    #### FISHING ACTIONS ####
    def use_fishingrod(self):
        print('Using Fishing Rod...')
        pyautogui.press('f')
        sleep(0.5)
        

    def skip_nibble(self):
        print('Skipping Nibble Dialogue...')
        pyautogui.press('e')
        

    def skip_landed(self):
        print('Skipping Landed Dialogue...')
        pyautogui.press('e')
        sleep(3)