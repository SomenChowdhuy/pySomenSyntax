"""
i= 1
while i<10:
    print(i)
    i+=2
"""
"""
i = 2
while i<20:
    print(i)
    i+=2
"""
def mul_tbl(n):
   for i in range(1,11):
       print("{}x{}= ".format(n,i,n * i))
n = input("Enter n(0 to exit): ")
n = int(n)

while n!=0:
    mul_tbl(n) 
    print("")
    n = input("Enter n(0 to exit): ") 
    n = int(n)
    
while True:
    print