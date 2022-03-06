# Content

[01. Classes and Attributes](#01-classes-and-attributes)

[02. Attributes (setattr, getattr, delattr, dict)](#02-attributes-setattr-getattr-delattr-dict)

[03. `__init__` and `self`](#03-__init__-and-self)

[04. Properties (getter, setter, deleter)](#04-properties-getter-setter-deleter)

[05. Dunder methods](#05-dunder-methods)

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


## 02. Attributes (setattr, getattr, delattr, dict)

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

    1. 

## 04. Properties (getter, setter, deleter)

## 05. Dunder methods

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