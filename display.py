import cv2 as cv
import numpy as np
from waves import Wave
from time import time


def main():
    width = 50
    height = 50
    waves = [Wave(-1, 0, frequency=0.05, wavelength=15, amplitude=42),
             Wave(width, height, frequency=0.1, wavelength=6, amplitude=42),
             Wave(width//2, height//2, frequency=0.05, wavelength=10, amplitude=42)]


    for t in range(1000):
        img = np.full((width, height, 1), 128, dtype="uint8")
        start = time()
        for r in range(height):
            for c in range(width):
                for wave in waves:
                    img[r][c] = wave.next(r, c, -t) + img[r][c]

        cv.imshow("wave", cv.resize(img, (1000, 1000), interpolation=cv.INTER_NEAREST))
        print(time() - start)
        cv.waitKey(1)


if __name__ == '__main__':
    main()
