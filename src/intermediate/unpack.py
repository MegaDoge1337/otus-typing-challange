"""
TODO:

`foo` expects two keyword arguments - `name` of type `str`, and `age` of type `int`.
"""

from typing import TypedDict, Unpack


class Person(TypedDict):
    name: str
    age: int


def foo(**kwargs: Unpack[Person]):
    pass


person2_1: Person = {"name": "The Meaning of Life", "age": 1983}
foo(**person2_1)
# foo(**{"name": "Brian", "age": 30}) # - error: Argument 1 to "foo" has incompatible type "**dict[str, object]"; expected "str" / Argument 1 to "foo" has incompatible type "**dict[str, object]"; expected "int"

# foo(**{"name": "Brian"}) - error: Argument 1 to "foo" has incompatible type "**dict[str, str]"; expected "int"
person2_2: dict[str, object] = {"name": "Brian", "age": 20}
# foo(**person2_2) - error: Argument 1 to "foo" has incompatible type "**dict[str, object]"; expected "str" / Argument 1 to "foo" has incompatible type "**dict[str, object]"; expected "int"
# foo(**{"name": "Brian", "age": "1979"}) - error: Argument 1 to "foo" has incompatible type "**dict[str, str]"; expected "int"
