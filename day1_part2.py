# a = int(input("First number: "))

# if a % 2 == 0:
#     print(f"{a} is even.")
# else:    print(f"{a} is odd.")

# score = int(input("Enter your score (0-100): "))
# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")

# username = ""
# password = ""
# username = str(input("Username: "))
# password = str(input("Password: "))

# if username == "Tom" and password == "1234":
#     print("Access granted.")
# else:
#     print("Access denied.")


for d in range(1, 101):
    if d % 3 == 0 and d % 5 == 0:
        print("FizzBuzz")   
    elif d % 3 == 0:
        print("Fizz")
    elif d % 5 == 0:
        print("Buzz")
    else:
        print(d)

import random
number = random.randint(1, 100)
guess = int(input("Guess the number (1-100): "))

while guess != number:
    if guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess the number (1-100): "))
print("Congratulations! You guessed the number.")

name = input("What's your name? ")
age = int(input("What's your age? "))
print(f"Hello, {name}! In 10 years, you'll be {age + 10}.")

fruits = ["apple", "banana", "cherry"]
print(fruits[0])    # apple  -- counting starts at 0!
print(fruits[1])    # banana
print(len(fruits))  # 3  -- how many items in the list
fruits.append("orange")  # add a new item to the end of the list
for fruit in fruits:
    print(f"{fruit} is delicious!")
len(fruits) # 4
for i in range(len(fruits)): # 0, 1, 2, 3
    print(f"Fruit {i + 1}: {fruits[i]}")

list1 = []
while True:
    object = input("Enter a number or a string (or 'done' to finish): ")
    if object == "done":
        break
    try:
        if object.isdigit():
            object = int(object)
        list1.append(object)
    except ValueError:
        print("That's not a valid object. Try again.")

if list1:
    print(f"You entered: {list1}")
else:
    print("No objects entered.")