
from game import Game;
from copy import deepcopy;
import uuid;

class Tree:
    __id = None;
    __value = None;
    __gameStatus = None;
    __subTrees = [];
    __moveToGetHere = None;

    def __init__(self, move):
        self.__moveToGetHere = move;
        self.__id = uuid.uuid4();
        print(self.__id);

    def calculateTree(self, game, depth, maxDepth):
        self.__gameStatus = game;
        if depth == maxDepth:
            self.__value = self.calculateLeaveValue();
            return self.__value;
        
        possibleMoves = game.getPossibleMoves();
        childValues = [];
        for move in possibleMoves:
            print("move " + str(move));
            # set new Depth
            newDepth = deepcopy(depth) + 1;
            
            # Versuche, bisherigen Node wiederzuverwenden
            currentNode = self.findNodeByMove(move);
            if currentNode is None:
                # deepCopy game for Movement
                newGame = deepcopy(game);
                # do Movement
                newGame.doMove(move);
                # Make Tree Object
                currentNode = Tree(move);
                self.addSubTree(currentNode);
                childValue = currentNode.calculateTree(newGame, newDepth, maxDepth);
                childValues.append(childValue);
            else:
                print("found");
                childValue = currentNode.calculateTree(currentNode.getGame(), newDepth, maxDepth);
                childValues.append(childValue);
        if self.__gameStatus.isMaxTurn():
            self.__value = max(childValues);
            return max(childValues);
        else:
            self.__value = min(childValues);
            return min(childValues);

    def calculateLeaveValue(self):
        return self.__gameStatus.gameModel.getFieldValue(self.__gameStatus.gameModel.PLAYER2_BASE) - self.__gameStatus.gameModel.getFieldValue(self.__gameStatus.gameModel.PLAYER1_BASE);

    def addSubTree(self, tree):
        self.__subTrees.append(tree);

    def getGame(self):
        return self.__gameStatus;

    def getSubtrees(self):
        return self.__subTrees;

    def getMoveToGetHere(self):
        return self.__moveToGetHere;

    def findNodeByMove(self, move):
        for tree in self.__subTrees:
            if tree.getMoveToGetHere() == move:
                return tree;
        return None;


root = Tree(None);
root.calculateTree(Game(), 0, 2);






