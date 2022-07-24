class Prisoner:
    def __init__(self, numberOfPrisoner):
        self.numberOfPrisoner = numberOfPrisoner

    def setStrategy(self, strategy):
        self.strategy = strategy

    def enterRoom(self, room):
        self.room = room
        # print('prisoner', self, ' with number ', self.numberOfPrisoner , ' enter room')
        room.prisonerEnterRoom(self)

    def leaveRoom(self):
        self.room.cleanUpRoom()
        self.room = None
        # print('prisoner', self, ' leave room')

    def openBox(self, choices):
        box = self.strategy.getChoice(choices)
        return box.openBoxAndGetNumber()