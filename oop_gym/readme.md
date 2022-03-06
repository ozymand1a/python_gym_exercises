# Content

 1. [Classes and instances](#01.classes-and-instances)
 2. Attributes (setattr, getattr, delattr, dict)
 3. `__init__` and `self`
 4. Properties (getter, setter, deleter)
 5. Dunder methods
 6. `@staticmethod`
 7. Slots
 8. Dunder method new
    

 9. `@classmethod`
 10. Encapsulation
 11. Monostate
 12. 
 13. 
 14.
 15.
 16.


 17.
 18.
 19.
 20.
 21.
 22.
 23.


## 01.Classes and instances

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
