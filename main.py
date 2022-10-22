import pyautogui
from multiprocessing import Process
from playback import initializePyAutoGUI, countdownTimer
from events import warning
from huntmethods import singles_hunt, hordes_hunt, fishing_hunt


def main():
    countdownTimer(3)
    initializePyAutoGUI()
    p1 = Process(target=checkForWarnings)
    p1.start()
    p2 = Process(target=checkForEncounter('singles', 'petalburg_woods'))
    p2.start()


def checkForWarnings():
    """
    Checks for any warnings that appear on the screen. Ex: Shiny, Disconnect, Captcha
    """
    while True:
        captcha_warning = pyautogui.locateCenterOnScreen('images\Events\pop_up.PNG', confidence=0.8)
        disconnect_warning = pyautogui.locateCenterOnScreen('images\Events\pop_up.PNG', confidence=0.8)
        shiny_warning = pyautogui.locateCenterOnScreen('images\Events\pop_up.PNG', confidence=0.8)

        # Send an alert
        if captcha_warning or disconnect_warning or shiny_warning is not None:
            print("Warning Detected.")
            warning()


def checkForEncounter(method: str, hunt: str):
    """
    Performs BOT actions.
    """
    valid_methods = ['singles', 'horde', 'fishing' ]
    if method not in valid_methods:
        raise ValueError("Invalid Method.")

    valid_hunts = ['petalburg_woods', 'route230', 'route119', ] # TODO: add more
    if hunt not in valid_hunts:
        raise ValueError("Invalid Hunt.")


    if method == 'singles':
        singles_hunt(hunt)

    elif method == 'hordes':
        hordes_hunt(hunt)

    elif method == 'fishing': 
        fishing_hunt(hunt)


if __name__ == '__main__':
    main()
    # pyautogui.displayMousePosition()
