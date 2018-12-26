class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)


class Students(object):
    def __init__(self, *args):
        self.names = args

    def __len__(self):
        return len(self.names)


ss = Students('Bob', 'Alice', 'Tim')
print(len(ss))


def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)


test_var_args('yasoob', 'python', 'eggs', 'test')


def greet_me(f_arg, *argv, **kwargs):
    print(f_arg)
    print(argv)
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))


greet_me('test', 'yahoo', 'sina', name="yasoob", lang="sohu")
