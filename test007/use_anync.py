import asyncio

async def do_sth(x):
    print('等待中：{0}'.format(x))
    await asyncio.sleep(x)

# 判断是否为携程
print(asyncio.iscoroutinefunction(do_sth))

coroutine = do_sth(5)

loop = asyncio.get_event_loop()
# 注册任务
task = loop.create_task(coroutine)
print(task)
# 等待协程任务执行结束
loop.run_until_complete(task)
print(task)