# Add the implementation every where you find a #to-do

### EXERCISE 1: write a function that return a tuple with the first and last letter of a word
def get_start_and_end_letter(word):
    return word[0], word[-1]

### EXERCISE 2: write a function that count the words of sentence
def get_words_count(string):
    return len(string.split())

### EXERCISE 3: write a function that reverse a word
def reverse(word):
    return word[::-1]

### EXERCISE 3-bis: write a function that check if a word is a palindrom (https://de.wikipedia.org/wiki/Palindrom)
def is_palindrom(word):
    return word == reverse(word)

### EXERCISE 4: write a function that capitalize a word (from name to Name)
def make_upper(word):
    return word.upper()

### EXERCISE 5: write a function that capitalize a word (from name to Name)
def make_capitalized(word):
    return word.capitalize()

### EXERCISE 6: write a function that swap lower with upper case letters in a word
def swap_case(word):
    return word.swapcase()



##################### TEST CAB #####################
import pytest
@pytest.mark.parametrize('input, expected', [("test string",("t","g"))])
def test_start_and_end_letter(input, expected):
    assert expected == get_start_and_end_letter(input)

@pytest.mark.parametrize('input, expected', [("test string",2), ("What If I try to write a really complex sentence?",10),("Sentence    with  many    leer    spaces     ",5)])
def test_words_count(input, expected):
    assert expected == get_words_count(input)

@pytest.mark.parametrize('input, expected', [("test","tset"), ("abc","cba"),("numeric","ciremun")])
def test_reverse(input, expected):
    assert expected == reverse(input)

@pytest.mark.parametrize('input, expected', [("hannah",True), ("neben",True),("federico",False)])
def test_palindrom(input, expected):
    assert expected == is_palindrom(input)

@pytest.mark.parametrize('input, expected', [("not-capitalize-me","NOT-CAPITALIZE-ME"), ("TEST","TEST"),("evopro","EVOPRO")])
def test_upper(input, expected):
    assert expected == make_upper(input)

@pytest.mark.parametrize('input, expected', [("evopro","Evopro"), ("what","What"),("tell me?","Tell me?")])
def test_capitalize(input, expected):
    assert expected == make_capitalized(input)

@pytest.mark.parametrize('input, expected', [("Fede","fEDE"), ("NoW","nOw"),("evoFLOW","EVOflow")])
def test_swap_case(input, expected):
    assert expected == swap_case(input)