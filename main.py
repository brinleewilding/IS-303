# importing the functions from wordle_functions.py

from wordle_functions import choose_word
from wordle_functions import get_guess
from wordle_functions import evaluate_guess
from wordle_functions import display_guess
from wordle_functions import has_won


play_again = True

# welcoming message and instructions for the game

print("-----------------------------------")
print("Welcome to Mystery Wordle!")
print("Guess the five-letter word.")
print("G = correct letter and position")
print("Y = correct letter, wrong position")
print("- = letter is not in the word")
print("There are no repeating letters in the secret word.")
print("-----------------------------------")

# main game loop that continues until the player chooses to stop playing

while play_again == True:
    secret_word = choose_word()
    passed_guesses = []
    won = False
    attempt = 1

    # loop that allows the player to make up to 6 attempts to guess the secret word

    while attempt <= 6 and not won:
        print("Attempt " + str(attempt) + " of 6")
        players_guess = get_guess(passed_guesses)
        
        passed_guesses.append(players_guess)


        feedback = evaluate_guess(players_guess, secret_word)
        display_guess(players_guess, feedback)

        if has_won(players_guess, secret_word):
            won = True

        attempt = attempt + 1

    # displaying the result of the game and asking the player if they want to play again   
    if won:
        print("Congrats you solved the puzzle")
    else:
        print(f"You lost, the secret word was: {secret_word}")

    answer = input("Play again? (yes/no): ").lower()
    if answer == "yes" or answer == "y":
        pass
    else:
        play_again = False
        print("Thanks for playing!")

    
        

