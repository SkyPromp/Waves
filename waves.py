from math import sin
from math import pi
from math import sqrt


class Wave:
    def __init__(self, r, c, frequency=0.05, wavelength=100, amplitude=127):
        self.amplitude = amplitude
        self.r = r
        self.c = c
        self.frequency = frequency
        # self.max_distance = 0
        self.wavelength = wavelength
        self.shift = 0
        self.pi2length = 2 * pi / self.wavelength
        self.freqlength = self.frequency * self.wavelength

    # def __repr__(self):
    #     return f"{self.amplitude} * sin(2 * pi / {self.wavelength} * (x + {self.wavelength} * {self.frequency} * t) + {self.shift})"

    def next(self, r, c, time):
        dr = r - self.r
        dc = c - self.c
        return self.amplitude * sin(self.pi2length * (sqrt(dr * dr + dc * dc) + self.freqlength * time) + self.shift)

    # def getDist(self, r, c):
    #     dr = r - self.r
    #     dc = c - self.c
    #     return sqrt(dr * dr + dc * dc)

    # def isMaxDist(self, r, c):
    #     if self.getDist(r, c) == self.max_distance:
    #         self.max_distance += 1
    #         return True
    #     return False
