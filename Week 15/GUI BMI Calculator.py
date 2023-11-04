#Week 15 Activity 2 , Jason Ng , S10262552

from tkinter import *

#function to calculate bmi
def calculate_bmi():
    weight = float(entWeight.get())
    height = float(entHeight.get())
    txtresult.delete("1.0", END)    # clear the content
    bmi = weight / (height * height)
    txtresult.insert(END, '{:.2f}'.format(bmi))


#Main Menu
window = Tk()			 		
window.title("BMI Calculator")
window.geometry('400x300')

#widgets
lblWeight = Label(window, text="Weight(kg)", width=12)
entWeight = Entry(window, fg='black', width=24)
lblHeight = Label(window, text="Height(m)", width=12)
entHeight = Entry(window, fg='black', width=24)
lblBMI = Label(window, fg = 'blue', text="BMI", width=12)
txtresult = Text(window, bg = 'yellow',fg='blue', width=18, height = 1)
btnCalculate = Button(window, text="Calculate", width=12,command = calculate_bmi)

#place widgets
lblWeight.place(x=20,y=20)
entWeight.place(x=120,y=20)

lblHeight.place(x=20,y=60)
entHeight.place(x=120,y=60)

lblBMI.place(x=20, y=100)
txtresult.place(x=120,y=100)

btnCalculate.place(x=290,y=100)

window.mainloop()
