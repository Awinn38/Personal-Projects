num_peppers = input("Set a number value for a variable called num_peppers: ")
num_peppersint = int(num_peppers)
num_onions = input("Set a number value for a variable called num_onions: ")
num_onionsint = int(num_onions)
num_tortillas = input("Set a number value for a variable called num_tortillas: ")
num_tortillasint = int(num_tortillas)
num_Total = num_peppersint + num_onionsint + num_tortillasint

if __name__=='__main__': 
    print('I have {} pepper(s) in my pantry'.format(num_peppers))
    print('I have {} onion(s) in my pantry'.format(num_onions))
    print('I have {} tortillas(s) in my pantry'.format(num_tortillas))
    print('I have a total of {} items in my party'.format(num_Total))
