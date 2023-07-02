"""
def mul_tbl(n):
   #  print(n,"X",1,"=",n*1)
   # print(n,"X",2,"=",n*2)
   # print(n,"X",3,"=",n*3)
   
    print("{} x {} = {}".format(n,1,n*1))
    print("{} x {} = {}".format(n,2,n*2))
    print("{} x {} = {}".format(n,3,n*3))
    print("{} x {} = {}".format(n,4,n*4))
    print("{} x {} = {}".format(n,5,n*5)) 
    print("{} x {} = {}".format(n,6,n*6))
    print("{} x {} = {}".format(n,7,n*7))
    print("{} * {} = {}".format(n,8,n*8))
    
mul_tbl(3)
"""
def mul_tbl(n):
  for i in range(1,11):
    print('{} x {} = {}'.format(n,i,n*i))
  
mul_tbl(3)
