# coding=utf-8
"""Item33
Validate subclasses with metaclasses.
"""


class Meta(type):
    """Metaclass is defined by inheriting from type."""
    def __new__(meta, name, bases, cls_dict):
        """If an exception is thrown, the class(represented by parameter name) construction is unsuccessful."""
        print meta, name, bases, cls_dict
        return type.__new__(meta, name, bases, cls_dict)


# class MyClass(object, metaclass=Meta):
#     """Metaclass parameter is only available in Python 3."""
#     stuff = 123

#     def foo(self):
#         return 'foo'

class MyClass_Python2(object):
    __metaclass__ = Meta
    stuff = 123

    def foo(self):
        return 'foo'


if __name__ == "__main__":
    c = MyClass_Python2()
    print(c.foo())
