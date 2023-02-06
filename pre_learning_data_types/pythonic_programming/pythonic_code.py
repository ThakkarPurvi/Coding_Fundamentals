""" In Python3 command prompt type:
        python3
        import this """

" Output "
""" 
The Zen of Python, by Tim Peters
=================================
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!  """

"""
A tuple is a collection of related values or a sequence of related values. 
The values stored in a tuple can be of any type and they are indexed by integers. 
Important differences between a tuple and a list is the fact that a tuple is considered immutable, 
whereas a list is mutable. 
Tuples are read only 
With tuple we use () parenthesis
You use a comma-separated list of objects in a tuple. 
Parenthesis are not needed around a tuple unless the tuple is nested in a larger data structure. 
"""

data_tuple = ("val1", "val2")
data_list = ["val1", "val2"]
data_dict = {"key1": "val1", "key2":"val2"}
print("=====================================")


people = [("James", "Adams"),("Amelia", "Stone"),("Arsh", "Texton"), ("Tom", "Hanks"),("Ened", "Gliton"),("Gordon", "Ramsey")]

print(type(people))
print(type(people[0]))
print(type(people[0][0]))
print(type(people[0][0][0]))
print(type(people[1]))
print("=========== ITERATING FROM A TUPLE ==========================")

for f_name, l_name in people:
    # print("{} {}".format(f_name, l_name))
    # print(f"f_name:", f_name, "l_name:", l_name)
    print(f_name, l_name)

print("============= UNPACKING FUNCTIONS USING * =====================")
def person_name(f_name, l_name):
    print(f_name, "last name is", l_name)

for p in people:
    person_name(*p)


fruit = ["lime", "FIG", "CHERRY", "Banana", "Coconut",  "pear", "apricot", "orange", "apple", "mango", "fig"]
sorted_fruit = sorted(fruit)

print("================ SORT LIST WITH CASE =====================")
print(sorted_fruit)



print("=================== SORT LIST IGNORING CASE =================")

def ignore_case(item):
    return item.lower()

sorted_fruit2 = sorted(fruit, key=ignore_case)
print(sorted_fruit2)

print("=================== SORT LIST WITH LENGTH  =================")

def name_by_lenth(item):
    return (len(item), item.lower())

sorted_fruit3 = sorted(fruit, key=name_by_lenth)
print(sorted_fruit3)



print("============ SORTING LIST WITH NUMBERS ===================")

nums = [100, 200, 500, 600, 20, 30, 46]

nums1 = sorted(nums)
print(nums1)

nums2 = sorted(nums, key=str)
print(nums2)



print("============ SORTING LIST OF BOOKS WITH import function ===================")

import re

poem = [
    "This is for all those people",
    "Who hide in the dark",
    "For those who feel hopeless",
    "For those with a broken heart",

    "This is for every child and teen",
    "Who is trying to flee from their fears",
    "For those who cry themselves to sleep",
    "For those who drown in their tears",

    "This is for people who hide their scars",
    "Upon their wrists and their thighs",
    "I want to remind each of you",
    "There is a reason you're alive",

    "You are here for a purpose",
    "You are needed in this place",
    "You are special, you are beautiful",
    "It doesn't matter what size, gender, or race"
    
    "You are perfect just the way you are",
    "You are priceless, a wonderful new",
    "You are dearly treasured by many",
    "There is no one more important than you"]

print(poem)

rx_poem = re.compile(r'^(the|a|an)\s+', re.I)

def strip_poem(title):
    stripped_title = rx_poem.sub("", title.lower())
    return stripped_title

for book in sorted(poem, key=strip_poem):
    print(book)



print("============ LAMBDA function ===================")

print("====== LAMBDA ADD 5 ======")
add5 = lambda x: x + 5
print(add5(2))
print(add5(10))


print("====== LAMBDA ADD 2 NUMBERS ======")
add_2_no = lambda x, y: x + y
print(add_2_no(2, 8))
print(add_2_no(21, 81))

print("====== LAMBDA A FUNCTION OVER A VALUE ======")
printResult = lambda func, value: print(func(value))

print(printResult(add5, 30))


print("====== LAMBDA IN LISTS ======")

fruit = ["lime", "FIG", "CHERRY", "Banana", "Coconut",  "pear", "apricot", "orange", "apple", "mango", "fig"]
sorted_fruit_with_lambda = sorted(fruit, key=lambda e: e.lower())

print(sorted_fruit_with_lambda)

print("======================== LIST COMPREHENSIONS ========================")
print("====== SQUARES ======")

lam_num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,25,35,45,55,65,75,85,100,105]
square = [x**2 for x in lam_num]
print(square)

print("====== EVEN LIST ======")

evens = [x * 2 for x in range(20)]
print(evens)


print("====== UPPER LIST ======")

fruit = ["lime", "FIG", "CHERRY", "Banana", "Coconut",  "pear", "apricot", "orange", "apple", "mango", "fig"]
ufruits = [f.upper() for f in fruit]
print(ufruits)

print("====== LIST WITHIN A LIST ======")
values = [2, 42, 18, 92, "boom", ["a", "b", "c"]]
print(values)

print("====== DOUBLE LIST WITHIN A LIST ======")
double = [v * 2 for v in values]
print(double)

print("======================== DICTIONARY ========================")
animals = ["OWL", "Badger", "bushbaby", "Tiger", "Wombat", "GORILLA", "AARDVARK"]
comp = {a.lower(): len(a) for a in animals}
print(comp)

print("======================== SET COMPREHENSION ========================")
print("======== PRINT UNIQUE WORD FROM A TXT FILE ========")

import re
with open("./import_this_python.txt") as python_in:
    p = {w.lower() for ln in python_in for w in re.split(r"\W+", ln) if w}
print(p)


print("================== LIST COMPREHENSION TO GENERATE A NUMBER =================")
sum_function = sum([x*x for x in range(11)])
print([x*x for x in range(11)])

print("======== PRINT SUM OF THOSE SQUARES ========")
print(sum_function)
sum_function2 = sum(x*x for x in range(11)) # USING GENERATOR USING LESS MEMORY
print(sum_function2)


print("======== COUNT LENGTH OF THE TEXT - LINE BY LINE ========")
page = open("./import_this_python.txt")   # Open the file
m = max(len(l) for l in page)             # Read the text line by line
page.close()                              # Check length of each line
print(m)                                  # find maximum length of the line.



print("======== USE GENERATOR FUNCTION WITH THE YIELD STATEMENT ========")

def numb():
    a = 0
    for i in range(3):
        yield a
        a = a + 1
    for i in range(3):
        yield a
        a = a - 1
    yield 100
    yield 200
    yield 300

for n in numb():
    print(n)

print("======== USE GENERATOR TO GET PRIME NUMBERS (SAVES MEMORY) ========")

def next_prime(limit):
    flags = set()

    for i in range(2, limit):
        if i in flags:
            continue
        for j in range(2 * i, limit +1, i):
            flags.add(j)
        yield i

for prime in next_prime(200):
    print(prime, end = " ")




print("======== CUSTOM TRIMMED GENERATOR FUNCTION TO  ========")
print("======== CUSTOM TRIMMED GENERATOR FUNCTION TO  ========")

def trimmed(import_this_python):
    with open(import_this_python) as file_in:
        for line in file_in:
            if line.endswith("\n"):
                line = line.rstrip("\n\r")
            yield line

for tl in trimmed("./import_this_python.txt"):
    print(tl)

print("======== CUSTOM TRIMMED GENERATOR FUNCTION TO  ========")

