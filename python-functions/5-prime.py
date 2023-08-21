def is_prime(number):
    for i in range(2,number):
        if number % 2 == 0:
         print('False')
        else:
         print('True')
    else:
        print('False')
        return
    return
print(is_prime(17))
print(is_prime(15))
print(is_prime(-5))
print(is_prime(0))