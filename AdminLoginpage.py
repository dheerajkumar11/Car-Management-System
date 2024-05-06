import tkinter
from tkinter import ttk
from tkinter import messagebox
import subprocess
import sys
import mysql.connector 
from tkinter import Tk, Frame, Label, Button
from tkinter import PhotoImage
from PIL import Image, ImageTk

def AdminUserlogin():
    subprocess.Popen(["python", "AdminUserlogin.py"])
    window.destroy()

def CreateInvoice():
    subprocess.Popen(["python", "CreateInvoiceadmin.py"])
    window.destroy()

def ServiceRequest():
    subprocess.Popen(["python", "ServiceRequestadmin.py"])
    window.destroy()

def UserCreation():
    subprocess.Popen(["python", "UserCreation.py"])
    window.destroy()

def SalesReport():
    subprocess.Popen(["python", "SaleReportadmin.py"])
    window.destroy()

def ServiceReport():
    subprocess.Popen(["python", "ServiceReportadmin.py"])
    window.destroy()

def Changepass():
    subprocess.Popen(["python", "ChangePassadmin.py"])
    window.destroy()

def Users():
    subprocess.Popen(["python", "Existingusers.py"])
    window.destroy()

window = tkinter.Tk()
window.title("Welcome Admin...")
window.geometry("1360x1000")

bg_image = Image.open("adminpage123.png")
bg_image = bg_image.resize((1360, 780), Image.ANTIALIAS)
bg1 = ImageTk.PhotoImage(bg_image)


label2 = Label(window, image=bg1)
label2.image = bg1
label2.place(x=0, y=0, relwidth=1, relheight=1)

frame = tkinter.Frame(window, bg="#A98267")
frame.place(relx=0.285, rely=0.5, anchor="center")


sale_invoice_frame = tkinter.LabelFrame(frame, text='Sales' , font=("Arial", 17 , 'bold'), bg="#A98267", padx=20, pady=20)
sale_invoice_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)

btnSaleInvoice = tkinter.Button(sale_invoice_frame, width=20, text="Create Invoice", font=("Comic Sans MS", 15,'bold'), bg="#A98267",command=CreateInvoice)
btnSaleInvoice.grid(row=1, column=0)

for widget in sale_invoice_frame.winfo_children():
    widget.grid_configure(padx=30, pady=3)

service_register_frame = tkinter.LabelFrame(frame, text='Service' , font=("Arial", 17 , 'bold'), bg="#A98267", padx=20, pady=20)
service_register_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

btnServiceregister = tkinter.Button(service_register_frame, width=20, text="Register Service", font=("Comic Sans MS", 15,'bold'), bg="#A98267" , command=ServiceRequest)
btnServiceregister.grid(row=1, column=0)

for widget in service_register_frame.winfo_children():
    widget.grid_configure(padx=30, pady=3)

reports_frame = tkinter.LabelFrame(frame, text='Reports', font=("Arial", 17 , 'bold'), bg="#A98267", padx=20, pady=20)
reports_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

btnSaleReport = tkinter.Button(reports_frame, width=20, text="Sales Report", font=("Comic Sans MS", 15,'bold'), bg="#FFF9E9" , command=SalesReport)
btnSaleReport.grid(row=1, column=0)

btnServiceReport = tkinter.Button(reports_frame, width=20, text="Service Report", font=("Comic Sans MS", 15,'bold'), bg="#FFF9E9" , command=ServiceReport)
btnServiceReport.grid(row=2, column=0)

for widget in reports_frame.winfo_children():
    widget.grid_configure(padx=30, pady=3)

user_creation_frame = tkinter.LabelFrame(frame, text='Users', font=("Arial", 17 , 'bold'), bg="#A98267", padx=20, pady=20)
user_creation_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)

btnSaleInvoice = tkinter.Button(user_creation_frame, width=20, text="Sale/Service User", font=("Comic Sans MS", 15,'bold'), bg="#FFF9E9" , command=UserCreation)
btnSaleInvoice.grid(row=1, column=0)

btnUsers = tkinter.Button(user_creation_frame, width=20, text="Existing Users", font=("Comic Sans MS", 15,'bold'), bg="#FFF9E9" , command=Users)
btnSaleInvoice.grid(row=1, column=0)

for widget in user_creation_frame.winfo_children():
    widget.grid_configure(padx=30, pady=3)

buttons_frame = tkinter.LabelFrame(frame, text="" , font=("Arial", 15), bg="#A98267", padx=20, pady=20)
buttons_frame.grid(row=4, column=0, sticky="news", padx=20, pady=10)

btnChangepass = tkinter.Button(buttons_frame, width=20, text="Change Password", font=("Comic Sans MS", 15,'bold'), bg="#FFF9E9" , command=Changepass)
btnChangepass.grid(row=1, column=0 )

btnSignout = tkinter.Button(buttons_frame, width=20, text="Sign out", font=("Comic Sans MS", 15,'bold'), bg="#FFF9E9" , command=AdminUserlogin)
btnSignout.grid(row=2, column=0)

btnExit = tkinter.Button(buttons_frame, width=20, text="Exit", font=("Comic Sans MS", 15,'bold'), bg="#FFF9E9" , command=window.destroy)
btnExit.grid(row=3, column=0)

for widget in buttons_frame.winfo_children():
    widget.grid_configure(padx=30, pady=3)

window.mainloop()



