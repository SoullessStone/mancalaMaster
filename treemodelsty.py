from game import Game;
from copy import deepcopy

class Tree:
    __divStatus = None;
    __gameStatus = None;
    __currentDiv = None;
    __subTrees = [];
    __moveListe = [];

    def __init__(self, div, game, moveliste):
        self.__currentDiv = div;
        self.__gameStatus = game;
        self.__moveListe = moveliste;

    def addSubTree(self, node):
        self.__subTrees.append(node);

    def calcDiv(self, div):
        self.__divStatus = (div + self.__currentDiv)/2;

    def getDivStatus(self):
        return self.__divStatus;

    def getSubTreeList(self):
        return self.__subTrees;

    def getCurrentDiv(self):
        return self.__currentDiv;

    def getMoveListe(self):
        return self.__moveListe;

    def getCurrentGame(self):
        return self.__gameStatus;

    def calculateTree(self, game, depth, maxdepth, divBefore, currentNode):
        possibleMoves = game.getPossibleMoves();
        for move in possibleMoves:
            if depth <= maxdepth:
                # set new Depth
                newDepth = deepcopy(depth) + 1;
                # deepCopy of moveListe for new Liste
                newmoveListe = deepcopy(currentNode.getMoveListe());
                # deepCopy game for Movement
                newGame = deepcopy(game);
                # do Movement
                newGame.doMove(move);
                # write move to Liste
                newmoveListe.append(move);
                # checkIfBetterMovement
                div = newGame.gameModel.getFieldValue(newGame.gameModel.PLAYER2_BASE) - newGame.gameModel.getFieldValue(newGame.gameModel.PLAYER1_BASE)
                node = Tree(div,newGame, newmoveListe);
                node.calcDiv(divBefore);
                currentNode.addSubTree(node);
                # do next Step
                self.calculateTree(newGame, newDepth,maxdepth, node.getDivStatus(), node);

    def resortingTree(self, currentNode):
        for node in currentNode.getSubTreeList():
            node.calcDiv(currentNode.getDivStatus());
            del node.getMoveListe[0];
            del node.getMoveListe[0];
            self.resortingTree(node);
        if currentNode.__gameStatus == None:
            self.calculateTree(currentNode.getCurrentGame(),0,2,currentNode.getDivStatus(), currentNode);
            
