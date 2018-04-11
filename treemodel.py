class Tree:
    __divStatus = None;
    __gameStatus = None;
    __subTrees = [];

    def __init__(self, div, game):
        self.__divStatus = div;
        self.__gameStatus = 0;

    def addSubTree(self, node):
        self.__subTrees.append(node);
