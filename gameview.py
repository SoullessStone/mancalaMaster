from tkinter import *;
from gamemodel import *;

game = GameModel();

fenster = Tk();

fenster.title("Testfenster");

def doPlayStep():
    fenster.title("Hallo");
    
def updateView(GameModel):
    points_p1.config(text=str(GameModel.getFieldValue(game.PLAYER1_BASE)));
    points_p2.config(text=str(GameModel.getFieldValue(game.PLAYER2_BASE)));
    
    p1_1["text"] = str(GameModel.getFieldValue(game.PLAYER1_1));
    p1_2["text"] = str(GameModel.getFieldValue(game.PLAYER1_2));
    p1_3["text"] = str(GameModel.getFieldValue(game.PLAYER1_3));
    p1_4["text"] = str(GameModel.getFieldValue(game.PLAYER1_4));
    p1_5["text"] = str(GameModel.getFieldValue(game.PLAYER1_5));
    p1_6["text"] = str(GameModel.getFieldValue(game.PLAYER1_6));

    p2_1["text"] = str(GameModel.getFieldValue(game.PLAYER2_1));
    p2_2["text"] = str(GameModel.getFieldValue(game.PLAYER2_2));
    p2_3["text"] = str(GameModel.getFieldValue(game.PLAYER2_3));
    p2_4["text"] = str(GameModel.getFieldValue(game.PLAYER2_4));
    p2_5["text"] = str(GameModel.getFieldValue(game.PLAYER2_5));
    p2_6["text"] = str(GameModel.getFieldValue(game.PLAYER2_6));
    
    

p1_1 = Button(fenster, text="0", command=doPlayStep);
p1_2 = Button(fenster, text="0", command=doPlayStep);
p1_3 = Button(fenster, text="0", command=doPlayStep);
p1_4 = Button(fenster, text="0", command=doPlayStep);
p1_5 = Button(fenster, text="0", command=doPlayStep);
p1_6 = Button(fenster, text="0", command=doPlayStep);

p2_1 = Button(fenster, text="0", command=doPlayStep);
p2_2 = Button(fenster, text="0", command=doPlayStep);
p2_3 = Button(fenster, text="0", command=doPlayStep);
p2_4 = Button(fenster, text="0", command=doPlayStep);
p2_5 = Button(fenster, text="0", command=doPlayStep);
p2_6 = Button(fenster, text="0", command=doPlayStep);


points_p1 = Label(fenster, text="0");
points_p2 = Label(fenster, text="0");

p2_1.grid(row=0, column=0, pady = 20);
p1_1.grid(row=1, column=0, pady = 20);
p2_2.grid(row=0, column=1, pady = 20);
p1_2.grid(row=1, column=1, pady = 20);
p2_3.grid(row=0, column=2, pady = 20);
p1_3.grid(row=1, column=2, pady = 20);
p2_4.grid(row=0, column=3, pady = 20);
p1_4.grid(row=1, column=3, pady = 20);
p2_5.grid(row=0, column=4, pady = 20);
p1_5.grid(row=1, column=4, pady = 20);
p2_6.grid(row=0, column=5, pady = 20);
p1_6.grid(row=1, column=5, pady = 20);


updateView(game);

fenster.mainloop();



    
