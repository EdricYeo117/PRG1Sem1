#Week15 Activity 3, Jason Ng, S10262552

from tkinter import *

#def function
#f = ( c * 9 / 5) + 32
def converttofahren():
    celsius = float(enttemp.get())
    entfahren.delete(END)
    fahren = ( celsius * 9 / 5 ) + 32
    entfahren.insert(END, '{:.1f}'.format(fahren))
#c =  (f – 32 ) * 5 / 9
def converttocelcius():
    fahren = float(entfahren.get())
    enttemp.delete(END)
    celcius = (fahren - 32) * 5 / 9
    enttemp.insert(END, '{:.1f}'.format(celcius))
    
    
#main menu
window = Tk()			 		
window.title("Temperature Converter")
window.geometry('400x300')

#widgets
lbltemp = Label(window, text="Temperature(Celcius)", width=15)
enttemp = Entry(window, fg='black',justify = 'center', width=24)
lblfahren = Label(window, text="Temperature(Fahrenheit)", width=20)
entfahren = Entry(window,fg='black',justify = 'center', width=24)
btnConverttoFahren = Button(window, text="Convert C to F", width=18,command = converttofahren)
btnConverttoCel = Button(window, text="Convert F to C", width=18,command = converttocelcius)

#place widgets
lbltemp.place(x=50,y=20)
enttemp.place(x=35,y=50)
btnConverttoFahren.place(x=34,y=80)

lblfahren.place(x=170,y=20)
entfahren.place(x=170,y=50)
btnConverttoCel.place(x=169,y=80)


window.mainloop()
