# l = [2,4,6,8]
# def square_list(l):
#     n = []
#     for i in l:
#         n.append(i*i)
#     return n 
# print(square_list(l))       

# map(function, iterable)
l = [2,3,4,5]
def add(x):
    return x+10
print(list(map(add,l)))

