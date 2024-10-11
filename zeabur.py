"""Python Type Challenges"""

from asyncio import Queue
from typing import (
    Any,
    Awaitable,
    Callable,
    ClassVar,
    Dict,
    Final,
    Iterable,
    List,
    Literal,
    LiteralString,
    NotRequired,
    Optional,
    Required,
    Tuple,
    TypedDict,
    TypeVar,
    Union,
    Unpack,
    assert_type,
)

"""
BASIC - any

TODO:

Modify `any_foo` so it takes an argument of arbitrary type.
"""


def any_foo(a: Any):
    pass


any_foo(1)
any_foo("10")
# any_foo(1, 2) - error: Too many arguments for "any_foo"

"""
BASIC - dict

TODO:

dict_foo should accept a dict argument, both keys and values are string.
"""


def dict_foo(x: Dict[str, str]):
    pass


dict_foo({"foo": "bar"})
# dict_foo({"foo": 1}) - error: Dict entry 0 has incompatible type "str": "int"; expected "str": "str"

"""
BASIC - final

TODO:

Make sure `my_list` cannot be re-assigned to.
"""

my_list: Final = []
my_list.append(1)
# my_list = [] - error: Cannot assign to final name "my_list"
# my_list = "something" - error: Cannot assign to final name "my_list" / Incompatible types in assignment (expression has type "str", variable has type "list[int]")

"""
BASIC - kwargs

TODO:

`kwargs_foo` takes keyword arguments of type integer or string.
"""


def kwargs_foo(**kwargs: Union[str, int]):
    pass


kwargs_foo(a=1, b="2")
# kwargs_foo(a=[1]) - error: Argument "a" to "kwargs_foo" has incompatible type "list[int]"; expected "str | int"

"""
BASIC - list

TODO:

list_foo should accept a list argument, whose elements are string.
"""


def list_foo(x: List[str]):
    pass


list_foo(["foo", "bar"])
# list_foo(["foo", 1]) - error: List item 1 has incompatible type "int"; expected "str"

"""
BASIC - optional

TODO:

optional_foo can accept an integer argument, None or no argument at all.
"""


def optional_foo(x: Optional[int] = None):
    pass


optional_foo(10)
optional_foo(None)
optional_foo()
# optional_foo("10") - error: Argument 1 to "optional_foo" has incompatible type "str"; expected "int | None"

"""
BASIC - parameter

TODO:

parameter_foo should accept an integer argument.
"""


def parameter_foo(x: int):
    pass


parameter_foo(10)
# parameter_foo("10") - error: Argument 1 to "parameter_foo" has incompatible type "str"; expected "int"

"""
BASIC - return

TODO:

return_foo should return an integer argument.
"""


def return_foo() -> int:
    return 1


assert_type(return_foo(), int)
# assert_type(return_foo(), str) - error: Expression is of type "int", not "str"

"""
BASIC - tuple

TODO:

tuple_foo should accept a tuple argument, 1st item is a string, 2nd item is an integer.
"""


def tuple_foo(x: Tuple[str, int]):
    pass


tuple_foo(("foo", 1))
# tuple_foo((1, 2)) - error: Argument 1 to "tuple_foo" has incompatible type "tuple[int, int]"; expected "tuple[str, int]"
# tuple_foo(("foo", "bar")) -  error: Argument 1 to "tuple_foo" has incompatible type "tuple[str, str]"; expected "tuple[str, int]"
# tuple_foo((1, "foo")) - error: Argument 1 to "tuple_foo" has incompatible type "tuple[int, str]"; expected "tuple[str, int]"

"""
BASIC - typealias

TODO:

Create a new type called Vector, which is a list of float.
"""

Vector = List[float]


def typealias_foo(v: Vector):
    pass


typealias_foo([1.1, 2])
# typealias_foo(1) - error: Argument 1 to "typealias_foo" has incompatible type "int"; expected "list[float]"
# typealias_foo(["1"]) - error: List item 0 has incompatible type "str"; expected "float"

"""
BASIC - union

TODO:

union_foo should accept a argument that's either a string or integer.
"""


def union_foo(x: Union[str, int]):
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

"""
INTERMEDIATE - await

TODO:

`run_async` takes an awaitable integer.
"""


def run_async(a: Awaitable[int]):
    pass


queue: Queue[int] = Queue()
queue2: Queue[str] = Queue()


async def async_function() -> int:
    return await queue.get()


async def async_function2() -> str:
    return await queue2.get()


run_async(async_function())
# run_async(1) - error: Argument 1 to "run_async" has incompatible type "int"; expected "Awaitable[int]"
# run_async(async_function2()) - error: Argument 1 to "run_async" has incompatible type "Coroutine[Any, Any, str]"; expected "Awaitable[int]"

"""
INTERMEDIATE - callable

TODO:

Define a callable type that accepts a string argument and returns None.
*The parameter name can be arbitrary.*
"""

SingleStringInput = Callable[[str], None]


def accept_single_string_input(func: SingleStringInput) -> None:
    pass


def string_name(name: str) -> None:
    pass


def string_value(value: str) -> None:
    pass


def int_value(value: int) -> None:
    pass


def new_name(name: str) -> str:
    return name


accept_single_string_input(string_name)
accept_single_string_input(string_value)
# accept_single_string_input(int_value) - error: Argument 1 to "accept_single_string_input" has incompatible type "Callable[[int], None]"; expected "Callable[[str], None]"
# accept_single_string_input(new_name) - error: Argument 1 to "accept_single_string_input" has incompatible type "Callable[[str], str]"; expected "Callable[[str], None]"

"""
INTERMEDIATE - class-var

TODO:

Class `ClassVarFoo` has a class variable `bar`, which is an integer.
"""


class ClassVarFoo:
    bar: ClassVar[int]


ClassVarFoo.bar = 1
# ClassVarFoo.bar = "1" - error: Incompatible types in assignment (expression has type "str", variable has type "int")
# ClassVarFoo().bar = 1 - error: Cannot assign to class variable "bar" via instance


"""
INTERMEDIATE - decorator

TODO:

Define a decorator that wraps a function and returns a function with the same signature.
"""

WrappedFunc = TypeVar("WrappedFunc", bound=Callable)


def decorator(func: WrappedFunc) -> WrappedFunc:
    return func


@decorator
def decorator_foo(a: int, *, b: str) -> None:
    pass


@decorator
def decorator_bar(c: int, d: str) -> None:
    pass


decorator_foo(1, b="2")
decorator_bar(c=1, d="2")

# decorator_foo(1, "2") - error: Too many positional arguments for "decorator_foo"
# decorator_foo(a=1, e="2") - error: Unexpected keyword argument "e" for "decorator_foo"
# decorator(1) - error: Value of type variable "WrappedFunc" of "decorator" cannot be "int"

"""
INTERMEDIATE - empty-tuple

TODO:

empty_tuple_foo should accept a empty tuple argument.
"""


def empty_tuple_foo(x: Tuple[()]):
    pass


empty_tuple_foo(())
# empty_tuple_foo((1)) - error: Argument 1 to "empty_tuple_foo" has incompatible type "int"; expected "tuple[()]"

"""
INTERMEDIATE - generic

TODO:

The function `generic_add` accepts two arguments and returns a value, they all have the same type.
"""

T1 = TypeVar("T1")


def generic_add(a: T1, b: T1) -> T1:  # type: ignore[empty-body]
    pass


assert_type(generic_add(1, 2), int)
assert_type(generic_add("1", "2"), str)
assert_type(generic_add(["1"], ["2"]), List[str])
# assert_type(generic_add(1, "2"), int) - error: Expression is of type "object", not "int"


"""
INTERMEDIATE - generic2

TODO:

The function `generic2_add` accepts two arguments and returns a value, they all have the same type.
The type can only be str or int.
"""

T2 = TypeVar("T2", int, str)


def generic2_add(a: T2, b: T2) -> T2:  # type: ignore[empty-body]
    pass


assert_type(generic2_add(1, 2), int)
assert_type(generic2_add("1", "2"), str)

# generic2_add(["1"], ["2"]) - error: Value of type variable "T2" of "add" cannot be "list[str]"
# generic2_add("1", 2) - error: Value of type variable "T2" of "add" cannot be "object"


"""
INTERMEDIATE - generic3

TODO:

The function `generic3_add` accepts one argument and returns a value, they all have the same type.
The type can only be int or subclasses of int.
"""

T3 = TypeVar("T3", bound=int)


def generic3_add(a: T3) -> T3:  # type: ignore[empty-body]
    pass


class MyInt(int):
    pass


assert_type(generic3_add(1), int)
assert_type(generic3_add(MyInt(1)), MyInt)
# assert_type(generic3_add("1"), str) - error: Value of type variable "T3" of "generic3_add" cannot be "str"
# generic3_add(["1"], ["2"]) - error: Value of type variable "T3" of "generic3_add" cannot be "list[str]" / Too many arguments for "generic3_add"
# generic3_add("1", 2) - erro: Value of type variable "T3" of "generic3_add" cannot be "str" / Too many arguments for "generic3_add"

"""
INTERMEDIATE - instance-var

TODO:

Class `InstanceVarFoo` has an instance variable `bar`, which is an integer.
"""


class InstanceVarFoo:
    bar: int


instance_var_foo = InstanceVarFoo()
instance_var_foo.bar = 1
# instance_var_foo.bar = "1" - error: Incompatible types in assignment (expression has type "str", variable has type "int")

"""
INTERMEDIATE - literal

TODO:

literal_foo only accepts literal 'left' and 'right' as its argument.
"""


def literal_foo(direction: Literal["left", "right"]):
    pass


literal_foo("left")
literal_foo("right")

b = "".join(["l", "e", "f", "t"])
# literal_foo(b) - error: Argument 1 to "literal_foo" has incompatible type "str"; expected "Literal['left', 'right']"


"""
INTERMEDIATE - literalstring

TODO:

You're writing a web backend.
Annotate a function `execute_query` which runs SQL, but also can prevent SQL injection attacks.

NOTE: You don't need to implement `execute_query`
"""


def execute_query(sql: LiteralString, parameters: Iterable[str] = ...):
    pass


# def query_user(user_id: str):
#     query = f"SELECT * FROM data WHERE user_id = {user_id}"
#     mypy ignored that case (https://github.com/python/mypy/issues/12554, https://github.com/python/mypy/issues/16169)
#     execute_query(sql=query) expect-type-error


def query_data(user_id: str, limit: bool) -> None:
    query = """
        SELECT
            user.name,
            user.age
        FROM data
        WHERE user_id = ?
    """

    if limit:
        query += " LIMIT 1"

    execute_query(query, (user_id,))


"""
INTERMEDIATE - self

TODO:

`return_self` should return an instance of the same type as the current enclosed class.
"""

FooSelf = TypeVar("FooSelf", bound="SelfFoo")


class SelfFoo:
    def return_self(self: FooSelf) -> FooSelf:  # type: ignore[empty-body]
        pass


class SubclassOfSelfFoo(SelfFoo):
    pass


f: SelfFoo = SelfFoo().return_self()
sf: SubclassOfSelfFoo = SubclassOfSelfFoo().return_self()
# sf: SubclassOfSelfFoo = SelfFoo().return_self() - error: Incompatible types in assignment (expression has type "SelfFoo", variable has type "SubclassOfSelfFoo")

"""
INTERMEDIATE - typed-dict

TODO:

Define a class `Student` that represents a dictionary with three keys:
- name, a string
- age, an integer
- school, a string
"""


class Student(TypedDict):
    name: str
    age: int
    school: str


student: Student = {"name": "Tom", "age": 15, "school": "Hogwarts"}
# student2: Student = {"name": 1, "age": 15, "school": "Hogwarts"}  - error: Incompatible types (expression has type "int", TypedDict item "name" has type "str")
# student3: Student = {(1,): "Tom", "age": 2, "school": "Hogwarts"} - error: Expected TypedDict key to be string litera
# student4: Student = {"name": "Tom", "age": "2", "school": "Hogwarts"} - error: Incompatible types (expression has type "str", TypedDict item "age" has type "int")
# student5: Student = {"name": "Tom", "age": 2} -  error: Missing key "school" for TypedDict "Student"
assert Student(name="Tom", age=15, school="Hogwarts") == dict(
    name="Tom", age=15, school="Hogwarts"
)

"""
INTERMEDIATE - typed-dict2

TODO:

Define a class `Student2` that represents a dictionary with three keys:
- name, a string
- age, an integer
- school, a string

Note: school can be optional
"""


class Student2(TypedDict):
    name: str
    age: int
    school: NotRequired[str]


student2_1: Student2 = {"name": "Tom", "age": 15}
student2_2: Student2 = {"name": "Tom", "age": 15, "school": "Hogwarts"}
# student2_3: Student2 = {"name": 1, "age": 15, "school": "Hogwarts"} - error: Incompatible types (expression has type "int", TypedDict item "name" has type "str")
# student2_4: Student2 = {(1,): "Tom", "age": 2, "school": "Hogwarts"} - error: Expected TypedDict key to be string literal
# student2_5: Student2 = {"name": "Tom", "age": "2", "school": "Hogwarts"} - error: Incompatible types (expression has type "str", TypedDict item "age" has type "int")
# student2_6: Student2 = {"z": "Tom", "age": 2}  # expect-type-error - error: Missing key "name" for TypedDict "Student2" / Extra key "z" for TypedDict "Student2"
assert Student2(name="Tom", age=15) == dict(name="Tom", age=15)
assert Student2(name="Tom", age=15, school="Hogwarts") == dict(
    name="Tom", age=15, school="Hogwarts"
)

"""
INTERMEDIATE - typed-dict3

TODO:

Define a class `Person` that represents a dictionary with five string keys:
    name, age, gender, address, email

The value of each key must be the specified type:
    name - str, age - int, gender - str, address - str, email - str

Note: Only `name` is required
"""


class Person(TypedDict, total=False):
    name: Required[str]
    age: int
    gender: str
    address: str
    email: str


person: Person = {
    "name": "Capy",
    "age": 1,
    "gender": "Male",
    "address": "earth",
    "email": "capy@bara.com",
}
person1: Person = {"name": "Capy"}
# person2: Person = {"age": 1, "gender": "Male", "address": "", "email": ""} - error: Missing key "name" for TypedDict "Person"


"""
INTERMEDIATE - unpack

TODO:

`unpack_foo` expects two keyword arguments - `name` of type `str`, and `age` of type `int`.
"""


class Person2(TypedDict):
    name: str
    age: int


def unpack_foo(**kwargs: Unpack[Person]):
    pass


person2_1: Person2 = {"name": "The Meaning of Life", "age": 1983}
unpack_foo(**person2_1)
# unpack_foo(**{"name": "Brian", "age": 30}) - error: Argument 1 to "unpack_foo" has incompatible type "**dict[str, object]"; expected "str" / Argument 1 to "unpack_foo" has incompatible type "**dict[str, object]"; expected "int"

# unpack_foo(**{"name": "Brian"}) - error: Argument 1 to "unpack_foo" has incompatible type "**dict[str, str]"; expected "int"
person2_2: dict[str, object] = {"name": "Brian", "age": 20}
# unpack_foo(**person2_2) - error: Argument 1 to "unpack_foo" has incompatible type "**dict[str, object]"; expected "str" / Argument 1 to "unpack_foo" has incompatible type "**dict[str, object]"; expected "int"
# unpack_foo(**{"name": "Brian", "age": "1979"}) - error: Argument 1 to "unpack_foo" has incompatible type "**dict[str, str]"; expected "int"
