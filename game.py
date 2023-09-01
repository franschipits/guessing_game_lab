"""A number-guessing game."""
import random
# Put your code here
print("Hi!")
print("Greetings player!")
name = input("Please enter your name: ")
print(f"Hi! {name}")
print("Choose random number between 1 and 100")

#num = random.randint(1, 101)
#guesses = 0
def guessing_game():
    guesses = 0
    num = random.randint(1, 101)
    while True: 
        #where user inputs 
        #check if input is just numbers
        #if contains letters : input wrong guess again 
        #else convert to int
        number = input("number: ")
        if number.isalpha():
            print("Type a number...")
        else:
            number = int(number)
            if number != num:
                if number > num:
                    print("Lower!")
                if number < num:
                    print("Higher!")
            guesses = guesses + 1
            if number == num:
                print(f"Congratulations! You got it in {guesses} guesses")
                break
guessing_game()
