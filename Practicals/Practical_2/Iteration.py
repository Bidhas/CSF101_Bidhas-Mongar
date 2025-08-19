def fibonacci(n):
    if n <= 0:#incase of -ve n values
        return "Invalid input"
    elif n == 1:#First Fibonacci number
        return 0
    elif n == 2:#Second Fibonacci number
        return 1
    a, b = 0, 1 #Initialize first two Fibonacci numbers
    #Iterate to calculate Fibonacci numbers up to n
    for i in range(2, n + 1):
        a, b = b, a + b
    return b #contains the nth Fibonacci number
#
n = int(input("Enter the value of n: "))
result = fibonacci(n)
print(f"The Fibonacci number at position {n} is {result}")