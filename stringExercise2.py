#strip() removes spaces at the beginning and at the end of the string:
txt = "  banana  "
s = txt.strip()
print("of all fruits",s,"is my favourite")

txt = "  best"
#s = txt.strip()
s = txt.strip()
#print("honesty is the",txt,"policy") 
print("honesty is the",s,'policy')

#Use the len method to print the length of the string
x = "hello dude"
#s = len(x)
#print(s)
print(len(x))

#Get the first character of the string txt
x = "Bye World"
print(x[0]) 

#Get the characters from index 2 to index 4 (llo)
txt = "Hello World"
print(txt[2:5]) 

#Return the string without any whitespace at the beginning or the end
txt = "  Hey threre  "
x = txt.strip()
print(x)

#Convert the value of txt to upper case
name = "somen"
print(name.upper())
print(name.capitalize())
name2 = "KAMRUL"
print(name2.lower())

#Replace the character H with a J
txt = "Hello World"
print(txt.replace('H','J')) 

#Insert the correct syntax to add a placeholder for the age parameter
age = 36 
txt = "My name is Somen and I am {}"
print(txt.format(age))