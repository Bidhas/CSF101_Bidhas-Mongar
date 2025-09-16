'''m = ['Pop', 'Rock', 'Jazz', 'Classical', 'Hip-Hop', 'R&B']
m.sort()
print(m)
print(type(m))
m.append('Country')
m.extend(['Blues', 'Reggae'])
print(m)
with open ("New file.txt", "w") as file:
    file.write("Whats up dude ? \n")
    file.write("This is my new file")
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("New file.txt", "w") as file:
    file.writelines(lines)
    
def factorial(n):
    if n==0 or n==1:
        return n 
    else:
        return n*factorial(n-1)
val = int(input("Enter any Positive Integer: "))
print(factorial(val))'''
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Example usage:
num = 7
print(f"Fibonacci({num}) =", fibonacci(num))


