#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_digit=int(str(number)[-1])
if last_digit > 5 and number >0:
    print('Last digit of '+ str(number)+' is '+str(last_digit)+' and is greater than 5')
elif last_digit == 0:
    print('Last digit of '+str(number)+ ' is '+str(last_digit) +' and is 0')
elif last_digit <6 and last_digit !=0:
    print('Last digit of '+str(number)+ ' is '+str(last_digit)+' and is less than 6 and not 0')
