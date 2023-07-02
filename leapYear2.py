for f in range(6):
    year = input("Enter year: ")
    year = int(year)
    if year%400 == 0 or year%100!=0 and year%4==0:
        print(year,'is leap year')
    else:
        print(year,'is not leap year')