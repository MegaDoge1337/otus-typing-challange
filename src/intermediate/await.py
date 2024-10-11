"""
TODO:

`run_async` takes an awaitable integer.
"""

from asyncio import Queue
from typing import Awaitable


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
