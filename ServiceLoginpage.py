import tkinter
from tkinter import ttk
from tkinter import messagebox
import subprocess
import sys
import mysql.connector 
from tkinter import Tk, Frame, Label, Button
from tkinter import PhotoImage
from PIL import Image, ImageTk

def ServiceRequest():
    subprocess.Popen(["python", "ServiceRequestser.py"])
    window.destroy()

def ServiceUserlogin():
    subprocess.Popen(["python", "ServiceUserlogin.py"])
    window.destroy()

def ServiceReport():
    subprocess.Popen(["python", "ServiceReportser.py"])
    window.destroy()

def Changepass():
    subprocess.Popen(["python", "ChangePassSer.py"])
    window.destroy()

window = tkinter.Tk()
window.title("Welcome.")
window.geometry("1360x1000")

bg_image = Image.open("serviceslogin123.png")
bg_image = bg_image.resize((1360, 780), Image.ANTIALIAS)
bg1 = ImageTk.PhotoImage(bg_image)

label2 = Label(window, image=bg1)
label2.image = bg1
label2.place(x=0, y=0, relwidth=1, relheight=1)

frame = tkinter.Frame(window ,bg="#57AEFE")
frame.place(relx=0.27, rely=0.55, anchor="center")


servicetasks_frame = tkinter.LabelFrame(frame, text='Tasks' , font=("Arial", 15 , 'bold'), bg="#57AEFE", padx=20, pady=20)
servicetasks_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)

btnServiceTicket = tkinter.Button(servicetasks_frame, width=20, text="Create Service Ticket", font=("Comic Sans MS", 15,'bold'), bg="gray64", command=ServiceRequest)
btnServiceTicket.grid(row=0, column=0)

btnReports = tkinter.Button(servicetasks_frame, width=20, text="Generate Service Report", font=("Comic Sans MS", 15,'bold'), bg="gray64", command=ServiceReport)
btnReports.grid(row=1, column=0)

for widget in servicetasks_frame.winfo_children():
    widget.grid_configure(padx=30, pady=10)


buttons_frame = tkinter.LabelFrame(frame, text="", font=("Arial", 20 , 'bold'), bg="#57AEFE", padx=20, pady=20)
buttons_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

btnChangepass = tkinter.Button(buttons_frame, width=20, text="Change Password", font=("Comic Sans MS", 15,'bold'), bg="gray63" , command=Changepass)
btnChangepass.grid(row=1, column=0 )

btnSignout = tkinter.Button(buttons_frame, width=20, text="Sign out", font=("Comic Sans MS", 15,'bold'), bg="gray64", command=ServiceUserlogin)
btnSignout.grid(row=2, column=0)

btnExit = tkinter.Button(buttons_frame, width=20, text="Exit", font=("Comic Sans MS", 15,'bold'), bg="gray64", command=window.destroy)
btnExit.grid(row=3, column=0)

for widget in buttons_frame.winfo_children():
    widget.grid_configure(padx=30, pady=10)

window.mainloop()