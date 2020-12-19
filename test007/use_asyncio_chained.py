import asyncio

async def compute(x, y):
    print('计算x + y => {0} + {1}'.format(x, y))
    await asyncio.sleep(1)
    return x + y

async def get_sum(x, y):
    sum = await compute(x, y)
    print('x + y = {0}'.format(sum))

loop = asyncio.get_event_loop()
loop.run_until_complete(get_sum(1, 2))
loop.close()