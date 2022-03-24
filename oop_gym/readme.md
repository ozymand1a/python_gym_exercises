# Content

[01. Classes and Attributes](#01-classes-and-attributes)

[02. Attributes (`setattr`, `getattr`, `delattr`, `__dict__`)](#02-attributes-setattr-getattr-delattr-dict)

[03. `__init__` and `self`](#03-__init__-and-self)

[04. Properties (`getter`, `setter`, `deleter`)](#04-properties-getter-setter-deleter)

[05. Dunder methods (`get`, `set`)](#05-dunder-methods-get-set)

[06. `@staticmethod`](#06-static-methods)

[07. Slots](#07-slots)

[08. Dunder method 'new'](#08-dunder-methods-new)


## 01. Classes and attributes

    1. Classes contain methods but not functions.

    2. Instance is a copy of class

    3. Instances of classes inherit class attributes.
    If we change attributes at class,
    we change this attribute at all instances.
    
    4. `self` is the argument that provides access to instances of class 

```python3
class TestClass:
    version = 1

print(TestClass.version) # 1
exm = TestClass()
TestClass.version = 2
print(exm.version) # 2
exm.version = 3
TestClass.version = 4
print(exm.version) # 3
```


## 02. Attributes (`setattr`, `getattr`, `delattr`, `dict`)

```python3
class User:
    name = "Test"
    age = 17
    
    def get_name(self):
        print(self.name)
        
print(User.name) # "Test"
print(getattr(User, "name")) # "Test"
print(getattr(User, "surname", "null")) # "null"

a = User()
print(getattr(User, "name")) # "Test"
setattr(a, "surname", "Test2")
print(a.surname) # "Test2"

delattr(User, "name")
print(User.name) # Error

a = User()
getattr(a, "get_name") # return function
```

## 03. `__init__` and `self`

    1. Methods like this "__method_name__" are called "dunder".
    They are also reserved at 'Python'.

    2. '__init__' is called when you create class instance

    3. `__init__` and `self` create separate namespaces

```python3
class User:
    def __init__(self):
        print('work!')

a = User() # "work!"
```

## 04. Properties (`getter`, `setter`, `deleter`)

    1. 

```python3
class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def set_name(self, value):
        self.name = value


```

## 05. Dunder methods (`get`, `set`)

    1. Allow more comfortable way to use property method

```python3
class Data:
    def __init__(self):
        self.value = ''

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value

class User:
    name = Data()
    surname = Data()

test = User()
test.name # ''
test.name = 111
test.name # 111
```

## 06. Static methods

    1. Allow to call class method (function) without
    creation of class's instance
    
    2. Using decorator @staticmethod is necessary!

```python3
class User:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_data(self):
        print(self.name)
        print(self.value)
    
    @staticmethod
    def get_sum(x, y):
        return x + y

User.get_sum(1, 3) # return 4!
```

## 07. Slots

    1. 

## 08. Dunder methods 'new'

    1.

## 09. `@classmethod`

    1. @classmethod allow to change values at all class instances

    2. return(cls) returns class instance with all class methods

    3. @classmethod allow to create class instance

    4. @classmethod allow to change class globally by cls.__attribute_name__

```python3
class User:
    version = 1

    def __init__(self, name='name1'):
        self.name = name
        
    @classmethod
    def set_name(cls, value):
        cls.version = value

a = User()
b = User()
c = User()

a.version # 1
a.version = 2
b.version # 1
a.set_name(3)
a.version # 2
b.version # 3
c.version # 3
```

```python
class User:
    version = 1

    def __init__(self, name='name1'):
        self.name = name
        
    @classmethod
    def set_name(cls, value):
        return cls(value)

a = User.set_name("name2")
a.name # "name2"
b = User()
a.set_name("name3")
a.name # "name2"
b = User()
b.set_name("name33")
b.name # "name1"
c = b.set_name("name44")
c.name # "name44"
```

## 10. Encapsulation

    1. Encapsulation doesn't work at Python :)
    
    2. Pseudo-encapsulation is provided by self.__atribute_name

```python
class User:
    def __init__(self, name="name1"):
        self.__name = name

a = User()
a.name # error
a._name # error
a.__name # error
a._User__name # "name1"
a._User__name = 22
a._User__name # 22
```

## 11. Monostate

    1. 

```python3
class User:
    args = {
        'version': 1,
        'flags': 2
    }

    def __init__(self):
        self.__dict__ = self.args

a = User()
b = User()

a.args # {'version': 1, 'flags': 2}
a.args['version'] = 2
a.args # {'version': 2, 'flags': 2}
b.args # {'version': 2, 'flags': 2}
User.args # {'version': 2, 'flags': 2}
```


## 12. Polymorphism (@singledispatch)

    1. At Python polymorphism is the overriding of methods

    2. At other programming languages polymorphism provides 
    different behaviour for methods

```python3
from functools import singledispatch

class User:
    @singledispatch
    def get_value(value):
        print("default: ", value)
    
    @get_value.register(int)
    def _(value):
        print("int: ", value)
    
    @get_value.register(str)
    def _(value):
        print("str: ", value)

User.get_value([1, 2, 3])  # default: [1, 2, 3]
User.get_value(True)  # int: True
```

## 13. Dunder methods (`__str__`, `__repr__`, `__len__`, `__del__`)

    1. __str__ - return info about class instance

    2. __repr__ - return some information for debug

    3. __len__ - override len() method for class instance

    4. __del__ - allow delete class instance

```python3
class User:
    def __init__(self, value="test"):
        self.value = value
    
    def __len__(self):
        return len(self.value)

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"<{self.value} object>"
    
    def __del__(self):
        print("Экземпляр класса был удалён!")

a = User()
a  # "test object"
len(a)  # 4
str(a)  # "test"
print(a)  # "test"
del a  # "Экземпляр класса был удалён!"
```

## 14. Dunder methods (`__bool__`, `__bytes__`, `__float__`, `__int__`)

    1. These dunder methods override python types

```python3
class User:
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return bool(self.value)

    def __bytes__(self):
        return str(self.value).encode()

    def __float__(self):
        return float(self.value)
    
    def __int__(self):
        return int(self.value)

a = User(1.100)
bool(a) # True
bytes(a) # b'1.1'
float(a) # 1.1
int(a) # 1
```

## 15. Dunder methods (`__pow__`, `__reversed__`, `__truediv__`)


## 17. Context manager

    1. Allow to work with instances in a 'with open' style

```python3
class User:
    def __init__(self, filename, flag):
        self.file = open(filename, flag)

    def __enter__(self):
        print('__enter__')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        self.file.close()

with User('test.txt', 'r') as file:
    print('work!')
# __enter__
# work!
# __exit__
```

## 18. Dunder methods (`__add__`, `__sub__`, `__eq__`, `__hash__`)


## 21. Inheritance and overriding

    1. Python provides inheritance as concept when you
    can create siblings classes with all methods of parent's class

    2. All methods of parent's class are contained automatically at siblings

    3. You can override parent's methods by rewriting them at sibling

```python3
class Base:
    def __init__(self, health):
        self.health = health

    def go_to(self):
        print('go_to')

    def get_damaged(self):
        self.health -= 10
        print('health: ', self.health)

    def restore_health(self):
        self.health += 10
        print('health: ', self.health)

class Wizard(Base):
    def __init__(self, health=100):
        super(Wizard, self).__init__(health)
        
    def get_damaged(self):
        self.health -= 20
        print('health: ', self.health)
        
    def restore_health(self):
        self.health += 30
        print('health: ', self.health)

class Paladin(Base):
    def __init__(self, health=200):
        super(Paladin, self).__init__(health)

    def get_damaged(self):
        self.health -= 5
        print('health: ', self.health)
        
    def restore_health(self):
        self.health += 25
        print('health: ', self.health)

wizard = Wizard()
wizard.go_to() # go_to
wizard.get_damaged() # 80
wizard.get_damaged() # 60
wizard.restore_health() # 90
```

## 22. `__isinstance__`, `__issubclass__`, `__getsizeof__`

    1. __isinstance__ - check that the variable belongs to the class

    2. __issubclass__ - check that class is the sibling class to other class

    3. __getsizeof__ - count memory usage of variable or class

```python3
class Base:
    def __init__(self, health):
        self.health = health

    def go_to(self):
        print('go_to')

    def get_damaged(self):
        self.health -= 10
        print('health: ', self.health)

    def restore_health(self):
        self.health += 10
        print('health: ', self.health)

class Wizard(Base):
    def __init__(self, health=100):
        super(Wizard, self).__init__(health)
        
    def get_damaged(self):
        self.health -= 20
        print('health: ', self.health)
        
    def restore_health(self):
        self.health += 30
        print('health: ', self.health)

class Paladin(Base):
    def __init__(self, health=200):
        super(Paladin, self).__init__(health)

    def get_damaged(self):
        self.health -= 5
        print('health: ', self.health)
        
    def restore_health(self):
        self.health += 25
        print('health: ', self.health)

issubclass(Paladin, Base) # True
paladin = Paladin()
issubclass(paladin, Base) # Error !

import sys
sys.getsizeof(paladin) # 48
sys.getsizeof(Paladin) # 1064

isinstance(paladin, Paladin) # True
isinstance(1, int) # True
```

## 23. Overriding parent's methods

    1. 

```python3

```

## 24. Dataclass

    1. Allow to store data

```python3
from typing import Any
from dataclasses import dataclass

@dataclass
class User:
    name: str = 'name'
    age: int = 26
    flags: list = "list"
    comment: Any = 'Any'
    
class Test(User):
    def get_name(self):
        return self.name

a = Test()
a.get_name() # 'name'
```

## 25. 