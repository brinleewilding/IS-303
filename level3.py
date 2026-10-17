

import random

counter = 0


def get_guess():
    while True:
        try:
            guess = int(input("Guess a whole number between 1-100: "))
        except ValueError:
            print("Inalid input, please enter a whole number.")
            continue

        if 1 <= guess <= 100:
            return guess
        print("Out of range, please enter a number between 1 and 100.")
        
       
            





play_game = input("Do you want to play the game? (Y/N): ").upper()

# creating a loop that will run as long as the user wants to play the game
while play_game == "Y":

    # having computer generate number
    random_number = random.randint(1, 100)
    counter = 0
   
    # Having user guess a number
    users_number = get_guess()
     # using a counter to keep track of how many guesses the user has made
    counter += 1
   
    #creating a loop that will run as long as the user has not guessed the number
    while users_number != random_number:

       

        # using if statements to give the user hints on whether their guess is too high or too low
        if users_number > random_number:
            print("lower")
        elif users_number < random_number:
            print("higher")
        elif users_number == random_number:
            print("Congratulations!")
       

        # asking the user to guess again
        users_number = get_guess()

        # using a counter to keep track of how many guesses the user has made
        counter += 1

    # once the user has guessed the number, the program will print out how many guesses it took them to guess the number
    if counter <= 3:
        print("You are amazing")
    elif counter <= 5 :
        print ("Impressive!")
    elif counter <= 7:
        print("Good Job")
    elif counter <= 9:
        print("took a little longer, but you got it!")
    elif counter > 9:
        print("You need to lock in")

    print(f"Number of guesses: {counter}")

    # asking the user if they want to play again
    play_game = input("Do you want to play the game? (Y/N): ").upper()

  


