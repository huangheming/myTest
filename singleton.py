def singleton(cls):
    s = None

    def wrap(*args, **kwargs):
        nonlocal s
        if not s:
            s = cls(*args, **kwargs)
            return s
        return s
    return wrap


# 用装饰器实现，__init__()方法只会调用一次
@singleton
class Book1(object):
    def __init__(self, name):
        print('__init__:' + name)
        self.name = name


def test1():
    b1 = Book1('11')
    print('b1.name: {}'.format(b1.name))
    b2 = Book1('22')
    # b2.name = '11'
    print('b2.name: {0}'.format(b2.name))
    b2.name = '22'
    print('b2.name: {0}'.format(b2.name))
    # b2.name = '22'
    print('b1.name: {}'.format(b1.name))


# 用__new__实现，这种方式每次Book2(*args, **kwargs)都会调用__init__()方法
class Book2Super(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Book2Super, cls).__new__(cls)
        return cls._instance


class Book2(Book2Super):
    def __init__(self, name):
        print('__init__:' + name)
        self.name = name


def test2():
    b1 = Book2('11')
    print('b1.name: {}'.format(b1.name))
    b2 = Book2('22')
    # b2.name = '22'
    print('b2.name: {0}'.format(b2.name))
    # b2.name = '22'
    print('b1.name: {}'.format(b1.name))


if __name__ == "__main__":
    test1()
    # test2()

