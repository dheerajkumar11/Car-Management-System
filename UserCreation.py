import tkinter
from tkinter import ttk, LabelFrame
import subprocess
from tkinter import messagebox
import mysql.connector 
from tkinter import Tk, Frame, Label, Button
from tkinter import PhotoImage
from PIL import Image, ImageTk

def AdminLoginpage():
    subprocess.Popen(["python", "AdminLoginpage.py"])
    window.destroy()

def usercreation():
    connection = mysql.connector.connect(host = "localhost", user = "root",password = "Dheeraj@97", database = "PythonProject")
    mycursor = connection.cursor()

    Username = userid_entry.get()
    user_password = password_entry.get()
    Department = department_combobox.get()

    mycursor.execute("INSERT INTO UserCredentials (Username , user_password , Department) VALUES (%s,%s,%s)" , (Username , user_password , Department ))
    
    messagebox.showinfo("Message", "ID created Succesfully")
    subprocess.Popen(["python", "AdminLoginpage.py"])
    window.destroy()

    connection.commit()
    connection.close()


window = tkinter.Tk()
window.title("User Creation")
window.geometry("1360x1000")

bg_image = Image.open("useraddition123.png")
bg_image = bg_image.resize((1360, 780), Image.ANTIALIAS)
bg1 = ImageTk.PhotoImage(bg_image)

label2 = Label(window, image=bg1)
label2.image = bg1
label2.place(x=0, y=0, relwidth=1, relheight=1)

frame = tkinter.Frame(window, bg="#000000")
frame.place(relx=0.295, rely=0.535, anchor="center")


usercreation_frame = tkinter.LabelFrame(frame, text='',font=("Arial", 20), bg="#000000", fg="#FDF0E0",padx=20, pady=20)
usercreation_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)

userid_label = tkinter.Label(usercreation_frame, text="User ID:",font=("Arial", 20), bg="#000000", fg="#FDF0E0")
userid_label.grid(row=0, column=0)
userid_entry = tkinter.Entry(usercreation_frame)
userid_entry.grid(row=0, column=1)

password_label = tkinter.Label(usercreation_frame, text="Password:",font=("Arial", 20),bg="#000000", fg="#FDF0E0")
password_label.grid(row=1, column=0)
password_entry = tkinter.Entry(usercreation_frame)
password_entry.grid(row=1, column=1)

department_label = tkinter.Label(usercreation_frame, text="Department:",font=("Arial", 20), bg="#000000",fg="#FDF0E0")
department_label.grid(row=2, column=0)
department_combobox = ttk.Combobox(usercreation_frame, values=["", "Sales", "Service"], width=17)
department_combobox.grid(row=2, column=1)


for widget in usercreation_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

buttons_frame = tkinter.LabelFrame(frame, text="",font=("Arial", 20), bg="#000000", padx=20, pady=20)
buttons_frame.grid(row=4, column=0, sticky="news", padx=20, pady=10)

btnCreateUser = tkinter.Button(buttons_frame, width=10, text="Create User",font=("Comic Sans MS", 20,'bold'), bg="mint cream", command=usercreation)
btnCreateUser.grid(row=0, column=0)

btnMainPage = tkinter.Button(buttons_frame, width=10, text="Main Page",font=("Comic Sans MS", 20,'bold'), bg="mint cream", command=AdminLoginpage)
btnMainPage.grid(row=0, column=1)

btnExit = tkinter.Button(buttons_frame, width=10, text="Exit",font=("Comic Sans MS", 20,'bold'), bg="mint cream", command=window.destroy)
btnExit.grid(row=0, column=2)

for widget in buttons_frame.winfo_children():
    widget.grid_configure(padx=25, pady=5)

window.mainloop()