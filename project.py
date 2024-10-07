import random
import sys
from hangman_images import HANGMANPICS


def read_words_from_file(filename):
    """Reads words from a file and returns a list of words."""
    try:
        with open(filename) as file:
            words = file.read().split()
            if not words:
                sys.exit("Error: File '{}' is empty.".format(filename))
            return words
    except FileNotFoundError:
        sys.exit("Error: File '{}' not found.".format(filename))


def random_word(words):
    """Selects a random word from a list of words."""
    return random.choice(words).upper()


def is_guess_correct(word,letter):
    """Checks if a guessed letter is correct."""
    return letter in word


def guessed_str_result(word, guessed_letters):
    """Builds a string representation of the word with guessed letters revealed."""
    guessed_string = ""
    # result = value_if_true if condition else value_if_false
    for letter in word:
        guessed_string = guessed_string + letter + ' ' if letter in guessed_letters else guessed_string + '_ '
    return f"\n{guessed_string}"


def hangman(index):
    """Returns the hangman image corresponding to the number of incorrect guesses."""
    return HANGMANPICS[index]


def main():
    words = read_words_from_file("words.txt")

    # while True continue play
    while True:

        word_to_guess = random_word(words)
        qty_unique_letters_of_word = len(set(word_to_guess))
        print("Hint:", word_to_guess)

        guessed_letters = set()
        lost_attemps = 0
        total_attemps = len(HANGMANPICS)

        print(guessed_str_result(word_to_guess, guessed_letters))

        while lost_attemps < total_attemps and len(guessed_letters) != qty_unique_letters_of_word:
            letter = input("\nGuess a letter: ").strip().upper()

            if not letter.isalpha() or len(letter) != 1:
                print("Please enter a single alphabetic letter.")
                continue

            if letter in guessed_letters:
                print("You've already guessed that letter.")
                continue

            if is_guess_correct(word_to_guess, letter):
                guessed_letters.add(letter)
            else:
                print(hangman(lost_attemps))
                lost_attemps += 1

            print(guessed_str_result(word_to_guess, guessed_letters))

        # check if user win
        if len(guessed_letters) == qty_unique_letters_of_word:
            print("\nYou won!")
        else:
            print("\nYou Lost. The word was:", word_to_guess)

        play_again = input("\nDo you wanna play more? (y/n): ").strip().lower()
        if play_again != 'y':
            sys.exit("Goodbye!")
            

if __name__ == "__main__":
    main()
