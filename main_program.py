import sys
import os
from tkinter import *
from tkinter import simpledialog,ttk

window=Tk()

# Add image file
bg = PhotoImage(file = "images/template.png")
  
# Show image using label
label1 = Label( window, image = bg)
label1.place(x = 0, y = 0)

width = 800 # Width 
height = 800 # Height
 
screen_width = window.winfo_screenwidth()  # Width of the screen
screen_height = window.winfo_screenheight() # Height of the screen
 
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)


window.title("Py-Retro")
window.geometry('%dx%d+%d+%d' % (width, height, x, y))

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
    

def display_text():
   global entry
   string= entry.get()
   label.configure(text=string)
   entry.delete(0, END)
   btn_inp.after(1, btn_inp.destroy)
   entry.after(1,entry.destroy)

#Initialize a Label to display the User Input
label=Label(window, text="", font=("Courier 22 bold"))
label.grid(column=1, row=0)
# label.pack()

#Create an Entry widget to accept User Input
entry= Entry(window, width= 40)
entry.focus_set()
entry.grid(column=1, row=1)
# entry.pack()

#Create a Button to validate Entry Widget
btn_inp=Button(window, text= "Okay",width= 20, command= display_text)
# btn_label.grid(column=1, row=0)
btn_inp.grid(column=1,row=2)



btn = Button(window, text="Snake Game", bg="black", fg="white",command=run_snake)
btn.grid(column=0, row=4)
btn2 = Button(window, text="Connect four", bg="black", fg="white",command=run_connect_four)
btn2.grid(column=0, row=6)
btn3 = Button(window, text="SuperHuman", bg="black", fg="white",command=run_superhuman)
btn3.grid(column=0, row=8)
btn4 = Button(window, text="Tetris", bg="black", fg="white",command=run_tetris)
btn4.grid(column=0, row=10)
btn5 = Button(window, text="Tictactoe", bg="black", fg="white",command=run_tictactoe)
btn5.grid(column=0, row=12)
window.mainloop()