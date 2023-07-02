num_To_words = dict()
num_To_words[1] = 'one'
num_To_words[2] = 'two'
num_To_words[3] = 'three'
num_To_words[4] = 'four'
num_To_words[4] = 'five' #Duplicate values will overwrite existing values
print(num_To_words)
print(type(num_To_words))
#alternative
num_To_words = {1:'one', 2:'two', 3:'three'}
num_To_words[4] = 'four'
print(num_To_words)

#access/refer value with key
num_To_words = {1:'one',2:'two',3:'three'}
print(num_To_words[3]) 

num_To_words = {1:'one',2:'two',3:'three'}
if 4 in num_To_words:
    print("available")
else:
    print("not found")

#Delete a member
num_To_words = {1:'one',2:'two',3:'three',4:'four'}
del num_To_words[3]
print(num_To_words) 

#for loop to print keys with values
num_To_words = {1:'one',2:'two',3:'three'}
for key,value in num_To_words.items():
    print(key,value)

#to check dictionary items    
print(dir(dict))

#To return keys or values
fruits = {'A':'apple','B':'banana','C':'coconut'}
print(fruits.keys()) 
print(fruits.values())

cars = {1:'Volvo',2:'BMW',3:'Toyota',4:'Tesla'}
print(cars.keys())
print(cars.values())

#to get an empth dictionary
fishes = { 
        1:'Catfish',
        2:'Barbel',
        3:'Tengra'
}
print(fishes)
fishes.clear()
print(fishes)

#To access values with key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.get('year'))
# print(thisdict[2]) 
print(thisdict.get('model'))
print(thisdict.get('brand'))
print(thisdict.get('price'))