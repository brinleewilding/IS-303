
import random

approved_list = ["rock", "paper", "scissors"]
game_counter = 0
player_wins = 0
computer_wins = 0
num_rounds = 0



# creating a function to prompt user to input choice
def get_player_choice():
    player_choice = input("Enter rock, paper, or scissors: ").lower()
     
    while player_choice not in approved_list:
        print("Sorry your choice is not a valid choice.")
        player_choice = input("Enter rock, paper, or scissors: ").lower()
    return player_choice
   
   

# creating a function to compare the user's choice with the computer's choice and return "win", "loss", or "tie"
def determine_winner (user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "win"
    else:
        return "loss"



# welcome user to the game
print("Welcome to Rock Paper Scissors!")

# asking the user how many rounds they want to play
num_rounds = int(input("How many rounds do you want to play? "))
while num_rounds <= 0 or num_rounds % 2 == 0:
    print("Please try again, the number must be a positive, odd number.")
    num_rounds = int(input("How many rounds do you want to play? "))



# define the choices
choices = ["rock", "paper", "scissors"]

# play the game
while game_counter < num_rounds:
    user_choice = get_player_choice()
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    result = determine_winner (user_choice, computer_choice)
   

    #increment game counter
    if result == "win":
        print("You Won!")
        player_wins += 1
        game_counter += 1

    elif result == "loss":
        print("You lost!")
        computer_wins +=1
        game_counter += 1

    else:
        print("Tie! Play again.")


#Present final score

print("-----------------")
print(f"Scores -- You: {player_wins} | Computer: {computer_wins}")

if player_wins > computer_wins:
    print("You win!")
elif computer_wins > player_wins:
    print("Computer wins!")

print("Thanks for playing!")



