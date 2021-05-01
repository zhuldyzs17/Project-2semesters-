#importing libraries pandas and csv
import csv
import pandas as pd

def calendar_olympic():
    f = pd.read_csv("https://raw.githubusercontent.com/zhuldyzs17/Project-2semesters-/main/Calendar.csv")
    print(f)
    
def medals_olympic():
    a = pd.read_csv("https://raw.githubusercontent.com/zhuldyzs17/Project-2semesters-/main/Medals.csv")
    print(a)

def athlets_olympic():
    d = pd.read_csv("https://raw.githubusercontent.com/zhuldyzs17/Project-2semesters-/main/Athlets.csv")
    print(d)

def kazakhstan_inRIO():
    x = pd.read_csv("https://raw.githubusercontent.com/zhuldyzs17/Project-2semesters-/main/Kazakhstan.csv")
    print(x)


#importing tkinter library
import tkinter as tk

#Create a window that shows buttons
win = tk.Tk()
win.title('Rio de Janeiro 2016')
win.config(bg = '#F0F8FF')
win.geometry("500x400")
win.minsize(400,400)
win.maxsize(200,200)
win.resizable(True, True)

#writing text for description
tk.Label(win, text='Summer Olympics Statistics 2016',
         bg=['black'],fg=['red'],
         font=("Calibri" ,20, "bold")
         ).pack()

#Create Buttons
btn1 = tk.Button(win, text="Calendar",
                 command=calendar_olympic,
                 bg=['#FF1493'],
                 fg=['black'],
                 font=("Arial", 20," bold"),
                 width=20,
                 height=1,
                 bd=10,
                 activebackground=['white']
                 )
 
btn2 = tk.Button(win, text="Medals",
                 command=medals_olympic,
                 bg=['#EE82EE'],
                 fg=['black'],
                 font=("Arial", 20, "bold"),
                 width=20,
                 height=1,
                 bd=10,
                 activebackground=['white']
                 )

btn3 = tk.Button(win, text="Athlets",
                 command=athlets_olympic,
                 bg=['#FF00FF'],
                 fg=['black'],
                 font=("Arial", 20, "bold"),
                 width=20,
                 height=1,
                 bd=10,
                 activebackground=['white']
                 )

btn4 = tk.Button(win, text="Kazakhstan",
                 command=kazakhstan_inRIO,
                 bg=['#FFC0CB'],
                 fg=['black'],
                 font=("Arial", 20 ,"bold"),
                 width=20,
                 height=1,
                 bd=10,
                 )


#allows you to position items on the window
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()


#the main loop that lauches the window
win.mainloop()

