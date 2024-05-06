import tkinter
from tkinter import ttk, LabelFrame
import subprocess
from tkinter import messagebox
import mysql.connector 
from tkinter import Tk, Frame, Label, Button
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import re

def ServiceLoginpage():
    subprocess.Popen(["python", "ServiceLoginpage.py"])
    window.destroy()

def generate_jobcard_number():
    # Connect to the database
    connection = mysql.connector.connect(host = "localhost", user = "root",password = "Dheeraj@97", database = "PythonProject")
    mycursor = connection.cursor()

    # Get the count of existing rows in the 'invoices' table
    mycursor.execute('SELECT COUNT(*) FROM ServiceRegister')
    row_count = mycursor.fetchone()[0]

    # Generate the next invoice number
    next_job_number = row_count + 1

    # Update the Entry widget with the new invoice number
    jobno_entry.delete(0, tkinter.END)
    jobno_entry.insert(0, str(next_job_number))

    # Close the database connection
    connection.close()

def serviceticket():

    first_name = firstname_entry.get()
    
    if not re.match(r'^[A-Za-z]+$', first_name):
        messagebox.showwarning("Warning", "Invalid first name. Only character strings are allowed.")
        return

    last_name = lastname_entry.get()

    if not re.match(r'^[A-Za-z]+$', last_name):
        messagebox.showwarning("Warning", "Invalid last name. Only character strings are allowed.")
        return

    phonenumber = phoneno_entry.get()

    if not re.match(r'^\d{10}$', phonenumber):
        messagebox.showwarning("Warning", "Invalid phone number. Please enter a 10-digit number.")
        return

    vin_number = vinnumber_entry.get().strip().upper()  # Convert to uppercase and remove leading/trailing whitespaces

    if not re.match(r'^[A-HJ-NPR-Z0-9]{17}$', vin_number):
        messagebox.showwarning("Warning", "Invalid VIN number. Please enter a valid 17-character VIN.")
        return
    
    if not all(entry.get() for entry in [firstname_entry, lastname_entry, streetaddress_entry, city_entry, phoneno_entry,
                                        vehiclemodel_entry, vinnumber_entry, ODOreading_entry ]):
        messagebox.showwarning("Warning", "All fields must be filled.")
        return

    connection = mysql.connector.connect(host = "localhost", user = "root",password = "Dheeraj@97", database = "PythonProject")
    mycursor = connection.cursor()

    Job_cardnumber = jobno_entry.get()
    First_name = firstname_entry.get()
    Last_name = lastname_entry.get()
    Street_address = streetaddress_entry.get()
    City = city_entry.get()
    State = state_combobox.get()
    Phone_number = phoneno_entry.get()
    Service_date = servicedate_entry.get()
    Vehicle_model = vehiclemodel_entry.get()
    Color = color_combobox.get()
    VIN_number = vinnumber_entry.get()
    Purchase_date = vehiclepurchasedate_entry.get()
    ODOmeter_reading = ODOreading_entry.get()
    Service_Type = servicetype_combobox.get()

    mycursor.execute("INSERT INTO ServiceRegister (Job_cardnumber , First_name , Last_name, Street_address , City , State , Phone_number , Service_date , Vehicle_model , Color  , VIN_number , Purchase_date , ODOmeter_reading , Service_Type ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" , (Job_cardnumber , First_name , Last_name, Street_address , City , State , Phone_number , Service_date , Vehicle_model , Color  , VIN_number , Purchase_date , ODOmeter_reading , Service_Type ))
    
    messagebox.showinfo("Message", "Service Ticket created Succesfully")
    subprocess.Popen(["python", "ServiceLoginpage.py"])
    window.destroy()

    connection.commit()
    connection.close()


window = tkinter.Tk()
window.title("Creating Service Request")
window.geometry("1360x1000")

bg_image = Image.open("serviceregister123.png")
bg_image = bg_image.resize((1360, 780), Image.ANTIALIAS)
bg1 = ImageTk.PhotoImage(bg_image)

label2 = Label(window, image=bg1)
label2.image = bg1
label2.place(x=0, y=0, relwidth=1, relheight=1)

frame = tkinter.Frame(window, bg="#D2EFEE")
frame.place(relx=0.355, rely=0.5, anchor="center")


SrCustomer_details_frame = tkinter.LabelFrame(frame, text='Customer Details', font=("Arial", 15, 'bold'), bg="#D2EFEE")
SrCustomer_details_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)

jobno_label = tkinter.Label(SrCustomer_details_frame, text="Job Card Number:" ,  font=("Arial", 15) , bg="#D2EFEE")
jobno_label.grid(row=0, column=0)
jobno_entry = tkinter.Entry(SrCustomer_details_frame)
jobno_entry.grid(row=0, column=1)

generate_button = tkinter.Button(SrCustomer_details_frame, text="Generate Job Number", font=("Arial", 15), command=generate_jobcard_number)
generate_button.grid(row = 0 , column = 2)

first_name_label = tkinter.Label(SrCustomer_details_frame, text="First Name:" ,  font=("Arial", 15) , bg="#D2EFEE")
first_name_label.grid(row=1, column=0)
firstname_entry = tkinter.Entry(SrCustomer_details_frame)
firstname_entry.grid(row=1, column=1)

last_name_label = tkinter.Label(SrCustomer_details_frame, text="Last Name:" ,  font=("Arial", 15) , bg="#D2EFEE")
last_name_label.grid(row=2, column=0)
lastname_entry = tkinter.Entry(SrCustomer_details_frame)
lastname_entry.grid(row=2, column=1)

street_address_label = tkinter.Label(SrCustomer_details_frame, text="Street Address:" ,  font=("Arial", 15) , bg="#D2EFEE")
street_address_label.grid(row=3, column=0)
streetaddress_entry = tkinter.Entry(SrCustomer_details_frame)
streetaddress_entry.grid(row=3, column=1)

city_label = tkinter.Label(SrCustomer_details_frame, text="City:" ,  font=("Arial", 15) , bg="#D2EFEE")
city_label.grid(row=4, column=0)
city_entry = tkinter.Entry(SrCustomer_details_frame)
city_entry.grid(row=4, column=1)

state_label = tkinter.Label(SrCustomer_details_frame, text="State:" ,  font=("Arial", 15) , bg="#D2EFEE")
state_label.grid(row=5, column=0)
state_combobox = ttk.Combobox(SrCustomer_details_frame,
                              values=["", "AL", "AK", "AR", "AZ", "CA", "CO", "CT", "DE", "FL",
                                      "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "MA",
                                      "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE",
                                      "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "RI",
                                      "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WI", "WV",
                                      "WY"], width=17)
state_combobox.grid(row=5, column=1)

phoneno_label = tkinter.Label(SrCustomer_details_frame, text="Phone Number:" ,  font=("Arial", 15) , bg="#D2EFEE")
phoneno_label.grid(row=6, column=0)
phoneno_entry = tkinter.Entry(SrCustomer_details_frame)
phoneno_entry.grid(row=6, column=1)

servicedate_label = tkinter.Label(SrCustomer_details_frame, text="Service In Date:" ,  font=("Arial", 15) , bg="#D2EFEE")
servicedate_label.grid(row=7, column=0)
servicedate_entry = DateEntry(SrCustomer_details_frame, selectmode = "day" , date_pattern='yyyy-mm-dd', width=17)
servicedate_entry.grid(row=7, column=1)

for widget in SrCustomer_details_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

SrVehicle_details_frame = tkinter.LabelFrame(frame, text='Vehicle Details', font=("Arial", 15, 'bold'), bg="#D2EFEE")
SrVehicle_details_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

vehiclemodel_label = tkinter.Label(SrVehicle_details_frame, text="Vehicle Model:",  font=("Arial", 15) , bg="#D2EFEE")
vehiclemodel_label.grid(row=0, column=0)
vehiclemodel_entry = tkinter.Entry(SrVehicle_details_frame)
vehiclemodel_entry.grid(row=0, column=1)

color_label = tkinter.Label(SrVehicle_details_frame, text="Color:",  font=("Arial", 15) , bg="#D2EFEE")
color_label.grid(row=0, column=2)
color_combobox = ttk.Combobox(SrVehicle_details_frame,
                              values=["", "Black", "White", "Blue", "Brown", "Yellow", "Silver",
                                      "Grey", "Red"], width=17)
color_combobox.grid(row=0, column=3)

vinnumber_label = tkinter.Label(SrVehicle_details_frame, text="VIN Number:",  font=("Arial", 15) , bg="#D2EFEE")
vinnumber_label.grid(row=1, column=0)
vinnumber_entry = tkinter.Entry(SrVehicle_details_frame)
vinnumber_entry.grid(row=1, column=1)

vehiclepurchasedate_label = tkinter.Label(SrVehicle_details_frame, text="Purchase Date:" ,  font=("Arial", 15) , bg="#D2EFEE")
vehiclepurchasedate_label.grid(row=2, column=0)
vehiclepurchasedate_entry = DateEntry(SrVehicle_details_frame, selectmode = "day" , date_pattern='yyyy-mm-dd', width=17)
vehiclepurchasedate_entry.grid(row=2, column=1)

for widget in SrVehicle_details_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

Servicetype_details_frame = tkinter.LabelFrame(frame, text='Type of Service', font=("Arial", 15, 'bold'), bg="#D2EFEE")
Servicetype_details_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

ODOreading_label = tkinter.Label(Servicetype_details_frame, text="ODO reading:",  font=("Arial", 15) , bg="#D2EFEE")
ODOreading_label.grid(row=0, column=0)
ODOreading_entry = tkinter.Entry(Servicetype_details_frame)
ODOreading_entry.grid(row=0, column=1)

servicetype_label = tkinter.Label(Servicetype_details_frame, text="Service Type:",  font=("Arial", 15) , bg="#D2EFEE")
servicetype_label.grid(row=0, column=2)
servicetype_combobox = ttk.Combobox(Servicetype_details_frame, values=["", "Free Service", "Paid Service"], width=17)
servicetype_combobox.grid(row=0, column=3)

for widget in Servicetype_details_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

buttons_frame = tkinter.LabelFrame(frame, text="", font=("Arial", 15, 'bold'), bg="#D2EFEE")
buttons_frame.grid(row=4, column=0, sticky="news", padx=20, pady=10)

btnServiceRequest = tkinter.Button(buttons_frame, width=20, text="Create Service Request",  font=("Comic Sans MS", 15,'bold') , bg="dark sea green", command=serviceticket)
btnServiceRequest.grid(row=1, column=0)

btnMainPage = tkinter.Button(buttons_frame, width=10, text="Main Page",  font=("Comic Sans MS", 15,'bold') , bg="dark sea green", command=ServiceLoginpage)
btnMainPage.grid(row=1, column=1)

btnExit = tkinter.Button(buttons_frame, width=10, text="Exit",  font=("Comic Sans MS", 15,'bold') , bg="dark sea green", command=window.destroy)
btnExit.grid(row=1, column=2)

for widget in buttons_frame.winfo_children():
    widget.grid_configure(padx=60, pady=10)

window.mainloop()