# class car is nothing but a template
# self>> a varoable that represent instance of the class using which you can acess method/function
# of class, also attribute/property data of the the class
# class car():
#     pass
# c1 = car()  # instance/ object
# print(type(c1))

# class car:
#     def accelerate(self):
#         print("Car is Accelerate")
# c1 = car
# c1.accelerate()
# print(c1)        


# class car:
#     def accelerate(self):
#         print("Car is Accelerate")
#     def brake(self):
#         print("Car is Stopping")
# c1 = car()
# c1.brake()
# c1.accelerate() 
# 
# Self>> self is not a python keyword, you can pass any variable name 
# class bank: # passing the data in the class
#     def deposit(self):
#         print("I am depositing the money")
#     def withdraw(self):
#         print("I am trying to withdraw money")    
# c1 = bank()
# c1.deposit()
# c1.withdraw()


# bank we ask for a default amount
# amount is attribute/property/data of class of bank
# class bank:
#     amount = 1000
#     def deposit(self, amount):
#         print("I am depositing the money")
#     def withdraw(self, amount_wirhdraw):
#         print("I am trying to withdraw money")
# dhrubo = bank()
# dhrubo.deposit(1000)
# #dhrubo.amount()


# multiple attributes

class Book:
    def __init__(self, name, author, title):
        self.name_of_book = name
        self.book_author = author
        self.title_name = title 
    def extract_deatails_name_title(self):
        print(self.name_of_book, self.title_name)
    def extract_deatails_name_author(self):
        print(self.name_of_book, self.book_author)
std1 = Book("Python", "Dhrubo", "Data Science")
std1.extract_deatails_name_author()
std1.extract_deatails_name_title()            