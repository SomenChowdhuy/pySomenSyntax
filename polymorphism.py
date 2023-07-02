#built in polymorphism function
name = 'Code unlimited'
Year = [2023,2022,2021,2020]
print(len(name))
print(len(Year))

#user defined polymorphism function
def sum(a,b,c=0):
    return a+b+c
print(sum(10,20))
print(sum(30,40,25))

#len() returns the number of characters
x = "Hello World"
print(len(x))   #built in polymorphism function

#For tuples len() returns the number of items in the tuple:
x = ('apple','banana','pear')
print(type(x),len(x))    # #built in polymorphism function

#For dictionaries len() returns the number of key/value pairs in the dictionary:
dict = {'name':'Somen',
        'age': 24,
        'City':'Feni'}
print(len(dict))


