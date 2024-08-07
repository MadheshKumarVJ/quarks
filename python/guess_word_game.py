import random

def guess_word(secret_word: str) -> bool:
    max_attempts = 5
    attempts = 0
    guessed_word = ['_'] * len(secret_word)
    
    print("Welcome to the word guess game!")
    print(" ".join(guessed_word))
    
    while attempts < max_attempts:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("enter a letter.")
            continue
        
        if guess in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_word[i] = guess
            print("Good guess!")
        else:
            attempts += 1
            print(f"Wrong guess! You have {max_attempts - attempts} attempts left.")
        
        print(" ".join(guessed_word))
        
        if '_' not in guessed_word:
            print("Congratulations! You've guessed the word correctly!")
            return True
    
    print(f"Sorry, you've run out of attempts. The word was '{secret_word}'.")
    return False

word_list = ["python", "javascript", "development", "interface", "function", "variable"]

secret_word = random.choice(word_list)

guess_word(secret_word)
