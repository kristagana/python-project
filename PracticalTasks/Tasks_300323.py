
# 1.Create a class named Car that has the following attributes: make, model, and year.
# It should also have a method called get_info() that returns a string with the car's make, model, and year.

# class Car:
#     make:str
#     model:str
#     year:int

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_info(self):
#         print(f"This is {self.make} {self.model} of {self.year} year.")

# mycar = Car("Mercedes Benz", "GLA", "2014")
# Car.get_info(mycar)

# 2.Create a class named Rectangle that has the following attributes: width and height. 
# It should also have methods called area() and perimeter() that return the area and perimeter of the rectangle, respectively.

# class Rectangle:
#     width:float
#     height:float

#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height


#     def perimeter(self):
#         return 2 * (self.width + self.height)


# rec = Rectangle(5.12, 2.4)
# print(f"The perimeter is {Rectangle.perimeter(rec)}.")
# print(f"The area is {Rectangle.area(rec)}.")

# 3.Create a class named BankAccount that has the # following attributes: account_number, balance, and owner_name.
# It should also have methods called deposit() and withdraw() that # update the balance accordingly.

# class BankAccount:
#     account:int
#     balance:float
#     owner:str
#     deposit:float
#     withdrawn:float

#     def __init__(self, account, balance, owner):
#         self.account = account
#         self.balance = balance
#         self.owner = owner 
    
#     def deposit(self, deposit):
#         self.balance = self.balance + deposit
    
#     def withdrawn(self, withdrawn):
#         self.balance = self.balance - withdrawn
    
#     def account_info(self):
#         print(f"Account {self.account} owner is {self.owner}, current balance is {acc.balance}.")

# acc = BankAccount(97500001234, 50, "Olia Bali")
# acc.deposit(20.50)
# acc.withdrawn(10.50)
# acc.account_info()

# from Monday session:

# class BankAccount:
#     account:int
#     balance:float
#     owner:str

#     def __init__(self, account, balance, owner):
#         self.account = account
#         self.balance = balance
#         self.owner = owner 
    
#     def deposit(self, deposit):
#         self.balance += deposit
    
#     def withdrawn(self, withdrawn):
#         if withdrawn > self.balance:
#             print("Not possible to withdraw")
#         else:
#             self.balance -= withdrawn
    
#     def account_info(self):
#         print(f"Account {self.account} owner is {self.owner}, current balance is {acc.balance}.")

# acc = BankAccount(97500001234, 50, "Olia Bali")
# acc.deposit(20.50)
# acc.withdrawn(40.50)
# acc.account_info()

# 4.Create a class named Person that has the following attributes: name, age, and address. 
# It should also have a method called get_info() that returns a string with the person's name, age, and address.

# class Person:
#     name:str
#     age:int
#     address:str

#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address

#     def get_info(self):
#         print(f"This is person's name is  {self.name}. Person is {self.age} years old. Person is from {self.address}.")

# p1 = Person("Krista", 27, "Riga")
# print(p1.get_info())

# 5.Create a class named Animal that has the following attributes: name and species.
# It should also have a method called speak() that returns a string with the animal's sound.

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#         self.sound = {"dog": "woof", "pig": "hrju-hrju","cow": "muu","cat": "meow"}
    
#     def sound(self):
#         if self.species in self.sound:
#             return self.sound[self.species]
#         else:
#             self.sound = "Unknown"      
    
# my_animal = Animal("Govs", "cow")
# print(Animal.sound(my_animal))

# 6.Create a base class named Vehicle that has the following attributes: make, model, and year. It should also have a method called get_info() that returns a string with the vehicle's make, model, and year.
# Then create two subclasses, Car and Truck, that inherit from Vehicle and add additional attributes and methods specific to each type of vehicle.


# class Vehicle:
#     make:str
#     model:str
#     year:int

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_info(self):
#         print(f"This is {self.make} {self.model} of {self.year} year.")

# class Car(Vehicle):
#     def __init__(self, make, model, year, gearbox):
#         super().__init__(make, model, year)
#         self.gearbox = gearbox

#     def get_car_info(self):
#         print(f"This is {self.make} {self.model} of {self.year} year. This car has {self.gearbox} gearbox.")

# class Truck(Vehicle):
#     def __init__(self,  make, model, year, specification):
#         super().__init__(make, model, year)
#         self.specification = specification
#     def get_truck_info(self):
#         print (f"This is {self.make} {self.model} {self.year}. This is {self.specification} truck.")

# mycar = Truck("Ford", "Transit", 2018, "Cargo Van")
# Truck.get_truck_info(mycar)

# 7.Create a base class named Person that has the following attributes: name, age, and address. 
# It should also have a method called get_info() that returns a string with the person's name, age, and address.
# Then create two subclasses, Student and Teacher, that inherit from Person and add additional attributes and methods specific to each role.

# - / Understood inheritance

# For I/O:
# 8.Write a Python program that reads a JSON file containing a list of dictionaries, sorts the list by a specific key, and writes the sorted list back to the file.

import json

data = [
    {"name": "Krista", "last_name": "Gana", "age": 27}, {"name": "Liana", "last_name": "Krav", "age": 19}, {"name": "Arturs", "last_name": "Zim", "age": 18},
    {"name": "Kristiana", "last_name": "G", "age": 37}, {"name": "Liga", "last_name": "Loc", "age": 55}
    ]

with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json", "r") as f:
    data = json.load(f)
    f.close()

with open("sor_data.json", "w") as f:
    json.dump(data, f)

with open("sor_data.json", "r") as f:
    data = json.load(f)

data_sort = sorted(data, key = lambda x: x['age']) 

with open("sor_data.json", "w") as f:
    json.dump(data_sort, f)

# 9.Write a Python program that reads a CSV file containing student grades, calculates their average score, and writes the average to a new file.

# -

# 10.Write a Python program that reads a CSV file containing student grades and writes a new CSV file with the grades sorted by student name.

# -