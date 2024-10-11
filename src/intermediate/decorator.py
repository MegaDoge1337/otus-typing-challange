"""
TODO:

Define a decorator that wraps a function and returns a function with the same signature.
"""

from typing import Callable, TypeVar

T = TypeVar("T", bound=Callable)


def decorator(func: T) -> T:
    return func


@decorator
def foo(a: int, *, b: str) -> None:
    pass


@decorator
def bar(c: int, d: str) -> None:
    pass


foo(1, b="2")
bar(c=1, d="2")

# foo(1, "2") - error: Too many positional arguments for "foo"
# foo(a=1, e="2") - error: Unexpected keyword argument "e" for "foo"
# decorator(1) - error: Value of type variable "T" of "decorator" cannot be "int"
