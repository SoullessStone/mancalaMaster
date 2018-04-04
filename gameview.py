from tkinter import *;

fenster = Tk();

fenster.title("Testfenster");

def doPlayStep():
    fenster.title("Hallo");

p1_1 = Button(fenster, text="4", command=doPlayStep);
p1_2 = Button(fenster, text="4", command=doPlayStep);
p1_3 = Button(fenster, text="4", command=doPlayStep);
p1_4 = Button(fenster, text="4", command=doPlayStep);
p1_5 = Button(fenster, text="4", command=doPlayStep);
p1_6 = Button(fenster, text="4", command=doPlayStep);

p2_1 = Button(fenster, text="4", command=doPlayStep);
p2_2 = Button(fenster, text="4", command=doPlayStep);
p2_3 = Button(fenster, text="4", command=doPlayStep);
p2_4 = Button(fenster, text="4", command=doPlayStep);
p2_5 = Button(fenster, text="4", command=doPlayStep);
p2_6 = Button(fenster, text="4", command=doPlayStep);


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
