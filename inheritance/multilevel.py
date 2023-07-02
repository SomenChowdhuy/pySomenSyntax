class A:
    def display1(self):
        print('I am inside A class')
class B(A):
    # display1()
    def display2(self):
        print('I am inside B class') 
class C(B):
    # display1(),display2()
    def display3(self):
        print('I am inside C class') 
c = C()        
c.display1()
c.display2()
c.display3()



#alternative method
class A:
    def display1(self):
        print('I am inside A class')
class B(A):
    # display1()
    def display2(self):
        print('I am inside B class')
class C(B):
    # display1(), display2()
    def display3(self):
        super().display1()
        super().display2()
        print('I am inside C class')

c = C()
c.display3()

# self exercise
class Person:
    def display1(self):
        print('I am a person')
class Teacher(Person):
    # display1
    def display2(self):
        print('I am a Teacher')
class Student(Teacher):
    # display1
    # display2
    def display3(self):
        super().display1()
        super().display2() 
        print('I am a Student')
s = Student()
s.display3()