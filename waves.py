from math import sin
from math import pi


class Wave:
    def __init__(self, r, c, frequency, wavelength=100, amplitude=127):
        self.amplitude = amplitude
        self.r = r
        self.c = c
        self.frequency = frequency
        # self.max_distance = 0
        self.wavelength = wavelength
        self.shift = 0

    # def __repr__(self):
    #     return f"{self.amplitude} * sin(2 * pi / {self.wavelength} * (x + {self.wavelength} * {self.frequency} * t) + {self.shift})"

    def next(self, r, c, time):
        return 128 + self.amplitude * \
               sin(
                   (2 * pi / self.wavelength) * (self.getDist(r, c) + self.wavelength * self.frequency * time) + self.shift
               )

    def getDist(self, r, c):
        return ((r - self.r) ** 2 + (c - self.c) ** 2) ** 0.5

    # def isMaxDist(self, r, c):
    #     if self.getDist(r, c) == self.max_distance:
    #         self.max_distance += 1
    #         return True
    #     return False
