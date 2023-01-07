import numpy as np
import pytesseract
from PIL import ImageGrab
import time


class Vision:
    def __init__(self):
        self.DEBUG = False
        self.img_left = None

    def TextFinder(self, img):
        text = pytesseract.image_to_string(img)
        return text
    
    def TextData(self, img):
        """
        Returns the text and the coordinates of the text in an image.
        """
        data = pytesseract.image_to_data(img)
        return data

    def CaptureImage(self, dimensions: tuple):
        """
        Returns a screenshot of the current window/game.
        """
        last_time = time.time()
        screen = np.array(ImageGrab.grab(bbox=dimensions))
        if self.DEBUG:
            print('Loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
        return screen

    def WordCoordinates(self, data):
        """
        Returns the x, y coordinates of a word from TextData.
        """
        x = data.split()[6]
        y = data.split()[7]
        return x, y
