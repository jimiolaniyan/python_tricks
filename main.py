###### Imports ########################
import functools
import copy
import json
import array
from typing import NamedTuple

from abc import ABCMeta, abstractmethod
from collections import namedtuple, OrderedDict, defaultdict, ChainMap, Counter
from types import MappingProxyType, SimpleNamespace

######### Looping ####################

######### iterator chain #############
integers = (i for i in range(1,9))
# squared = (i * i for i in integers)

def squared(seq):
    for i in seq:
        yield i * i

negated = (-i for i in squared(integers))

# print(list(negated))

######## Generator expressions #######
gen  = ('Hello' for _ in range(3))
# for item in gen:
#     print(item)

# # Won't print anything
# for item in gen:
#     print(item)

even_squares = (x * x for x in range(10) if x % 2 == 0)

# for item in even_squares:
#     print(item)

# for x in ('Bom dia' for i in range(3)): # in-line expression
#     print(x)
######### Generators #################

def bounded_repeater(value, max_repeats):
    count = 0
    while True:
        if count >= max_repeats:
            return
        count += 1
        yield value

def bounded_repeater_simplified(value, max_repeats):
    for _ in range(max_repeats):
        yield value

def yield_once(value):
    yield value
    yield '4'

# for item in yield_once(2):
#     print(item)

def repeater(value):
    while True:
        yield value

# gen_obj = repeater('Hi')
bounded_gen_obj = bounded_repeater_simplified('hi', 11) 
# for item in bounded_gen_obj:
#     print(item)

######### Iterators ##################

class BoundedRepeater:
    def __init__(self, value, max_repeats: float):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value 

repeater = BoundedRepeater('Hello', 3)
# for item in repeater:
#     print(item)

class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value   
    
class RepeaterIterator:
    def __init__(self, source):
        self.source = source


# repeater = Repeater('Hello')

### WARNING: infinite loop begins
# for item in repeater:
#     print(item)

# iterator = repeater.__iter__()

### WARNING: infinite loop begins
# while True:   
#     item = iterator.__next__()
#     print(item)

a = range(20, 40)

# for i, val in enumerate(range(20, 30, 2)):
#     print(val)

lst = [1, 2, 3, 4, 5]
# del lst[:] # delete all elements in the list without deleting the list. keeps the list reference
# print(lst)

copied = lst[:]  # create (shallow) copies of existing lists
# print(copied is lst)

######## Data Structures #############

######## Sets and Multisets #############
seta = {'a', 'e', 'i'}  # set syntax, similar to dict
setb = {x*x for x in range(10)}  # set comprehension
# print(seta, setb, sep='\n')

letters = set('leeggoo')
letters.add(('y','w','h'))
letters.remove('e')
# print(letters)
# print(letters.union(seta))

fset = frozenset({'y','w','h'})
dicta = {fset: 'lb'}
# print(dicta)

inventory = Counter()
a = {'book': "f"}
b = {'book': "d"}
# c = {'book': 1}
inventory.update(a) # outputs: Counter({'book': 'f'})
inventory.update(b) # outputs: Counter({'book': 'df'})
# inventory.update(c) # TypeError: unsupported operand type(s) for +: 'int' and 'str'


######### Records ####################
class Car:
    def __init__(self, make: str, year: str, price: float):
        self.make = make
        self.year = year
        self.price = price

# car1 = Car()
# print(car1)

Vehicle = namedtuple('Vehicle', ['make', 'year', 'type'])
p2 = Vehicle('honda', '2012', 'motorcycle')
# p2.make = 'toyota'

x = NamedTuple('col', [('x', float), ('y', int)])
# print(x(12,31))

class Motor(NamedTuple):
    color: str
    mileage: float
    automatic:bool

# motor1 = Motor('red', 29811.12, True)
# print(motor1)

car1 = SimpleNamespace(color='red', price=12121)
# print(car1, car1.color, sep='\n')

######## list #########################
arr = 'one', 'two', 'three'
arr = arr + (22, 'y') # add tuples to get a new tuple. The trailing comma is important
# print(arr)

arr_ = array.array('f', (2,3,4))
arr_.append(4)
arr_[2] = 19
# print(arr_)

byte = bytes((12,15,4,24))
bt = bytearray((12,15,4,24))
bt.append(22)
del bt[0]
# print(byte, bt)

######## dict ########################
d = OrderedDict(one=1, two=2, three=3) # order is not maintained
d['four'] = 4 #order is maintained
# print(d, d.keys())

dd = defaultdict(list)
dd['cat'] = ['a', 'b', 'c']
dd['dog'] = 12

# print(dd['cats']) # This will return an empty array

dict1 = {'one': 11, 'two': 2}
dict2 = {'three': 3, 'four': 4}
cmap = ChainMap(d, dd, dict1, dict2)
cmap['five'] = 5
cmap['six'] = 6
# print(cmap['five'])

writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)

writable['three'] = 3
# print(read_only['one'])
# print(read_only)

######## classes #####################

######## Instance, Class, and Static Methods ##########
class Menu:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    def __repr__(self):
        return '{}({!r})'.format(self.__class__.__name__, self.ingredients)

    @classmethod
    def jollof_rice(cls):
        return cls(['rice', 'tomato', 'onion', 'maggi'])

# print(Menu(['rice', 'fish']))
# print(Menu.jollof_rice())

class MyClass:
    a = 2
    def method(self):
        # self.classesmethod()
        # self.staticsmethod()
        return 'instance method', self
    
    def fwe(self):
        print('egeg')

    @classmethod
    def classesmethod(cls, self):
        # cls.fwe('p')
        self.name = 10
        # print(self.name)
        return 'class method', cls
    
    @staticmethod
    def staticsmethod(cls, self):
        self.n = 1
        # print(cls.a)
        # print('avfaef')
        return 'static method'

c = MyClass()
# MyClass.fwe('r')
MyClass.classesmethod(c)
MyClass.staticsmethod(MyClass, c)
# print(c.n,c.name)
# print(c.method())

######## class vs instance variables ###########
class CountedObjs:
    count = 0
    def __init__(self):
        self.__class__.count += 1
        # self.count += 1  # This actually mirrors the class variable and doesn't update with every new instance created 

class Dog:
    legs = 4

    def __init__(self, name):
        self.name = name

jack = Dog('jack')
jill = Dog('jill')

jack.legs = 6  # creates a new instance varaible that shows the 'legs' class variable 
# print(jack.legs, jack.__class__.legs)
# print(jill.legs)
# print(Dog.legs)
######## namedtuples #################
Car = namedtuple('Car', 'color mileage')
# Car = namedtuple('Car', [
#     'color',
#     'mileage',
# ])

new_car = Car('red', 3434)

# print(new_car.color)
# print(new_car[1])
# print(*new_car)

# print(new_car._asdict()) # returns an OrderedDict
# print(json.dumps(new_car._asdict()))

class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'

c = MyCarWithMethods('red', 345545)
# print(c.hexcolor())
# print(Car._fields)

####### Abstract Base Classes #########
class Base(metaclass=ABCMeta):
    
    @abstractmethod
    def foo(self):
        pass
    
    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass
    
    # def bar(self):
    #     pass

# c = Concrete()
####### cloning objects #############
xs = [[1,2,3], [4,5,6]]
# ys = list(xs) # shallow copy
# ys = copy.copy(xs) # shallow copy

# ys = copy.deepcopy(xs)

xs[0].append(7)
# print(xs)
# print(ys)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "{}({!r}, {!r})".format(__class__.__name__, self.x, self.y)

a = Point(23, 54)
b = copy.copy(a)
# print(a is b)

class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return "{}({!r}, {!r})".format(__class__.__name__, self.topleft, self.bottomright)

rect = Rectangle(Point(0,1), Point(5,6))
srect = copy.copy(rect)
drect = copy.deepcopy(srect)

rect.topleft.x = 34

# print(rect) 
# print(srect)
# print(drect)
######### Error classes #############
class NameTooShortError(ValueError):
    pass

def validate(val):
    if len(val) < 10:
        raise NameTooShortError

# validate('love')

######## printing ###################

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __str__(self):
        return "{{'{}':'{}'}}".format('color', self.color) # use '{{' and '}}' in str formatting to ignore '{' and '}'
    def __repr__(self):
        return '{}({}, {})'.format(__class__.__name__, self.color, self.mileage)

a_car = Car('green', 90);
# print(repr(a_car))

####### Argument unpaking ############
def afunc(*args, **kwargs):
    print(args)
    print(kwargs)

dict_vec = {'y': 0, 'z': 1, 'x': 1}
# afunc(*dict_vec)

######## args and kwargs ##############
def an(func):
    def wrapper(*args,**kwargs):
        print(func, args, kwargs)
        result = func(*args, **kwargs)
        print("result from wrapper {}".format(result))
        return result
    return wrapper

@an
def a(greeting, name, *args, **kwargs):
    return '{}, {}, {}'.format(greeting, name, kwargs)

# print(a('a', 'b', b=2))

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

class BlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'

# print(BlueCar('green', 4334).color)

def func(key=1, *args, **kwargs):
    print(kwargs)

# func(keys=6) # prints {'keys': 6}
###### Decorators with arguments ######
def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('TRACE: calling {} '
            'with arguments: {}, {}'
            .format(func.__name__, args, kwargs))
        result = func(*args, **kwargs)
        print('TRACE: {} returned {!r}'
        .format(func.__name__, result))
        return result
    return wrapper

@trace
def say(name, line):
    """Nice formatter"""
    return "{}: {}".format(name, line)

# print(say('wife', 'I love my husband'))

###### Decorators #######
def split(func):
    def wrapper():
        return list(func())
    return wrapper

def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

@split
@uppercase
def greet():
    return 'Hello'

# print(greet())
###########################
def null_decorator(func):
    return func

@null_decorator
def greet_dec():
    return 'Hello!'

# greet = null_decorator(greet_dec)

# print(greet())
###### Lambda closures ########
def make_adder_lambda(n):
    return lambda x: x+n

# print(make_adder_lambda(4)(3))

###### Lambdas #######
add = lambda x, y: x + y
# print((lambda x, y: x + y)(5, 3))

tuples = [(1, 'g'), (2, 'f'), (3, 'a'), (4, 'b')]

# def lambda_(tup):
#     return tup[1]
    
# You can replace the lambda expression with lambda_ above
# print(sorted(tuples, key=lambda x:x[1]))

# print(sorted(range(-5, 6), key=lambda x: x*x))

###### __call__ ######
class Adder:
    def __init__(self, n):
        self.n = n
    
    def __call__(self, x):
        return self.n + x

# plus_3 = Adder(3)
# print(plus_3(4))
# print(callable(Adder))

###### Closures ######

def make_adder(n):
    def add(x):
        return x + n
    return add

plus_3 = make_adder(3)
plus_5 = make_adder(5)

# print(make_adder(3)(4))
# print(plus_5(4))

def get_speak_func(text, vol):
    def whisper():
        return text.lower() + '...'
    
    def yell():
        return text.upper() + '!'

    if vol > 0.5:
        return yell
    else:
        return whisper

# print(get_speak_func('hi', 0.7)())

##############################################

def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)

# print(speak('Hey, THEre'))

#############################################

def yell(text):
    return text.upper() + '!'

def whisper(text):
    return text.lower() + '!'

def greet(func):
    greeting = func('Hi, I am here')
    print(greeting)

bark = yell

del yell
# greet(bark)
# greet(whisper)

# print(" ".join(list(map(bark, ['you', 'are', 'barking']))))

############## Context Manager #########

## Class based
class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'r')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# with ManagedFile('hello.txt') as f:
#     f.write('Hey \n')
#     f.write('Hey!')


# context manager-based
from contextlib import contextmanager

@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()

# with managed_file('hello.txt') as f:
#     f.write('h')
#     f.write('g')