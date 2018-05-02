from tkinter import *;
from game import Game;
from player_random import RandomPlayer;
from player_alphabeta import AlphaBetaPlayer;
from player_minmax import MinMaxPlayer;
from time import sleep;


    
# Wie kann man das Model updaten?
class GameView:
     
    player = "MINMAX";
    
    fenster = None;
    game = Game();
    
    randomPlayer = RandomPlayer();
    
    alphabetaPlayer = AlphaBetaPlayer();
    
    minmaxPlayer = MinMaxPlayer();   
    if player == "MINMAX":
        minmaxPlayer.init(game,2);
        
    delayAiMove = 0;
    
        
    def updateView(self):
        self.points_p1.config(text=str(self.game.gameModel.getFieldValue(self.game.gameModel.PLAYER1_BASE)));
        self.points_p2.config(text=str(self.game.gameModel.getFieldValue(self.game.gameModel.PLAYER2_BASE)));
        
        self.p1_1["text"] = str(self.game.gameModel.getFieldValue(self.game.gameModel.PLAYER1_1));
        self.p1_2["text"] = str(self.game.gameModel.getFieldValue(self.game.gameModel.PLAYER1_2));
        self.p1_3["text"] = str(self.game.gameModel.getFieldValue(self.game.gameModel.PLAYER1_3));
        self.p1_4["text"] = str(self.game.gameModel.getFieldValue(self.game.gameModel.PLAYER1_4));
        self.p1_5["text"] = str(self.game.gameModel.getFieldValue(self.game.gameModel.PLAYER1_5));
        self.p1_6["text"] = str(self.game.gameModel.getFieldValue(self.game.gameModel.PLAYER1_6));

        self.p2_1["text"] = str(self.game.gameModel.getFieldValue(self.game.gameModel.PLAYER2_1));
        self.p2_2["text"] = str(self.game.gameModel.getFieldValue(self.game.gameModel.PLAYER2_2));
        self.p2_3["text"] = str(self.game.gameModel.getFieldValue(self.game.gameModel.PLAYER2_3));
        self.p2_4["text"] = str(self.game.gameModel.getFieldValue(self.game.gameModel.PLAYER2_4));
        self.p2_5["text"] = str(self.game.gameModel.getFieldValue(self.game.gameModel.PLAYER2_5));
        self.p2_6["text"] = str(self.game.gameModel.getFieldValue(self.game.gameModel.PLAYER2_6));
            
        if self.game.isMaxTurn():
            self.player1_turn["text"] = "Spieler 1 darf spielen";
            self.player2_turn["text"] = "";
        if self.game.isMinTurn():
            self.player1_turn["text"] = "";
            self.player2_turn["text"] = "Spieler 2 darf spielen";
        if self.game.isTerminal():
            self.player1_turn["text"] = "";
            self.player2_turn["text"] = "";
            self.terminal["text"] = "Aus die Maus...";
            return;
        
        if self.player == "RANDOM" and self.game.isMinTurn():
            if self.delayAiMove == 50:
               self.randomPlayer.doMove(); # Erst jetzt (UI konnte sich updaten, User sieht Ergebnis seines Zuges
               self.delayAiMove = 0;
            else:
                self.delayAiMove = self.delayAiMove + 1;

        if self.player == "ALPHABETA" and self.game.isMinTurn():
            if self.delayAiMove == 50:
                self.alphabetaPlayer.doMove();
                self.delayAiMove = 0;
            else:
                self.delayAiMove = self.delayAiMove + 1;

        if self.player == "MINMAX" and self.game.isMinTurn():
            if self.delayAiMove == 50:
                self.minmaxPlayer.doMove();
                self.delayAiMove = 0;
            else:
                self.delayAiMove = self.delayAiMove + 1;
            
            
        self.fenster.after(50,self.updateView);

    def doPlayStep(self,button):
        # Do Play in Game
        self.game.doMove(button);
        
    def __init__(self):
        self.fenster = Tk();
        self.fenster.title("Mancala");
        self.fenster.after(50,self.updateView);
        
        self.p1_1 = Button(self.fenster, text="0", command=lambda: self.doPlayStep(self.game.gameModel.PLAYER1_1));
        self.p1_2 = Button(self.fenster, text="0", command=lambda: self.doPlayStep(self.game.gameModel.PLAYER1_2));
        self.p1_3 = Button(self.fenster, text="0", command=lambda: self.doPlayStep(self.game.gameModel.PLAYER1_3));
        self.p1_4 = Button(self.fenster, text="0", command=lambda: self.doPlayStep(self.game.gameModel.PLAYER1_4));
        self.p1_5 = Button(self.fenster, text="0", command=lambda: self.doPlayStep(self.game.gameModel.PLAYER1_5));
        self.p1_6 = Button(self.fenster, text="0", command=lambda: self.doPlayStep(self.game.gameModel.PLAYER1_6));

        self.p2_1 = Button(self.fenster, text="0", command=lambda: self.doPlayStep(self.game.gameModel.PLAYER2_1));
        self.p2_2 = Button(self.fenster, text="0", command=lambda: self.doPlayStep(self.game.gameModel.PLAYER2_2));
        self.p2_3 = Button(self.fenster, text="0", command=lambda: self.doPlayStep(self.game.gameModel.PLAYER2_3));
        self.p2_4 = Button(self.fenster, text="0", command=lambda: self.doPlayStep(self.game.gameModel.PLAYER2_4));
        self.p2_5 = Button(self.fenster, text="0", command=lambda: self.doPlayStep(self.game.gameModel.PLAYER2_5));
        self.p2_6 = Button(self.fenster, text="0", command=lambda: self.doPlayStep(self.game.gameModel.PLAYER2_6));

        self.points_p1 = Label(self.fenster, text="0");
        self.points_p2 = Label(self.fenster, text="0");
        self.player1_turn = Label(self.fenster, text="");
        self.player2_turn = Label(self.fenster, text="");
        self.terminal = Label(self.fenster, text="");
        self.reset = Button(self.fenster, text="Reset",command= self.game.reset);

        self.p2_6.grid(row=0, column=0, pady = 20);
        self.p1_1.grid(row=4, column=0, pady = 20);
        self.p2_5.grid(row=0, column=1, pady = 20);
        self.p1_2.grid(row=4, column=1, pady = 20);
        self.p2_4.grid(row=0, column=2, pady = 20);
        self.p1_3.grid(row=4, column=2, pady = 20);
        self.p2_3.grid(row=0, column=3, pady = 20);
        self.p1_4.grid(row=4, column=3, pady = 20);
        self.p2_2.grid(row=0, column=4, pady = 20);
        self.p1_5.grid(row=4, column=4, pady = 20);
        self.p2_1.grid(row=0, column=5, pady = 20);
        self.p1_6.grid(row=4, column=5, pady = 20);
        self.points_p1.grid(row=2, column=5, pady = 20);
        self.points_p2.grid(row=2, column=0, pady = 20);
        self.player1_turn.grid(row=4, column=6, pady = 20);
        self.player2_turn.grid(row=0, column=6, pady = 20);
        self.terminal.grid(row=2, column=6, pady = 20);
        self.reset.grid(row=2, column=7, pady = 20);

        self.randomPlayer.setGame(self.game);
        self.alphabetaPlayer.setGame(self.game);
        
        self.fenster.mainloop();



view = GameView();
