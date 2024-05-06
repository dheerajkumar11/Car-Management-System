import tkinter
from tkinter import *
from tkinter import ttk
import subprocess
import mysql.connector 
from PIL import Image, ImageTk

def AdminLoginPage():
    subprocess.Popen(["python", "AdminLoginpage.py"])
    window.destroy()

connection = mysql.connector.connect(host = "localhost", user = "root",password = "Dheeraj@97", database = "PythonProject")
mycursor = connection.cursor()

mycursor.execute("SELECT * FROM UserCredentials WHERE Department !='admin' ")


window = tkinter.Tk()
window.title("Sale Report")
window.geometry("800x400")

bg_image = Image.open("report123.png")
bg_image = bg_image.resize((800, 400), Image.ANTIALIAS)
bg1 = ImageTk.PhotoImage(bg_image)

label2 = Label(window, image=bg1)
label2.image = bg1
label2.place(x=0, y=0, relwidth=1, relheight=1)


style = ttk.Style()
style.theme_use('clam')
style.configure("Treeview", background="white", 
                fieldbackground="white", foreground="black")

tree = ttk.Treeview(window, column=("Username", "Password", "Department"), show='headings', height=11)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Username")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Password")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Department")

i = 0

for x in mycursor:
    tree.insert('', i , text = "" , values = (x[0] , x[1] , x[2]))
    i = i + 1


tree.pack()

frame = tkinter.Frame(window)
frame.pack()

buttons_frame = tkinter.LabelFrame(frame, text="")
buttons_frame.grid(row=4, column=0, sticky="news", padx=20, pady=10)

btnSignout = tkinter.Button(buttons_frame, width=10, text="Back", command=AdminLoginPage)
btnSignout.grid(row=1, column=0)

btnExit = tkinter.Button(buttons_frame, width=10, text="Exit", command=window.destroy)
btnExit.grid(row=1, column=2)

for widget in buttons_frame.winfo_children():
    widget.grid_configure(padx=60, pady=10)

window.mainloop()