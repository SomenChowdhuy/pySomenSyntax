#public member
class student:
    def __init__(self, name):
        self.sname = name;
newstudent = student("Somen Chowdhury")  #create an object called newstudent
print(newstudent.sname)

#private member
"""
class student:
    def __init__(self,name):
        self.__sname = name
newstudent = student('Somen Chowdhury')  # #create an object called newstudent
print(newstudent.__sname)
"""

#The protected member is accessible. from inside the class and its sub-class
"""
class student:
    def __init__(self,name):
        self._sname = name
obj = student('Fiza')
print(obj._sname)
"""

#public members
class student:
    def __init__(self,name,rank,points):
        self.name = name
        self.rank = rank
        self.points = points
s1 = student('Somen',1,100)
s2 = student('Rony',2,200)
s3 = student('Fiza',3,75)
s4 = student('Fatema',4,60)
print("I am "+s1.name+"\nand I got rank",+s1.rank) 
print("I am "+s2.name+"\nand I got rank",+s2.rank)
print("I am "+s3.name+"\nand I got rank",+s3.rank)
print("I am "+s4.name+"\nand I got rank",+s4.rank)
