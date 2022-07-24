import copy

class Room:
    def __init__(self, boxes):
        self.boxesCopy = boxes
        self.indexBoxes()
        self.cleanUpRoom()

    def indexBoxes(self):
        for idx, box in enumerate(self.boxesCopy):
            box.boxNumber = idx + 1

    ## func used by game/env
    def cleanUpRoom(self):
        # print('clean up room')
        self.boxes = copy.deepcopy(self.boxesCopy)
        self.prisoner = None

    ## func used by prisoner
    def prisonerEnterRoom(self, prisoner):
        self.prisoner = prisoner

    def getAvailableBoxes(self):
        boxesToChoose = []
        for box in self.boxes:
            if box.isClosed:
                boxesToChoose.append(box)
        return boxesToChoose