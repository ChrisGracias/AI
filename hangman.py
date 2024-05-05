import random

# List of words for the game
word_list = ["apple", "banana", "orange", "grape", "kiwi", "strawberry", "blueberry", "watermelon", "pineapple", "peach"]

# Function to choose a random word from the word list
def choose_word(word_list):
    return random.choice(word_list)

# Function to display the current state of the word with blanks for unknown letters
def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

# Function to check if the player has guessed all the letters in the word
def is_word_complete(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

# Function to play the Hangman game
def play_hangman():
    word = choose_word(word_list)
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts_left > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Correct guess!")
            print(display_word(word, guessed_letters))
            if is_word_complete(word, guessed_letters):
                print("Congratulations, you guessed the word!")
                break
        else:
            guessed_letters.append(guess)
            attempts_left -= 1
            print(f"Incorrect guess! {attempts_left} attempts left.")
            print(display_word(word, guessed_letters))
    
    if attempts_left == 0:
        print(f"Sorry, you ran out of attempts. The word was '{word}'.")

# Start the game
play_hangman()
