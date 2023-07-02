class Phone:                       #parent class, super class, base class
    def call(self):
        print('You can call')
    def message(self):
        print('You can message')
class Samsung:                     #child class, sub class, derived class
    def call(self):
        print('You can call')
    def message(self):
        print('You can message') 
    def photo(self):
        print('You can take photo') 
p = Phone()
p.call()
p.message()        
s = Samsung()
s.call()
s.message()
s.photo()

#alternative
class Phone:
    def call(self):
        print('You can call')
    def message(self):
        print('You can message') 
class Samsung(Phone):
    # call, message
    def photo(self):
        print('You can take photos')
s = Samsung()
s.call()
s.message()
s.photo()
print(issubclass(Samsung,Phone))
print(issubclass(Phone,Samsung))

#practise yourself
class Animal:
    def eat(self):
        print('I can eat')
    def sleep(self):
        print('I can sleep')
class Dog(Animal):
    # eat, sleep
    def run(self):
        print('I can run')
d = Dog()
d.eat()
d.sleep()
d.run()
print(issubclass(Dog,Animal))