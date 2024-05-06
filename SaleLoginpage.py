import tkinter
from tkinter import ttk
from tkinter import messagebox
import subprocess
import sys
import mysql.connector 
from tkinter import Tk, Frame, Label, Button
from tkinter import PhotoImage
from PIL import Image, ImageTk

def SaleUserlogin():
    subprocess.Popen(["python", "SaleUserlogin.py"])
    window.destroy()

def CreateInvoice():
    subprocess.Popen(["python", "Createinvoicesale.py"])
    window.destroy()

def SaleReport():
    subprocess.Popen(["python", "SaleReportsale.py"])
    window.destroy()

def Changepass():
    subprocess.Popen(["python", "ChangePassSale.py"])
    window.destroy()

window = tkinter.Tk()
window.title("Welcome.")
window.geometry("1360x1000")

bg_image = Image.open("salelogin123.png")
bg_image = bg_image.resize((1360, 780), Image.ANTIALIAS)
bg1 = ImageTk.PhotoImage(bg_image)

label2 = Label(window, image=bg1)
label2.image = bg1
label2.place(x=0, y=0, relwidth=1, relheight=1)

frame = tkinter.Frame(window ,bg="#525252")
frame.place(relx=0.235, rely=0.5, anchor="center")


saletasks_frame = tkinter.LabelFrame(frame, text='Tasks' , font=("Arial", 18 , 'bold'), bg="#525252", fg="#E3E5E0", padx=20, pady=20)
saletasks_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)

btnSaleInvoice = tkinter.Button(saletasks_frame, width=20, text="Create Invoice", font=("Comic Sans MS", 15,'bold'), bg="#525252", command=CreateInvoice)
btnSaleInvoice.grid(row=0, column=0)

btnReports = tkinter.Button(saletasks_frame, width=20, text="Generate Sale Report", font=("Comic Sans MS", 15,'bold'), bg="#525252", command=SaleReport)
btnReports.grid(row=1, column=0)

for widget in saletasks_frame.winfo_children():
    widget.grid_configure(padx=30, pady=10)

buttons_frame = tkinter.LabelFrame(frame, text="" , font=("Arial", 15 , 'bold'), bg="#525252", padx=20, pady=20)
buttons_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

btnChangepass = tkinter.Button(buttons_frame, width=20, text="Change Password", font=("Comic Sans MS", 15,'bold'), bg="#B6891B" , command=Changepass)
btnChangepass.grid(row=1, column=0 )

btnSignout = tkinter.Button(buttons_frame, width=20, text="Sign out" , font=("Comic Sans MS", 15,'bold'), bg="#B6891B", command=SaleUserlogin)
btnSignout.grid(row=2, column=0)

btnExit = tkinter.Button(buttons_frame, width=20, text="Exit" , font=("Comic Sans MS", 15,'bold'), bg="#B6891B", command=window.destroy)
btnExit.grid(row=3, column=0)

for widget in buttons_frame.winfo_children():
    widget.grid_configure(padx=30, pady=10)

window.mainloop()