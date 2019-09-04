class  my_object:
    def __init__(self):
        self.number = 10
    def how_much(self):
        return self.number
    def set_value(self, value):
        self.number = value

class little_object(my_object):
    def __init__(self):
        super().__init__()
        self.number = self.number -1
    def foo(self):
        return self.number-1
    def __del__(self):
        print('Oh I die...')

o = my_object()
print(o)
print(o.number)
o.set_value(11)
print(o.how_much())

l = little_object()
print(l.number)
print(l.foo())

print(isinstance(l,my_object))
print(isinstance(l,little_object))
print(isinstance(l,object))
print(issubclass(little_object, my_object))
print(issubclass(bool,int))

del l
