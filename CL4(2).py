for f in range(6):
    n = input("Enter n: ")
    n = int(n)
    
    if n>=0 or n%2 == 0:
        print(n,'is positive & even number')
    elif n>=0 or n%2!=0:
        print(n,'is positive & odd number') 
    elif n<=0 and n%2 == 0:
        print(n, 'is negative & even number')
    else:
        print(n,'is negative & odd number')
        