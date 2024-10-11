"""
TODO:

`foo` takes keyword arguments of type integer or string.
"""

from typing import Union


def foo(**kwargs: Union[str, int]):
    pass


foo(a=1, b="2")
# foo(a=[1]) - error: Argument "a" to "foo" has incompatible type "list[int]"; expected "str | int"
