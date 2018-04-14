from gamemodel import GameModel

class Game:
    gameModel = None;
    __MAX_TURN = 0;
    __MIN_TURN = 1;
    __lastMove = None;

    # Returns, if it is the turn of MAX
    def isMaxTurn(self):
        return self.gameModel.getTurn() == self.__MAX_TURN;
    
    # Returns, if it is the turn of MIN
    def isMinTurn(self):
        return self.gameModel.getTurn() == self.__MIN_TURN;
    
    # Returns the initial state
    def reset(self):
        self.gameModel = GameModel();

    # Do Bean Final Movement
    def doTerminalBeanMovement(self):
        newValue = self.gameModel.getFieldValue(self.gameModel.PLAYER1_BASE) +  self.gameModel.getFieldValue(self.gameModel.PLAYER1_1) + self.gameModel.getFieldValue(self.gameModel.PLAYER1_2) + self.gameModel.getFieldValue(self.gameModel.PLAYER1_3) + self.gameModel.getFieldValue(self.gameModel.PLAYER1_4) + self.gameModel.getFieldValue(self.gameModel.PLAYER1_5) + self.gameModel.getFieldValue(self.gameModel.PLAYER1_6);
        self.gameModel.changeFieldValue(self.gameModel.PLAYER1_BASE, newValue);
        self.gameModel.changeFieldValue(self.gameModel.PLAYER1_1,0);
        self.gameModel.changeFieldValue(self.gameModel.PLAYER1_2,0);
        self.gameModel.changeFieldValue(self.gameModel.PLAYER1_3,0);
        self.gameModel.changeFieldValue(self.gameModel.PLAYER1_4,0);
        self.gameModel.changeFieldValue(self.gameModel.PLAYER1_5,0);
        self.gameModel.changeFieldValue(self.gameModel.PLAYER1_6,0);
        newValue = self.gameModel.getFieldValue(self.gameModel.PLAYER2_BASE) +  self.gameModel.getFieldValue(self.gameModel.PLAYER2_1) + self.gameModel.getFieldValue(self.gameModel.PLAYER2_2) + self.gameModel.getFieldValue(self.gameModel.PLAYER2_3) + self.gameModel.getFieldValue(self.gameModel.PLAYER2_4) + self.gameModel.getFieldValue(self.gameModel.PLAYER2_5) + self.gameModel.getFieldValue(self.gameModel.PLAYER2_6);
        self.gameModel.changeFieldValue(self.gameModel.PLAYER2_BASE, newValue);
        self.gameModel.changeFieldValue(self.gameModel.PLAYER2_1,0);
        self.gameModel.changeFieldValue(self.gameModel.PLAYER2_2,0);
        self.gameModel.changeFieldValue(self.gameModel.PLAYER2_3,0);
        self.gameModel.changeFieldValue(self.gameModel.PLAYER2_4,0);
        self.gameModel.changeFieldValue(self.gameModel.PLAYER2_5,0);
        self.gameModel.changeFieldValue(self.gameModel.PLAYER2_6,0);
    
    # Do a move on current state
    def doMove(self, move):
        if self.isTerminal():
            return;
        if not self.isFieldOnCurrentPlayerSide(move):
            print("Move " + str(move) + " is not legal");
            return;
        # Get Bean count
        beans = self.gameModel.getFieldValue(move);

        # No Beans in Field no Move possible
        if beans == 0:
            print("Move " + str(move) + " no beans to move");
            return;

        # set last Move
        self.__lastMove = move;
        
        # Remove all beans from taken holder
        self.gameModel.changeFieldValue(move, 0);
        currentField = move + 1;
        while beans > 0:
            if (self.isMaxTurn() and currentField == self.gameModel.PLAYER2_BASE):
                currentField = 0;
                continue; # Player 1 does not put beans into Player 2 base
            if (self.isMinTurn() and currentField == self.gameModel.PLAYER1_BASE):
                currentField = currentField + 1;
                continue; # Player 2 does not put beans into Player 1 base

            # Add bean to current Field
            currentValue = self.gameModel.getFieldValue(currentField);
            newValue = currentValue + 1;
            self.gameModel.changeFieldValue(currentField, newValue);
            # One bean taken, less remain
            beans = beans - 1;

            # if it is the last bean and it is put on an empty field on the players side, the
            # the player can take the one bean on his side and the beans on the other side
            if newValue == 1 and beans == 0 and self.isFieldOnCurrentPlayerSide(currentField):
                self.handleLastBeanOnOwnEmptyField(currentField);
            
            # Move to next field
            currentField = currentField + 1;
            if currentField == self.gameModel.PLAYER2_BASE + 1:
                currentField = 0;
        # Other Players turn
        self.gameModel.switchTurn();
    
    # Returns the last move leading to this state
    def getLastMove(self):
        return self.__lastMove;
    
    # Returns all possible moves of this state
    def getPossibleMoves(self):
        i = self.gameModel.PLAYER1_1;
        minI = i;
        maxI = self.gameModel.PLAYER1_6;
        if self.isMinTurn():
            i = self.gameModel.PLAYER2_1;
            minI = i;
            maxI = self.gameModel.PLAYER2_6;
        possibleMoves = [];
        for move in range(minI, maxI + 1):
            if self.gameModel.getFieldValue(move) != 0:
                possibleMoves.append(move);
        return possibleMoves;
    
    # Returns all successor states
    def expand(self):
        raise NotImplementedError("You should have implemented this");
    
    # Returns, if the current state is terminal
    def isTerminal(self):
        fieldsToCheck = self.getPlayerOneMoves();
        playerOneSideEmpty = self.areAllFieldsEmpty(fieldsToCheck);
        fieldsToCheck = self.getPlayerTwoMoves();
        playerTwoSideEmpty = self.areAllFieldsEmpty(fieldsToCheck);
        if(playerOneSideEmpty or playerTwoSideEmpty):
            self.doTerminalBeanMovement();
        return (playerOneSideEmpty or playerTwoSideEmpty);
    
    # Returns the evaluation of a state related to MAX
    def evalValueForMax(self):
        raise NotImplementedError("You should have implemented this");
    
    # Returns the evaluation for a terminal state (for MAX)
    def utility(self):
        raise NotImplementedError("You should have implemented this");
    
    def __init__(self):
        self.gameModel = GameModel();

    ############################################################################
    ############################ Hilfsmethoden #################################
    ############################################################################
    
    def areAllFieldsEmpty(self, fields):
        allEmpty = True;
        for field in fields:
            if self.gameModel.getFieldValue(field) != 0:
                allEmpty = False;
        return allEmpty;
    
    def getPlayerOneMoves(self):
        return [self.gameModel.PLAYER1_1,
                         self.gameModel.PLAYER1_2,
                         self.gameModel.PLAYER1_3,
                         self.gameModel.PLAYER1_4,
                         self.gameModel.PLAYER1_5,
                         self.gameModel.PLAYER1_6];
    
    def getPlayerTwoMoves(self):
        return [self.gameModel.PLAYER2_1,
                         self.gameModel.PLAYER2_2,
                         self.gameModel.PLAYER2_3,
                         self.gameModel.PLAYER2_4,
                         self.gameModel.PLAYER2_5,
                         self.gameModel.PLAYER2_6];
    
    def isFieldOnCurrentPlayerSide(self, move):
        if self.isMinTurn():
            return move in self.getPlayerTwoMoves();
        if self.isMaxTurn():
            return move in self.getPlayerOneMoves();
    
    def getCurrentPlayerBase(self):
        if self.isMinTurn():
            return self.gameModel.PLAYER2_BASE;
        if self.isMaxTurn():
            return self.gameModel.PLAYER1_BASE;
    
    def handleLastBeanOnOwnEmptyField(self, curField):
        opposingField = self.getOpposingField(curField);
        beansOnOpposingField = self.gameModel.getFieldValue(opposingField);
        if beansOnOpposingField == 0:
            return; # in this case, nothing happens
        playerBase = self.getCurrentPlayerBase();
        beanCountInBase = self.gameModel.getFieldValue(playerBase);
        self.gameModel.changeFieldValue(playerBase, beanCountInBase + beansOnOpposingField + 1);
        self.gameModel.changeFieldValue(opposingField, 0);
        self.gameModel.changeFieldValue(curField, 0);

    def getOpposingField(self, field):
        if field == self.gameModel.PLAYER1_1:
            return self.gameModel.PLAYER2_6;
        if field == self.gameModel.PLAYER1_2:
            return self.gameModel.PLAYER2_5;
        if field == self.gameModel.PLAYER1_3:
            return self.gameModel.PLAYER2_4;
        if field == self.gameModel.PLAYER1_4:
            return self.gameModel.PLAYER2_3;
        if field == self.gameModel.PLAYER1_5:
            return self.gameModel.PLAYER2_2;
        if field == self.gameModel.PLAYER1_6:
            return self.gameModel.PLAYER2_1;
        if field == self.gameModel.PLAYER2_1:
            return self.gameModel.PLAYER1_6;
        if field == self.gameModel.PLAYER2_2:
            return self.gameModel.PLAYER1_5;
        if field == self.gameModel.PLAYER2_3:
            return self.gameModel.PLAYER1_4;
        if field == self.gameModel.PLAYER2_4:
            return self.gameModel.PLAYER1_3;
        if field == self.gameModel.PLAYER2_5:
            return self.gameModel.PLAYER1_2;
        if field == self.gameModel.PLAYER2_6:
            return self.gameModel.PLAYER1_1;
        


























