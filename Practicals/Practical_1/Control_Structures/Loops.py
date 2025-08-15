for i in range (1,6):
    print(i)
# Using a while loop to count down from 5 to 1
count = 5 
while count > 0:
    print(count)
    count -= 1
#Calculate the sum of numbers for 1 to 10 using a for loop
total = 0
for number in range(1, 11):
    total += number
print(f"The sum of numbers from 1 to 10 is: {total}")
#using for loop to iterate through a list of fruits
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
#using Nested loops to create a multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i * j}")
    print()