import pyautogui
from utils import add_Encounter, record_OBS, notify_user
from playback import playActions
from time import sleep
from random import uniform


def warning():
    notify_user()  # Send a text/call
    record_OBS()  # Capture clip
    exit()


def run_Away(button):
    current_posiiton = pyautogui.position()
    pyautogui.click(button)  # Clicks run button
    sleep(0.1)
    pyautogui.moveTo(current_posiiton)
    add_Encounter()  # Adds encounter to the counter
    sleep(1.25)  # Waits for animation to end
    return


#### SINGLES ####
def petalburg_woods():
    # Run left for a few steps
    pyautogui.keyDown('a')
    sleep(uniform(0.25, 0.5))
    pyautogui.keyUp('a')
    # Run right for a few steps
    pyautogui.keyDown('d')
    sleep(uniform(0.25, 0.5))
    pyautogui.keyUp('d')
    return


def route216():
    # Run left for a few steps
    pyautogui.keyDown('a')
    sleep(uniform(0.25, 0.5))
    pyautogui.keyUp('a')
    # Run right for a few steps
    pyautogui.keyDown('d')
    sleep(uniform(0.25, 0.5))
    pyautogui.keyUp('d')
    return


#### HORDES ####
def teleport():
    pyautogui.press('z')
    # TODO: Sleep
    return


def heal_unova():
    playActions('recordings\pokecenter_unova.json')
    pokecenter_unova = None
    # TODO: set a time limit before catches an error
    while pokecenter_unova == None:
        pokecenter_unova = pyautogui.locateCenterOnScreen('images/Events/pokecenter_unova.PNG', confidence=0.8)


def icirrus_city():
    teleport()
    heal_unova() # Heal
    playActions('recordings\DRAGONSPRIAL.json') # Get into position
    return


# TODO: Add more Horde Replays


#### FISHING ####
def fishing():
    pyautogui.press('f')
    sleep(0.5)
    return


def skip_nibble():
    pyautogui.press('e')
    return


def skip_landed():
    pyautogui.press('e')
    sleep(3)
    return