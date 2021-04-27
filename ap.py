import asyncio
import time
import random

async def say(what, when):
    while (True):
        await asyncio.sleep(random.randint(1, when)/10)
        print(what)

loop = asyncio.get_event_loop()

loop.create_task(say('first hello', 2))
loop.create_task(say('second hello', 1))

loop.run_forever()
loop.close()
