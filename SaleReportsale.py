# Import the required libraries
import tkinter
from tkinter import *
from tkinter import ttk
import subprocess
import mysql.connector 
from PIL import Image, ImageTk
import pandas as pd
from tkinter import messagebox
from datetime import datetime

def SaleLoginPage():
    subprocess.Popen(["python", "SaleLoginpage.py"])
    window.destroy()

def export_to_excel():
    # Fetch data from the database
    mycursor.execute("SELECT Invoice_number, Invoice_date, First_name, Last_name, Vehicle_model, Vinnumber, Color, Sale_from FROM Invoice_details ORDER BY Invoice_date")
    all_entries = mycursor.fetchall()

    # Create a DataFrame from the fetched data
    df = pd.DataFrame(all_entries, columns=["Invoice number", "Sale Date", "First Name", "Last Name", "Vehicle Model", "VIN Number", "Color", "Sale From"])

    timestamp = datetime.now().strftime("%Y.%m.%d_%H.%M.%S")
    filename = f"sale_report_{timestamp}.xlsx"

    # Export the DataFrame to an Excel file
    df.to_excel(filename, index=False)
    messagebox.showinfo("Message" , f"Report exported to {filename}")


connection = mysql.connector.connect(host = "localhost", user = "root",password = "Dheeraj@97", database = "PythonProject")
mycursor = connection.cursor()

mycursor.execute("SELECT Invoice_number,Invoice_date, First_name , Last_name, Vehicle_model, Vinnumber, Color, Sale_from FROM Invoice_details ORDER BY Invoice_date")

all_entries = mycursor.fetchall()

window = tkinter.Tk()
window.title("Sale Report")


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



tree = ttk.Treeview(window, column=("Invoice number", "Sale Date", "First Name","Last Name","Vehicle Model","VIN Number","Color","Sale From"), show='headings', height=11)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Invoice number")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Sale Date")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="First Name")
tree.column("# 4", anchor=CENTER)
tree.heading("# 4", text="Last Name")
tree.column("# 5", anchor=CENTER)
tree.heading("# 5", text="Vehicle Model")
tree.column("# 6", anchor=CENTER)
tree.heading("# 6", text="Vin Number")
tree.column("# 7", anchor=CENTER)
tree.heading("# 7", text="Color")
tree.column("# 8", anchor=CENTER)
tree.heading("# 8", text="Sale From")

i = 0

for x in all_entries:
    tree.insert('', i , text = "" , values = (x[0] , x[1] , x[2] , x[3] , x[5] , x[5] , x[6] ,x[7]))
    i += 1


tree.pack()

tree.bind("<ButtonRelease-1>", lambda event: tree.focus_set())


frame = tkinter.Frame(window)
frame.pack()

buttons_frame = tkinter.LabelFrame(frame, text="")
buttons_frame.grid(row=10, column=0, sticky="news", padx=20, pady=10)

btnSignout = tkinter.Button(buttons_frame, width=10, text="Back", font=("Comic Sans MS", 15,'bold'), command=SaleLoginPage)
btnSignout.grid(row=1, column=0)

btnprint = tkinter.Button(buttons_frame, width=10, text="Export", font=("Comic Sans MS", 15,'bold') , command=export_to_excel)
btnprint.grid(row=1, column=1)

btnExit = tkinter.Button(buttons_frame, width=10, text="Exit", font=("Comic Sans MS", 15,'bold'), command=window.destroy)
btnExit.grid(row=1, column=2)

for widget in buttons_frame.winfo_children():
    widget.grid_configure(padx=60, pady=10)
window.mainloop()





        