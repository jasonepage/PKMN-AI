import time, json, pyautogui
from utils import add_encounter
from vision import Vision
from bot_actions import Bot


def singles_hunt():
    """
    Performs a single encounter hunt. 
    """
    bot = Bot()
    vision = Vision()
    start_time = time.time()

    while True:
        screen = vision.get_screenshot()
        text = vision.find_text(screen)
        # img_left = pyautogui.locateCenterOnScreen(f'images/Hunts/{location}.PNG', confidence=0.8, region=(1250, 0, 200, 1080))
        # img_right = pyautogui.locateCenterOnScreen(f'images/Hunts/{location}.PNG', confidence=0.8, region=(960, 0, 200, 1080))

        # Run Away
        if 'run' in text.lower() or 'ru' in text.lower():
            # get the coordinates of the "run" text
            run_button = vision.find_word_coordinates(screen, 'run')
            pyautogui.click(run_button)
            add_encounter(1)
            
        # Wait
        else:
            elapsed_time = time.time() - start_time
            if elapsed_time > 1:
                bot.find_single_encounters(0.5) # img_left, img_right
                elapsed_time = 0
                start_time = time.time()


def hordes_hunt():
    """
    Performs a horde encounter hunt. 
    """
    bot = Bot()
    vision = Vision()
    start_time = time.time()

    while True:
        screen = vision.get_screenshot()
        text = vision.find_text(screen)

        # Run Away
        if 'run' in text.lower() or 'ru' in text.lower():
            # get the coordinates of the "run" text
            run_button = vision.find_word_coordinates(screen, 'run')
            pyautogui.click(run_button)
            add_encounter(5)
        
        # Sweet Scent
        elif 'sweet scent' in text.lower() or 'replenish' in text.lower() or 'pp' in text.lower():
            bot.skip_dialogue()
    
        else:      
            elapsed_time = time.time() - start_time
            if elapsed_time > 3:
                bot.sweet_scent()
                elapsed_time = 0
                start_time = time.time()
        

def fishing_hunt():
    """
    Performs a fishing encounter hunt. 
    """
    bot = Bot()
    vision = Vision()
    start_time = time.time()

    while True:
        screen = vision.get_screenshot()
        text = vision.find_text(screen)

        # Run Away
        if 'run' in text.lower() or 'ru' in text.lower():
            # get the coordinates of the "run" text
            run_button = vision.find_word_coordinates(screen, 'run')
            pyautogui.click(run_button)
            add_encounter(1)

        elif 'nibble' in text.lower() or 'landed' in text.lower():
            bot.skip_dialogue()

        # Wait
        else:
            # print(text)
            elapsed_time = time.time() - start_time
            if elapsed_time > 2:
                bot.use_fishingrod()
                elapsed_time = 0
                start_time = time.time()
        


# TODO: Add a function to hatch eggs
def hatch_eggs():
    pass