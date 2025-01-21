from functools import reduce

# words = ["Data", "Science", "Course"]
# result = reduce(lambda x, y: x + " " + y, words)
# print(result)

# number =[1,2,5,3,100,1000,6,10000]
# result = reduce(lambda x,y: x if x>y else y, number)
# print(result)


def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))
print(factorial(5))    