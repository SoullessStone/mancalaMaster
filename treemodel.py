from game import Game;
from copy import deepcopy;
import uuid;
import gc;
import time;

class Tree:
    __id = None;
    __value = None;
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

        # "Experiment"
        # Wenn jemand nicht mehr ziehen kann, bekommt der Gegner die eigenen Steine
        # Das muss man einrechnen
        if not possibleMoves:
            self.__gameStatus.doTerminalBeanMovement();
            if self.__gameStatus.isMinTurn():
                print("MinMaxPlayer ist dran und es gibt keine Züge mehr");
            else:
                print("Human ist dran und es gibt keine Züge mehr");
            print("Score: " + str(self.calculateLeaveValue()));
            return self.calculateLeaveValue();
                
        
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

        # Sollte mit Experiment nicht mehr vorkommen
        if not childValues: # childValues ist leer
            print("used this... not good");
            return self.calculateLeaveValue(); ######### EVTL NOCH ÜBERLEGEN....
        
        if self.__gameStatus.isMinTurn():
            self.__value = max(childValues);
            #print(self.__value);
            return self.__value;
        else:
            self.__value = min(childValues);
            return self.__value;

    def calculateLeaveValue(self):
        return self.__gameStatus.gameModel.getFieldValue(self.__gameStatus.gameModel.PLAYER2_BASE) - self.__gameStatus.gameModel.getFieldValue(self.__gameStatus.gameModel.PLAYER1_BASE);

    def addSubTree(self, tree):
        self.__subTrees.append(tree);

    def getGame(self):
        return self.__gameStatus;

    def getValue(self):
        return self.__value;

    def setValue(self, value):
        self.__value = value;

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

    def deleteAllNodesExeptWhenMatchingMove(self, move):
        for tree in self.__subTrees:
            if not tree.getMoveToGetHere() == move:
                del(tree);
        gc.collect();

    def traverse(self):
        print(str(self.__depth) + " " + str(self.__id) + " -> move to get here: " + str(self.__moveToGetHere) + ", value: " + str(self.__value));
        for tree in self.__subTrees:
            tree.traverse();

    def getBestMoveForCurrentPlayer(self):
        maxTree = Tree(None,None,None);
        for tree in self.__subTrees:
            print("move nr " + str(tree.getMoveToGetHere()) + " -> " + str(tree.getValue()));
            if maxTree.getValue() == None or tree.getValue() > maxTree.getValue():
                maxTree = tree;
        return maxTree.getMoveToGetHere();
'''
# Wir wollen einen Baum, der bei Tiefe 0 anfängt und maximal 2 tief ist
startDepth = 0;
maxDepth = 6;
# Neuen Tree erstellen und bis maxDepth ausrechnen
root = Tree(None,Game(),0);

start = time.time();
root.calculateTree(startDepth, maxDepth);
end = time.time();
print("Dauer, um den ganzen Baum zu berechnen: " + str(end - start));
#root.traverse();
# Move von Max ausrechnen (min würde automatisch ziehen)
moveToDo = root.getBestMoveForCurrentPlayer();
print("Move to do: " + str(moveToDo));
# Es wurde ein move gezogen und wir holen den neuen Root
newRoot = root.findNodeByMove(moveToDo);
# Speicher freiräumen
root.deleteAllNodesExeptWhenMatchingMove(moveToDo);
# Baum erweitern (Anmerkung: die effektive Tiefe des Baumes bleibt maxDepth. Depth-Attribut wird aber immer von 0 gezählt)
print("Neuer Baum: ");
startDepth = startDepth+1;
maxDepth = maxDepth+1;

start = time.time();
root.calculateTree(startDepth, maxDepth);
end = time.time();
print("Dauer, um nur eine neue Schicht zuunterst hinzuzufügen: " + str(end - start));
#newRoot.traverse();
# Einfach die outputs von traverse vergleichen, um zu sehen, welche Bäume noch da sind :)
'''



print 

# Beispiel: Der Baum wird zuerst aufgebaut und anschliessend erweitert (bestehende nodes bleiben, bekommen nur einen neuen Value)
#root = Tree(None,Game(),0);
#root.calculateTree(0, 1);
#root.traverse();
#print("best move-value for max: " + str(root.getBestMoveForMax()));
#root.calculateTree(0,4);
#root.traverse();
#print("best move-value for max: " + str(root.getBestMoveForMax()));
