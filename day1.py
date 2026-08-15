# Exercise 1: Greeter
name = input("What's your name? ")
color = input("What's your favorite color? ")
print(f"Hi {name}, {color} is a great choice!")

# Exercise 2: Age in days
age = int(input("How old are you? "))
days = age * 365
print(f"You are roughly {days} days old.")

# Exercise 3: Calculator
a = int(input("First number: "))
b = int(input("Second number: "))
print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
print(f"Quotient: {a / b}")

# Exercise 4: Flow control
age = int(input("How old are you? "))

if age >= 18:
    print("You're an adult.")
elif age >= 13:
    print("You're a teenager.")
else:
    print("You're a kid.")

if age >= 18 and age < 65:
    print("Working age.")

