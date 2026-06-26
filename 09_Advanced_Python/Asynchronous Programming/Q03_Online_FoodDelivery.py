import asyncio
async def prepare_food():
    print("Preparing Food...")
    await asyncio.sleep(4)
    print("Food Ready!")
async def watch_tv():
    print("Watching TV...")
    await asyncio.sleep(2)
    print("TV Finished")
async def main():
    await asyncio.gather(prepare_food(), watch_tv())
asyncio.run(main())