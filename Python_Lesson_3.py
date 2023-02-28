# Task 1
a = 11
b = 20
print("The items are the same") if a == b else print("The items are different")

print("================================")
# Task 2
name = input("What's your name? ")
b = int(input("What is your age?: "))
if b > 18:
    print("Welcome to the club, " + name)
else:
    print("Sorry, you are not allowed to enter")

print("================================")

# Task 2.1
for x in range(0, 100, 7):
    print(x)

# Task 2.2
a = input("Enter a word: ")
b = ""
for x in range (len(a)-1, -1, -1):
    b = b + a[x]
print(b)