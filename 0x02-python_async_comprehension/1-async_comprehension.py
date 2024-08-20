#!/usr/bin/env python3
"""
Corutine to collect list of numbers
"""
import asyncio
from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension function for 10 random numbers
    Argumenets:
        no arguments
    Return:
        10 differnt numbers
    """
    return [i async for i in async_generator()]
