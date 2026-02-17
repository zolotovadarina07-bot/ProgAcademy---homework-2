year = int(input('Input year: '))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("366 days")
else:
    print("365 days")