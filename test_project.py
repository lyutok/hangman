from project import is_guess_correct, guessed_str_result, hangman
from hangman_images import HANGMANPICS

def test_is_guess_correct():
    assert is_guess_correct("cat", "a") == True
    assert is_guess_correct("cat", "q") == False


def test_guessed_str_result():
    assert guessed_str_result("WHALE", ("W", "E")) == "\nW _ _ _ E "
    assert guessed_str_result("WHALE", ()) == "\n_ _ _ _ _ "
    assert guessed_str_result("TURTLE", ("U", "E", "L", "R")) == "\n_ U R _ L E "
    assert guessed_str_result("ALPACA", ("A", "P", "L", "C")) == "\nA L P A C A "

def test_hangman():
    assert hangman(1) == HANGMANPICS[1]
