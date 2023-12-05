from tkinter import *


die = {
0 : '🎲',
1 : '⚀',
2 : '⚁',
3 : '⚂',
4 : '⚃',
5 : '⚄',
6 : '⚅',
}

App = Tk()
# App.iconbitmap(r"ye.ico")
# App.title('Dice Roller')
# App.geometry('700x600')
App['background'] = 'black'


Dice = Label(App, text=die[0], font=('Times', 100),foreground='white', background='black')
Dice.grid(row=0, column=0, padx=25, pady=5)

def roll():
    from random import randint
    i = randint(0,6)
    msg = Label(App, text=die[i], font=('Times', 100), foreground='white',background='black', width=2)
    msg.grid(row=0, column=0, padx=25, pady=5)


B = Button(App, text='Roll', command=roll)
B.grid(row=1, column=0)
    


App.mainloop()