import numpy as np
import pytesseract
import time
from mss import mss


class Vision:
    def __init__(self):
        self.DEBUG = False
        self.img_left = None
        self.screen = mss()
        self.region = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}

    def get_screenshot(self):
        """
        Returns a screenshot of the current window/game.
        """
        last_time = time.time()
        img = np.array(self.screen.grab(self.region))
        if self.DEBUG:
            print('Loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
        return img

    def find_text(self, img):
        text = pytesseract.image_to_string(img)
        return text

    def find_word_coordinates(self, img, keyword):
        """
        Returns the coordinates of a word in an image.
        """
        data = pytesseract.image_to_data(img)

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
            print(words)

            # If the line is empty, skip it
            if len(words) == 0:
                continue
            
            # Get the word and its coordinates
            word = words[-1]

            left = words[left_index]
            top = words[top_index]

            # if the word is "run", then click the coordinates
            if word.lower() == keyword:
                return (int(left), int(top)) # x, y coordinates