import tkinter
from tkinter import ttk, LabelFrame
import subprocess
from tkinter import messagebox
import mysql.connector 
from tkinter import Tk, Frame, Label, Button
from tkinter import PhotoImage
from PIL import Image, ImageTk

def SaleLoginpage():
    subprocess.Popen(["python", "SaleLoginpage.py"])
    window.destroy()

def toggle_password_visibility():
    if show_password_var.get():
        newpassword_entry.config(show="")
    else:
        newpassword_entry.config(show="*")

def change_password():

    connection = mysql.connector.connect(host = "localhost", user = "root",password = "Dheeraj@97", database = "PythonProject")
    mycursor = connection.cursor()


    mycursor.execute("UPDATE UserCredentials SET user_password = '"+newpassword_entry.get()+"' WHERE Username = '"+ userid_entry.get()+"';")

    connection.commit()
    connection.close()

    
    messagebox.showinfo("Message", "Password Changed successfully")
    subprocess.Popen(["python", "SaleUserlogin.py"])
    window.destroy()


window = tkinter.Tk()
window.title("Change Password")
window.geometry("1360x1000")

bg_image = Image.open("changepass123.png")
bg_image = bg_image.resize((1360, 780), Image.ANTIALIAS)
bg1 = ImageTk.PhotoImage(bg_image)

label2 = Label(window, image=bg1)
label2.image = bg1
label2.place(x=0, y=0, relwidth=1, relheight=1)


frame = tkinter.Frame(window, bg="#BCB49F")
frame.place(relx=0.5, rely=0.55, anchor="center")

changepass_frame = tkinter.LabelFrame(frame, text='' , font=("Arial", 15 , 'bold'), bg="#BCB49F", padx=20, pady=20)
changepass_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)

userid_label = tkinter.Label(changepass_frame, text="User ID:" , font=("Arial", 20), bg="#BCB49F", padx=20, pady=20)
userid_label.grid(row=0, column=0)
userid_entry = tkinter.Entry(changepass_frame , font=("Arial", 20))
userid_entry.grid(row=0, column=1) 

newpassword_label = tkinter.Label(changepass_frame, text="New Password" ,font=("Arial", 20), bg="#BCB49F", padx=20, pady=20)
newpassword_label.grid(row=1, column=0) 
newpassword_entry = tkinter.Entry(changepass_frame, show ="*" , font=("Arial", 20))
newpassword_entry.grid(row=1, column=1)

show_password_var = tkinter.BooleanVar()
show_password_checkbox = tkinter.Checkbutton(
    changepass_frame,
    text="Show Password",
    variable=show_password_var,
    command=toggle_password_visibility,
    font=("Arial", 16),
    bg="#BCB49F",
)
show_password_checkbox.grid(row=1, column=2, sticky="w")

for widget in changepass_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

buttons_frame = tkinter.LabelFrame(frame, text="",font=("Arial", 20), bg="#BCB49F", padx=20, pady=20)
buttons_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

btnchangepass = tkinter.Button(buttons_frame, width=15, text="Change Password", font=("Comic Sans MS", 20,'bold'), command=change_password)
btnchangepass.grid(row=0, column=0)

btnMainPage = tkinter.Button(buttons_frame, width=15, text="Main Page",font=("Comic Sans MS", 20,'bold'), bg="mint cream", command=SaleLoginpage)
btnMainPage.grid(row=0, column=1)

for widget in buttons_frame.winfo_children():
    widget.grid_configure(padx=30, pady=5)


window.mainloop()