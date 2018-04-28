from game import Game;
from copy import deepcopy;
import uuid;

class Tree:
    __id = None;
    __value = -1;
    __gameStatus = None;
    __subTrees = [];
    __moveToGetHere = None;

    def __init__(self, move, game, depth):
        self.__moveToGetHere = move;
        self.__gameStatus = game;
        self.__id = uuid.uuid4();
        self.__subTrees = [];
        self.__depth = depth;

    def calculateTree(self, depth, maxDepth):
        if depth == maxDepth:
            self.__value = self.calculateLeaveValue();
            return self.__value;
        
        possibleMoves = self.__gameStatus.getPossibleMoves();
        childValues = [];
        for move in possibleMoves:
            # set new Depth
            newDepth = deepcopy(depth) + 1;

            # Versuche, bisherigen Node wiederzuverwenden
            currentNode = self.findNodeByMove(move);
            if currentNode is None:
                # deepCopy game for Movement
                newGame = deepcopy(self.__gameStatus);
                # do Movement
                newGame.doMove(move);
                # Make Tree Object
                currentNode = Tree(move, newGame, newDepth);
                self.addSubTree(currentNode);
                childValue = currentNode.calculateTree(newDepth, maxDepth);
                childValues.append(childValue);
            else:
                #print("found: ", str(move) + " " + str(currentNode.getId()));
                childValue = currentNode.calculateTree(newDepth, maxDepth);
                childValues.append(childValue);
        if self.__gameStatus.isMinTurn():
            self.__value = max(childValues);
            #print(self.__value);
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

    def getValue(self):
        return self.__value;

    def getId(self):
        return self.__id;

    def getSubtrees(self):
        return self.__subTrees;

    def getMoveToGetHere(self):
        return self.__moveToGetHere;

    def findNodeByMove(self, move):
        for tree in self.__subTrees:
            if tree.getMoveToGetHere() == move:
                return tree;
        return None;

    def traverse(self):
        print(str(self.__depth) + " " + str(self.__id) + " -> move to get here: " + str(self.__moveToGetHere) + ", value: " + str(self.__value));
        for tree in self.__subTrees:
            tree.traverse();

    def getBestMoveForMax(self):
        maxTree = Tree(None,None,None);
        for tree in self.__subTrees:
            print(tree.getValue());
            if tree.getValue() > maxTree.getValue():
                maxTree = tree;
        return maxTree.getValue();

root = Tree(None,Game(),0);
root.calculateTree(0, 1);
root.traverse();
print("best move-value for max: " + str(root.getBestMoveForMax()));
root.calculateTree(0,4);
root.traverse();
print("best move-value for max: " + str(root.getBestMoveForMax()));
