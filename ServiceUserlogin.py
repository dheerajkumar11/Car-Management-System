import tkinter
from tkinter import ttk
from tkinter import messagebox
import subprocess
import sys
import mysql.connector 
from tkinter import Tk, Frame, Label, Button
from tkinter import PhotoImage
from PIL import Image, ImageTk

def main():
    subprocess.Popen(["python", "main.py"])
    window.destroy()

def toggle_password_visibility():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

def ServiceLoginpage():

    connection = mysql.connector.connect(host = "localhost", user = "root",password = "Dheeraj@97", database = "PythonProject")
    mycursor = connection.cursor()

    mycursor.execute("SELECT * FROM UserCredentials WHERE Username = '"+ userid_entry.get()+"' AND user_password = '"+password_entry.get()+"' AND Department = 'Service';")
    result = mycursor.fetchone()

    if result == None :
        subprocess.Popen(["python", "ServiceWrongCred.py"])
        window.destroy()

    else:

        messagebox.showinfo("Message", "Login Successful")
        subprocess.Popen(["python", "ServiceLoginpage.py"])
        window.destroy()


window = tkinter.Tk()
window.title("AutoDealer Insight Service Login")
window.geometry("1360x1000")

bg_image = Image.open("servicelogin123.png")
bg_image = bg_image.resize((1360, 800), Image.ANTIALIAS)
bg1 = ImageTk.PhotoImage(bg_image)

label2 = Label(window, image=bg1)
label2.image = bg1
label2.place(x=0, y=0, relwidth=1, relheight=1)

frame = tkinter.Frame(window, bg="#DFF8FC")
frame.place(relx=0.685, rely=0.5, anchor="center")

user_info_frame = tkinter.LabelFrame(frame, text='Service Login' , font=("Arial", 20 , 'bold'), bg="#DFF8FC", padx=20, pady=20)
user_info_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)

userid_label = tkinter.Label(user_info_frame, text="User ID:" , font=("Arial", 20 , 'bold'), bg="#DFF8FC", padx=20, pady=20)
userid_label.grid(row=0, column=0)

password_label = tkinter.Label(user_info_frame, text="Password:" , font=("Arial", 20 , 'bold'), bg="#DFF8FC", padx=20, pady=20)
password_label.grid(row=1, column=0)  # r=1, column = 0

userid_entry = tkinter.Entry(user_info_frame , font=("Arial", 20))
password_entry = tkinter.Entry(user_info_frame , show = "*" , font=("Arial", 20))
userid_entry.grid(row=0, column=1)  # row = 0 col = 1
password_entry.grid(row=1, column=1)

show_password_var = tkinter.BooleanVar()
show_password_checkbox = tkinter.Checkbutton(
    user_info_frame,
    text="Show Password",
    variable=show_password_var,
    command=toggle_password_visibility,
    font=("Arial", 16 , 'bold'),
    bg="#DFF8FC",
)
show_password_checkbox.grid(row=1, column=2, sticky="w")

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Buttons
buttons_frame = tkinter.LabelFrame(frame, text="", font=("Arial", 20), bg="#DFF8FC", padx=20, pady=20)
buttons_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)

btnSignIn = tkinter.Button(buttons_frame, width=10, text="Sign-In", font=("Comic Sans MS", 20 , 'bold'), command=ServiceLoginpage)
btnSignIn.grid(row=3, column=0)

btnSignIn = tkinter.Button(buttons_frame, width=10, text="Main page", font=("Comic Sans MS", 20 , 'bold'), command=main)
btnSignIn.grid(row=3, column=1)

btnExit = tkinter.Button(buttons_frame, width=10, text="Exit", font=("Comic Sans MS", 20 , 'bold'), command=window.destroy)
btnExit.grid(row=3, column=2)

for widget in buttons_frame.winfo_children():
    widget.grid_configure(padx=30, pady=10)

window.mainloop()