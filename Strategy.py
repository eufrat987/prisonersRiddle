import random

class RandomStrategy:
    def __init__(self, prisoner):
        pass

    def getChoice(self, availableToChoose):
        return random.choice(availableToChoose)


class LoopStrategy:
    def __init__(self, prisoner):
        self.toChoose = prisoner.numberOfPrisoner

    def getChoice(self, availableToChoose):
        for box in availableToChoose:
            if box.boxNumber == self.toChoose:
                self.toChoose = box.numberInside
                return box
        return None