#!/usr/bin/env python3
""" Async programmes and coroutines """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ await asyncio async programme coroutines """

    chill = random.random() * max_delay
    await asyncio.sleep(chill)
    return chill
