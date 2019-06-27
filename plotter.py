from tkinter import *
import matplotlib.pyplot as plt
import fnmatch
import os
from tkinter import messagebox


def getvalue(lower,upper,y,m,d): # Function to get the values of temperature and time from the file
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file,f"Temp_log_{y}_{m}_{d}*"): # Checks if the file on a date exists
            f = open(file,"r")
            l = f.readlines()
            x = []
            y = []
            x_s = []
            y_s = []
            f.close()
            # splits the lines into an array containing the values then retrieves the useful values
            for i in l:
                sub = i.split("\t")
                x += [float(sub[3]+"."+sub[4])]
                y += [float(sub[6])]
            for i in range(len(x)):
                if x[i]>=lower and x[i]<upper:
                    x_s.append(x[i])
                    y_s.append(y[i])

    return x_s,y_s
    
def marker(x,y): # Function to plot the graph
    plt.xlabel("Time(hours)")
    plt.ylabel("Temperature(degree Celsius)")
    plt.title("Temperature vs Time")
    plt.grid(True)
    plt.plot(x,y)
    plt.show()

def layout(): # Defines the layout of the app
    #Setting up the window
    window = Tk()
    window.title("Temperature Plotter")
    window.geometry('350x200')

    #Setting Up the input area
    year  = Label(window, text="Enter The Year")
    month = Label(window, text="Enter The Month")
    date  = Label(window, text="Enter The Date")

    year.grid(column=1, row=1)
    month.grid(column=1, row=2)
    date.grid(column=1, row=3)

    year_txt = Entry(window,width=10)
    year_txt.grid(column=2, row=1)
    
    month_txt = Entry(window,width=10)
    month_txt.grid(column=2, row=2)
    
    date_txt = Entry(window,width=10)
    date_txt.grid(column=2, row=3)
    
    ''' There are three shifts 00:00 to 08:00
        08:00 to 16:00 and 16:00 to 23:59 '''

    def shift_one():
        y = year_txt.get()
        m = month_txt.get()
        d = date_txt.get()             
        try:
            x_s,y_s = getvalue(0,8,y,m,d)  
            marker(x_s,y_s)
        except:
            messagebox.showwarning("Check the Date","File does not exit or No date entered")
            


    def shift_two():
        y = year_txt.get()
        m = month_txt.get()
        d = date_txt.get()
        try:
            x_s,y_s = getvalue(8,16,y,m,d)  
            marker(x_s,y_s)
        except:
            messagebox.showwarning("Check the Date","File does not exit or No date entered")
                

    def shift_three():
        y = year_txt.get()
        m = month_txt.get()
        d = date_txt.get()
        try:
            x_s,y_s = getvalue(16,24,y,m,d)  
            marker(x_s,y_s)
        except:
            messagebox.showwarning("Check the Date","File does not exit or No date entered")


    btn1 = Button(window, text="Shift One", command=shift_one)
    btn1.grid(column=1, row=4)
    
    btn2 = Button(window, text="Shift Two", command=shift_two)
    btn2.grid(column=2, row=4)
    
    btn3 = Button(window, text="Shift Three", command=shift_three)
    btn3.grid(column=3, row=4)
    
    window.mainloop()


if __name__ == "__main__":
    layout()
