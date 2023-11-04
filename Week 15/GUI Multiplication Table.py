#Week 15 Activity 1 , Jason Ng , S10262552

# 1. Import tkinter 
from tkinter import *

# 2. Define functions
def display_table():
    n = int(entNumber.get())
    txtTable.delete("1.0", END)    # clear the content
    for i in range(1,13):
        row = "{:3} x {:2} = {:3}\n".format(i, n, i * n)
        txtTable.insert(END, row)  # insert new content
        
# 3. Create main window 
window = Tk()			 		
window.title("Multiplication Table")
window.geometry('400x300')

# 4. Add widgets e.g. Label, Entry, Button, Text
lblNumber = Label(window, text="Enter number", width=12)
entNumber = Entry(window, fg='red', width=24)
btnDisplay = Button(window, text="Display table", width=12 ,command = display_table)
txtTable = Text(window, fg='blue', width=18, height=12)

# Organize (lay out) the widgets using place() manager
lblNumber.place(x=20, y=20)     # column 1, row 1
btnDisplay.place(x=20, y=60)    # column 1, row 2
entNumber.place(x=120, y=20)    # column 2, row 1
txtTable.place(x=120, y=60)     # column 2, row 2

# 5. Add main event loop (to handle user events)
window.mainloop()

