import asyncio

from taskiq_broker.broker import broker


@broker.task()
async def simple_task_2():
    print('Simple task 2 is running')
    await asyncio.sleep(2)
    print('Simple task 2 is done')