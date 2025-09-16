# python_code_tips

## From 11 python_code_tips
> https://www.youtube.com/watch?v=8OKTAedgFYg

### 1. Iterate with enumerate instead or range(len(x))

Bad way
```python
data = [1,2,-4,-3]
for i in range(len(data)):
   if data[i] <0 :
      data[i] = 0
      
print(data)
```

Better way
```python
data = [1,2,-4,-3]
for idx, num in enumerate(data):
    if num < 0:
       data[idx] = 0
       
print(data)
```

### 2. Use list comprehension instead of raw for loops

Bad Way; if super short and is not readable
```python
squares = []
for i in range(10):
    squares.append(i*i)
print(squares)
```

Better way; if super short and is not readable
```python
squares = [i*i for i in range(10)]
print(squares)
```

List comprehension example
```
connections = [conn for conn in some_list]
```

### 3. Sort complex iterables with sorted()

Simple iterable sorting using list
```python
data = [3,5,1,10,9]
sorted_data = sorted(data)
print(sorted_data)
```

Complex iterable sorting using dict of list
```python
data = [ {"name": "max", "age" : 6},
         {"name": "lisa", "age" :20},
	 {"name": "ben", "age" :9}]
	 
sorted_data = sorted(data, key=lambda x: x["age"])
print(sorted_data)
```

### 4. Store unique values with Sets

```python
my_list = [1,2,3,4,5,6,7,7,7]
my_set = set(my_list)
print(my_list)

primes = {2,3,5,7,11,13,17,19}
print(primes)

```

### 5. Save memory with Generators
```python

connections = (conn for conn in some_list)
```

### 6. Define default values in Dictionaries with .get() and .setdefault()
```python
my_dict = {"item": "football", "price": 10.00}
count = my_dict.get("count", 0)
print(count)

count = my_dict.setdefault("count", 0)
print(count)
```

### 7. Count hashable objects with collections.Counter
https://docs.python.org/3/library/collections.html#collections.Counter

Print the counts of all lists
```python
from collections import Counter

my_list = [10,10,10,5,5,2,9,9,9,9,9,9]
counter = Counter(my_list)

print(counter)
```

Find the most common
```python
from collections import Counter

my_list = [10,10,10,5,5,2,9,9,9,9,9,9]
counter = Counter(my_list)

most_common = counter.most_common(1)
print(most_common)
```

Find the least common
```python
from collections import Counter

my_list = [10,10,10,5,5,2,9,9,9,9,9,9]
counter = Counter(my_list)

least_common = counter.most_common()[-1]
print(least_common)
```

### 8. Format strings with f-Strings (Python 3.6+)

```python
name = "Bob"
my_string = f"Hello {name}"
print(my_strin)
```

### 9. Concatenate strings with .join()
```python

strings_to_join = ["Join", "this", "string"]
message = " ".join(strings_to_join)
print(message)

Join this string
```

### 10. Merge dictionaries with {**d1, **d2} (Python 3.5+)

https://towardsdatascience.com/merge-dictionaries-in-python-d4e9ce137374

```python
d1 = {"name": "Alex", "age": 25}
d2 = {"name": "Alex", "city": "New York"}
merged_dict = {**d1, **d2}
print(merged_dict)
```

### 11. Simplify if-statements with if x in list

```python
colors = ["red", "green", "blue"]

c = "red"
if c in colors:
   print(f"{c} is main color")
```

### Random items

Use vars() to enuermtae objects with properties into dictionaries

```python
class Example:

   def __init__():
      self._name = None
      
   @property
   def name(self)
		try :
			return self._name
		except Exception as e:
			raise e

example = Example()
print(vars(example))

{"_name" : None }

```

## From 10 Python Tips and Tricks for Writing Better Code
> https://www.youtube.com/watch?v=C-gEQdGVXbk

1.) Ternary Conditionals
Instead of the following
```python
condtion = True
if condition:
   x = 1
else:
   x = 0
```
You can write this one oneline with Ternary Conditionals
```python
condition = True
x = if condition else 0
```

2.) Unerscore Placholers with large numbers
```python
num1 = 10_000_000_000
```
Seperators in output
```python
num1 = 10_000_000_000
num2 = 100_000_000
total = num1 + num2
print(f'{total:,}')

10,100,000,000
```
3.) Context Managers
Bad smell, the code works but you want to use context managers for auto closing
```python
f = open('test.txt', 'r')

file_contents = f.read()

f.close()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)

```
Context manager
```python
with open('test.txt', 'r') as f:
   file_contents = f.read()
   
words = filel_contents.split(' ')
word_count = len(words)
print(word_count)
```
**not just for files, can be with databases or anything with managing resources and requiring some type of setup and shutdown.
4.) Enumerate
Looping but manually keeping up with the index
```python
names = ['Bob', 'Doyle', 'Joe']
index = 0
for name in names:
    print(index, name)
    index += 1
```
Enumerate, keeps up with index automatically
```python
names = ['Bob', 'Doyle', 'Joe']
for index, name in enumerate(names):
    print(index,name)
```
5.) Zip
Looping through two lists that correspond
```python
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
for index, name in enumerate(names):
    hero = heroes[index]
    print(f"{name} is actually {hero}")
```

Using zip instead of enumerate
```python
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
for name, hero in zip(names, heroes):
    print(f"{name} is actually {hero}")
```

6.) Unpacking
Zip actual returns a tuple and in the previous example we were unpacking
```python
# Packed example
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
for value in zip(names, heroes):
    print(value)
('Peter Parker, Spiderman)
```
Unpacking exmaple
```python
a, b = (1,2)
print(a)
print(b)
```
Unpacking but only using one value
```python
a, _ = (1, 2)
print(a)
```
Unpack with more than exists
```python
a,b,c = (1,2) #ValueError not enough values to unpack (expected 3, got 2)
a,b,c = (1,2,3,4,5) #ValueError too many values to unpack (expected 3)

a, b, *c = (1 ,2, 3, 4, 5) # by putting an * in front of C c gets allthe other values

a,b,*_ = (1,2,3,4,5) #ignores everything else after a,b

a,b,*c,d = (1,2,3,4,5) #a,b set to first two values, d is set to last, c has the values in the middle
```

7.) Setattr/Getattr
Initiall python uses dynmaic attributes
```python
class Person():
   pass
   
person = Person()

# dynamic attributes in python
person.first = "Bob"
person.last = "Doyle"
```
Using setattr directly you can use variables
```python
class Person():
   pass

first_key = "first"
first_val = "Bob"

setattr(person, first_key, first_val)
```

Using setattr to set the person attributes
```python
class Person():
   pass
   
person = Person()

person_info = {'first': 'Corey', 'last': 'Schafer'}

for key, value in person_info.items():
    setattr(person, key, value)
```
Using getattr to retrive keys

```python
class Person():
   pass
   
person = Person()

person_info = {'first': 'Corey', 'last': 'Schafer'}

for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))
```

8.) Getpass
Typing in secret values

Wrong way
```python
username = input('Username: ')
password = input('Password: ')

Print('Logging in...)
```

Better way with getpass
```python
from getpass import getpass

username = input('Username: ')
password = getpass('Password: ')

print('Logging in...)
```

9.) Python dash m
What happens with the -m option?
```python
# Creating a virtual environment with venv module
python -m venv .venv

# Start debug server
python -m smtpd -c DebuggingServer -n localhost:1025
```
-m search sys.path for the named module and execute contents like main module


10.) Help/Dir
```python
python
>>>help # interactive help in python interpreter

>>>help(http) # help on specific modules
```
```python
dir(http) #returns a list of valid attributes for the object passed
```
