import asyncio
import time

async def get_data():
    await asyncio.sleep(1)
    return "Data"

async def main():
    data = await get_data()
    print(data)

async def refactored_use_effect():
    start_time = time.time()
    data = await get_data()
    print(data)
    print(f"Time taken: {time.time() - start_time} seconds")

asyncio.run(refactored_use_effect())
