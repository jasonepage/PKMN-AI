import pyautogui, time
from utils import add_encounter, get_window_dimensions, find_window
from vision import Vision
from bot_actions import Bot
import json


def singles_hunt(location: str):
    """
    Performs a single encounter hunt. 
    """
    bot = Bot()
    vision = Vision()
    with open("location_data.json", 'r') as f:  # get location data
        location_data = json.load(f)
    # TODO: Print the correct image coordinates

    while True:
        run_button = pyautogui.locateCenterOnScreen('images/Events/run_button.PNG', confidence=0.8, region=(0,540, 960, 540))
        check_location = pyautogui.locateCenterOnScreen(f'images/location/{location}.PNG', confidence=0.5)
        img_left = pyautogui.locateCenterOnScreen(f'images/Hunts/{location}.PNG', confidence=0.8, region=(1250, 0, 200, 1080))
        img_right = pyautogui.locateCenterOnScreen(f'images/Hunts/{location}.PNG', confidence=0.8, region=(960, 0, 200, 1080))

        # Run Away
        if run_button is not None:
            bot.run_away(run_button)
            add_encounter(1)
            
        # Find Encounter
        elif check_location is not None:
            bot.find_encounter(img_left, img_right)
            
        # Wait
        else:
            print('No checkpoint location found.')
            continue


def hordes_hunt(location: str):
    """
    Performs a horde encounter hunt. 
    """
    bot = Bot()
    vision = Vision()
    while True:
        check_location = pyautogui.locateCenterOnScreen(f'images/Hunts/{location}.PNG', confidence=0.8)
        pokeMMO = get_window_dimensions(find_window("РokеMМO"))
        screen = vision.CaptureImage(pokeMMO)
        data = vision.TextData(screen)

        # Split the data into lines
        lines = data.split('\n')

        # Extract the header row from the lines
        header = lines[0].split()

        # Find the index of the "left" and "top" columns
        left_index = header.index('left')
        top_index = header.index('top')

        # Iterate through the lines
        for line in lines[1:]:
            # Split the line into words
            words = line.split()
            
            # If the line is empty, skip it
            if len(words) == 0:
                continue
            
            # Get the word and its coordinates
            word = words[-1]
            # if the word isn't run, or sweet, or replenish, then skip it
            if word.lower() != 'run' and word.lower() != 'sweet' and word.lower() != 'replenish':
                continue

            left = words[left_index]
            top = words[top_index]

            # if the word is "run", then click the coordinates
            if word.lower() == 'run':
                bot.run_away((int(left), int(top)))
                add_encounter(1)

            # if the dialogue has "PP" or "Replenish", then press "E"
            if word.lower() == 'sweet' or word.lower() == 'replenish':
                print(word, 'leppa')
                bot.replenish_leppa()
            
        # Wait
        else:
            time.sleep(0.5)
            print('No checkpoint location found.')
            continue
        

def fishing_hunt(location: str):
    """
    Performs a fishing encounter hunt. 
    """
    bot = Bot()
    vision = Vision()
    while True:
        run_button = pyautogui.locateCenterOnScreen('images/Events/run_button.PNG', confidence=0.8)
        check_location = pyautogui.locateCenterOnScreen(f'images/Hunts/{location}.PNG', confidence=0.5)
        nibble = pyautogui.locateCenterOnScreen('images/Events/fishing/nibble.PNG', confidence=0.8)
        landed = pyautogui.locateCenterOnScreen('images/Events/fishing/landed.PNG', confidence=0.8)

        # Run away
        if run_button is not None:
            bot.run_away(run_button)
            add_encounter(1)

        # Skip
        elif nibble is not None:
            bot.skip_nibble()
        elif landed is not None:
            bot.skip_landed()

        # Fish
        elif check_location is not None:
            bot.use_fishingrod()
    
        # Wait
        else:
            print('No checkpoint location found.')
            continue


# TODO: Add a function to hatch eggs
def hatch_eggs():
    pass