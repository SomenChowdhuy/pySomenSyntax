#set does not allow duplicate values and set items are unchangeable
x = set()
x.add(10)
x.add(20)
x.add(30)
x.add(40)
x.add(50)
print(type(x))
print(x)
x.add(50)
print(x)
# true and 1 are considered as the same value
set = {'orange',30,40,False,True,1}
print(set)

#union operator
x = {1,2,3}
y = {4,5,6}
print(x|y) 

#intersection operator
x = {1,2,3,4}
y = {3,4,5,6}
print(x&y)

#difference operator
x = {1,2,3,4}
y = {5,6,7,8}
print(x-y)

#XOR operator
x = {1,2,3,4}
y = {3,4,5,6}
print(x^y)

#converting list to set and set to list
li = [1,2,2,3,4,5,6,7,7,8]
m = set(li)
print(m)
n = list(m)
print(n)