"""
- Functions are a way of isolating code that is
needed in more than one place by refactoring it to make it much more modular.
- Functions are defined with the def statement or def keyword.
- Functions returns a value.
- Functions can take various types of parameters, parameter types are dynamic.
- Functions, more often than not, can return one object of any type using the return statement.
- If there is no return statement, the function simply returns None.
"""

print("====== FUNCTIONS e.g. ======")

def say_hello():
    print("Hello World")
    print()

say_hello()
# Output: Hello World

print("====== FUNCTIONS type None (if we use print) ======")

hello = say_hello()
# Output: Hello World
type(hello)
# Output: class<'NoneType'>

print("====== FUNCTIONS type str (if we use return) ======")
def get_hello():
    return "Hello World!!!"
get_hello()
hello = get_hello()
print(hello)
# Output: Hello World!!!
type(hello)
# Output: class<'str'>

print("====== NUMBERS IN FUNCTIONS ======")

def sqrt(num):
    return num ** .5
m = sqrt(2525)
n = sqrt(121)
print(m)
print(n)

print("====== PRINTING USING STRING  FORMATTER ======")
print(f"Square root of 2525: {m}")
print(f"Square root of 121: {n}")

print("====== FUNCTION TAKING 0 PARAMETER ======")

def fun_one():
    print("Hello World")
fun_one()
# Output: "Hello World"

print("====== FUNCTION TAKING 1 PARAMETER ======")

def fun_two(n):
    return n ** 2
print(fun_two(5))
# Output: 25

print("====== FUNCTION TAKING PARAMETER AS COUNT ======")

def fun_three(count = 3):
    for i in range(count):
        print("spam",end = " ")
print(fun_three())
# Output: spam spam spam None

print("====== FUNCTION TAKING PARAMETER AS COUNT WITH AN ADDITIONAL PARAMETER 10 WHILE PRINT ======\n")

def fun_three(count = 3):
    for i in range(count):
        print("spam",end = " ")
print(fun_three(10))
# Output: spam spam spam spam spam spam spam spam spam spam None


print("\n====== FUNCTION TAKING OPTIONAL PARAMETER ======\n")

def fun_four(n, *opt):
    print("fun_four():")
    print("n is ", n)
    print("opt is ", opt)
    print("-" * 20)
print(fun_four("apple"))
# Output: fun_four():
# n is  apple
# opt is  ()        =====> ()(is a tuple)
# --------------------

print("\n====== FUNCTION TAKING OPTIONAL PARAMETERS ======\n")

print(fun_four("apple", "bluberry", "peach", "cherry"))

# Output: fun_four():
# n is  apple
# opt is  ()
# --------------------

print("\n====== FUNCTION TAKING OPTIONAL PARAMETERS ======\n")

def fun_five(*, spam=0, eggs=0):
    print("fun_five():")
    print("spam is:", spam)
    print("eggs is:", eggs)
    print()

print(fun_five(spam=1, eggs=5))

print("\n====== FUNCTION TAKING OPTIONAL PARAMETERS ======\n")

# def fun_six(** named):
#     print("fun_six():")
#     for n in named:
#         print(n, "==>", named[n])
#
# print(fun_six(n = "lanelpot", quest = "grail", color = "red"))

def fun_six(**named):
    print(named)
    print(type(named))

print(fun_six(n = "lanelpot", quest = "grail", color = "red"))
# Output: {'n': 'lanelpot', 'quest': 'grail', 'color': 'red'}
# <class 'dict'>

print("\n====== FUNCTION TAKING DEFAULT PARAMETERS ======\n")

def spam(greeting, whom="world"):
    print(f"{greeting}, {whom}")

print(spam("hello"))
print(spam("hello", "Jeremy"))

def ham(*, f_name, f_format = "txt"):
    print(f"Processing {f_name} as {f_format}")

print(ham(f_name = "apples"))
print(ham(f_name = "toast", f_format="csv"))


print("\n====== NAME RESOLUTION ======\n")

""" 
Scope: A scope is the area of a Python program, where an unqualified 
    (not preceded by a module name) name can be looked up. 
    Scopes are used dynamically. There are 4 nested scopes that are 
    searched for names in the following order:
    local    : local names bound within a function
    nonlocal : local names + local names of outer function(s)
    global   : the current module's global names
    builtin  : built-in functions(content of_builtins_module)
    
- Within a functions: all assignments and declarations create local names. 
    All variables found outside of local scope 
    (i.e. outside the function) are read-only. 
- Inside functions: local scope references 
    the local name of the current function. 
- Outside functions: local scope is the same as the global scope - the module's namespace.
    Class definitions also create a local scope. 
- Nested functions: provide another scope. 
    Code in function B which is defined inside 
    function A has read-only access to all of A's variables. 
    This is nonlocal scope 
"""

print("\n====== SCOPE ======\n")

global_scope = 42

def function_a():
    local_scoped_variable = 5
    def function_b():       # nested function
        local_scoped_variable_in_nested_function = 32
        print("function_b(): local_scoped_variable_in_nested_function:", local_scoped_variable_in_nested_function)
        print("function_b(): local_scoped_variable:", local_scoped_variable)
        print("function_b(): global_scope:", global_scope)
        print("function_b(): type(global_scope) is", type(global_scope))
    return function_b
f = function_a()
print(type(f))
# Output: <class 'function'>
print(f())
# Output: function_b(): local_scoped_variable_in_nested_function: 32
# function_b(): local_scoped_variable: 5
# function_b(): global_scope: 42
# function_b(): type(global_scope) is <class 'int'>



