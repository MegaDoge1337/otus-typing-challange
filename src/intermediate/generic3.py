"""
TODO:

The function `add` accepts one argument and returns a value, they all have the same type.
The type can only be int or subclasses of int.
"""

from typing import TypeVar, assert_type

T = TypeVar("T", bound=int)


def add(a: T) -> T:  # type: ignore[empty-body]
    pass


class MyInt(int):
    pass


assert_type(add(1), int)
assert_type(add(MyInt(1)), MyInt)
# assert_type(add("1"), str) - error: Value of type variable "T" of "add" cannot be "str"
# add(["1"], ["2"]) - error: Value of type variable "T" of "add" cannot be "list[str]" / Too many arguments for "add"
# add("1", 2) - erro: Value of type variable "T" of "add" cannot be "str" / Too many arguments for "add"
