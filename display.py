import cv2 as cv
import numpy as np
from waves import Wave


def main():
    width = 250
    height = 250
    wave = Wave(width//2, height//2, 0.05, 10)

    for t in range(1000):
        img = np.zeros((width, height, 1), dtype="uint8")
        for r in range(height):
            for c in range(width):
                img[r][c] = wave.next(r, c, -t)

        cv.imshow("wave", cv.resize(img, (1000, 1000), interpolation=cv.INTER_NEAREST))
        cv.waitKey(1)


if __name__ == '__main__':
    main()
