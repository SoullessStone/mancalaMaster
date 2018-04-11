
from game import Game;
from copy import deepcopy;
import uuid;

class Tree:
    __id = None;
    __value = None;
    __gameStatus = None;
    __subTrees = [];
    __moveToGetHere = None;

    def __init__(self, move, game):
        self.__moveToGetHere = move;
        self.__gameStatus = game;
        self.__id = uuid.uuid4();
        print(self.__id);

    def calculateTree(self, depth, maxDepth):
        if depth == maxDepth:
            self.__value = self.calculateLeaveValue();
            return self.__value;
        
        possibleMoves = self.__gameStatus.getPossibleMoves();
        childValues = [];
        for move in possibleMoves:
            print("move " + str(move));
            # set new Depth
            newDepth = deepcopy(depth) + 1;


            # deepCopy game for Movement
            newGame = deepcopy(self.__gameStatus);
            # do Movement
            newGame.doMove(move);
            # Make Tree Object
            currentNode = Tree(move, newGame);
            self.addSubTree(currentNode);
            childValue = currentNode.calculateTree(newDepth, maxDepth);
            childValues.append(childValue);
            # Versuche, bisherigen Node wiederzuverwenden
            #currentNode = self.findNodeByMove(move);
            #if currentNode is None:
                # deepCopy game for Movement
            #    newGame = deepcopy(self.__gameStatus);
                # do Movement
            #    newGame.doMove(move);
                # Make Tree Object
            #    currentNode = Tree(move, newGame);
            #    self.addSubTree(currentNode);
            #    childValue = currentNode.calculateTree(newDepth, maxDepth);
            #    childValues.append(childValue);
           # else:
            #    print("found");
            #    childValue = currentNode.calculateTree(newDepth, maxDepth);
             #   childValues.append(childValue);
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

    def traverse(self):
        print(str(self.__id) + " -> " + str(self.__moveToGetHere));
        for tree in self.__subTrees:
            tree.traverse();

root = Tree(None,Game());
root.calculateTree(0, 2);
root.traverse();






