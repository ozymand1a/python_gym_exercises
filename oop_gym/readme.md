# Content

 1. Object and classes
 2. Class attributes
 3. `__init__` and `self`
 4. Setter, getter, deliter
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



## 01. Object and classes

    1. Classes contain not functions but methods

    2. Instances of classes inherit class attributes.
    If we change attributes at class,
    we change this attribute at all instances.
    
    3. 

## 02. Attributes (setattr, getattr, delattr, dict)

    1. 

## 06. Static methods

    1. Allow to call class method (function) without
    creation of class's instance
    
    2. Using decorator @staticmethod is necessary!

```python
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
