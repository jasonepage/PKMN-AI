import cv2 as cv
import numpy as np
import pytesseract
from PIL import ImageGrab
import time

class Vision:
    def __init__(self):
        self.DEBUG = True
        self.img_left = None


    def TextFinder(self, img):
        """
        Finds text in an image.
        """
        text = pytesseract.image_to_string(img)
        return text


    def CaptureImage(self, dimensions: tuple):
        """
        Finds an image in an image.
        """
        last_time = time.time()
        screen = np.array(ImageGrab.grab(bbox=dimensions))
        print('Loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()

        if self.DEBUG:
            cv.imshow('window', cv.cvtColor(screen, cv.COLOR_BGR2RGB))
            if cv.waitKey(25) & 0xFF == ord('q'):
                cv.destroyAllWindows()
                exit()

def main():
    vision = Vision()
    while True:
        vision.CaptureImage((0, 40, 800, 640))


if __name__ == '__main__':
    main()
        

