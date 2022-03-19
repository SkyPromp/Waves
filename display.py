import cv2 as cv
import numpy as np
from waves import Wave
from time import time


def main():
    width = 45
    height = 45
    waves = [Wave(-1, 0, frequency=0.05, wavelength=15, amplitude=42),
             Wave(width, height, frequency=0.1, wavelength=6, amplitude=42),
             Wave(width//2, height//2, frequency=0.05, wavelength=10, amplitude=42)]

    for t in range(1000):
        start = time()
        img = np.full((height, width, 1), 128, dtype="uint8")
        for r in range(height):
            for c in range(width):
                for wave in waves:
                    img[r][c] = wave.next(r, c, -t) + img[r][c]

        print(time() - start)
        cv.imshow("wave", img)
        cv.waitKey(1)


if __name__ == '__main__':
    main()
