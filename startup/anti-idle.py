from asyncio import sleep

async def continuous_print():
    while True:
        print('I am awake!!')
        sleep(300)
    return False
await continuous_print()