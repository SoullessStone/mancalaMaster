class Tree:
    __divStatus = None;
    __gameStatus = None;
    __subTrees = [];

    def __init__(self, div, game):
        self.__divStatus = div;
        self.__gameStatus = 0;

    def addSubTree(self, node):
        self.__subTrees.append(node);

    def calculateTree(self):
        possibleMoves = self.__gameStatus.getPossibleMoves();
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
                # Make Tree Object
                node = Tree(newDiv,newGame);
                currentNode.addSubTree(node);
                # do next Step
                self.doAlphaBeta(newGame, newDepth,maxdepth, newmoveListe, newDiv, node);
