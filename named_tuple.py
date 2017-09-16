from collections import namedtuple

class Foo(namedtuple("Foo", "x", "y")):

    __slots__ = ()

    def __str__(self):
        return "foolish({})".format(self.x, self.y)

    def __format__(self, spec):
        return self.__str__()



