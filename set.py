#set does not allow duplicate values and set items are unchangeable
s = set()
print(type(s))
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)
s.add(4) 
print(s)

# true and 1 are considered as the same value
s = {True,"apple","cherry",1,2,'banana'}
print(s)
#union operator
s1 = {1,2,3,4}
s2 = {3,4,5,6}
s3 = s1|s2
print(s3)

#intersection operator
s1 = {1,2,3,4}
s2 = {3,4,5,6}
s3 = s1 & s2
print(s3) 

#difference operator
s1 = {1,2,3,4}
s2 = {3,4,5,6}
s3 = s1 - s2 
print(s3)

#XOR operator
s1 = {1,2,3,4}
s2 = {3,4,5,6}
s3 = s1 ^ s2
print(s3) 

x = {2,4,5,6}
y = {5,6,7,8}
z = x ^ y
print(z)

#converting list to set and set to list
li = [1,2,2,3,4,5,6,7,7,8,] 
s = set(li)
print(s)
li1 = list(s)
print(li1)

#if we want to do it in a single line then- 
li = [1,2,2,3,4,5,6,7,7,8]
li1 = list(set(li))
print(li1) 