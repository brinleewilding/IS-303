import random

def one_play(s):
    guess = int(input("Guess a number between 1 and 100: "))
    while not (guess >= 1 and guess <= 100):
            guess = int(input("Invalid number. Please try again: "))
    
        numb_guesses += 1
    
        #Determine the need of guess adjustment
    if guess > solution:
        print("Lower")
    elif guess < solution:
        print("Higher")
    elif guess == solution:
        print("Congratulations! You guessed the number!")

    
guess = 0
numb_guesses = 0

print("Welcome to the Higher/Lower Game!")


# get a random number for user to guess
solution = random.randint(1, 100)

while guess != solution:
    one_play(solution)


print(f"It took you {numb_guesses} guesses.")
