import asyncio

# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay, id):
    print("Fetching data... id:", id)
    await asyncio.sleep(delay) # Simulate an I/O operation with a sleep
    print("Data fetched, id:", id)
    return {"data": "Some data", "id": id} # Return some data

async def main():
    results=await asyncio.gather(fetch_data(3, 1),fetch_data(1, 2),fetch_data(4, 3),fetch_data(2, 4))
    for r in results:
        print(r)

asyncio.run(main())

#--> gather function is not good at error handling so you have to define error handling logic in you coroutine function