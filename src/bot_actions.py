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

    #### SINGLES ACTIONS ####
    def find_single_encounter(self, img_left: NoneType or pyscreeze.Point, img_right: NoneType or pyscreeze.Point):
        """
        Moves the player to the left or right depending on their position in game.
        """
        print('Finding Single Encounters...')
        if img_left is not None:
            pyautogui.keyDown('d') # Start moving right if user has reached furthest left point

        if img_right is not None: 
            pyautogui.keyUp('d') # Start moving left if user has reached furthest right point
            pyautogui.keyDown('a')


    def find_single_encounters(self, seconds: float):
        """
        Moves the player to the left or right depending on their position in game.
        """
        print('Finding Single Encounters...')
        # press 'd' for seconds seconds
        pyautogui.keyDown('d')
        sleep(seconds)
        pyautogui.keyUp('d')

        pyautogui.keyDown('a')
        sleep(seconds)
        pyautogui.keyUp('a')


    #### HORDES ACTIONS ####
    def teleport(self):
        print('Teleporting...')
        pyautogui.press('z')


    def sweet_scent(self):
        print('Using Sweet Scent...')
        pyautogui.press('x')


    def skip_dialogue(self):
        print('Skipping Dialogue...')
        pyautogui.press('e')


    #### FISHING ACTIONS ####
    def use_fishingrod(self):
        print('Using Fishing Rod...')
        pyautogui.press('f')
