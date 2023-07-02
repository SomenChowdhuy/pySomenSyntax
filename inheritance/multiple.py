# exercise 1
class A:
    def display(self):
        print('I am inside A class') 
class B:
    def display(self):
        print('I am inside B class')
class C(A,B):
    # A--> display()
    # B--> display()
    def display(self):
        print('I am inside C class')
c = C()
c.display()

# exercise 2 
class A:
    def display(self):
        print('I am inside A class')
class B:
    def display(self):
        print('I am inside B class')
class C(A,B):
   # A-->display()
   # B-->display()
   pass
c = C()
c.display()

# exercise 2 
class A:
    def display(self):
        print('I am inside A class')
class B:
    def display(self):
        print('I am inside B class')
class C(B,A):
   # A-->display()
   # B-->display()
   pass
c = C()
c.display()