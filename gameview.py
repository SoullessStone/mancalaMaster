from tkinter import *;
from game import Game;


    
# Wie kann man das Model updaten?
class GameView:
    fenster = None;
    game = Game();
    
        
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
        self.fenster.after(2,self.updateView);

    def doPlayStep(self,button):
        # Do Play in Game
        self.game.gameModel.changeFieldValue(button,button);
        
    def __init__(self):
        self.fenster = Tk();
        self.fenster.title("Mancala");
        self.fenster.after(2,self.updateView);
        
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

        self.p2_6.grid(row=0, column=0, pady = 20);
        self.p1_1.grid(row=1, column=0, pady = 20);
        self.p2_5.grid(row=0, column=1, pady = 20);
        self.p1_2.grid(row=1, column=1, pady = 20);
        self.p2_4.grid(row=0, column=2, pady = 20);
        self.p1_3.grid(row=1, column=2, pady = 20);
        self.p2_3.grid(row=0, column=3, pady = 20);
        self.p1_4.grid(row=1, column=3, pady = 20);
        self.p2_2.grid(row=0, column=4, pady = 20);
        self.p1_5.grid(row=1, column=4, pady = 20);
        self.p2_1.grid(row=0, column=5, pady = 20);
        self.p1_6.grid(row=1, column=5, pady = 20);
        
        self.fenster.mainloop();



view = GameView();
