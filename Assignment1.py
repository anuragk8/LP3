def fibonacci_r(n):
    if n == 1:
        fib = 1
    
    elif n == 2:
        fib = 1

    else:
        fib = fibonacci_r(n-1) + fibonacci_r(n-2)
    
    return fib

def fibonacci_i(n):
    a = 0
    b = 1
    if n == 0:
        return 0
    
    elif n == 1:
        return 1

    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b        
            


n = int(input("Enter a number: "))

print("Recursively: ")

for i in range (1, n+1):
    print(fibonacci_r(i))
print("Iteratively: ")

for i in range (1, n+1):
    print(fibonacci_i(i))
