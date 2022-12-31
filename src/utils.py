import json
from twilio.rest import Client
import pyautogui


def add_encounter(amount: int):
    """
    Adds n amount of encounters to the existing count of encounters.
    """
    with open("encounters_data/encounters4.json", 'r') as f:  # open encounter json profile to get current encounters
        data = json.load(f)

    data['encounters'] += amount  # add encounter

    with open("encounters_data/encounters4.json", "w") as f:  # update encounter json profile with additional encounters
        json.dump(data, f)
    return


def record_OBS():
    """
    Captures a OBS Replay Buffer Clip by pressing Alt+S when Replay Buffer is enabled.
    """
    # OBS Replay Buffer (enabled)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('s')
    return


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
    return