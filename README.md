# HANGMAN GAME
#### Video Demo:  <URL [HERE](https://youtu.be/gaLi8doG4d8)>
#### Description:

Hangman is an equivalent of a classic word guessing game played between two or more players. One player (a computer) thinks of a word and the other player (a user) attempts to guess it by suggesting letters within a certain number of attempts.

**Objective:**
The objective of Hangman is for the player(s) to guess the secret word correctly before running out of attempts. The game typically ends in one of two ways: either the player successfully guesses the word within the allotted number of attempts, or he failes to do so and the full hangman figure is drawn.

The number of attempts (usually represented by the number of body parts of the hangman figure) is predetermined.

Winning and Losing:
If the player successfully guesses the entire word or phrase before the hangman figure is fully drawn, he wins the game.
If the hangman figure is fully drawn (all body parts are added) before the entire word or phrase is guessed, the player loses the game.

**Features**
Randomly selects a word from a list of words read from a file.
Displays a hint for the word to be guessed.
Allows players to guess letters one at a time.
Provides feedback on whether the guessed letter is correct.
Displays a hangman figure representing incorrect guesses.
Ends the game when the word is fully guessed or the hangman figure is complete.
Allows players to play multiple rounds and tracks wins and losses.


**Implementation Details:**
Files:
hangman_images.py - contains the list of all hangman stages images in ASCII code.
words.txt - contains the list of the words from which one of the words will be randomly chosen for the guess.
test_project.py - contains unit tests for the code
project.py - contains the main logic to run the game

How the program handles the problem:
1 - the program opens .txt file with the words and returns the list of the words using function 'read_words_from_file' function
2 - randomly picks up a word from the list using 'random_word' function
3 - compares user guess with a word using 'is_guess_correct' function
4 - proms if a user enters non-alphabetical characters or nothing
5 - displays a guessed string using 'guessed_str_result' function
6 - check if a user wins

**Usage**
Ensure you have Python installed on your system.
Clone this repository to your local machine.
Navigate to the directory containing the Python files.
Run the hangman.py file using the command python hangman.py.
Follow the on-screen instructions to play the game.
Enjoy playing Hangman!

**Dependencies**
Python 3.x

**Additional Information**
This Hangman game was developed as a fun project to practice Python programming skills.
