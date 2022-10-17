import pyautogui
from multiprocessing import Process
from playback import initializePyAutoGUI, countdownTimer
from events import warning
from huntmethods import singles_hunt, hordes_hunt, fishing_hunt


def main():
    countdownTimer()
    initializePyAutoGUI()
    p1 = Process(target=checkForWarnings)
    p1.start()
    p2 = Process(target=checkForEncounter(0, 'route230'))
    p2.start()


def checkForWarnings():
    while True:
        captcha_warning = pyautogui.locateCenterOnScreen('images\Events\pop_up.PNG', confidence=0.8)
        disconnect_warning = pyautogui.locateCenterOnScreen('images\Events\pop_up.PNG', confidence=0.8)
        shiny_warning = pyautogui.locateCenterOnScreen('images\Events\pop_up.PNG', confidence=0.8)

        # Send an alert
        if captcha_warning or disconnect_warning or shiny_warning is not None:
            warning()


def checkForEncounter(method, hunt= None):
    if method == 0:
        singles_hunt(hunt)

    elif method == 1:
        hordes_hunt(hunt)

    elif method == 2: 
        fishing_hunt(hunt)


if __name__ == '__main__':
    main()
