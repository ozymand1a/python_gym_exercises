class User:
    __slots__ = ['name', 'age']

    def __init__(self, name="name1", age=20):
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)


if __name__ == '__main__':
    user = User()
    user.hh = 1  # Attribute error
