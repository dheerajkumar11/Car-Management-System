

import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
from tkinter import Tk, Frame, Label, Button
from tkinter import PhotoImage
from PIL import Image, ImageTk



def AdminUserlogin():
    subprocess.Popen(["python", "AdminUserlogin.py"])
    window.destroy()

def SaleUserlogin():
    subprocess.Popen(["python", "SaleUserlogin.py"])
    window.destroy()

def ServiceUserlogin():
    subprocess.Popen(["python", "ServiceUserlogin.py"])
    window.destroy()


window = tkinter.Tk()
window.title("Welcome to AutoDealer Insight")
window.geometry("1360x1000")


bg_image = Image.open("background12.png")
bg_image = bg_image.resize((1360, 1000), Image.ANTIALIAS)
bg1 = ImageTk.PhotoImage(bg_image)


label2 = Label(window, image=bg1)
label2.image = bg1
label2.place(x=0, y=0, relwidth=1, relheight=1)  


frame = tkinter.Frame(window, bg="#748079")
frame.place(relx=0.5, rely=0.5, anchor="center")


user_role_frame = tkinter.LabelFrame(frame, text='Welcome to AutoDealer Insight', font=("Comic Sans MS", 20, "bold"), bg="#748079", padx=20, pady=20)
user_role_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)


btnAdminLogin = Button(user_role_frame, width=20, text="Admin Login", font=("Comic Sans MS", 20, "bold"), command=AdminUserlogin, bg="#748079" )
btnAdminLogin.grid(row=1, column=0, pady=10)

btnSalesLogin = Button(user_role_frame, width=20, text="Sales Login", font=("Comic Sans MS", 20, 'bold'), command=SaleUserlogin, bg="#748079" )
btnSalesLogin.grid(row=2, column=0, pady=10)

btnServiceLogin = Button(user_role_frame, width=20, text="Service Login", font=("Comic Sans MS", 20, 'bold'), command=ServiceUserlogin, bg="#748079"  )
btnServiceLogin.grid(row=3, column=0, pady=10)


for widget in user_role_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

window.mainloop()