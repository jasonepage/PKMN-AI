import pyautogui
from events import *


def singles_hunt(hunt):
    while True:
        run_button = pyautogui.locateCenterOnScreen('images/Events/run_button2.PNG', confidence=0.8, region=(0,0, 750, 1500))
        if hunt is not None:
            check_location = pyautogui.locateCenterOnScreen(f'images\Hunts\{hunt}.PNG', confidence=0.5)

        # Run Away
        if run_button is not None:
            run_Away(run_button)

        # Hunt
        elif check_location is not None:
            petalburg_woods()
            
        # Wait
        else: 
            pass


def hordes_hunt(hunt):
    # TODO: Finish Horde Hunt's Logic
    icirrus_city()
    for i in range(6):
        # sweet_scent()

        run_button = None
        while run_button is None:
            run_button = pyautogui.locateCenterOnScreen('images/Events/run_button2.PNG', confidence=0.8)
        run_Away(run_button)


def fishing_hunt(hunt):
    while True:
        run_button = pyautogui.locateCenterOnScreen('images/Events/run_button2.PNG', confidence=0.8)
        check_location = pyautogui.locateCenterOnScreen(f'images\Hunts\{hunt}.PNG', confidence=0.5)
        nibble = pyautogui.locateCenterOnScreen('images/Events/nibble.PNG', confidence=0.8)
        landed = pyautogui.locateCenterOnScreen('images\Events\landed.PNG', confidence=0.8)

        # Run away
        if run_button is not None:
            run_Away(run_button)

        # Skip
        elif nibble is not None:
            skip_nibble()
        elif landed is not None:
            skip_landed()

        # Fish
        elif check_location is not None:
            fishing()

        # Wait
        else:
            pass
