from datetime import datetime


class Rand:
    X_0 = 1

    def __init__(self, max_i, use_time=False):
        # constants
        self.a = 48271
        self.b = 0
        self.m = 2 ** 31 - 1

        # initial x
        if use_time:
            self.x = datetime.now().microsecond or Rand.X_0
        else:
            self.x = Rand.X_0

        self.i = 0
        self.max_i = max_i

    def __next__(self):
        if self.i == self.max_i:
            raise StopIteration

        self.i += 1

        self.x = (self.a * self.x + self.b) % self.m
        return self.x

    def __iter__(self):
        return self


if __name__ == '__main__':
    for i, rand in enumerate(Rand(20, True)):
        print(i + 1, rand)
