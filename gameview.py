from tkinter import *;
from gamemodel import *;

#Dummy, remove when game is ready
class Data:
    game = GameModel();
    i = 1;
    def getData(self):
        self.game.changeFieldValue(0, self.i);
        self.i = self.i + 1;
        return self.game;
    
# Wie kann man das Model updaten?
class GameView:
    fenster = None;
    gameModel = GameModel();
    data = Data();

    def doPlayStep(self):
        self.fenster.title("Mancala");
        
    def updateView(self):
        model = self.data.getData();
        self.points_p1.config(text=str(model.getFieldValue(model.PLAYER1_BASE)));
        self.points_p2.config(text=str(model.getFieldValue(model.PLAYER2_BASE)));
        
        self.p1_1["text"] = str(self.gameModel.getFieldValue(self.gameModel.PLAYER1_1));
        self.p1_2["text"] = str(self.gameModel.getFieldValue(self.gameModel.PLAYER1_2));
        self.p1_3["text"] = str(self.gameModel.getFieldValue(self.gameModel.PLAYER1_3));
        self.p1_4["text"] = str(self.gameModel.getFieldValue(self.gameModel.PLAYER1_4));
        self.p1_5["text"] = str(self.gameModel.getFieldValue(self.gameModel.PLAYER1_5));
        self.p1_6["text"] = str(self.gameModel.getFieldValue(self.gameModel.PLAYER1_6));

        self.p2_1["text"] = str(self.gameModel.getFieldValue(self.gameModel.PLAYER2_1));
        self.p2_2["text"] = str(self.gameModel.getFieldValue(self.gameModel.PLAYER2_2));
        self.p2_3["text"] = str(self.gameModel.getFieldValue(self.gameModel.PLAYER2_3));
        self.p2_4["text"] = str(self.gameModel.getFieldValue(self.gameModel.PLAYER2_4));
        self.p2_5["text"] = str(self.gameModel.getFieldValue(self.gameModel.PLAYER2_5));
        self.p2_6["text"] = str(self.gameModel.getFieldValue(self.gameModel.PLAYER2_6));
        self.fenster.after(2, self.updateView)
        
    def __init__(self):
        self.fenster = Tk();
        self.fenster.after(2, self.updateView)
        
        self.p1_1 = Button(self.fenster, text="0", command=self.doPlayStep);
        self.p1_2 = Button(self.fenster, text="0", command=self.doPlayStep);
        self.p1_3 = Button(self.fenster, text="0", command=self.doPlayStep);
        self.p1_4 = Button(self.fenster, text="0", command=self.doPlayStep);
        self.p1_5 = Button(self.fenster, text="0", command=self.doPlayStep);
        self.p1_6 = Button(self.fenster, text="0", command=self.doPlayStep);

        self.p2_1 = Button(self.fenster, text="0", command=self.doPlayStep);
        self.p2_2 = Button(self.fenster, text="0", command=self.doPlayStep);
        self.p2_3 = Button(self.fenster, text="0", command=self.doPlayStep);
        self.p2_4 = Button(self.fenster, text="0", command=self.doPlayStep);
        self.p2_5 = Button(self.fenster, text="0", command=self.doPlayStep);
        self.p2_6 = Button(self.fenster, text="0", command=self.doPlayStep);

        self.points_p1 = Label(self.fenster, text="0");
        self.points_p2 = Label(self.fenster, text="0");

        self.p2_1.grid(row=0, column=0, pady = 20);
        self.p1_1.grid(row=1, column=0, pady = 20);
        self.p2_2.grid(row=0, column=1, pady = 20);
        self.p1_2.grid(row=1, column=1, pady = 20);
        self.p2_3.grid(row=0, column=2, pady = 20);
        self.p1_3.grid(row=1, column=2, pady = 20);
        self.p2_4.grid(row=0, column=3, pady = 20);
        self.p1_4.grid(row=1, column=3, pady = 20);
        self.p2_5.grid(row=0, column=4, pady = 20);
        self.p1_5.grid(row=1, column=4, pady = 20);
        self.p2_6.grid(row=0, column=5, pady = 20);
        self.p1_6.grid(row=1, column=5, pady = 20);
        
        self.fenster.mainloop();



view = GameView();



    
