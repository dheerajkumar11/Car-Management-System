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

def SaleLoginpage():
    subprocess.Popen(["python", "SaleLoginpage.py"])
    window.destroy()


def generate_invoice_number():
    # Connect to the database
    connection = mysql.connector.connect(host = "localhost", user = "root",password = "Dheeraj@97", database = "PythonProject")
    mycursor = connection.cursor()

    # Get the count of existing rows in the 'invoices' table
    mycursor.execute('SELECT COUNT(*) FROM Invoice_Details')
    row_count = mycursor.fetchone()[0]

    # Generate the next invoice number
    next_invoice_number = row_count + 1

    # Update the Entry widget with the new invoice number
    invoiceno_entry.delete(0, tkinter.END)
    invoiceno_entry.insert(0, str(next_invoice_number))

    # Close the database connection
    connection.close()


def create_invoice():


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
                                         invoiceno_entry, invoicedate_entry, salefrom_entry, vehiclemodel_entry,
                                         vinnumber_entry, manufactureyear_entry]):
        messagebox.showwarning("Warning", "All fields must be filled.")
        return
    
    connection = mysql.connector.connect(host = "localhost", user = "root",password = "Dheeraj@97", database = "PythonProject")
    mycursor = connection.cursor()

    First_name = firstname_entry .get()
    Last_name = lastname_entry.get()
    Gender = gender_combobox.get()
    BirthDate = dob_entry.get()
    StreetAddress = streetaddress_entry.get()
    City = city_entry.get()
    State = state_combobox.get()
    Phonenumber = phoneno_entry.get()
    Invoice_number = invoiceno_entry.get()
    Invoice_date = invoicedate_entry.get()
    Sale_from = salefrom_entry.get()
    Vehicle_model = vehiclemodel_entry.get()
    Vinnumber = vinnumber_entry.get()
    Color = color_combobox.get()
    Manufacture_year = manufactureyear_entry.get()

    mycursor.execute("INSERT INTO Invoice_Details (First_name , Last_name , Gender, BirthDate , StreetAddress , City , State , Phonenumber , Invoice_number , Invoice_date , Sale_from , Vehicle_model , Vinnumber , Color , Manufacture_year ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" , (First_name,Last_name,Gender,BirthDate , StreetAddress , City , State , Phonenumber , Invoice_number , Invoice_date , Sale_from , Vehicle_model , Vinnumber , Color , Manufacture_year))
    
    messagebox.showinfo("Message", "Created Invoice Succesfully")
    subprocess.Popen(["python", "SaleLoginpage.py"])
    window.destroy()

    connection.commit()
    connection.close()


window = tkinter.Tk()
window.title("Creating Invoice")
window.geometry("1360x1000")

bg_image = Image.open("invoicecreation12.png")
bg_image = bg_image.resize((1360, 780), Image.ANTIALIAS)
bg1 = ImageTk.PhotoImage(bg_image)

label2 = Label(window, image=bg1)
label2.image = bg1
label2.place(x=0, y=0, relwidth=1, relheight=1)

frame = tkinter.Frame(window, bg="#E4E4E4")
frame.place(relx=0.375, rely=0.5, anchor="center")

Customer_details_frame = tkinter.LabelFrame(frame, text='Customer Details', font=("Arial", 15 , 'bold'), bg="#E4E4E4", padx=20, pady=20)
Customer_details_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)

first_name_label = tkinter.Label(Customer_details_frame, text="First Name:" , font=("Arial", 15 , 'bold'), bg="#E4E4E4")
first_name_label.grid(row=0, column=0)
firstname_entry = tkinter.Entry(Customer_details_frame)
firstname_entry.grid(row=0, column=1)

last_name_label = tkinter.Label(Customer_details_frame, text="Last Name:" , font=("Arial", 15 , 'bold'), bg="#E4E4E4")
last_name_label.grid(row=1, column=0)
lastname_entry = tkinter.Entry(Customer_details_frame)
lastname_entry.grid(row=1, column=1)

gender_label = tkinter.Label(Customer_details_frame, text="Gender:", font=("Arial", 15, 'bold'), bg="#E4E4E4")
gender_label.grid(row=2, column=0)
gender_combobox = ttk.Combobox(Customer_details_frame, values=["", "Male", "Female", "Unknown"], width=17)
gender_combobox.grid(row=2, column=1)

dateofbirth_label = tkinter.Label(Customer_details_frame, text="Date of Birth: " , font=("Arial", 15 , 'bold'), bg="#E4E4E4")
dateofbirth_label.grid(row=3, column=0)
dob_entry = DateEntry(Customer_details_frame, selectmode = "day" , date_pattern='yyyy-mm-dd', width=17)
dob_entry.grid(row=3, column=1)

street_address_label = tkinter.Label(Customer_details_frame, text="Street Address:", font=("Arial", 15 , 'bold'), bg="#E4E4E4")
street_address_label.grid(row=4, column=0)
streetaddress_entry = tkinter.Entry(Customer_details_frame)
streetaddress_entry.grid(row=4, column=1)

city_label = tkinter.Label(Customer_details_frame, text="City:", font=("Arial", 15 , 'bold'), bg="#E4E4E4")
city_label.grid(row=5, column=0)
city_entry = tkinter.Entry(Customer_details_frame)
city_entry.grid(row=5, column=1)

state_label = tkinter.Label(Customer_details_frame, text="State:", font=("Arial", 15,'bold'), bg="#E4E4E4")
state_label.grid(row=6, column=0)
state_combobox = ttk.Combobox(Customer_details_frame, values=["", "AL", "AK", "AR", "AZ", "CA", "CO", "CT", "DE", "FL",
                                                              "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA",
                                                              "MA",
                                                              "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC", "ND",
                                                              "NE",
                                                              "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA",
                                                              "RI",
                                                              "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WI",
                                                              "WV",
                                                              "WY"], width=17)
state_combobox.grid(row=6, column=1)

phoneno_label = tkinter.Label(Customer_details_frame, text="Phone Number:", font=("Arial", 15 , 'bold'), bg="#E4E4E4")
phoneno_label.grid(row=7, column=0)
phoneno_entry = tkinter.Entry(Customer_details_frame)
phoneno_entry.grid(row=7, column=1)

for widget in Customer_details_frame.winfo_children():
    widget.grid_configure(padx=10, pady=3)

Vehicle_details_frame = tkinter.LabelFrame(frame, text='Vehicle Details' , font=("Arial", 15 , 'bold'), bg="#E4E4E4", padx=20, pady=20)
Vehicle_details_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

invoiceno_label = tkinter.Label(Vehicle_details_frame, text="Invoice Number:", font=("Arial", 15, 'bold'), bg="#E4E4E4")
invoiceno_label.grid(row=0, column=0)

generate_button = tkinter.Button(Vehicle_details_frame, text="Generate Invoice Number", font=("Arial", 15 , 'bold'), command=generate_invoice_number)
generate_button.grid(row = 0 , column = 2)

invoice_date_label = tkinter.Label(Vehicle_details_frame, text="Invoice Date :" , font=("Arial", 15 , 'bold'), bg="#E4E4E4")
invoice_date_label.grid(row=1, column=0)

invoiceno_entry = tkinter.Entry(Vehicle_details_frame)
invoicedate_entry = DateEntry(Vehicle_details_frame, selectmode = "day" , date_pattern='yyyy-mm-dd', width=17)
invoiceno_entry.grid(row=0, column=1)
invoicedate_entry.grid(row=1, column=1)

salefrom_label = tkinter.Label(Vehicle_details_frame, text="Sale From:", font=("Arial", 15 , 'bold'), bg="#E4E4E4")
salefrom_label.grid(row=2, column=0)
salefrom_entry = tkinter.Entry(Vehicle_details_frame)
salefrom_entry.grid(row=2, column=1)

vehiclemodel_label = tkinter.Label(Vehicle_details_frame, text="Vehicle Model:", font=("Arial", 15 , 'bold'), bg="#E4E4E4")
vehiclemodel_label.grid(row=3, column=0)
vehiclemodel_entry = tkinter.Entry(Vehicle_details_frame)
vehiclemodel_entry.grid(row=3, column=1)

vinnumber_label = tkinter.Label(Vehicle_details_frame, text="VIN Number:", font=("Arial", 15 , 'bold'), bg="#E4E4E4")
vinnumber_label.grid(row=4, column=0)
vinnumber_entry = tkinter.Entry(Vehicle_details_frame)
vinnumber_entry.grid(row=4, column=1)

color_label = tkinter.Label(Vehicle_details_frame, text="Color:", font=("Arial", 15 , 'bold'), bg="#E4E4E4")
color_label.grid(row=5, column=0)
color_combobox = ttk.Combobox(Vehicle_details_frame, values=["", "Black", "White", "Blue", "Brown", "Yellow", "Silver",
                                                             "Grey", "Red"], width=17)
color_combobox.grid(row=5, column=1)

manufactureyear_label = tkinter.Label(Vehicle_details_frame, text="Year of Manufacture:", font=("Arial", 15 , 'bold'), bg="#E4E4E4")
manufactureyear_label.grid(row=6, column=0)
manufactureyear_entry = tkinter.Entry(Vehicle_details_frame)
manufactureyear_entry.grid(row=6, column=1)

for widget in Vehicle_details_frame.winfo_children():
    widget.grid_configure(padx=10, pady=3)



buttons_frame = tkinter.LabelFrame(frame, text="", font=("Arial", 15 , 'bold'), bg="#E4E4E4", padx=20, pady=20)
buttons_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

btnCreateInvoice = tkinter.Button(buttons_frame, width=10, text="Create Invoice", font=("Comic Sans MS", 15 , 'bold'), bg="lavender", command=create_invoice)
btnCreateInvoice.grid(row=1, column=0)

btnMainPage = tkinter.Button(buttons_frame, width=10, text="Main Page", font=("Comic Sans MS", 15 , 'bold'), bg="lavender", command=SaleLoginpage)
btnMainPage.grid(row=1, column=1)

btnExit = tkinter.Button(buttons_frame, width=10, text="Exit", font=("Comic Sans MS", 15 , 'bold'), bg="lavender", command=window.destroy)
btnExit.grid(row=1, column=2)

for widget in buttons_frame.winfo_children():
    widget.grid_configure(padx=60, pady=2)

window.mainloop()