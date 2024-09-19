import asyncio

# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay, id):
    print("Fetching data... id:", id)
    await asyncio.sleep(delay) # Simulate an I/O operation with a sleep
    print("Data fetched, id:", id)
    return {"data": "Some data", "id": id} # Return some data
    

# Define another coroutine that calls the first coroutine
# async def main():
#     task1 = fetch_data(2, 1)
#     task2 = fetch_data(2, 2)
#     result1 = await task1
#     print (f"Received result: {result1}")
#     result2 = await task2
#     print (f" Received result: {result2}")

# here it will not run task1 and task2 symountaneosly you need to create a task

async def main():
    task1=asyncio.create_task(fetch_data(3, 1))
    task2=asyncio.create_task(fetch_data(2, 2))
    task3=asyncio.create_task(fetch_data(1, 3))

    r1=await task1
    r2=await task2
    r3=await task3
    #--> this says that if cpu is idle do other tasks. Our goal is to not let cpu sit idle
    print(r1,r2,r3)

asyncio.run(main())