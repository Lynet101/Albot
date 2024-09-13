import cv2
import numpy as np

class Program():
    def __init__(self):
        self.path = '/home/slindau/Downloads/'
        self.name = input('Enter file name: ')
        self.img = cv2.imread(f'{self.path}{self.name}.png')
        hh, ww = img.shape[:2]
        self.main()
    
    def main():
        mask()
        morphology()
        # save results
        cv2.imwrite(f'{self.path}{self.name}.new.png', self.result)


    def mask():
        # threshold on white
        # Define lower and uppper limits
        lower = np.array([20, 20, 20])
        upper = np.array([255, 255, 255])

        # Create mask to only select black
        self.thresh = cv2.inRange(self.img, lower, upper)

    def morphology():
        # apply morphology
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20,20))
        morph = cv2.morphologyEx(self.thresh, cv2.MORPH_CLOSE, kernel)

        # invert morp image
        mask = 255 - morph

        # apply mask to image
        self.result = cv2.bitwise_and(self.img, self.img, mask=mask)




