def fibonacci_sequence(n):
    x=[] #init list
    for i in range (n):
        x.append(map(i,((n-1)+(n-2))))

   
    return 
# fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))