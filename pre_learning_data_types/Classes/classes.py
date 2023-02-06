"""
Classes, as already mentioned, are a very powerful tool to organize code.
A class is a definition that represents a thing. The thing could be a file,
e.g. a process, a database record, a strategy, a string, a person, or a truck.

The class itself describes both data, which represents one instance of the thing,
and methods, which are functions that act upon the data.
There can be both class data, which is shared by all instances,
and instance only data, which is only accessible from the instance itself.

A class is the basic unit of object-oriented programming.
When it comes to defining classes, the syntax used is, you start with
the class keyword, followed by the class name.

class Classname(base_class):        # (base_class) if inheritance is involved.

The simplest form of a class definition could look like this,

class ClassName(): # empty ()because I'm not inheriting from a base class,
    pass              # and then the definition of the class, we'll just use the pass keyword.

- Normally, the contents of a class definition will be method definitions and shared data.
- A class definition creates a new local namespace.
    All variable assignments go into this new namespace.
    All methods are called via the instance or the class name.
- A list of base classes may be specified in parenthesis after the class name.
In this case, the class is then considered to extend or inherit from the space class.
"""


class Spam():
    def eggs(self):
        pass
    def _beverage(self):
        pass

s = Spam()
s.eggs()
s.toast = "butter"
print(s.toast)
print(s._beverage)


"""
Object instances.

- An object instance is an object created from a class.
    Each object instance has its own private attributes, which are usually
    created in the _init_ initialization method.
- Call class name as a function
- self contains attributes
- Syntax
obj = ClassName(args...)

Instance attributes.

An instance of a class (AKA object), normally contains methods and data.
To access these attributes, use the "dot notation", that is, object.attribute.

Instance attributes are considered dynamic.
They can be accessed directly from the object.
You can create, update and delete attributes in this way.

Attributes cannot be made private, but names that begin with an underscore are
understood by convention to be for internal use only. Users of your class will
not consider methods that begin with an underscore to be part of your class's API.

Again, this is convention only but should be understood and applied.

"""

print("\n-------- Instances Methods--------\n")

class Rabbit:
    def __init__(self, size, danger):
        self._size = size
        self._danger = danger
        self._victims = []
    def threaten(self):
        print(f"I am a {self._size} bunny with {self._danger}!")

r1 = Rabbit("large", "sharp pointy teeth")
print(r1.threaten())


print("\n-------- Constructors --------\n")

"""
Constructors, 

if a class defines a method named __inti__, it will be automatically called when object instances created. 
This is considered the constructor. 

The object being created, is implicitly past is the first parameter to __init__. 
This parameter is named self by very strong conviction. 
Data attributes can be assigned to self. 
These attributes can then be accessed by other methods, within the same class. 



Getters and setters. 

Getter and setter methods can be used to access and objects data. 
These are traditional in other object-oriented programming languages. 
A getter a retrieve a piece of data a private variable from self. 
A setter assigns a value to a variable or self. 
"""

class Knight(object):
    def __init__(self, name):
        self._name = name

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

k = Knight("Gate")
print(k.get_name())

k.set_name("John")

print(k.get_name())


"""
Properties, 
- While object attributes can be accessed directly, in many cases, 
    the class needs to demonstrate some control over the attributes. 

- A more elegant approach is to use properties. 
    A property is a kind of managed attribute. Properties are accessed directly, 
    much like normal attributes or variables, but getter a setter and deleter 
    functions are implicitly called, so that the class can control 
    what values are stored or retrieved from the attributes. 
    
- You can create get a setter into later properties. 

- To create the get a property apply the @property decorator to a method with 
    the name you want. It receives no parameters other than self. 
      
- To create the setter property, create a second function with the property name. 
    Decorate this property with the name plus .setter. In other words, 
    if the property name is spam, the decorator will be @spam.setter. 
    The setter method will take one additional parameter other than self, 
    which is the value assigned to the property. 

- It is common for a setter property to rise an error if the value being assigned 
is invalid. 

- While you seldom need a delete a property, creating it is the same as for 
    setter property but instead  use "@propertyname.deleter"

Lets now we use our class Knight definition by using properties. """


class Knight():
    def __init__(self, name, title, color):
        self._name = name
        self._title = title
        self._color = color

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def title(self):
        return self._title

k = Knight("Gate", "Sir", "blue")
print({k.name}, {k.color})
# Output: {'Gate'} {'blue'}

k.color = "Red"
print({k.name}, {k.color})
# Output: {'Gate'} {'Red'}

