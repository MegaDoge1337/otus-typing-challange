"""
TODO:

foo should accept a argument that's either a string or integer.
"""

from typing import Union


def foo(x: Union[str, int]):
    pass


foo("foo")
foo(1)
# union_foo([]) - error: Argument 1 to "foo" has incompatible type "list[Never]"; expected "str | int"
