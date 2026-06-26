import asyncio
async def user1():
    print("Processing User 1...")
    await asyncio.sleep(2)
    print("User 1 Completed")
async def user2():
    print("Processing User 2...")
    await asyncio.sleep(2)
    print("User 2 Completed")
async def main():
    await asyncio.gather(user1(), user2())
asyncio.run(main())