# Add the implementation every where you find a #to-do

### EXERCISE 1: write a function that return a tuple with the first and last letter of a word
def get_start_and_end_letter(word):
    return word[0], word[-1]




##################### TEST CAB #####################
import pytest
@pytest.mark.parametrize('word, expected', [("test string",("t","g"))])
def test_start_and_end_letter(word, expected):
    assert expected == get_start_and_end_letter(word)