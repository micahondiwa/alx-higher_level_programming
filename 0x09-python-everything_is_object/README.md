# Python - Everything is object

- Projects done during my Full Stack Software Engineering studies at [ALX Africa](https://www.alxafrica.com/software-engineering-2022/), a course offered by [Holberton School](https://www.holbertonschool.com/).

## Technologies

- Files written in ```vi```, ```vim```, and ```emacs``` editors. 
- Files wriiten according to the betty coding style. Checked using [betty-style.pl](https://github.com/holbertonschool/Betty/blob/master/betty-style.pl) and [betty-doc.pl](https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl).
- Files tested on ```Ubuntu 20.04``` LTS using ```gcc```.
- ```Python3.4``` files 

## Files

- [0-answer.txt](0-answer.txt)- What function would you use to print the type of an object?
- [1-answer.txt](1-answer.txt)- How do you get the variable identifier (which is the memory address in the CPython implementation)?
- [2-answer.txt](2-answer.txt)- In the following code, do ```a``` and ```b``` point to the same object? Answer with ```Yes``` or ```No```:
```
>>> a = 89
>>> b = 100
```
- [3-answer.txt](3-answer.txt) - In the following code, do ```a``` and ```b``` point to the same object? Answer with ```Yes``` or ```No```.

```
>>> a = 89
>>> b = 89
 ```
- [4-answer.txt](4-answer.txt) - In the following code, do ```a``` and ```b``` point to the same object? Answer with ```Yes``` or ```No```.
```
>>> a = 89
>>> b = a
```

- [5-answer.txt](5-answer.txt) - In the following code, do ```a``` and ```b``` point to the same object? Answer with ```Yes``` or ```No```.
```
>>> a = 89
>>> b = a + 1
```

- [6-answer.txt](6-answer.txt) - What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```
- [7-answer.txt](7-answer.txt) - What do these 3 lines print?
```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 == s2)
```
- [8-answer.txt](8-answer.txt) - What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```
- [9-answer.txt](9-answer.txt) - What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```
- [10-answer.txt](10-answer.txt) - What do these 3 lines print?
```
>>> l2 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 == l2)
```
- [11-answer.txt](11-answer.txt) - What do these 3 lines print?
```
>>> l2 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 is l2)
```
- [12-answer.txt](12-answer.txt) - What do these 3 lines print?
```
>>> l2 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```
- [13-answer.txt](13-answer.txt) - What do these 3 lines print?
```
>>> l2 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```
- [14-answer.txt](14-answer.txt) - What do this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```
- [15-answer.txt](15-answer.txt) - What do this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```
- [16-answer.txt](16-answer.txt) - What do this script print?
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```
- [17-answer.txt](17-answer.txt) - What do this script print?
```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```
- [18-answer.txt](18-answer.txt) - What do this script print?
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```
- [19-copy_list.py](19-copy_list.py) - Write a function ```def copy_list(l):``` that returns a **copy** of a list.

- [20-answer.txt](20-answer.txt) - Is ```a``` a tuple? Answer with ```Yes``` or ```No```.
```
a = ()
```
- [21-answer.txt](21-answer.txt) - Is ```a``` a tuple? Answer with ```Yes``` or ```No```.
```
a = (1, 2)
```

- [22-answer.txt](22-answer.txt) - Is ```a``` a tuple? Answer with ```Yes``` or ```No```.
```
a = (1)
```
- [23-answer.txt](23-answer.txt) - Is ```a``` a tuple? Answer with ```Yes``` or ```No```.
```
a = (1, )
```
- [24-answer.txt](24-answer.txt) - What does this script print?
```
a = (1)
b = (1)
a is b
```
- [25-answer.txt](25-answer.txt) - What does this script print?
```
a = (1, 2)
b = (1, 2)
a is b
```
- [26-answer.txt](26-answer.txt) - What does this script print?
```
a = ()
b = ()
a is b
```
- [27-answer.txt](27-answer.txt) - Will the last line of this script print ```139926795932424```? Answer with ```Yes``` or ```No```.
```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```

- [28-answer.txt](28-answer.txt) - Will the last line of this script print ```139926795932424```? Answer with ```Yes``` or ```No```.
```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```
- [100-magic_string.py](100-magic_string.py) - Write a function ```magic_string()``` that returns a string “BestSchool” n times the number of the iteration.

- [101-locked_class.py](101-locked_class.py) - Write a class ```LockedClass``` with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called ```first_name```.
- [103-line1.txt](103-line1.txt) - How many int objects are created by the execution of the first line of the script?
 ``` 
a = 1
b = 1
```
- [103-line2.txt](103-line2.txt) - How many int objects are created by the execution of the second line of the script
``` 
a = 1
b = 1
```
- [104-line1.txt](104-line1.txt) - How many int objects are created by the execution of the first line of the script?
```
a = 1024
b = 1024
del a
del b
c = 1024
```
- [104-line2.txt](104-line2.txt) - How many int objects are created by the execution of the second line of the script?
```
a = 1024
b = 1024
del a
del b
c = 1024
```
- [104-line3.txt](104-line3.txt) - After the execution of line 3, is the int object pointed by ```a``` deleted? Answer with ```Yes``` or ```No```.
```
a = 1024
b = 1024
del a
del b
c = 1024
```
- [104-line4.txt](104-line4.txt) - After the execution of line 4, is the int object pointed by ```b``` deleted? Answer with ```Yes``` or ```No```.
```
a = 1024
b = 1024
del a
del b
c = 1024
```
- [104-line5.txt](104-line5.txt) - How many int objects are created by the execution of the last line of the script? 
```
a = 1024
b = 1024
del a
del b
c = 1024
```
- [105-line1.txt](105-line1.txt) - Assuming we are using a CPython implementation of Python3 with default options/configuration: Before the execution of line 2 (```print("Love")```), how many int objects have been created and are still in memory?
```
print("I")
print("Love")
print("Python")
```
- [106-line1.txt](106-line1.txt) -  How many string objects are created by the execution of the first line of the script?
```
a = "SCHL"
b = "SCHL"
del a
del b
c = "SCHL"
```
- [106-line2.txt](106-line2.txt) - How many string objects are created by the execution of the second line of the script?
```
a = "SCHL"
b = "SCHL"
del a
del b
c = "SCHL"
```
- [106-line3.txt](106-line3.txt)- After the execution of line 3, is the string object pointed by ```a``` deleted? Answer with ```Yes``` or ```No```. 
```
a = "SCHL"
b = "SCHL"
del a
del b
c = "SCHL"
```
- [106-line4.txt](106-line4.txt)- After the execution of line 4, is the string object pointed by ```b``` deleted? Answer with ```Yes``` or ```No```. 
```
a = "SCHL"
b = "SCHL"
del a
del b
c = "SCHL"
```
- [106-line5.txt](106-line5.txt) - How many string objects are created by the execution of the last line of the script.
```
a = "SCHL"
b = "SCHL"
del a
del b
c = "SCHL"
```
