import tkinter
from tkinter import *
from tkinter import ttk
import subprocess
import mysql.connector 
from PIL import Image, ImageTk
import pandas as pd
from tkinter import messagebox
from datetime import datetime

def ServiceLoginPage():
    subprocess.Popen(["python", "ServiceLoginpage.py"])
    window.destroy()

def export_to_excel():
    mycursor.execute("SELECT Job_cardnumber, Service_date, First_name, Last_name, Vehicle_model, VIN_number, ODOmeter_reading, Service_Type FROM ServiceRegister ORDER BY Service_date")
    all_entries = mycursor.fetchall()

    df = pd.DataFrame(all_entries, columns=["Job Card Number", "Service Date", "First Name", "Last Name", "Vehicle Model", "VIN Number", "ODO Reading", "Service Type"])

    timestamp = datetime.now().strftime("%Y.%m.%d_%H.%M.%S")
    filename = f"service_report_{timestamp}.xlsx"

    df.to_excel(filename, index=False)
    messagebox.showinfo("Message" , f"Service Report exported to {filename}")

connection = mysql.connector.connect(host = "localhost", user = "root",password = "Dheeraj@97", database = "PythonProject")
mycursor = connection.cursor()

mycursor.execute("SELECT Job_cardnumber,Service_date, First_name , Last_name, Vehicle_model, VIN_number, ODOmeter_reading, Service_Type FROM ServiceRegister ORDER BY Service_date")

all_entries = mycursor.fetchall()

window = tkinter.Tk()
window.title("Service Report")
window.geometry("1300x450")


bg_image = Image.open("report123.png")
bg_image = bg_image.resize((1360, 780), Image.ANTIALIAS)
bg1 = ImageTk.PhotoImage(bg_image)

label2 = Label(window, image=bg1)
label2.image = bg1
label2.place(x=0, y=0, relwidth=1, relheight=1)


style = ttk.Style()
style.theme_use('clam')
style.configure("Treeview", background="white", 
                fieldbackground="white", foreground="black")


tree = ttk.Treeview(window, column=("Job Card Number", "Service Date", "First Name","Last Name","Vehicle Model","VIN Number","ODO Reading","Service Type"), show='headings', height=11)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Job Card Number")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Service Date")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="First Name")
tree.column("# 4", anchor=CENTER)
tree.heading("# 4", text="Last Name")
tree.column("# 5", anchor=CENTER)
tree.heading("# 5", text="Vehicle Model")
tree.column("# 6", anchor=CENTER)
tree.heading("# 6", text="Vin Number")
tree.column("# 7", anchor=CENTER)
tree.heading("# 7", text="ODO Reading")
tree.column("# 8", anchor=CENTER)
tree.heading("# 8", text="Service Type")

i = 0

for x in all_entries:
    tree.insert('', i , text = "" , values = (x[0] , x[1] , x[2] , x[3] , x[5] , x[5] , x[6] ,x[7]))
    i += 1


tree.pack()

frame = tkinter.Frame(window)
frame.pack()

buttons_frame = tkinter.LabelFrame(frame, text="")
buttons_frame.grid(row=4, column=0, sticky="news", padx=20, pady=10)

btnSignout = tkinter.Button(buttons_frame, width=10, text="Back", font=("Comic Sans MS", 15,'bold') , command=ServiceLoginPage)
btnSignout.grid(row=1, column=0)

btnprint = tkinter.Button(buttons_frame, width=10, text="Export", font=("Comic Sans MS", 15,'bold') , command=export_to_excel)
btnprint.grid(row=1, column=1)

btnExit = tkinter.Button(buttons_frame, width=10, text="Exit", font=("Comic Sans MS", 15,'bold') , command=window.destroy)
btnExit.grid(row=1, column=2)

for widget in buttons_frame.winfo_children():
    widget.grid_configure(padx=60, pady=10)
window.mainloop()

