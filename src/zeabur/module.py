"""Python Type Challenges"""

from typing import Any, Dict, Final, List, Optional, Tuple, Union, assert_type


def any_foo(a: Any):
    """
    BASIC - any

    TODO:

    Modify `foo` so it takes an argument of arbitrary type.
    """
    pass


any_foo(1)
any_foo("10")
# any_foo(1, 2) - error: Too many arguments for "any_foo"


def dict_foo(x: Dict[str, str]):
    """
    BASIC - dict

    TODO:

    foo should accept a dict argument, both keys and values are string.
    """
    pass


dict_foo({"foo": "bar"})
# dict_foo({"foo": 1}) - error: Dict entry 0 has incompatible type "str": "int"; expected "str": "str"


def final_list() -> None:
    """
    BASIC - final

    TODO:

    Make sure `my_list` cannot be re-assigned to.
    """
    my_list: Final = []
    my_list.append(1)
    # my_list = [] - error: Cannot assign to final name "my_list"
    # my_list = "something" - error: Cannot assign to final name "my_list" / Incompatible types in assignment (expression has type "str", variable has type "list[int]")


def kwargs_foo(**kwargs: Union[str, int]):
    """
    BASIC - kwargs

    TODO:

    `foo` takes keyword arguments of type integer or string.
    """
    pass


kwargs_foo(a=1, b="2")
# kwargs_foo(a=[1]) - error: Argument "a" to "kwargs_foo" has incompatible type "list[int]"; expected "str | int"


def list_foo(x: List[str]):
    """
    BASIC - list

    TODO:

    foo should accept a list argument, whose elements are string.
    """
    pass


list_foo(["foo", "bar"])
# list_foo(["foo", 1]) - error: List item 1 has incompatible type "int"; expected "str"


def optional_foo(x: Optional[int] = None):
    """
    BASIC - optional

    TODO:

    foo can accept an integer argument, None or no argument at all.
    """
    pass


optional_foo(10)
optional_foo(None)
optional_foo()
# optional_foo("10") - error: Argument 1 to "optional_foo" has incompatible type "str"; expected "int | None"


def parameter_foo(x: int):
    """
    BASIC - parameter

    TODO:

    foo should accept an integer argument.
    """
    pass


parameter_foo(10)
# parameter_foo("10") - error: Argument 1 to "parameter_foo" has incompatible type "str"; expected "int"


def return_foo() -> int:
    """
    BASIC - return

    TODO:

    foo should return an integer argument.
    """
    return 1


assert_type(return_foo(), int)
# assert_type(return_foo(), str) - error: Expression is of type "int", not "str"


def tuple_foo(x: Tuple[str, int]):
    """
    BASIC - tuple

    TODO:

    foo should accept a tuple argument, 1st item is a string, 2nd item is an integer.
    """
    pass


tuple_foo(("foo", 1))
# tuple_foo((1, 2)) - error: Argument 1 to "tuple_foo" has incompatible type "tuple[int, int]"; expected "tuple[str, int]"
# tuple_foo(("foo", "bar")) -  error: Argument 1 to "tuple_foo" has incompatible type "tuple[str, str]"; expected "tuple[str, int]"
# tuple_foo((1, "foo")) - error: Argument 1 to "tuple_foo" has incompatible type "tuple[int, str]"; expected "tuple[str, int]"

Vector = List[float]


def typealias_foo(v: Vector):
    """
    BASIC - typealias

    TODO:

    Create a new type called Vector, which is a list of float.
    """
    pass


typealias_foo([1.1, 2])
# typealias_foo(1) - error: Argument 1 to "typealias_foo" has incompatible type "int"; expected "list[float]"
# typealias_foo(["1"]) - error: List item 0 has incompatible type "str"; expected "float"


def union_foo(x: Union[str, int]):
    """
    BASIC - union

    TODO:

    foo should accept a argument that's either a string or integer.
    """
    pass


union_foo("foo")
union_foo(1)
# union_foo([]) - error: Argument 1 to "union_foo" has incompatible type "list[Never]"; expected "str | int"

"""
BASIC - variable

TODO:

`a` should be an integer.
"""

a: int
a = 2
# a = "1" - error: Incompatible types in assignment (expression has type "str", variable has type "int")
