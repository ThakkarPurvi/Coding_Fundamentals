# bool

""" In Python Console,
Input: True
Output: True

Input: False
Output: False

Input: true
Output: Error

Input: True or False
Output: True

Input: True and False
Output: False

Input: True + True
Output: 2

Input: True + False
Output: 1

Input: False + False
Output: 0

Input: 1 + True
Output: 2

"""
# Numbers
""" Integers                - Whole real numbers - can perform simple arithmetic operations 
    Floating Point Decimals - Decimals numbers """

# Integers
""" 
Input: 5*5
Output: 25
======================

BODMAS 
Brackets 
Orders
Divisions (/)
Multiplication (*)
Addition (+)
Subtraction (-)

======================
Input: (5-2) * 2
Output: 6
======================
Input: 17 / 3 
Output: 5.666666666666667
======================
Input: 17 // 3 
Output: 5
======================
Input: 17 % 3 
Output: 2
======================
Input: 17 / 0
Output: ZeroDivisionError 
"""

# Strings
"""
Input: "Hello Python!!!"
Output: 'Hello Python!!!'
============= MULTI LINE BREAKS =============
Input: """Hello
Python"""
Output: 'Hello\nPython'
=========== STRING CONCATENATION ===============
Input: test = "Hello"
Input: test 
Output: 'Hello'
Input: test + "World"
Output: 'HelloWorld'

=========== IMMUTABILITY ===============
Input: a = "Hello"
Input: b = a 
Input: a = a + "World"
print(a)
print(b)

a = 'HelloWorld'
b = 'Hello'

=========== STRING SLICING ===============

-10  -9  -8  -7  -6  -5  -4  -3  -2  -1     =====> Negative Index
  0   1   2   3   4   5   6   7   8   9     =====> Positive Index
+---+---+---+---+---+---+---+---+---+---+
| H | E | L | L | O | W | O | R | L | D |
+---+---+---+---+---+---+---+---+---+---+
    1   2   3   4   5   6   7   8   9       =====> Positive Slice
   -9  -8  -7  -6  -5  -4  -3  -2  -1       =====> Negative Slice
    
=============    
Input: a[1:5]
Output: 'ello'

======================
Input: a[0:8] 0r a[:8]
Output: 'HelloWor'

=============
Input: a[:-8]
Output: 'He'

============
Input: a[-8]
Output: 'l'


"""

# Lists
""" 
- Single Dimension
- Mutable - can be changed
- Can contain data of different types 
- represented using square brackets []
- Lists are ordered and changeable.


=================
Input: a = []
Input: b = [1, "string", True, 2.3]
Input: b[2]
Output: True

===========
Input: b[-1]
Output: 2.3

=========== SLICING A LIST ===========
Input: b[-3:]   OR     b[1:]
Output: ['string', True, 2.3]

=========== ADDING IN A LIST USING append ===========
Input: b.append("test")
Input: b
Output: [1, 'string', True, 2.3, 'test']

=========== INSERTING IN A LIST USING insert ===========
Input: b.insert(2, "mytest")
Input: b
Output: [1, 'string', 'mytest', True, 2.3, 'test']

=========== CHECK LENGTH OF A LIST USING len ===========
Input: len(b)
Output: 6

=========== USING SLICING OPERATOR TO REPLACE AN ITEM EXISTING IN A DIFFERENT INDEX ===========
Input: b[1:2] = ["replace1", 2]
Input: b
Output: [1, 'replace1', 2, 'mytest', True, 2.3, 'test']

=========== DELETE USING EMPTY LIST [] ===========
Input: b[1:2] = []
Input: b
Output: [1, 2, 'mytest', True, 2.3, 'test']

=========== DELETE USING del() ===========
Input: del(b[1])
Input: b
Output: [1, 'mytest', True, 2.3, 'test']

=========== MULTI-DIMENSIONAL LIST ===========
Input: c = [a, b]
Input: c
Output: [[], [1, 'mytest', True, 2.3, 'test']]

=========== RETRIEVE LIST USING INDEX ===========
Input: c[1]
Output: [1, 'mytest', True, 2.3, 'test']

===========
Input: c[1]
Output: [1, 'mytest', True, 2.3, 'test']

===========
Input: c[1][1]
Output: 'mytest'

=========== APPEND IN -- MULTI-DIMENSIONAL LIST ===========
Input: c.append(c)
Input: c
Output: [[], [1, 'mytest', True, 2.3, 'test'], [...]]

===========
Input: c[2][1]
Output: [1, 'mytest', True, 2.3, 'test']

===========
Input: c[2][1][1]
Output: 'mytest'

"""

# Sets
"""
- Does not repeat items - All Unique 
- LISTS the UNIQUE Values 
- The insertion order has not maintained 
- 1 & True are treated a bool 
- Sets do not support the concept of indexing for RETRIEVING  
- use {} curly brackets 
- Sets are IMMUTABLE
- Sets are unordered and unindexed.

======================
Input: a
Input: b = {1, "string", 2.3, 1, 1, True}
Output: {1, 2.3, 'string'}

======================
Input: "string" in b
Output: True

======================
Input: "string" in c[1]
Output: False

======================
Input: "test" in c[1]
Output: True

"""

# Dictionaries
""""
- Uses {} brackets 
- consists of key value pair 
- each key is unique in a dictionary
- extract value using the key 
- keys can be of nay data types (e.g BOOL. NUM, INT, FLOAT, STRING)
- Dictionaries are MUTABLE 
- Associates Relationship 
- Dictionaries are unordered, changeable and indexed.


Input: a = {}
Input: b = {"a" : 1, "b" : 2, "c" : 3}
Input: b["a"]
Output: 1


============ CHANGE THE VALUE IN A DICTIONARY ===============
Input: b["a"] = "anything"
Input: b["a"]
Output: "anything"

============ ADD NEW KEY AND VALUE IN A DICTIONARY ===============
Input: b["d"] = 4
Input: b
Output: {'a': 'anything', 'b': 2, 'c': 3, 'd': 4}

============ OBTAIN LIST OF ALL KEYS FROM A DICTIONARY ===============
Input: list(b)
Output: ['a', 'b', 'c', 'd']

============ DELETE and REMOVE KEY VALUE PAIR IN A DICTIONARY ===============
Input: del(b["d"])
Output: {'a': 'anything', 'b': 2, 'c': 3}

"""

# Tuples

"""
- A tuple consists of a number of values seperated by commas
- Tuples are IMMUTABLE
- Tuples can be indexed as list 
- Tuples are ordered and unchangeable.
- represented using round brackets ()


===========
Input: t = 1,2,3,4
Input: t
Output: (1, 2, 3, 4)

=========== INDEX A TUPLE ===========
Input: t[0]
Output: 1

=========== RECURSIVE TUPLE ===========
Input: u = 7, t
Input: u
Output: (7, (1, 2, 3, 4))

=========== LENGTH IN A TUPLE ===========
Input: len(u)
Output: 2

=========== 
Input: t2 = "hello"
Input: len(t2)
Output: 5

=========== 
Input: t3 = "hello",
Input: len(t3)
Output: 1

"""