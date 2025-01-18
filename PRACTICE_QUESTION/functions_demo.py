# def greetings(name):
#     print("Welcome to the Office", name)
# greetings("Dhrubo")

# def func():
#     return "This is my first function "
# # func() + "in Python"
# print(func()+ "in Python") 
# 
# def func():
#     return "This is my first function ", 1,2.2, True,(3+7j)
# a,b,c,d,e = func()
# print(b)

# def square(num):
#     return num*num
# square(5)      
# 
# def numbers(a):
#     n = []
#     for i in a:
#         if type(i) == int or type(i) == float:
#             n.append(i)
#     return n  
# print(numbers([1,2,2.2,5,True,"Dhrubo", False, 3+7j]))

# nested list

# def numbers(a):
#     n = []
#     for i in a:
#         if type(i) == list:
#             for j in i:
#                 if type(j) == int or type(j) == float:
#                     n.append(j)
#         else:
#             if type(i) == int or type(i) == float:
#                 n.append(i)
#     return n            
# print(numbers([1,2,2.2,5,True,"Dhrubo", False, 3+7j,[101,2.5,True]]))   
# 
# variable length argument when you don't know the number of arguments
# 
# def sum(*num): # this function any size or variable length of argument
#     return num

# print(sum(1,2))   

# A function which can take any number of values and return the sum
# def sum(*num):
#     s = 0
#     for i in num:
#         s = s+i
#     return s
# print(sum(1,2,3,4,5,6,7,8,9,10))    

# variable argument with default argument

# write a function can take number of values and return the list

# def return_list(*num):
#     a = [] # list
#     for i in num:
#         if type(i) == list:
#             a.append(i)
#     return a 
# print(return_list([1,2,3,4,5,6,7,8,9,10],(1,2,3.3), True, "Dhrubo", [5,26,[68,85,8]]))

# subpart = " to the course" # global variable can be accessed from anywhere or outside of the function
# def greet():
#     message = "Hello welcome" + subpart
#     return message
# print(greet())

# function inside a function

# def mark_subject(**marks):
#     def total_marks(marks_list):
#         return sum(marks_list)
#     marks_list = [] 
#     for sub, mark in marks.items():
#         marks_list.append(mark)
#     return marks_list
# #print(mark_subject(English = 80, Math = 90, Physics = 85, Chemistry = 75))  
# print(sum(mark_subject(English = 80, Math = 90, Physics = 85, Chemistry = 75)))      

# calling function from outside of the function

# def total_marks(marks_list):
#         return sum(marks_list)
# def mark_subject(**marks):
#     marks_list = [] 
#     for sub, mark in marks.items():
#         marks_list.append(mark)
#     return total_marks(marks_list)
# #print(mark_subject(English = 80, Math = 90, Physics = 85, Chemistry = 75))  
# print(mark_subject(English = 80, Math = 90, Physics = 85, Chemistry = 75))

# find power 

def find_power(num, power):
    return num*power
print(find_power(2,2))   