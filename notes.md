# Python Tricks reading notes

## Patterns (Chapter 2)

### Assertions

* Assertions are meant to inform the developer of unrecovearble errors in the program  not recoverable ones like FileNotFoundError
* They should cover conditions that are impossible to reach
* Assertion should never be raised unless there is a bug that causes an impossible situation to occur
* It is not a mechanism for handling run time errors

``` python
assert expression1, expression2  # expression2 is an optional error message
```

* Assertions can be disabled with `-O` and `-OO` command line swtiches or by setting the `PYTHONOPTIMIZE` environent vairiable
* Do not use `assert` for data validation
* Do not use tuples with assert statements. They always evaluate to `True`
  
``` python
assert(1==2, 'fail')  # this will not fail
```

### Comma Placement

* Favour:
  
  ``` python
  names = ['Alice',
           'Bob',
           'Captain', # Notice the trailing comma
          ]
  ```

  over:

  ```python
  names = ['Alice', 'Bob', 'Captain']
  ```

* Removing comma on multiple lines will concatenate string
  
  ```python
  names = ['Alice'
           'Bob'
           'Captain'
          ]
  ```

  outputs:
  
  ```python
  ['AliceBobCaptain']
  ```
  
### Context Manager

* Context Manager is a *protocol* an object needs to follow to support `with` statement
* Add `__enter__` and `__exit__` to object in order to function as context manager
* Alternative use `@contextmanager` decorator from `contextlib`

### Underscores

#### Single Leading Underscore `_var`

* This is used to indicate that the variable or method is used internally by convention
* It is not enforced by the python interpreter
* It is similar to a private variable in Java although not enforced
* Python does not import names that begin with underscore when using a _wilcard_ import
* Note: wildcard imports should generally be avoided

#### Single Trailig Underscore `var_`

* Used to avoid naming clashes with keywords like `class_`, `def_`

#### Double Leading Underscore `__var`

* This is enforced in the interpreter and it is used to avoid name collisions in subclasses

### String formatting

## Functions

### Functions are First-class

#### Functions are objects

* All data in a Python program is represented by objects or relations between objects. Things like strings, lists, modules, and functions are all objects. There’s nothing particularly special about functions in Python. They’re also just objects.

* Assigning a function to another vairiable doesn't call another function, it simply points to the original function

* `__name__` is a string identifier attached to every function  during creation

#### Functions Can Be Stored in Data Structures

``` python
funcs = [bark, str.lower, str.capitalize]
```

#### Functions Can Be Passed to Other Functions

* Functions that can __accept__ other functions as arguments are also called higher-order functions.

#### Functions Can Be Nested

* These are often called nested functions or inner func-
tions.

#### Functions Can Capture Local State

* This is the basic idea behind closures.
* A closure remembers the values from its enclosing lexical scope even when the program flow is no longer in that scope.

#### Objects Can Behave Like Functions

* by defining the __call__method in the class

### Lambas

* Simple example
  
  ``` python
  add = lambda x, y: x + y
  ```

* Lambda functions have an *implicit* return statement

#### Lambdas You Can Use

* When should you use lambda functions in your code? Technically, any time you’re expected to supply a function object you can use a lambda expression
* Lambdas also work as lexical closures

#### When not to use Lambdas

* Complicated `map()` or `filter()` constructs using lambdas. Prefer list comprehensions here.
* Avoid doing anything complex that will be difficult to maintain in the future

### Decorators

* Python’s decorators allow you to extend and modify the
behavior of a callable without permanently modifying the callable itself.

#### Decorator basics

* Deocrators “decorate” or “wrap” another function and let you execute code __before__ and __after__ the wrapped function runs
* A decorator is a callable that takes a callable as input and returns another callable

#### Applying multiple decorators

* Python applies decorators like a stack

#### Decorators with arguments

* Just use `*args` and `**kwargs` to define the wrapper and also when calling the decorated function

#### Debugging decorators

* Always use `functools.wraps` to decorate the wrapper function

### `*args` and `**kwargs`

* They allow a function to accept _optional arguments_
* `args` collects optional agruments in a tuple while `kwargs` collects keyword arguments in a dictionary
* Pass optional or keyword parameters from one function to another using the argument-unpacking operators `*` and `**`

### Argument unpaking

* function arguments can be unpacked using `*` and `**` operators
* `*` is used for iterables and `**` for dictionaries
* using a single * for dictionaries will pass a the keys instead of the values

## Classes

### `is` vs `==`

* `is` ensures strict equality. i.e. it checks if two variables point to the same object
* `==` determines whether two variables are identical i.e. both variables hold the same data

### `__repr__` vs `__str__`

* `__str__` is the `user-friendly` version for display the object's properties
* `__repr__` is sometimes used as a debugging aid. It is also a fall back when __str__ is not defined or in the interperter
* Use `__unicode__` instead of `__str__` in Python 2

### Cloning objects

* Assignment statements in Python do not create copies of objects, they only bind names to an object.
* Python’s built-in mutable collections like lists, dicts, and sets can be copied by calling their factory functions on an existing collection:
  
* ``` python
  new_list = list(original_list)
  new_dict = dict(original_dict)
  new_set = set(original_set)
  ```

* Using factory functions only creates shallow copies
* A shallow copy means constructing a new collection object and then populating it with references to the child objects found in the original
* A deep copy makes the copying process recursive by copying the entire object tree
* use `copy.deepcopy()` to do a deep copy if making a modification to the child objects
* use `copy.copy()` to do a shallow copy to be explicit about making a shallow copy
* `copy.copy()` and `copy.deepcopy()` can also be used for cloning class objects

### Abstract Base Classes

* Abstract Base Classes (ABCs) ensure that derived classes implement particular methods from the base class
* create a Base class with `metaclasss=ABCMeta` and mark its methods as with the `@abstractmethod`

### namedtuples

* Downsides of tuples
  * You can’t give names to individual properties stored in a tuple
  * It’s hard to ensure that two tuples have the same number of fields and the same properties stored on them
* namedtuples are a memory-efficient shortcut to defining an immutable class in Python manually
* namedtuples can be subclassed like normal class
* use the namedtuple's `_fields` attribute to get its _fields_
* `_asdict()` helper method returns an OrderedDict

### class vs instance variables

* Use _instance_`.__class__` when referencing a class variable from a class instance

### Instance, Class, and Static Methods

* instance methods can modify state on the object instance and on the class itself
* it’s possible to call a static method on an object instance
* Using class methods makes it possible to add as many alternative constructors as necessary
* staticmethods are easier to test since they do not require a class instance
* It is possible for a classmethod to call instance and static methods
* classmethods and staticmethods can also modify instance state if given an object instance

## Data Structures

### Dictionaries

* Python’s dictionaries are indexed by keys that can be of any hashable type
* A hashable object has a hash value which never changes during its lifetime (see `__hash__`), and it can be compared to other objects (see `__eq__`). In addition, hashable objects which compare as equal must have the same hash value.
* Immutable types like strings and numbers are hashable and work well as dictionary keys. You can also use tuple objects as dictionary keys, as long as they contain only hashable types themselves.
* `defaultdict` accepts a callable in its constructor whose return value will be used if a requested key cannot be found.
* ChainMap data structure groups multiple dictionaries into a single mapping. Lookups search the underlying mappings
one by one until a key is found.
* Use `types.MappingProxyType` to make a dict read only

### Arrays

* Typed array data structure that only allows elements that have the same data type stored in them
* Dynamic arrays with different data types take up more space
* Tuples are immutable
* Arrays created with the `array.array` class are _typed arrays_
* String arrays are immutable. They can be made _mutable_ by storing each character in a list
* Strings are recursive data structures
* Bytes objects are immutable sequences of single bytes (integers in the range of 0 <= x <= 255)
* The `bytearray` type is a mutable sequence of integers in the range 0 <= x <= 255

### Records, structs

* SimpleNamespace instances expose their keys as class attributes. This means you can use obj.key “dotted" attribute access instead of the obj['key']

### Sets and Multisets

* A set is an unordered collection of objects that does not allow duplicate elements
* Sets do not support indexing and slicing
* The frozenset class implements an immutable version of set that cannot be changed after it has been constructed
* Frozensets are immutable and can be used as dictionary keys
* A multiset  that allows elements in the set to have more than one occurrence. (through `collections.Counter`)

### Stacks

* A stack is a collection of objects that supports fast last-in, first-out (LIFO) semantics for inserts and deletes
* Performance-wise, a proper stack implementation is expected to take _O(1)_ time for insert and delete operations
* The `deque` class implements a double-ended queue that supports adding and removing elements from either end in O(1) time
* Use `deque.popleft()` to remove first element in a queue
* Priority Queues return the highest or lowest element in a queue based on each element's priority

## Looping & Iteration

### Pythonic loops

* When you see code that uses `range(len(...))` to iterate over a container you can usually simplify and improve it further.
* `for i in range(a, n, s):` __a__ is start value, __n__ is the stop value and __s__ is the step size

### List comprehension 

* Syntax: `values = [expression for item in collection if condition]`
* List comprehensions should not exceed one level of nesting for comprehensions

### Slicing

* Syntax: `lst[start:end:step]` where default step is `1`
* _Sushi_ (:) operator is used for creating (shallow) copies of existing lists

### Iterators

* iterators provide a common interface that allows you to process every element of a container while being completely isolated from the container’s internal structure.
* `__iter__` returns the iterator object
* `__next__` returns values in the iterator
* In Python 3, the method that retrieves the next value from an iterator is called `__next__`
* In Python 2, the same method is called next (no underscores)

### Generators

* Generators look like regular functions but instead of using the return statement, they use yield to pass data back to the caller.
* Calling a generator function doesn’t run the function but creates and returns a generator object
* When a `yield` is invoked, it passes control back to the caller of the function — but it only does so temporarily
* Execution can be resumed at any time by calling `next()` on the generator
* Generators stop generating values as soon as control flow returns from the generator function by any means other than a `yield` statement

### Generator Expressions

* Once a generator expression has been consumed, it can’t be restarted or reused
* Syntax: `genexpr = (expression for item in collection if condition)` where `if condition` is optional
* Generator functions can be used in-line with other statements

### Generator chaining

* Generators can be chained together to form data processing pipelines
