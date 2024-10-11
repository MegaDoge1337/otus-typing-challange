"""
TODO:

foo should accept a tuple argument, 1st item is a string, 2nd item is an integer.
"""

from typing import Tuple


def foo(x: Tuple[str, int]):
    pass


foo(("foo", 1))
# foo((1, 2)) - error: Argument 1 to "foo" has incompatible type "tuple[int, int]"; expected "tuple[str, int]"
# foo(("foo", "bar")) -  error: Argument 1 to "foo" has incompatible type "tuple[str, str]"; expected "tuple[str, int]"
# foo((1, "foo")) - error: Argument 1 to "foo" has incompatible type "tuple[int, str]"; expected "tuple[str, int]"
