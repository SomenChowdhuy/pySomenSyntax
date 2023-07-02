try:
    fp = open('mynewfile.txt','r') 
    content = fp.read()
    fp.close() 
except FileNotFoundError:
    print('Your file is not found/available') 

try:
    fp = open('mynewfile.txt','r') 
    content = fp.read()
    fp.close() 
    print("bye bye")
except FileNotFoundError:
    print('Sorry file does not exist')
    


n1 = 10
n2 = 0
print(n1/n2)



