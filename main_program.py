import sys
import os
from tkinter import *

window=Tk()

window.title("Running Python Script")
window.geometry('550x200')

def run_snake():
    os.system('snake.py')

def run_connect_four():
    os.system('connect_four.py')

def run_superhuman():
    os.system('superhuman.py')
    
def run_tetris():
    os.system('tetris.py')

def run_tictactoe():
    os.system('tictactoe.py')

btn = Button(window, text="Snake Game", bg="black", fg="white",command=run_snake)
btn.grid(column=0, row=0)
btn2 = Button(window, text="Connect four", bg="black", fg="white",command=run_connect_four)
btn2.grid(column=0, row=2)
btn3 = Button(window, text="SuperHuman", bg="black", fg="white",command=run_superhuman)
btn3.grid(column=0, row=4)
btn4 = Button(window, text="Tetris", bg="black", fg="white",command=run_tetris)
btn4.grid(column=0, row=6)
btn5 = Button(window, text="Tic Tac Toe", bg="black", fg="white",command=run_tictactoe)
btn5.grid(column=0, row=8)
window.mainloop()