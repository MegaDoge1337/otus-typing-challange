"""
TODO:

`return_self` should return an instance of the same type as the current enclosed class.
"""

from typing import TypeVar

T = TypeVar("T", bound="Foo")


class Foo:
    def return_self(self: T) -> T:  # type: ignore[empty-body]
        pass


class SubclassOfFoo(Foo):
    pass


f: Foo = Foo().return_self()
sf: SubclassOfFoo = SubclassOfFoo().return_self()
# sf: SubclassOfFoo = Foo().return_self() - error: Incompatible types in assignment (expression has type "Foo", variable has type "SubclassOfFoo")
