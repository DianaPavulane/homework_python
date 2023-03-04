# Task 1.1
a = 11
b = 20
print("The items are the same") if a == b else print("The items are different")

print("================================")
# Task 1.2
name = input("What's your name? ")
b = int(input("What is your age?: "))
if b > 18:
    print("Welcome to the club, " + name)
else:
    print("Sorry, you are not allowed to enter")

print("================================")
print("================================")

# Task 2.1
for x in range(0, 100, 7):
    print(x)
print("================================")
# Task 2.2
a = input("Enter a word: ")
b = ""
for x in range (len(a)-1, -1, -1):
    b += a[x]
print(b)
print("================================")
# Task 2.3
def factorial(x):
    factorial = 1
    if x >= 0:
        for i in range (1, x+1):
            factorial = factorial * i
        return factorial
    else:
        print("Invalid input")

print("================================")
print("================================")
# Practical Task 3.1: Write a Python function to find the Max of three numbers.
def max_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(max_three(5, 2, 11))

print("================================")

# Practical Task 3.2: Write a Python program to reverse a string.
a = "234abcd"
b = ""
for x in range (len(a)-1, -1, -1):
    b += a[x]
print(b)

print("================================")

# Practical Task 3.3: Third Practical Task
def sum_numbers(*numbers: float) -> float:
    """Sum the numbers"""
    return sum(numbers)

print(sum_numbers(1, 2, 3, 4, 5, ))

print("================================")
