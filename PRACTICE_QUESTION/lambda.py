# def suqare(x):
#     return x*x
# print(suqare(5))   

# suqare_lambda = lambda x: x*x
# print(suqare_lambda(2))

# add = lambda a,b: a+b
# print(add(2,2))

# even = lambda n: n%2==0
# print(even(4))

# a = ["python","Data Science", "Dhrubo"]
# print(sorted(a))

# n = int(input("Enter the number: "))
# res = 1
# for i in range(1, n+1):
#     res *=i
# print(res)

# n = int(input("Enter Your Number: "))
# def factorial(n):
#     res = 1
#     for i in range(1, n+1):
#         res *=i
#     return res    
# print(factorial(n))        

fact_num = lambda n: 1 if n ==0 else n*fact_num(n-1)
print(fact_num(5))