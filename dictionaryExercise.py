x = dict()
x[0] = 'one'
x[1] = 'two'
x[2] = 'three'
x[3] = 'four'
x[3] = 'five'
print(x)
print(type(x))


x = {0:'one',1:'two',3:'three'} 
x[4] = 'four'
print(type(x),x)


#refer to value with its key
num_to_word = {1:'one',2:'two',3:'three',4:'four'}
print(num_to_word[3])


num_to_word = {1:'one',2:'two',3:'three',4:'four'}
if 4 in num_to_word:
    print("available")
else:
    print("not available") 
    
    
num_to_word = {1:'one',2:'two',3:'three',4:'four'}
print(num_to_word.get(3))

    
#remove a number
num_to_word = {1:'one', 2:'two',3:'three',4:'four'}
del num_to_word[3] 
print(num_to_word) 

#to print keys
num_to_word = {10:'ten',20:'twenty',30:'thirty'}
print(num_to_word.keys())  

#to print values
num_to_word = {10:'ten',20:'twenty',30:'thirthy'}
print(num_to_word.values())

#for loop to print key and values
num_to_word = {1:'one',2:'two',3:'three'}
for key,value in num_to_word.items():
    print(key,value)
    
#to clear a dictionary
names = {'name1':'Faria','name2':'Trisha','name3':'Somen'}
print(names)
names.clear()
print(names)



