

import random

counter = 0


# having computer generate number


play_game = input("Do you want to play the game? (Y/N): ").upper()

# creating a loop that will run as long as the user wants to play the game
while play_game == "Y":

    # having computer generate number
    random_number = random.randint(1, 100)

    # Having user guess a number
    users_number = int(input("Guess a whole number between 1-100: "))

    #creating a loop that will run as long as the user has not guessed the number
    while users_number != random_number:

        # using a counter to keep track of how many guesses the user has made
        counter += 1

        # using if statements to give the user hints on whether their guess is too high or too low
        if users_number > random_number:
            print("lower")
        elif users_number < random_number:
            print("higher")
        elif users_number == random_number:
            print("Congratulations!")
        else :
            print("Invalid input, please try again, please input a whole number between 1-100: ")

        # asking the user to guess again
        users_number = int(input("Guess a whole number between 1-100: "))

    # once the user has guessed the number, the program will print out how many guesses it took them to guess the number
    if counter <= 3:
        print("You are amazing")
    elif counter <= 5 :
        print ("Impressive!")
    elif counter <= 7:
        print("Good Job")
    elif counter <= 9:
        print("took a little longer, but you got it!")
    elif counter > 10:
        print("You need to lock in")

    # asking the user if they want to play again
    play_game = input("Do you want to play the game? (Y/N): ").upper()

  


