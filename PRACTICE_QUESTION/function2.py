# int is not iterable
# iterable is an python object / sequential 
# iterator is an object a representing a stream of data. And return the data one by one 

# s = "Dhrubo"
# for i in s:
#     print(i)
#iter(s) # iterator syntax or object

# for i in "Dhrubo":
#     l = iter(i)
# print(next(l))

# take a list and gives square of each of the list

# def square(num):
#     res = []
#     for i in num:
#         res.append(i*i)
#     return res
# print(square([2,4]))    

# def square(num):
#     res = []
#     for i in range(num+1):
#         res.append(i*i)
#     return res
# print(square(10))

# Yield genral function uses return statement but a genrator function use yield
def square_number_generators(num):
    for i in range(num):
        yield i*i
#print(square_number_generators(10))   # yield is creating a genrator / iterator object
gen = square_number_generators(10)
print(next(gen))
print(next(gen))