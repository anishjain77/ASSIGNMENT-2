# Program: Check if a number is even or odd

# Step 1: Take an integer input from the user
num = int(input("Enter an integer: "))

# Step 2: Check whether the number is even or odd
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
# Program: Sum of numbers from 1 to 50

# Step 1: Initialize a variable to store the sum
total = 0

# Step 2: Use a for loop to iterate from 1 to 50
for i in range(1, 51):
    total += i  # Add each number to total

# Step 3: Print the total sum
print("The sum of numbers from 1 to 50 is:", total)
