import asyncio
import logging

from taskiq_broker.broker import broker
from tasks.some_tasks_1.tasks import simple_task_1
from tasks.some_tasks_2.tasks import simple_task_2

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
           '%(lineno)d - %(name)s - %(message)s'
)

logger = logging.getLogger(__name__)


async def main():
    await broker.startup()

    logger.info("Sending task 1")
    await simple_task_1.kiq()

    logger.info("Sending task 2")
    await simple_task_2.kiq()

    await broker.shutdown()


if __name__ == "__main__":
    asyncio.run(main())