import pyautogui
from multiprocessing import Process
from playback import initializePyAutoGUI, countdownTimer
from events import BotActions
from huntmethods import singles_hunt, hordes_hunt, fishing_hunt


def checkForWarnings():
    """
    Checks for any warnings that appear on the screen. Ex: Shiny, Disconnect, Captcha
    """
    
    while True:
        captcha_warning = pyautogui.locateCenterOnScreen('images/Events/captcha_warning.PNG', confidence=0.8)
        disconnect_warning = pyautogui.locateCenterOnScreen('images/Events/disconnect_warning.PNG', confidence=0.8)
        shiny_warning = pyautogui.locateCenterOnScreen('images/Events/shiny_warning.PNG', confidence=0.8)

        # Send an alert
        if captcha_warning or disconnect_warning or shiny_warning is not None:
            print("Warning Detected.")
            BotActions.warning()


def checkForEncounter(method: str, hunt: str):
    """
    Performs BOT actions.
    """
    valid_methods = ['singles', 'hordes', 'fishing' ]
    if method not in valid_methods:
        raise ValueError("Invalid Method.")

    valid_hunts = ['petalburg_woods', 'route230', 'route119', 'driftveil_city', ]
    if hunt not in valid_hunts:
        raise ValueError("Invalid Hunt.")


    if method == 'singles':
        singles_hunt(hunt)

    elif method == 'hordes':
        hordes_hunt(hunt)

    elif method == 'fishing': 
        fishing_hunt(hunt)


def main():
    countdownTimer(3)
    initializePyAutoGUI()
    p1 = Process(target=checkForWarnings)
    p1.start()
    p2 = Process(target=checkForEncounter('hordes', 'driftveil_city'))
    p2.start()


if __name__ == '__main__':
    main()
    # pyautogui.displayMousePosition()