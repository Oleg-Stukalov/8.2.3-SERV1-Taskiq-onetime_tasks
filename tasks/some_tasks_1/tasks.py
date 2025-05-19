import asyncio

from taskiq_broker.broker import broker


@broker.task()
async def simple_task_1():
    print('Simple task 1 is running')
    await asyncio.sleep(2)
    print('Simple task 1 is done')