import random





def choose_word():
    # This function selects and returns a secret word from a predefined list of words
    words = ["Brave", "Stone", "Dream", "Flame", "Pride", "Swift", "Cloud", "Plant", "Grace", "Storm", "Ocean", "Heart", "Light", "Music", "Trail"]
    secret_word = random.choice(words)
    return secret_word.lower()  

def get_guess(passed_guesses):
    # validate guess by checking if its 5 letters and not repeating guesses

    meets_criteria = False

    # loop that continues until the player inputs a valid guess
    while meets_criteria == False:
        
        players_guess = input("Enter a five-letter word: ").lower().strip()
        length_of_players_guess = len(players_guess)

        if length_of_players_guess == 5:
            if players_guess.isalpha():
                if players_guess not in passed_guesses:
            
                    meets_criteria = True
                else:
                    print("Please guess a word you haven't guessed before.")
            else: 
                print("Please only input letters.")
        else:
            print("Word is not 5 letters. Please try again")

    return players_guess    
            

        

def evaluate_guess(players_guess, secret_word):
    # This function checks if the letters are in the right place (compares)
    # compares the index of each letter in the guess with the secret word
    feedback = []
    for i in range(len(secret_word)):
        if players_guess[i] == secret_word[i]:
            feedback.append("G") # Correct letter and position
         

        elif players_guess[i] in secret_word:
            feedback.append("Y")  # Correct letter but wrong position
            
        else:
            feedback.append("-")  # Incorrect letter
            
    return feedback




def display_guess(players_guess, feedback):
    # prints the guess and its feedback with spaces between each symbol
    print("Guess: " + " ".join(players_guess).upper())
    print("Feedback: " + " ".join(feedback))



def has_won(players_guess, secret_word):
    # Returns True if the guess matches the secret word, False otherwise
    return players_guess == secret_word
