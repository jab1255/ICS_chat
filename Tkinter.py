# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 17:21:34 2018

@author: User
"""

from tkinter import *

# initialize the window 
root = Tk()

##Frame = "Blank space to put on stuff"
#topframe = Frame(root)
##place the frame in window
#topframe.pack()
#bottomframe = Frame(root)
#bottomframe.pack(side = BOTTOM)
#
##creating a button 
#button1 = Button(topframe, text = "Button 1", fg = "green")
#button2 = Button(topframe, text = "2", fg = "red")
#button3 = Button(topframe, text = "3", fg = "yellow")
#button4 = Button(bottomframe, text = "OK", fg = "blue")
#
##DO NOT Forget to pack 
#button1.pack(side = LEFT)
#button2.pack(side = LEFT)
#button3.pack(side = LEFT)
#button4.pack(side = BOTTOM)
#
#one = Label (root, text = "One", bg = "Red", fg = "White")
#one.pack()
## bg = background color; fg = font color
#two = Label (root, text = "TWO", bg = "green", fg = "black")
##fill = X makes the label as wide as the x value of the window
#two.pack(fill = X)
#three =Label (root, text = "WHAT", bg = "black", fg = "white")
#three.pack (side = RIGHT, fill = Y)

#use grid layout for more control over the window design 
login_label = Label(root, text = "NAME")
passw_label = Label(root, text = "PASSWORD")
entry_1 = Entry(root)
entry_2 = Entry(root)
#by default column = 0, sticky = aling (North, East, West, South)
login_label.grid(row = 0, sticky = E)
entry_1.grid(row = 0, column = 1)
passw_label.grid(row = 1, sticky = E)
entry_2.grid(row = 1, column = 1)

c = Checkbutton(root, text = "Remember me")
c.grid(columnspan = 2)

#binding a function to a widget 
def printName():
    print("Hello my name is Jorge")
#this print in the Console
button_1 = Button(root, text = "Print my name", command = printName)
button_1.grid(columnspan = 3, sticky = W)

#binding a function to a widget part 2 : WATING FOR AN EVENT
def printName2(event):
    print("Hello my name is Jorge")

button_2 = Button(root, text = "AAA")
#"<Button-1>" : RIGHT MOUSE CLICK
button_2.bind("<Button-1>", printName2)
button_2.grid(row = 2, column = 2)

def leftClick(event):
    print('left')

def middleClick(event):
    print('center')

def rightClick(event):
    print('right')
    
frame = Frame(root, width = 300, height = 300)
frame.bind("<Button-1>", leftClick)
#midleClick = scrolling down thingy on the mouse
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
frame.grid(row = 4)
'''
Events: 
    '''

# loop it until closing window 
root.mainloop()