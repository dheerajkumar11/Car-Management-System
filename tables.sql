use PythonProject;
create table UserCredentials (

Username varchar(20),
user_password varchar(20),
Department varchar(20)

);

create table Invoice_Details (

First_name varchar(20),
Last_name varchar(20),
Gender varchar(20),
BirthDate date,
StreetAddress varchar(40),
City varchar(20),
State varchar(5),
Phonenumber long , 
Invoice_number int,
Invoice_date date,
Sale_from varchar(20),
Vehicle_model varchar(20),
Vinnumber varchar(20),
Color varchar(20),
Manufacture_year year

);

create table ServiceRegister (

Job_cardnumber int,
First_name varchar(20),
Last_name varchar(20),
Street_address varchar(50),
City varchar(20),
State varchar(10),
Phone_number int ,
Service_date date,
Vehicle_model varchar(20),
Color varchar(10),
VIN_number varchar(20),
Purchase_date date,
ODOmeter_reading int,
Service_Type varchar(20)
);



insert into UserCredentials (Username , user_password ,  Department)
values ('admin','12345', 'admin');



select * from Invoice_Details;

select * from UserCredentials;

select * from ServiceRegister;




