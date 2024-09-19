#--> gather function is not good at error handling so you have to define error handling logic in you coroutine function. We will use more prefered function called taskgroup
import asyncio
import time

async def fetch_data(delay, id):
    print("Fetching data... id:", id)
    await asyncio.sleep(delay) # Simulate an I/O operation with a sleep
    print("Data fetched, id:", id)
    return {"data": "Some data", "id": id} # Return some data

async def main():
    start_t=time.time()
    tasks=[]

    async with asyncio.TaskGroup() as tg:
        for i, delay in enumerate([3,2,4,1], start=1):
            task=tg.create_task(fetch_data(delay,i))
            tasks.append(task)

    results=[task.result() for task in tasks]

    for result in results:
        print(result)
    end_t=time.time()
    print(f"Time take is {end_t-start_t} sec")
asyncio.run(main())