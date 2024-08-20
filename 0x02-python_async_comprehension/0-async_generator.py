#!/usr/bin/env python3
"""
Coroutine with no arguments
"""
import asyncio
import random


async def async_generator():
    """
    async_generator function to loop 10 times
    Arguments:
        no arguments
    Returns:
        nothing
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
