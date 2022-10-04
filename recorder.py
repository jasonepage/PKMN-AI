from pynput import keyboard
from time import time

# Reminder to global start_time when you want to access it/modifiy it
start_time = None 
# Create a list of unreleased keys to prevent multiple packets from being sent while holding a key
unreleased_keys = []
# storing all input events
input_events = []


def main():
    runListeners()


def elapsed_time():
    global start_time
    return time() - start_time


def on_press(key):
    # 
    global unreleased_keys
    if key in unreleased_keys:
        return 
    else:
        unreleased_keys.append(key)

    try:
        print('alphanumeric key {} pressed at {}'.format(key.char, elapsed_time()))
    except AttributeError:
        print('special key {} pressed at {}'.format(key, elapsed_time()))


def on_release(key):
    print('{} released at {}'.format(key, elapsed_time()))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


def runListeners():

    # collect keyboard
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        global start_time
        start_time = time()
        listener.join()


# Run Program
if __name__ == '__main__':
    main()