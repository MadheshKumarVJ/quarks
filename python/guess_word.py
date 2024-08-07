import random

def is_correct_guess(secret_word, guessed_word):
    return guessed_word.lower() == secret_word

def play_game():
    secret_word = 'guess'
    max_attempts = 5
    attempts = 0
    print("Welcome to the game!")
    print(f"You have {max_attempts} attempts.")

    while attempts < max_attempts:
        guessed_word = input("Enter your guess: ")
        attempts += 1
        if is_correct_guess(secret_word, guessed_word):
            print("Congratulations! Your guess is correct.")
            break
        else:
            print(f"Incorrect, you have {max_attempts - attempts} attempts left.")
    
    if attempts == max_attempts and not is_correct_guess(secret_word, guessed_word):
        print(f"Sorry, you have used all your attempts. The correct word is '{secret_word}'.")

play_game()
