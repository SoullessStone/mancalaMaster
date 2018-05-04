from random import randint;
from game import Game;
from treemodel import Tree;

class MinMaxPlayer:

    def setGame(self, game):
        self.game = game;

    def init(self, game, maxDepth, isMax):
        self.game = game;
        self.maxDepth = maxDepth;
        self.startDepth = 0;
        self.isMax = isMax;
        self.tree = Tree(None, game, 0, isMax);
        print("Berechne initialen Baum");
        self.alpha = -9999;
        self.beta = 9999;
        self.tree.calculateTree(0, self.maxDepth, self.alpha, self.beta);
        print("Done!");

    def doMove(self):
        # Spielstand nach Max-Zug in Tree nachführen
        lastMoveByMax = self.game.getLastMove();
        if lastMoveByMax:
            print("lastMoveByMax: " + str(lastMoveByMax));
            self.updateMinMaxTree(lastMoveByMax);
        if self.isMax:
            moveToDo = self.tree.getBestMoveForMax();
        else:
            moveToDo = self.tree.getBestMoveForMin();
        print("moveToDo: " + str(moveToDo));
        self.game.doMove(moveToDo);
        self.updateMinMaxTree(moveToDo);
        
        #moveToDo = self.tree.getBestMoveForCurrentPlayer();
        #print("best move: " + str(moveToDo));

        #root.deleteAllNodesExeptWhenMatchingMove(lastMoveByMax);

    def updateMinMaxTree(self, move):
        self.tree = self.tree.findNodeByMove(move);
        self.startDepth = self.startDepth + 1;
        self.maxDepth = self.maxDepth + 1;
        self.tree.calculateTree(self.startDepth, self.maxDepth, self.alpha, self.beta);
'''
game = Game();
player = MinMaxPlayer();
player.init(game, 3);

game.doMove(4);

player.doMove();
'''
