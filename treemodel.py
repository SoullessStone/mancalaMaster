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
    __alphaBetaOn = False;

    def __init__(self, move, game, depth, isMax):
        self.__moveToGetHere = move;
        self.__gameStatus = game;
        self.__id = uuid.uuid4();
        self.__subTrees = [];
        self.__depth = depth;
        self.__isMax = isMax;
        if isMax:
            self.__minMaxFnc1 = max;
            self.__minMaxFnc2 = min;
        else:
            self.__minMaxFnc1 = min;
            self.__minMaxFnc2 = max;

    def calculateTree(self, depth, maxDepth, alpha, beta):
        # Aufhören, wenn wir die maximale Tiefe erreichen
        if depth == maxDepth:
            # Spiel bewerten und Wert zurückgeben
            self.__value = self.calculateLeaveValue();
            return self.__value;

        # Mögliche Züge ausrechnen
        possibleMoves = self.__gameStatus.getPossibleMoves();
        # Array für mögliche Werte der Züge erstellen
        childValues = [];                
        
        for move in possibleMoves:
            # Neue Tiefe setzen
            newDepth = deepcopy(depth) + 1;

            # Versuche, bisherigen Node wiederzuverwenden
            currentNode = self.findNodeByMove(move);
            if currentNode is None:
                # Es wurde keine Node gefunden, der wiederverwendet werden kann
                # deepCopy game für neuen Zug
                newGame = deepcopy(self.__gameStatus);
                # Neuen Zug ausführen
                newGame.doMove(move);
                # Neuen Node anlegen
                currentNode = Tree(move, newGame, newDepth, self.__isMax);
                self.addSubTree(currentNode);
                # Wert des Nodes berechnen (rekursiv)
                childValue = currentNode.calculateTree(newDepth, maxDepth, alpha, beta);

                # AlphaBetaPruning kann ein- und ausgeschaltet werden
                if self.__alphaBetaOn:
                    # AlphaBetaPruning gemäss Folien
                    if newGame.isMaxTurn():
                        alpha = self.__minMaxFnc1(alpha, childValue);
                        if alpha >= beta:
                            return beta;
                    else:
                        beta = self.__minMaxFnc2(beta, childValue);
                        if alpha >= beta:
                            return alpha;
                
                childValues.append(childValue);
            else:
                # Node kann wiederverwendet werden
                # Nur Wert des Nodes neu berechnen
                childValue = currentNode.calculateTree(newDepth, maxDepth, alpha, beta);
                childValues.append(childValue);

        # Min und Max unterschiedlich behandeln
        if self.__gameStatus.isMinTurn():
            if not childValues:
                # finale Züge ausführen (siehe Spielende Mancala)
                self.__gameStatus.doTerminalBeanMovement();
                print("MinMaxPlayer ist dran und es gibt keine Züge mehr");
                print("Score: " + str(self.calculateLeaveValue()));
                # Spielstanddifferenz zurückliefern
                return self.calculateLeaveValue();
            else:
                # Es gibt noch Züge
                # Neues Value berechnen und zurückliefern
                # __minMaxFnc2 wird auf max oder min gesetzt, je nachdem ob der Computer
                # MAX- oder MIN-Spieler ist.
                self.__value = self.__minMaxFnc2(childValues);
                return self.__value;
        else:
            if not childValues:
                # finale Züge ausführen (siehe Spielende Mancala)
                self.__gameStatus.doTerminalBeanMovement();
                print("Human ist dran und es gibt keine Züge mehr");
                print("Score: " + str(self.calculateLeaveValue()));
                return self.calculateLeaveValue();
            else:
                # Es gibt noch Züge
                # Neues Value berechnen und zurückliefern
                # __minMaxFnc2 wird auf max oder min gesetzt, je nachdem ob der Computer
                # MAX- oder MIN-Spieler ist.
                self.__value = self.__minMaxFnc1(childValues);
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

    def getBestMoveForMin(self):
        maxTree = Tree(None,None,None, self.__isMax);
        for tree in self.__subTrees:
            print("min-move nr " + str(tree.getMoveToGetHere()) + " -> " + str(tree.getValue()));
            if tree.getValue() is None:
                continue;
            if maxTree.getValue() == None or tree.getValue() > maxTree.getValue():
                maxTree = tree;
        return maxTree.getMoveToGetHere();

    def getBestMoveForMax(self):
        maxTree = Tree(None,None,None, self.__isMax);
        maxTree.setValue(9999);
        for tree in self.__subTrees:
            print("max-move nr " + str(tree.getMoveToGetHere()) + " -> " + str(tree.getValue()));
            if tree.getValue() is None:
                continue;
            if maxTree.getValue() == None or tree.getValue() < maxTree.getValue():
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
