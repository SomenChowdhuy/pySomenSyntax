"""
s = 'abcd'
print(len(s))
print(s[0:2])
print(s[1:3])
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-2:])
print(s[-3:])
print(s[:])
print(type(s))
print(10+10)
print("10"+"10")
print('abc'+'def')
print(10*3)
print('10'*3)
print('Bangladesh'*3)
print('100'+'100')
print(10+'10')
"""
"""
name = "Dimik"
name = name.upper()
print(name)
name = name.lower()
print(name)

district = "chittagong"
district= district.capitalize()
print(district)
district = district.upper()
print(district)
lower_dis = district.lower()
print(lower_dis)
district[0] = 'd'
print(district)
"""
"""
s = 'Bangladesh'
print(s.find('Bangla'))
print(s.find('desh'))
print(s.startswith('Bangla'))
print(s.endswith('desh')) 
"""
# split and join
my_string = "Apples,Oranges,Pears,Bananas,Berries"
print(my_string.split(","))
num = "2,4,6,8,10"
num = num.split(",")
print(num)

my_string = "I code for 2 hours everyday"
my_string = my_string.split()
print(my_string)
s = "mango","banana","apple","guava"
print(", ".join(s))

country = "Bangladesh","Nepal","Bhutan","Thailand","India"
print("___".join(country))