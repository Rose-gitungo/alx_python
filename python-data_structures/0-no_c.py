def no_c(my_string):
    unwanted ='c'+'C'
    new_string=''.join(x for x in my_string if x not in unwanted)
    return new_string

unwanted ='c'+'C'
my_string='Chicago'
new_string=''.join(x for x in my_string if x not in unwanted)
print(new_string)