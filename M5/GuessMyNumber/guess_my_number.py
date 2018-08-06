"""Activity 8"""
print('Think of a number between 0 to 100')
LOW = 0
HIGH = 100
"""Guess the number"""
while True:
    GUESS = (HIGH+LOW)//2
    USER = input('Is your secret number ' + str(GUESS) + '\n')
    if USER == 'h':
        LOW = GUESS
    elif USER == 'l':
        HIGH = GUESS
    elif USER == 'c':
        print('Your secret number is : '+str(GUESS))
        break
    else:
        print('Invalid entry')
        GUESS = (HIGH+LOW)//2
