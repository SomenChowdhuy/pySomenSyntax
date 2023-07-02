for f in range(6):
    n = input("Enter a number: ")
    n = int(n)
    if n>=0:
        if n%2 ==0:
            print(n,'is +ve and even number')
        else:
            print(n,'is -ve and odd number')
    else:
        if n%2 == 0:
            print(n,'is negative and even number')
        else:
            print(n,'is negative and odd number')

"""
if n%2==0:
    print(n,'is even number')
else:
    print(n,'is odd number')
"""