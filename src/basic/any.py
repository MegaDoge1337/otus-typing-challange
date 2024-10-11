"""
TODO:

Modify `any_foo` so it takes an argument of arbitrary type.
"""

from typing import Any


def any_foo(a: Any):
    pass


any_foo(1)
any_foo("10")
# any_foo(1, 2) - error: Too many arguments for "any_foo"
