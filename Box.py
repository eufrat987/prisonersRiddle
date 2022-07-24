class Box:
    def __init__(self, numberInside):
        self.numberInside = numberInside
        self.isClosed = True
        self.boxNumber = None

    def openBoxAndGetNumber(self):
        self.isClosed = False
        # print('open box: ', self.numberInside)
        return self.numberInside