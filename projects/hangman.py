import random

# List of words
words = ["alpha", "beta", "charlie", "delta"]


# Choose a random word
def choose_word():
    return random.choice(words)


# Function to check the current state
# _ _ _ _ _
# l
# _ l _ _ _
# h
# _ l _ h _
# t
# Message: letter not in word
def display_word(word, guesses):
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()


def play_game():
    word = choose_word()
    guesses = []  # Mutable
    turns = 10

    while turns > 0:
        # Display the current state of the word
        display_word(word, guesses)

        # Ask the user for their guess
        guess = input("Guess a letter: ")

        # Check if the guess is valid
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid guess. Please enter a single letter.")
            continue

        if guess in guesses:
            print("You have already guessed that leter. Try again")
            continue

        # Add the guess to the list of guesses
        guesses.append(guess)

        # Check if guess is in the word:
        if guess in word:
            print("Good guess!")
        else:
            print("Sorry, the letter is not in the word.")
            turns -= 1 # turns = turns - 1
            print("Turns left: ", turns)

        # Check if the word has been guessed
        if all(letter in guesses for letter in word):
            print("Congratulations, you guess the word!")
            return

    # player runs out of the turns
    print("Sorry, you ran out of turns. The word was", word)


def main():
    print("Welcome to Hangman")
    play_game()
    print("Thanks for playing")


if __name__ == "__main__":
    main()















