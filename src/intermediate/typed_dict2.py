"""
TODO:

Define a class `Student` that represents a dictionary with three keys:
- name, a string
- age, an integer
- school, a string

Note: school can be optional
"""

from typing import NotRequired, TypedDict


class Student(TypedDict):
    name: str
    age: int
    school: NotRequired[str]


student: Student = {"name": "Tom", "age": 15}
student2: Student = {"name": "Tom", "age": 15, "school": "Hogwarts"}
# student3: Student = {"name": 1, "age": 15, "school": "Hogwarts"} - error: Incompatible types (expression has type "int", TypedDict item "name" has type "str")
# student4: Student = {(1,): "Tom", "age": 2, "school": "Hogwarts"} - error: Expected TypedDict key to be string literal
# student5: Student = {"name": "Tom", "age": "2", "school": "Hogwarts"} - error: Incompatible types (expression has type "str", TypedDict item "age" has type "int")
# student6: Student = {"z": "Tom", "age": 2}  # expect-type-error - error: Missing key "name" for TypedDict "Student" / Extra key "z" for TypedDict "Student"
assert Student(name="Tom", age=15) == dict(name="Tom", age=15)
assert Student(name="Tom", age=15, school="Hogwarts") == dict(
    name="Tom", age=15, school="Hogwarts"
)
