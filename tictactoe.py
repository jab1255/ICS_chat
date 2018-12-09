from tkinter import *
import tkinter.messagebox
tkk = Tk()
tkk.title("ICS TIC TAC TOE")

gg = True

def c(b):
    
    global gg
    
    if b['text'] == " " and gg == True:
        #Send to server : {}
        b['text'] = "X"
        gg = False
        
    if b['text'] == " " and gg == False:
        b['text'] = "O"
        gg = True    
        
        
        
    elif(b1['text'] == "X" and b2['text'] == 'X' and b3['text'] == 'X' or
         b4['text'] == "X" and b5['text'] == 'X' and b6['text'] == 'X' or
         b7['text'] == "X" and b8['text'] == 'X' and b9['text'] == 'X' or
         b3['text'] == "X" and b5['text'] == 'X' and b7['text'] == 'X' or
         b1['text'] == "X" and b5['text'] == 'X' and b9['text'] == 'X' or
         b1['text'] == "X" and b4['text'] == 'X' and b7['text'] == 'X' or
         b2['text'] == "X" and b5['text'] == 'X' and b8['text'] == 'X' or
         b3['text'] == "X" and b6['text'] == 'X' and b9['text'] == 'X'):
        tkinter.messagebox.showinfo("Resukts", "X just won the game")
    
    elif(b1['text'] == "O" and b2['text'] == 'O' and b3['text'] == 'O' or
         b4['text'] == "O" and b5['text'] == 'O' and b6['text'] == 'O' or
         b7['text'] == "O" and b8['text'] == 'O' and b9['text'] == 'O' or
         b3['text'] == "O" and b5['text'] == 'O' and b7['text'] == 'O' or
         b1['text'] == "O" and b5['text'] == 'O' and b9['text'] == 'O' or
         b1['text'] == "O" and b4['text'] == 'O' and b7['text'] == 'O' or
         b2['text'] == "O" and b5['text'] == 'O' and b8['text'] == 'O' or
         b3['text'] == "O" and b6['text'] == '0' and b9['text'] == 'O'):
        tkinter.messagebox.showinfo("Results" , "O just won the game")
        
        
b = StringVar() 

b1 = Button(tkk,text=" ",font = ('courier 34 bold'), height = 4, width = 8, command = lambda: c(b1))
b1.grid(row=1, column = 0, sticky= S+N+E+W)
b2 = Button(tkk,text=" ",font = ('courier 34 bold'), height = 4, width = 8, command = lambda: c(b2))
b2.grid(row=1, column = 1, sticky = S+N+E+W)
b3 = Button(tkk,text=" ",font = ('courier 34 bold'), height = 4, width = 8, command = lambda: c(b3))
b3.grid(row=1, column = 2, sticky = S+N+E+W)
b4 = Button(tkk,text=" ",font = ('courier 34 bold'), height = 4, width = 8, command = lambda: c(b4))
b4.grid(row=2, column = 0, sticky = S+N+E+W)
b5 = Button(tkk,text=" ",font = ('courier 34 bold'), height = 4, width = 8, command = lambda: c(b5))
b5.grid(row=2, column = 1, sticky = S+N+E+W)
b6 = Button(tkk,text=" ",font = ('courier 34 bold'), height = 4, width = 8, command = lambda: c(b6))
b6.grid(row=2, column = 2, sticky = S+N+E+W)
b7 = Button(tkk,text=" ",font = ('courier 34 bold'), height = 4, width = 8, command = lambda: c(b7))
b7.grid(row=3, column = 0, sticky = S+N+E+W)
b8 = Button(tkk,text=" ",font = ('courier 34 bold'), height = 4, width = 8, command = lambda: c(b8))
b8.grid(row=3, column = 1, sticky = S+N+E+W)
b9 = Button(tkk,text=" ",font = ('courier 34 bold'), height = 4, width = 8, command = lambda: c(b9))
b9.grid(row=3, column = 2, sticky = S+N+E+W)
tkk.mainloop()
       
        
    