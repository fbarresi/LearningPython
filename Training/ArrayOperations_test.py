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

### EXERCISE 3: write a function that returns the first n even numbers
def get_even(n):
    return list(range(2,n*2+1,2))

### EXERCISE 4: write a function that returns the first n odd numbers
def get_odd(n):
    return list(range(1,n*2+1,2))

### EXERCISE 5: write a function that reverse an array
def reverse_array(numbers):
    n = numbers.copy()
    n.reverse()
    return n

### EXERCISE 6: write a function that sorts an array descending
def sort_array_desc(numbers):
    n = numbers.copy()
    n.sort()
    n.reverse()
    return n

### EXERCISE 7: write a function that sorts an array descending according to its digits descending
def sort_array_per_digits(array):
    n = array.copy()
    n.sort(key=count_digit)
    n.reverse()
    return n
def count_digit(arg):
    return len(str(arg))

##################### TEST CAB #####################
import pytest
@pytest.mark.parametrize('numbers, expected', [([1,2,3,4,5,6,7,8,9,10],[1,3,5,7,9]), ([2,2],[]), ([1],[1])])
def test_remove_even(numbers, expected):
    assert expected == remove_even(numbers)
@pytest.mark.parametrize('numbers, expected', [([1,2,3,4,5,6,7,8,9,10],[2,4,6,8,10]),([1,1],[]), ([2],[2])])
def test_remove_odd(numbers, expected):
    assert expected == remove_odd(numbers)
@pytest.mark.parametrize('n, expected', [(5,[2,4,6,8,10]),(1,[2]), (2,[2,4])])
def test_get_even(n, expected):
    assert expected == get_even(n)
@pytest.mark.parametrize('n, expected', [(4,[1,3,5,7])])
def test_get_odd(n, expected):
    assert expected == get_odd(n)
@pytest.mark.parametrize('numbers, expected', [([7,5,3,1],[1,3,5,7]),([1,2,36,7,8],[8,7,36,2,1])])
def test_reverse_array(numbers, expected):
    assert expected == reverse_array(numbers)
@pytest.mark.parametrize('numbers, expected', [([7,2,3,1],[7,3,2,1]),([1,2,36,7,8],[36,8,7,2,1])])
def test_sort_array_desc(numbers, expected):
    assert expected == sort_array_desc(numbers)
@pytest.mark.parametrize('numbers, expected', [([100,1000,0.00001],[0.00001,1000,100]),(["pear","banana","apple"],["banana", "apple", "pear"])])
def test_sort_array_per_digits(numbers, expected):
    assert expected == sort_array_per_digits(numbers)
