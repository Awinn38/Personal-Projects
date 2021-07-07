day  = int(input('What day of the month of September 2019 would you like to know? (Please enter a number 1-30): '))

if day in range(1,31):
    if day%7 == 2:
        print("That day was Monday")
    if day%7 == 3:
        print("That day was Tuesday")
    if day%7 == 4:
        print("That day was Wednesday")
    if day%7 == 5:
        print("That day was Thursday")
    if day%7 == 6:
        print("That day was Friday")
    if day%7 == 0:
        print("That day was Saturday")
    if day%7 == 1:
        print("That day was Sunday")
else:
    print("I'm sorry Please try entering a number between 1-30")
     