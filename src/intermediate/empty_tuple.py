"""
TODO:

foo should accept a empty tuple argument.
"""

from typing import Tuple


def foo(x: Tuple[()]):
    pass


foo(())
# foo((1)) - error: Argument 1 to "foo" has incompatible type "int"; expected "tuple[()]"
