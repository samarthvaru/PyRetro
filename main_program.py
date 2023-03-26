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

width = 600 # Width 
height = 600 # Height
 
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

button_image = PhotoImage(file="images/Tic Tac Toe.png")


# create a frame to contain the buttons
button_frame = Frame(window)
button_frame.pack()
button_frame.image = button_image

#Initialize a Label to display the User Input
label=Label(button_frame, text="", font=("Courier 22 bold"))
# label.grid(column=1, row=0)
label.place(relx = 0.5,
                   rely = 0.5,
                   anchor = 'center')
# label.pack()

#Create an Entry widget to accept User Input
entry= Entry(button_frame, width= 40, bd=0, highlightthickness=0)
entry.focus_set()
entry.pack()
# entry.pack()

#Create a Button to validate Entry Widget
btn_inp=Button(button_frame, text= "Okay",width= 20, command= display_text)
# btn_label.grid(column=1, row=0)
btn_inp.pack()



# create 5 buttons in the frame
button1 = Button(button_frame,text="Snake Game", bd=0, fg="white",font=("Helvetica", 20),command=run_snake,width=20, height=1,highlightthickness=0)
button1.pack(padx=10, pady=10)

button2 = Button(button_frame, text="Connect four",bd=0, fg="white",font=("Helvetica", 20),command=run_connect_four,width=20, height=1,highlightthickness=0, highlightbackground="white")
button2.pack(padx=10, pady=10)

button3 = Button(button_frame, text="SuperHuman",bd=0, fg="white",font=("Helvetica", 20),command=run_superhuman,width=20, height=1,highlightthickness=0, highlightbackground="white")
button3.pack(padx=10, pady=10)

button4 = Button(button_frame, text="Tetris",bd=0, fg="white",font=("Helvetica", 20),command=run_tetris,width=20, height=1,highlightthickness=0, highlightbackground="white")
button4.pack(padx=10, pady=10)

button5 = Button(button_frame, text="Tictactoe",bd=0, image= button_image,fg="white",font=("Helvetica", 20),command=run_tictactoe,highlightthickness=0, highlightbackground="white")
button5.pack(padx=10, pady=10)

# center the frame containing the buttons
button_frame.place(relx=0.5, rely=0.6, anchor="center")


window.mainloop()