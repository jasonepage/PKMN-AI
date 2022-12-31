import pyautogui
from src.events import *
import json

def singles_hunt(hunt: str):
    """
    Performs a single encounter hunt. 
    """
    with open("location_data.json", 'r') as f:  # get location data
        location_data = json.load(f)

    # TODO: Print the correct json value
    # print(location_data[hunt][0].value())

    while True:
        run_button = pyautogui.locateCenterOnScreen('images/Events/run_button.PNG', confidence=0.8, region=(0,540, 960, 540))
        check_location = pyautogui.locateCenterOnScreen(f'images/Hunts/{hunt}.PNG', confidence=0.5)
        img_left = pyautogui.locateCenterOnScreen(f'images/Hunts/{hunt}.PNG', confidence=0.8, region=(1250, 0, 200, 1080))
        img_right = pyautogui.locateCenterOnScreen(f'images/Hunts/{hunt}.PNG', confidence=0.8, region=(960, 0, 200, 1080))

        # Run Away
        if run_button is not None:
            run_away(run_button)

        # Find Encounter
        elif check_location is not None:
            singles(img_left, img_right)
            
        # Wait
        else: 
            continue


def hordes_hunt(hunt: str):
    """
    Performs a horde encounter hunt. 
    """
    # TODO: Finish Hordes Hunt's Logic
    
    while True:
        run_button = pyautogui.locateCenterOnScreen('images/Events/run_button.PNG', confidence=0.8, region=(0,540, 960, 540))
        check_location = pyautogui.locateCenterOnScreen(f'images/Hunts/{hunt}.PNG', confidence=0.5)
        leppa_replenish = pyautogui.locateCenterOnScreen('images/Events/leppa_replenish.PNG', confidence=0.8)
        leppa_replenish2 = pyautogui.locateCenterOnScreen('images/Events/leppa_replenish2.PNG', confidence=0.8)

        if leppa_replenish or leppa_replenish2 is not None:
            replenish_leppa()

        elif leppa_replenish is None:

            # Run Away
            if run_button is not None:
                run_away(run_button)
                add_encounter(5)

            # Find Encounter
            elif check_location is not None:
                sweet_scent()
            
            # Wait
            else:
                continue
    

def fishing_hunt(hunt: str):
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
            run_away(run_button)
            add_encounter(1)

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
            continue


def hatch_eggs():

    # 
    return