# Add the implementation every where you find a #to-do

### EXERCISE 1: write a function that return a tuple with the first and last letter of a word
def get_start_and_end_letter(word):
    return word[0], word[-1]


### EXERCISE 1: write a function that count the words of sentence
def get_words_count(string):
    return len(string.split())


##################### TEST CAB #####################
import pytest
@pytest.mark.parametrize('input, expected', [("test string",("t","g"))])
def test_start_and_end_letter(input, expected):
    assert expected == get_start_and_end_letter(input)

@pytest.mark.parametrize('input, expected', [("test string",2), ("What If I try to write a really complex sentence?",10),("Sentence    with  many    leer    spaces     ",5)])
def test_words_count(input, expected):
    assert expected == get_words_count(input)