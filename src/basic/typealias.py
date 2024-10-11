"""
TODO:

Create a new type called Vector, which is a list of float.
"""

from typing import List

Vector = List[float]


def foo(v: Vector):
    pass


foo([1.1, 2])
# foo(1) - error: Argument 1 to "foo" has incompatible type "int"; expected "list[float]"
# foo(["1"]) - error: List item 0 has incompatible type "str"; expected "float"
