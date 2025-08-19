def fibonacii(n):
    if n < 0:#To handle negative values
        print("Invalid Value of n")
    elif n <= 1: #Base case
        return n 
    else:
        result = fibonacii(n-1) + fibonacii(n-2)#To show recursion and calculate the Fibonacci number
        return result
n = int(input("Enter the value of n: "))#get input from the user for the n value
result = fibonacii(n)#To generate the Fibonacci number of the n value provided by the user
print (f"The Fibonacii Number of {n} is {result}")#Display the result
