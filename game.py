"""A number-guessing game."""
import random
# Put your code here
print("hi")
print("Greetings player")
name = input("please enter your name:")
print(name)
print("Choose random number between 1 and 100")

# while True: 
#     number = input("number: ")
#     num = random.randint(1, 101)
#     if number != num:
#         print(num)
#     if number == num:
#         break

while True: 
    guesses = 0
    number = input("number: ")
    num = random.randint(1, 101)
    if number != num:
        if number > num:
            print("Lower")
        if number < num:
            print("Higher")
        guesses + 1
    if number == num:
        print(f"Congratulations! You got it in {guesses}")