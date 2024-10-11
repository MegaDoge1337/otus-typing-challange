"""
TODO:

foo only accepts literal 'left' and 'right' as its argument.
"""

from typing import Literal


def foo(direction: Literal["left", "right"]):
    pass


foo("left")
foo("right")

b = "".join(["l", "e", "f", "t"])
# foo(b) - error: Argument 1 to "foo" has incompatible type "str"; expected "Literal['left', 'right']"
