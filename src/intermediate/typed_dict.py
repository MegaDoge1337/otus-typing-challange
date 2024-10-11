"""
TODO:

Define a class `Student` that represents a dictionary with three keys:
- name, a string
- age, an integer
- school, a string
"""

from typing import TypedDict


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
