import json
from time import sleep
from twilio.rest import Client
import pyautogui
import win32gui


def enum_callback1(hwnd, window_list):
    window_list.append((hwnd, win32gui.GetWindowText(hwnd)))


def enum_callback(hwnd, window_list):
    window_list.append(hwnd)


def find_window(title):
    window_list = []
    win32gui.EnumWindows(enum_callback, window_list)
    for hwnd in window_list:
        if win32gui.GetWindowText(hwnd) == title:
            return hwnd
    return None


def find_windows():
    window_list = []
    win32gui.EnumWindows(enum_callback1, window_list)
    return window_list


def get_window_dimensions(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    left = rect[0]
    top = rect[1]
    width = rect[2] - left
    height = rect[3] - top
    return left, top, width, height


def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # https://pyautogui.readthedocs.io/en/latest/introduction.html
    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
    pyautogui.FAILSAFE = True


def countdownTimer(seconds: int):
    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, seconds):
        print(".", end="", flush=True)
        sleep(1)
    print("Go")


def send_warning():
    """
    Messages the user, captures Replay Buffer clip, and exits the script.
    """
    notify_user()  # Send a text/call
    record_OBS()  # Capture clip
    exit()


def add_encounter(amount: int):
    """
    Adds n amount of encounters to the existing count of encounters.
    """
    with open("encounters/encounters1.json", 'r') as f:  # open encounter json profile to get current encounters
        data = json.load(f)

    data['encounters'] += amount  # add encounter

    with open("encounters/encounters1.json", "w") as f:  # update encounter json profile with additional encounters
        json.dump(data, f)


def record_OBS():
    """
    Captures a OBS Replay Buffer Clip by pressing Alt+S when Replay Buffer is enabled.
    """
    # OBS Replay Buffer (enabled)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('s')


def notify_user():
    """
    Uses Twilio to message and call the user to notify them that a warning message has appeared.
    """
    with open('TwilioConfig.json', 'r') as credentials:
        config = json.load(credentials)
    client = Client(config["accountSID"], config["authToken"])
    myTwilioNumber = config["myTwilioNumber"]
    myCellPhone = config["myCellPhone"]

    # TODO: Add an image of the screen in the message and customize the text in the message. 
    notification = "A warning has been found!"  # maybe add the screenshot of your screen to the text message?
    message = client.messages.create(to=myCellPhone,
                                     from_=myTwilioNumber,
                                     body=notification)

    call = client.calls.create(to=myCellPhone,
                               from_=myTwilioNumber,
                               url="http://demo.twilio.com/docs/voice.xml")


if __name__ == "__main__":
    print(find_windows())
    hwnd = find_window("РokеMМO")
    print(hwnd)