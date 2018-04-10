from game import Game;
from copy import deepcopy

class AlphaBetaPlayer:

    __bestMoveListe = [];

    __bestDiv = 0;

    def setGame(self, game):
        self.currentGame = game;

    def doMove(self):
        if self.currentGame.isMinTurn():
            self.doAlphaBeta(self.currentGame, 0, 2, []);




    def checkIfBetterMoveMax(self, moveListe, div):
        if(self.__bestDiv < div):
            self.__bestDiv = div;
            self.__bestMoveListe = moveListe;
            print("Div is " + str(div) + " on Move " + str(moveListe));

    def checkIfBetterMoveMin(self, moveListe, div):
        if(self.__bestDiv>div):
            self.__bestDiv = div;
            self.__bestMoveListe = moveListe;
            print("Div is " + str(div) + " on Move " + str(moveListe));



    #momentan nur immer am schauen bester Max Move (logikfehler von mir) muss ich noch anpassen
    def doAlphaBeta(self, game, depth, maxdepth, moveListe):
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
                if newGame.isMinTurn():
                    self.checkIfBetterMoveMin(newmoveListe, div);
                else:
                    self.checkIfBetterMoveMax(newmoveListe, div);
                self.doAlphaBeta(newGame, newDepth,maxdepth, newmoveListe);
                
        
