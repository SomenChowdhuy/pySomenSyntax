while True:
    x = int(input('Enter the 1st number: '))
    y = int(input('Enter the 2nd number: '))
    if x==0 and y==0:
        break
    try:
        print('Result is: ',x/y)
    except ZeroDivisionError:
        print('Sorry! Divide by zero not possible')
    else:
        print('Well done')