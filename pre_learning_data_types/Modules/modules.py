print("\n====== MODULES ======\n")

"""
File containing python code
ends with .py
no real difference from scripts"""

"""
Module: A module is a file containing Python definitions and statements. 
The file name is the module name with the suffix.py appended.
Within a module, the module's name (as a string) is available as 
the value of the global variable name. 

To use a module names spam.py say import spam 

This does not enter the name of the functions defined in spam directly into the symbol table;
it only adds the module name spam. Use the module name to access the functions or other attributes. 

Python uses modules to contain functions that can be loaded as needed by scripts. 
A simple module contains 1 or more functions,
more complex modules can obtain initialization code as well. 
Python classes are also implemented as modules. 

A module is only loaded once, even there are multiple places in an application that import it.

Modules and packages should be documented with docstrings.

When working with module you need to us the import statements. 
- import statement loads modules 
- There are 3 variations on the import statement:
    ===> import module
        loads the module so its data and functions can be used, but does not put its attributes 
        (name of class, functions, and variables) into the current namespace. 
    ===> from module import function-list
        import only the function(s) specified into the current namespace. 
        Other functions are not available (even through they are loaded into memory)
    ===> from module import * (use with caution!)
        loads the module, and imports all functions that do not start with an underscore into current namespace. 
        This should be used with caution, as it can pollute the current namespace 
        and possibly overwrite builtin attributes from a different module.        
"""

"""
A package is a group of related modules or subpackages. 
The grouping is physical, that is, a package is a folder that contains one or more modules. 
It is a way of giving a hierarchical structure to the module namespace so that all modules do not 
live in the same folder. 

A package may have an initialization script named __init__.py. 
If present, this script is executed when the package or any of its contents are loaded. 
(In Python2, __init__.py was required.)

Modules in packages are accessed by prefixing the module with the package name using the 
dot notation used to access module attributes. 

As an example, if module eggs is in package spam, then to call the scramble function in eggs, 
you would likely call spam.eggs.scramble().

By default, importing a package name by itself has no effect. 
You must explicitly load the modules in the packages. 
You should usually import the module using its package name, like from spam import eggs, 
to import the eggs module from the spam package. 

Packages can be nested. Let's now take a look at a package example. 
"""

import sys
sys.version_info[0]

lab_exercise = "Comprehensions"
lab_type = "lab-code"
python_version = ("%s.%s.%s" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))
print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

#====================================

#CODE1: Create a list with various elements and then define a list comprehension that filters on it
randomChars = ['a', 0, -3, 10, 4, 'p', '>', 7]
squaresList = [ x**2 for x in randomChars if type(x) == int ]
print(squaresList)

#CODE2: Create a list with various animal names and then define a set comprehension that filters on it
animalsList = [ 'whale', 'TIGER', 'lion', 'lion', 'X', 'ELEPHANT', 'cheetah', 'cat', 'DOG', 'W' ]
animalsSet = { animal[0].upper() + animal[1:].lower() for animal in animalsList if len(animal) > 1 }
print(animalsSet)

#CODE3: Create a dict of square roots and then iterate of the items printing out each key-value pair
squareRoots = {x: x**0.5 for x in range(1,10)}
for idx, squareRoot in squareRoots.items():
  print(f'{idx} ---> {squareRoot:.2f}')


sys.version_info[0]

lab_exercise = "Generators"
lab_type = "lab-code"
python_version = ("%s.%s.%s" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))
print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

#====================================

#CODE1: Create a Generator Function that implements and yields the Fibonacci sequence
def fibonacci(max):
  a, b = 0, 1
  while a <max:
    yield a
    a, b = b, a+b

#CODE2: Iterate over the fibonacci generator function
numbers = 50
for num in fibonacci(numbers):
  print(num)

#CODE3: Use Generator Expressions to discover sum, min, and max of the square roots of a random list of numbers
import random
numbers = random.sample(range(1, 100), 20)
sumNumbers = sum(n**0.5 for n in numbers)
minNumbers = min(n**0.5 for n in numbers)
maxNumbers = max(n**0.5 for n in numbers)

#CODE4: Use f-string to format and print sum, min, and max
print(f"sum={sumNumbers} min={minNumbers} max={maxNumbers}")

sys.version_info[0]

lab_exercise = "Lambdas"
lab_type = "lab-code"
python_version = ("%s.%s.%s" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))
print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

#====================================

#CODE1: Use Lambda and Map to double numbers in a list
numbers = [1, 4, 6, 7, 9, 1, 43, 2, 2]
doubledMap = map(lambda x : x*2, numbers)
print(list(doubledMap))

#CODE2: Use Lambda and Filter to split list of numbers into odds and evens
numbers = [0, 24, 3, 7, 5, 2, 634, 26, 8, 33, 333, 100]
odds = filter(lambda x : x % 2 != 0, numbers)
evens = filter(lambda x : x % 2 == 0, numbers)
print(list(odds))
print(list(evens))