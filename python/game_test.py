import random

def guess_word(secret_word, guessed_word):
    return secret_word.lower() == guessed_word.lower()
      
def play_game():
    secret_word_list = ['apple', 'berry', 'peach', 'kiwis']  # Fixed typo in list name
    secret_word = random.choice(secret_word_list)  # Corrected typo in list name

    max_attempts = 5
    attempts = 0
    print("Welcome to the 'Guess the Fruit Name' game!")
    print(f"You have {max_attempts} attempts in this game.")

    while attempts < max_attempts:
        guessed_word = input("Enter your guess: ")
        attempts += 1  # Corrected increment

        if guess_word(secret_word, guessed_word):
            print("Good guess!")
            break
        else:   
            print(f"Incorrect, you have {max_attempts - attempts} attempts left.")
    
    if attempts == max_attempts and not guess_word(secret_word, guessed_word):
        print(f"Sorry, you lost. The correct word is '{secret_word}'.")

play_game()
