# Add the implementation every where you find a #to-do

### EXERCISE 1: write a function that removes all even numbers from an array
def remove_even(numbers):
    l = numbers.copy()
    for i in l:
        if i % 2 == 0:
            numbers.remove(i)
    return numbers

### EXERCISE 2: write a function that removes all odd numbers from an array
def remove_odd(numbers):
    l = numbers.copy()
    for i in l:
        if i % 2 != 0:
            numbers.remove(i)
    return numbers



##################### TEST CAB #####################
import pytest
@pytest.mark.parametrize('numbers, expected', [([1,2,3,4,5,6,7,8,9,10],[1,3,5,7,9])])
def test_remove_even(numbers, expected):
    assert expected == remove_even(numbers)
@pytest.mark.parametrize('numbers, expected', [([1,2,3,4,5,6,7,8,9,10],[2,4,6,8,10])])
def test_remove_odd(numbers, expected):
    assert expected == remove_odd(numbers)