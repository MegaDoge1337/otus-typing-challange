"""
TODO:

foo should accept a list argument, whose elements are string.
"""

from typing import List


def foo(x: List[str]):
    pass


foo(["foo", "bar"])
# foo(["foo", 1]) - error: List item 1 has incompatible type "int"; expected "str"
