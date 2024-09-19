import asyncio

async def fetch_data(delay:int):
    print("Fetching data.....")
    await asyncio.sleep(delay) #--> Simulating some i/o bound functions
    print("Data Fetched")
    return {'data':delay}

async def main():
    print("Started main coroutine")
    task=fetch_data(3)
    result=await task
    print("Results is",result)
    print("Main coroutine ended")

asyncio.run(main())