print('string')
print("Welcome to String")
s = "Bangladesh"
print(s)
#multiline strings
z = """Lorem ipsum dolor lorem,
lorem ipsum dolor,lorem
ipsum dolor........"""
print(z) 

s = '''I love Bangladesh,I 
love Bangladesh,I love
Bangladesh'''
print(s)

w = "Hello,World!"
print(w[1])

for x in 'banana':
    print(x)

for i in '12345':
    print(i)

for name in 'Somen':
    print(name)
    
for f in 'apple':
    print(f)

s = "Bye, World!"
print(len(s))

s = "Hello, there!"
print(len(s))

txt = "The best things in life are free!"
print('free' in txt)
print('life' in txt)
print('best' in txt)

txt = "The best things in life are free"
if 'free' in txt:
    print("yes, free is present")
    
txt = "I love coding all day long"
if 'coding' in txt:
    print('Yes, coding is present')

txt = "What's wrong with you?"
if 'wrong' in txt:
    print("Yes, wrong is present")
    
txt = 'I abhor you'
print('love' not in txt)
    
txt = "In fact, knowledge is not cheap"
if 'costly' not in txt:
    print('No, costly is not present')

for i in 'Chittagong':
    print(i)
    
s = "Welcome Back!"
print(s[2:5])
print(s[:5])
print(s[2:])
print(s[-5:-2])

print(s.upper())
print(s.lower())

#remove whitespace from the beginning and the end
s1 = " Hello, World!"
print(s1.strip())

s2 = "Hello, World! "
print(s2.strip()) 

s3 = "Well done! "
print(s3.strip())

s4 = " Have fun coding"
print(s4.strip())

#replace the string
txt = "Hello,there"
print(txt.replace('H','J'))

txt2 = "Bye for now"
print(txt.replace('now','today'))

txt3 = "See you there"
print(txt3.replace('there','tomorrow')) 

#split 
w = "Hello,World"
print(w.split(","))

w1 = "Welcome,back!"
print(w1.split(","))

w = "Good Night Buddies"
print(w.split())
#concatenate two strings
x = "Nice to "
y = "Meet you"
z = x + y
print(z)

s1 = "Glad to"
s2 = " Meet you"
s3 = s1 + s2
print(s3)

#To add a space between them, add  " ":
s1 = "Stay"
s2 = "tuned!"
s3 = s1+' '+s2
print(s3)

w1 = "Stay"
w2 = "Focused"
w3 = w1+" "+w2
print(w3)

txt = "superstar"
print(txt.capitalize())

#print("somen"+"chowdhury") 
#print("somen"+2023)
#String Formatting
"""
age = 35
txt = "My name is Khan and i am "+age
print(txt)
"""
age = 35 
txt = "My name is khan and I am {}"   #{} denotes the placeholder
print(txt.format(age))

phone = "01881859243"
txt = "My contact no is {}"
print(txt.format(phone))

b_date = "1998"
txt = "My birth year is {}"
print(txt.format(b_date))

quantity = 3
item = 500
price = 50
txt = "I want {} pieces of items {} for {} dollars"
price(txt.format(quantity,item,price)) 

quantity = 3
item = 400
price = 60
txt = "I want to pay {2} dollars for {0} pieces of item {1}"
print(txt.format(quantity,item,price)) 

#join
w = "somen","nadia","faria","emon"
print(", ".join(w)) 

w = "100","200","300","400","500"
print("____".join(w)) 

w = "100","200","300"
print(", ".join(w))

