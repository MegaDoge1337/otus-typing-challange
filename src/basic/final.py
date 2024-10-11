"""
TODO:

Make sure `my_list` cannot be re-assigned to.
"""

from typing import Final

my_list: Final = []
my_list.append(1)
# my_list = [] - error: Cannot assign to final name "my_list"
# my_list = "something" - error: Cannot assign to final name "my_list" / Incompatible types in assignment (expression has type "str", variable has type "list[int]")
