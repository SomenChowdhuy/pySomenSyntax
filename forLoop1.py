"""
def mul_tbl(n):
    print(n,'x1= ',n*1)
    print(n,'x2 =',n*2)
    print(n,'x3 =',n*3)
    print(n,'x4 =',n*4)
    print(n,'x5 =',n*5)


n = input('Enter the number: ')
n= int(n) 
for i in range(1,n+1):
    mul_tbl(i)
    print("")
"""
"""
fruits = ['mango','apple','banana','orange']
for f in fruits:
    print(f)
"""
"""
cars = ['volvo','toyota','BMW']
for c in cars:
    print(c)
"""
Even_numbers = [2,4,6,8,10]
for i in range(5):
    print(i,Even_numbers[i])
    
for i in range(1,11,2):
    print(i)