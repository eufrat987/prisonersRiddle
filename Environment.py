import random

from Prisoner import Prisoner
from Box import Box
from Room import Room

class Env:
    def __init__(self, numberOfPrisoners, numberOfChanses):
        self.numberOfPrisoners = numberOfPrisoners
        self.numberOfChanses = numberOfChanses
        self.__generate()
        self.room = Room(self.boxes)

    def __generate(self):
        self.allPrisoners = []
        self.boxes = []
        self.__populateList(self.allPrisoners, Prisoner)
        self.__populateList(self.boxes, Box)

    def setPrisonersStrategy(self, Strategy):
        for prisoner in self.allPrisoners:
            prisoner.setStrategy(Strategy(prisoner))

    def __populateList(self, list, getObject):
        allNumbers = [i for i in range(1, self.numberOfPrisoners + 1)]
        while len(allNumbers) > 0:
            pickedUp = False
            while not pickedUp:
                randomNumber = random.randint(1, self.numberOfPrisoners + 1)
                try:
                    allNumbers.remove(randomNumber)
                    pickedUp = True
                except ValueError:
                    pass
            list.append(getObject(randomNumber))