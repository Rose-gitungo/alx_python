def is_prime(number):
    for i in range(2,number):
        if number % 2 == 0:
         print('False')
        else:
         print('True')
    else:
        print('False')
        return