# coding=utf-8
"""Item32
Attribute dictionary.
"""

class LazyDB(object):
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = "Value for %s" % name
        setattr(self, name, value)
        return value


class LoggingLazyDB(LazyDB):
    def __getattr__(self, name):
        print "Called __getattr__(%s)" % name
        return super(LoggingLazyDB, self).__getattr__(name)


if __name__ == "__main__":
    data = LoggingLazyDB()
    print data.__dict__
    # hasattr(data, "foo")
    getattr(data, "foo")
    print data.__dict__