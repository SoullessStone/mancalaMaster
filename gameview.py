from tkinter import *;
from gamemodel import *;

game = GameModel();

fenster = Tk();

fenster.title("Testfenster");

def doPlayStep():
    fenster.title("Hallo");


p1_var1 = Tk.StringVar();
p1_var2 = Tk.StringVar();
p1_var3 = Tk.StringVar();
p1_var4 = Tk.StringVar();
p1_var5 = Tk.StringVar();
p1_var6 = Tk.StringVar();

p2_var1 = Tk.StringVar();
p2_var2 = Tk.StringVar();
p2_var3 = Tk.StringVar();
p2_var4 = Tk.StringVar();
p2_var5 = Tk.StringVar();
p2_var6 = Tk.StringVar();

p1_var1.set("4");
p1_var2.set("4");
p1_var3.set("4");
p1_var4.set("4");
p1_var5.set("4");
p1_var6.set("4");

p2_var1.set("4");
p2_var2.set("4");
p2_var3.set("4");
p2_var4.set("4");
p2_var5.set("4");
p2_var6.set("4");
    

p1_1 = Button(fenster, textVariable=p1_var1, command=doPlayStep);
p1_2 = Button(fenster, textVariable=p1_var2, command=doPlayStep);
p1_3 = Button(fenster, textVariable=p1_var3, command=doPlayStep);
p1_4 = Button(fenster, textVariable=p1_var4, command=doPlayStep);
p1_5 = Button(fenster, textVariable=p1_var5, command=doPlayStep);
p1_6 = Button(fenster, textVariable=p1_var6, command=doPlayStep);

p2_1 = Button(fenster, textVariable=p2_var1, command=doPlayStep);
p2_2 = Button(fenster, textVariable=p2_var2, command=doPlayStep);
p2_3 = Button(fenster, textVariable=p2_var3, command=doPlayStep);
p2_4 = Button(fenster, textVariable=p2_var4, command=doPlayStep);
p2_5 = Button(fenster, textVariable=p2_var5, command=doPlayStep);
p2_6 = Button(fenster, textVariable=p2_var6, command=doPlayStep);


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


fenster.mainloop();


def updateView(GameModel):
    points_p1.config(text=str(GameModel.getFieldValue(game.PLAYER1_BASE)));
    points_p2.config(text=str(GameModel.getFieldValue(game.PLAYER2_BASE)));
    
    p1_var1.set(GameModel.getFieldValue(game.PLAYER1_1));
    p1_var2.set(GameModel.getFieldValue(game.PLAYER1_2));
    p1_var3.set(GameModel.getFieldValue(game.PLAYER1_3));
    p1_var4.set(GameModel.getFieldValue(game.PLAYER1_4));
    p1_var5.set(GameModel.getFieldValue(game.PLAYER1_5));
    p1_var6.set(GameModel.getFieldValue(game.PLAYER1_6));

    p2_var1.set(GameModel.getFieldValue(game.PLAYER2_1));
    p2_var2.set(GameModel.getFieldValue(game.PLAYER2_2));
    p2_var3.set(GameModel.getFieldValue(game.PLAYER2_3));
    p2_var4.set(GameModel.getFieldValue(game.PLAYER2_4));
    p2_var5.set(GameModel.getFieldValue(game.PLAYER2_5));
    p2_var6.set(GameModel.getFieldValue(game.PLAYER2_6));
    
