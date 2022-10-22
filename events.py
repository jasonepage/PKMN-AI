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

    # Move cursor back to original position
    pyautogui.moveTo(current_posiiton)
    add_Encounter()  # Adds encounter to the counter
    sleep(1.25)  # Waits for animation to end


#### SINGLES ####
def petalburg_woods():
    pyautogui.keyDown('a')
    pyautogui.keyDown('d') 
    sleep(uniform(0.25, 0.5))
    pyautogui.keyUp('d')


def singles(img_left, img_right):
    if img_left is not None:
        pyautogui.keyDown('d') # Start moving right if user has reached furthest left point

    if img_right is not None: 
        pyautogui.keyUp('d') # Start moving left if user has reached furthest right point
        pyautogui.keyDown('a')


#### HORDES ####
def teleport():
    pyautogui.press('z')
    sleep(2)


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