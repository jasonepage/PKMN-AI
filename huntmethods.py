import pyautogui
from events import *


def singles_hunt(hunt: str):
    """
    Performs a single encounter hunt. 
    """
    while True:
        run_button = pyautogui.locateCenterOnScreen('images/Events/run_button.PNG', confidence=0.8, region=(0,0, 750, 1500))
        check_location = pyautogui.locateCenterOnScreen(f'images\Hunts\{hunt}.PNG', confidence=0.5)
        img_left = pyautogui.locateCenterOnScreen(f'images\Hunts\{hunt}.PNG', confidence=0.8, region=(1250, 0, 200, 1080))
        img_right = pyautogui.locateCenterOnScreen(f'images\Hunts\{hunt}.PNG', confidence=0.9, region=(960, 0, 200, 1080))

        # Run Away
        if run_button is not None:
            run_Away(run_button)

        # Find Encounter
        elif check_location is not None:
            singles(img_left, img_right)
            
        # Wait
        else: 
            pass


def hordes_hunt(hunt):
    """
    Performs a horde encounter hunt. 
    """
    # TODO: Finish Horde Hunt's Logic
    icirrus_city()
    for i in range(6):
        # sweet_scent()

        run_button = None
        while run_button is None:
            run_button = pyautogui.locateCenterOnScreen('images/Events/run_button.PNG', confidence=0.8)
        run_Away(run_button)


def fishing_hunt(hunt):
    """
    Performs a fishing encounter hunt. 
    """
    while True:
        run_button = pyautogui.locateCenterOnScreen('images/Events/run_button.PNG', confidence=0.8)
        check_location = pyautogui.locateCenterOnScreen(f'images\Hunts\{hunt}.PNG', confidence=0.5)
        nibble = pyautogui.locateCenterOnScreen('images/Events/fishing/nibble.PNG', confidence=0.8)
        landed = pyautogui.locateCenterOnScreen('images/Events/fishing/landed.PNG', confidence=0.8)

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
