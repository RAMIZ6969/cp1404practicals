import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    car = Car()
    assert car.odometer == 0, "Car does not set odometer correctly"

    # Test if Car sets the fuel correctly
    car = Car(fuel=10)
    assert car.fuel == 10

    car = Car()
    assert car.fuel == 0


def phrase_to_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a .
    >>> phrase_to_sentence('hello')
    'Hello.'
    >>> phrase_to_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> phrase_to_sentence('This subject rocks')
    'This subject rocks.'
    >>> phrase_to_sentence('')
    '.'
    >>> phrase_to_sentence('    hello')
    'Hello.'
    """
    sentence = phrase.strip().capitalize()
    if sentence and sentence[-1] != '.':
        sentence += '.'
    elif not sentence:
        sentence = '.'
    return sentence


if __name__ == "__main__":
    run_tests()
    doctest.testmod()
