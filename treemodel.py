class Tree:
    __value = None;
    __gameStatus = None;
    __subTrees = [];

    def calculateTree(self, game, depth, maxDepth, parentNode):
        self.__gameStatus = game;
        if depth == maxdepth:
            self.calculateLeaveValue();
            return self.__value;
        
        possibleMoves = game.getPossibleMoves();
        childValues = [];
        for move in possibleMoves:
            # set new Depth
            newDepth = deepcopy(depth) + 1;
            # deepCopy game for Movement
            newGame = deepcopy(game);
            # do Movement
            newGame.doMove(move);
            # Make Tree Object
            node = Tree();
            parentNode.addSubTree(node);
            childValue = self.calculateTree(newGame, newDepth, maxDepth, node);
            childValues.append(childValue);
        if self.__gameStatus.isMaxTurn():
            self.__value = max(childValues);
            return max(childValues);
        else:
            self.__value = min(childValues);
            return min(childValues);

    def calculateLeaveValue(self):
        # diff function whatever

    def addSubTree(self):
        # todo
