from game import Game;
from copy import deepcopy

class AlphaBetaPlayer:

    __bestMoveListe = [];

    __bestDiv = -99;

    __currentTree = None;

    def setGame(self, game):
        self.currentGame = game;

    def doMove(self):
        if self.currentGame.isMinTurn():
            self.doAlphaBeta(self.currentGame, 0, 15, [], self.currentGame.gameModel.getFieldValue(self.currentGame.gameModel.PLAYER2_BASE) - self.currentGame.gameModel.getFieldValue(self.currentGame.gameModel.PLAYER1_BASE));
        self.currentGame.doMove(self.__bestMoveListe[0]);
        self.resetAlphaBeta();



    def checkIfBetterMove(self, moveListe, div):
        if(self.__bestDiv < div):
            self.__bestDiv = div;
            self.__bestMoveListe = moveListe;
            print("Div is " + str(div) + " on Move " + str(moveListe));

    def resetAlphaBeta(self):
        self.__bestMoveListe = [];
        self.__bestDiv = -99;

    #erster Step Biuldup Tree
    def doBiuldUpTree(self, game, depth, maxdepth, moveListe, divBefore, currentNode):
        

    #momentan nur immer am schauen bester Max Move (logikfehler von mir) muss ich noch anpassen
    def doAlphaBeta(self, game, depth, maxdepth, moveListe, divBefore, currentNode):
        possibleMoves = game.getPossibleMoves();
        for move in possibleMoves:
            if depth <= maxdepth:
                # set new Depth
                newDepth = deepcopy(depth) + 1;
                # deepCopy of moveListe for new Liste
                newmoveListe = deepcopy(moveListe);
                # deepCopy game for Movement
                newGame = deepcopy(game);
                # do Movement
                newGame.doMove(move);
                # write move to Liste
                newmoveListe.append(move);
                # checkIfBetterMovement
                div = newGame.gameModel.getFieldValue(newGame.gameModel.PLAYER2_BASE) - newGame.gameModel.getFieldValue(newGame.gameModel.PLAYER1_BASE)
                newDiv = (div+divBefore)/2;
                self.checkIfBetterMove(newmoveListe, newDiv);
                # Make Tree Object
                node = Tree(newDiv,newGame);
                currentNode.addSubTree(node);
                # do next Step
                self.doAlphaBeta(newGame, newDepth,maxdepth, newmoveListe, newDiv, node);

        

    
                
        
