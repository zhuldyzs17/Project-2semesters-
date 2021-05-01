#importing libraries pandas and csv
import csv
import pandas as pd

#Create classes for each buttons
#here will be a link to the csv file that we will receive information
def calendar_olympic():
    f = pd.read_csv("https://raw.githubusercontent.com/zhuldyzs17/Project-2semesters-/main/Calendar.csv")
    print(f.to_string(max_rows=10))
    
def medals_olympic():
    a = pd.read_csv("https://raw.githubusercontent.com/zhuldyzs17/Project-2semesters-/main/Medals.csv")
    print(a.to_string(max_rows=10))

def athlets_olympic():
    d = pd.read_csv("https://raw.githubusercontent.com/zhuldyzs17/Project-2semesters-/main/Athlets.csv")
    print(d.to_string(max_rows=10))

def kazakhstan_inRIO():
    x = pd.read_csv("https://raw.githubusercontent.com/zhuldyzs17/Project-2semesters-/main/Kazakhstan.csv")
    print(x.to_string(max_rows=10))

def tokyo2020():
    y = pd.read_csv("https://raw.githubusercontent.com/zhuldyzs17/Project-2semesters-/main/TOKYO2020.csv")
    print(y.to_string(max_rows=10))

#importing tkinter library
import tkinter as tk

#Create a window that shows buttons
root = tk.Tk()
root.title('Rio de Janeiro 2016')
root.config(bg = '#FFDAB9')
root.geometry("500x400")
root.minsize(400,400)
root.maxsize(200,200)
root.resizable(True, True)

#writing text for description
tk.Label(root, text='Summer Olympics Statistics 2016',
         bg=['#F0FFFF'],fg=['#778899'],
         font=("Calibri" ,20, "bold"),
         width=130,
         height=1,
         bd=10,
         activebackground=['black']
         ).pack()

#Create Buttons
#and edit these created buttons
btn1 = tk.Button(root, text="Calendar",
                 command=calendar_olympic,
                 bg=['#FF1493'],
                 fg=['black'],
                 font=("Arial", 20," bold"),
                 width=20,
                 height=1,
                 bd=10,
                 activebackground=['white']
                 )

btn2 = tk.Button(root, text="Medals",
                 command=medals_olympic,
                 bg=['#EE82EE'],
                 fg=['black'],
                 font=("Arial", 20, "bold"),
                 width=20,
                 height=1,
                 bd=10,
                 activebackground=['white']
                 )

btn3 = tk.Button(root, text="Athlets",
                 command=athlets_olympic,
                 bg=['#FF00FF'],
                 fg=['black'],
                 font=("Arial", 20, "bold"),
                 width=20,
                 height=1,
                 bd=10,
                 activebackground=['white']
                 )

btn4 = tk.Button(root, text="Kazakhstan",
                 command=kazakhstan_inRIO,
                 bg=['#FFC0CB'],
                 fg=['black'],
                 font=("Arial", 20 ,"bold"),
                 width=20,
                 height=1,
                 bd=10,
                 activebackground=['white']
                 )

btn5 = tk.Button(root, text="Tokyo2020",
                 command=tokyo2020,
                 bg=['#FF69B4'],
                 fg=['black'],
                 font=("Arial", 20 ,"bold"),
                 width=20,
                 height=1,
                 bd=10,
                 activebackground=['white']
                 )


#allows you to position items on the window
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()

#the main loop that lauches the window
root.mainloop()
