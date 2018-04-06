from random import randint;
from game import Game;

class RandomPlayer:

    def setGame(self, game):
        self.game = game;

    def doMove(self):
        if self.game.isMinTurn():
            possibleMoves = self.game.getPossibleMoves();
            length = len(possibleMoves);
            randomIndex = randint(0, length -1);
            self.game.doMove(possibleMoves[randomIndex]);
