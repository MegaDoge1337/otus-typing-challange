"""

TODO:

foo should accept a dict argument, both keys and values are string.
"""

from typing import Dict


def foo(x: Dict[str, str]):
    pass


foo({"foo": "bar"})
# foo({"foo": 1}) - error: Dict entry 0 has incompatible type "str": "int"; expected "str": "str"
