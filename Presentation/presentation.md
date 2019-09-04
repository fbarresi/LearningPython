---
logoImg: "https://static.wixstatic.com/media/3f290a_bdf9f0fbf29f48d5a1b1ef6be8d94b2f~mv2_d_2100_1500_s_2.png/v1/fill/w_126,h_130,al_c,q_80,usm_0.66_1.00_0.01/Titelbild2.webp"
highlightTheme: "monokai-sublime"
separator: "----"
---

# Python

----

 von **Monty Python** zum **Python**...

 entwichelt von Guido van Rossum <br><i>(erst Google, dann Dropbox)</i><br>die komplette Geschische <a href="https://de.wikipedia.org/wiki/Python_(Programmiersprache)">hier</a> oder [hier](http://www.igfd.org/?q=python).

note: 
geboren aus dem Frust der Nutzung von ABC.

----
# Leitfahden? 
Klar, immer dabei! 
Ich muss sie nur importieren... 

```python
import this
```
gemacht!

----

### Was macht Python so stark?
- einfach (less keywords)
- open source
- interpretiert (typeless variables)

----

### interpre-was???

![](https://www.data-science-architect.de/wp-content/uploads/2019/03/compInt.jpg)

----

### interpre-was???
![](https://www.data-science-architect.de/wp-content/uploads/2019/03/pythonAusf%C3%BChrung.jpg)
<small>und <img src="https://upload.wikimedia.org/wikipedia/commons/b/b0/Pypy_logo.png" height=30 /> ?</small>

note: PyPy ist ein Just-in-Time-Compiler für die Programmiersprache Python, der selbst in Python geschrieben ist. Da die Programmierer mit einer Python-Implementierung in Python selbst (und nicht in C, wie dies bei der Referenzimplementierung CPython der Fall ist) experimentieren können, macht PyPy es einfacher, Bereiche zu finden, in denen die Python-Implementierung verbessert werden kann. Darüber hinaus erlaubt PyPy den Entwicklern durch seine Flexibilität, mit mehreren Implementierungen eines speziellen Features zu experimentieren. Eines der Ziele des Projektes war es, einen Python-Interpreter zu entwickeln, der schneller als CPython ist, was im März 2008 erstmals gelang.[4] Mittlerweile ist PyPy in einer überwiegenden Zahl von Benchmarks schneller als CPython,[5] – und in Sonderfällen sogar schneller als C.[6]

----
# hands on python

----

### Variables
- typeless
- no extra declaration
- managed memory
----
### List
- mixed
- dynamics
- double indexed
----
### List indexes
![](https://cdn.programiz.com/sites/tutorial2program/files/python-list-index.png)

----

### Lists methods
<small>

<table>
<thead><tr><td>Method</td><td>Description</td></tr></thead>
<tr><td>append()</td> <td>Add an element to the end of the list</td></tr>
<tr><td>extend()</td> <td>Add all elements of a list to the another list</td></tr>
<tr><td>insert()</td> <td>Insert an item at the defined index</td></tr>
<tr><td>remove()</td> <td>Removes an item from the list</td></tr>
<tr><td>pop()</td> <td>Removes and returns an element at the given index</td></tr>
<tr><td>clear()</td> <td>Removes all items from the list</td></tr>
<tr><td>index()</td> <td>Returns the index of the first matched item</td></tr>
<tr><td>count()</td> <td>Returns the count of number of items passed as an argument</td></tr>
<tr><td>sort()</td> <td>Sort items in a list in ascending order</td></tr>
<tr><td>reverse()</td> <td>Reverse the order of items in the list</td></tr>
<tr><td>copy()</td> <td>Returns a shallow copy of the list</td></tr>
</table>

</small>

----

### Operators

- all logical and arithmetical operators are included

----

### Conditions

- Logical Operators
- falsy ```None``` variables
- special operators (```in``` - ```not``` - ```is```)

----

### Loops
- the ```for``` loop
- the ```while``` loop

----

### Dictionaries
- built-in complex object
- naturally json structure
----
#### Dictionary methods
<font SIZE="3">

<table>
<thead><tr><td>Method</td><td>Description</td></tr></thead>
<tr><td>clear()</td> <td>Remove all items form the dictionary</td></tr>
<tr><td>copy()</td> <td>Return a shallow copy of the dictionary</td></tr>
<tr><td>fromkeys(seq[,v])</td> <td>Return a new dictionary with keys from seq and value equal to v (defaults to None)</td></tr>
<tr><td>get(key[,d])</td> <td>Return the value of key. If key doesnot exit, return d (defaults to None)</td></tr>
<tr><td>items()</td> <td>	Return a new view of the dictionary's items (key, value)</td></tr>
<tr><td>key()</td> <td>Return a new view of the dictionary's keys</td></tr>
<tr><td>pop(key[,d])</td> <td>Remove the item with key and return its value or d if key is not found. If d is not provided and key is not found, raises KeyError</td></tr>
<tr><td>popitem()</td> <td>Remove and return an arbitary item (key, value). Raises KeyError if the dictionary is empty</td></tr>
<tr><td>setdefault(key[,d])</td> <td>If key is in the dictionary, return its value. If not, insert key with a value of d and return d (defaults to None)</td></tr>
<tr><td>update([other])</td> <td>Update the dictionary with the key/value pairs from other, overwriting existing keys</td></tr>
<tr><td>values()</td> <td>Return a new view of the dictionary's values</td></tr>
</table>

</font>


----

#### Dictionary build-in funcions
<small>

<table>
<thead><tr><td>Method</td><td>Description</td></tr></thead>
<tr><td>all()</td> <td>Return True if all keys of the dictionary are true (or if the dictionary is empty)</td></tr>
<tr><td>any()</td> <td>Return True if any key of the dictionary is true. If the dictionary is empty, return False</td></tr>
<tr><td>len()</td> <td>Return the length (the number of items) in the dictionary</td></tr>
<tr><td>cmp()</td> <td>Compares items of two dictionaries</td></tr>
<tr><td>sorted()</td> <td>	Return a new sorted list of keys in the dictionary</td></tr>
</table>

</small>

----



### Functions
```python
def my_function(parameter1, parameter2):
    if parameter1 > parameter2:
        pass
    else:
        parameter1
```

----
#### args und kwargs
Python can map parameters from lists or dictionaries
```python
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')
```
or
```python
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

>>> greet_me(name="yasoob")
name = yasoob
```
----

### User inputs (and casting)

```python
test_text = input ("Enter a number: ")

test_number = int(test_text)

if test_number % 2 == 0 :
    print('the number you entered is even!')
else:
    print('the number you entered is odd!')

```

----


### Classes

- custom objects with methods, properties etc...
- can implement special function of ```object```

----

### Module

Modules (and submodules) in Python are easy folder with a ```__init__.py``` file.

An ```import``` statement execute this file.


<small>
Python has a package manager ```pip``` for public (and privates) modules
</small>

----

### Exercises

fork or download here: https://github.com/fbarresi/PythonExercises