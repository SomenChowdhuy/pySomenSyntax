
for f in range(6):
    x = float(input("Enter 1st number: "))
    y = float(input("Enter 2nd number: "))
    operator = input("Enter + - * / %: ")
    
    if operator == '+': 
        sum = x + y
        print("Sum is: ",sum)
    elif operator == '-': 
        sub = x - y
        print("Sub is: ",sub)
    elif operator == '/': 
        res = x/y
        print("Result is: ",res)
    elif operator == '*':
        product = x * y
        print("Res is: ",product)
    elif operator == '%':
        Mod = x % y
        print("Mod is: ",Mod)
    else:
        print("Enter the valid operator")
    