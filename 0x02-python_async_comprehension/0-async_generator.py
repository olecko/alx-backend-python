#!/usr/bin/env python3
""" 
coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module.
"""

from random import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """Yields a random int 10 times"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random() * 10
