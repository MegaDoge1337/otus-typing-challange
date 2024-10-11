"""
TODO:

Class `Foo` has a class variable `bar`, which is an integer.
"""

from typing import ClassVar


class Foo:
    bar: ClassVar[int]


Foo.bar = 1
# Foo.bar = "1" - error: Incompatible types in assignment (expression has type "str", variable has type "int")
# Foo().bar = 1 - error: Cannot assign to class variable "bar" via instance
