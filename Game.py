from Environment import Env
from Strategy import *

class Game:
    def __init__(self, strategy):
        env = Env(100, 50)
        env.setPrisonersStrategy(strategy)
        self.env = env

    def prisonerRound(self, prisoner):
        endOfRound = False
        success = False
        roundNumber = 1
        prisoner.enterRoom(self.env.room)

        while not endOfRound:
            # print('round ', roundNumber)
            choinces = self.env.room.getAvailableBoxes()
            pickedUp = prisoner.openBox(choinces)

            if pickedUp == None or roundNumber > self.env.numberOfChanses:
                endOfRound = True

            if pickedUp == prisoner.numberOfPrisoner:
                endOfRound = True
                success = True

            roundNumber += 1

        prisoner.leaveRoom()
        return success

    def run(self):
        prisonersWin = True
        numberOfSuccesses = 0
        for prisoner in self.env.allPrisoners:
            successful = self.prisonerRound(prisoner)
            # print('prisoner', prisoner, ' is winned? ', successful)
            if not successful:
                prisonersWin = False
                break
            numberOfSuccesses += 1
        return prisonersWin, numberOfSuccesses


def strategyStats(strategy):
    stats = dict()
    wins = 0
    total = 0

    for i in range(100):
        game = Game(strategy)
        win, numOfSmallWin = game.run()
        if win: wins += 1
        total += 1

        stats[numOfSmallWin] = stats.get(numOfSmallWin, 0) + 1

    print(stats)
    print(wins, total, float(wins) / total)


strategyStats(RandomStrategy)
strategyStats(LoopStrategy)



