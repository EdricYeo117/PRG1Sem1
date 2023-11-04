#Week15 Activity 4, Jason Ng , S10262552
# 1. Import tkinter 
from tkinter import *

def placemulti():
    f2.pack()
    f2.pack_forget()
    f1.place(x=160,y=20)
def placebmi():
    f1.pack()
    f1.pack_forget()
    f2.place(x=160,y=20)
        
def display_table():
    n = int(entNumber.get())
    txtTable.delete("1.0", END)    # clear the content
    for i in range(1,13):
        row = "{:3} x {:2} = {:3}\n".format(i, n, i * n)
        txtTable.insert(END, row)  # insert new content
        
def calculate_bmi():
    weight = float(entWeight.get())
    height = float(entHeight.get())
    txtresult.delete("1.0", END)    # clear the content
    bmi = weight / (height * height)
    txtresult.insert(END, '{:.2f}'.format(bmi))

#main menu
window = Tk()
window.title('Sample GUI Application')
window.geometry('700x500')

# Frame Math
f1 = Frame(window, bg='light yellow', width=400, height=350)

lblNumber = Label(f1, text="Enter number", width=12)
entNumber = Entry(f1, fg='red', width=24)
btnDisplay = Button(f1, text="Display table", width=12 ,command = display_table)
txtTable = Text(f1, fg='blue', width=18, height=12)


# Frame BMI
f2 = Frame(window, bg='light blue', width=400, height=350)
lblWeight = Label(f2, text="Weight(kg)", width=12)
entWeight = Entry(f2, fg='black', width=24)
lblHeight = Label(f2, text="Height(m)", width=12)
entHeight = Entry(f2, fg='black', width=24)
lblBMI = Label(f2, fg = 'blue', text="BMI", width=12)
txtresult = Text(f2, bg = 'yellow',fg='blue', width=18, height = 1)
btnCalculate = Button(f2, text="Calculate", width=12,command = calculate_bmi)

# frame select
f3 = Frame(window, bg='light gray', width=150, height=350)
lblmainmenu = Label(f3, text = 'Main Menu' ,fg ='blue', bg ='light gray' , font = ('Arial',13) , width = 14)
btnMultitable = Button(f3,text = 'Multiplaction Table',fg = 'blue',width=14,command = placemulti)
btnBMI = Button(f3,text = 'BMI Calculator',fg = 'blue',width=14,command = placebmi)

#Place mainmenu
f3.place(x=10,y=20)
lblmainmenu.place(x=10,y=20)
btnMultitable.place(x=20,y=55)
btnBMI.place(x=20,y=100)

f1.place(x=160,y=20)
lblNumber.place(x=20, y=20)
btnDisplay.place(x=20, y=60)
entNumber.place(x=120, y=20)
txtTable.place(x=120, y=60)

f2.place(x=160,y=20)
lblWeight.place(x=20,y=20)
entWeight.place(x=120,y=20)
lblHeight.place(x=20,y=60)
entHeight.place(x=120,y=60)
lblBMI.place(x=20, y=100)
txtresult.place(x=120,y=100)
btnCalculate.place(x=290,y=100)
    
window.mainloop()
