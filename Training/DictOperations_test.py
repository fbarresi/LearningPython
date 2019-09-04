# Add the implementation every where you find a #to-do

### EXERCISE 1: count the keys of a dictionary
def count_keys(dictionary):
    return len(dictionary)

### EXERCISE 2: write a function that returns a dictionary of n key from 0 to n and value 1
def get_dictionary(n):
    return dict.fromkeys(range(n),1)

### EXERCISE 3: write a function that returns the first n even numbers as dictionary keys and their square as value
def get_even(n):
    return {x: x*x for x in range(2*n+1)[1::] if x%2 == 0}

### EXERCISE 4: write a function that returns the first n odd numbers as dictionary keys and their 3rd power as value
def get_odd(n):
    return {x: x**3 for x in range(2*n+1)[1::] if x%2 == 1}



##################### TEST CAB #####################
import pytest
@pytest.mark.parametrize('dict, expected', [({},0), ({'test':1},1), ({'121':121,'222':222},2)])
def test_count_keys(dict, expected):
    assert expected == count_keys(dict)

@pytest.mark.parametrize('n, expected', [(2,{0:1,1:1}),(3,{0:1,1:1,2:1}), (0,{})])
def test_get_dictionary(n, expected):
    assert expected == get_dictionary(n)

@pytest.mark.parametrize('n, expected', [(5,{2:4,4:16,6:36,8:64,10:100}),(1,{2:4}), (2,{2:4,4:16})])
def test_get_even(n, expected):
    assert expected == get_even(n)

@pytest.mark.parametrize('n, expected', [(4,{1:1,3:27,5:125,7:343})])
def test_get_odd(n, expected):
    assert expected == get_odd(n)


