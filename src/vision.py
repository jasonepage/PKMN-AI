import cv2
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


"""def main():
    font = cv2.FONT_HERSHEY_SIMPLEX
    vision = Vision()
    while True:
        screen = vision.CaptureImage((0, 40, 800, 640))
        data = vision.TextData(screen)

        # Calculate the coordinates for the text box
        text_x = 10
        text_y = 50
        
        # Display the text on the image
        cv2.putText(screen, data, (text_x, text_y), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
        
        cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            exit()
        
        time.sleep(0.05)


if __name__ == '__main__':
    main()
        """