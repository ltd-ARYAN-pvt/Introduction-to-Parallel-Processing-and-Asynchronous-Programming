#--> Asyncio is not multithreading or multiprocessing it is a way to do task concurrently
import asyncio

#--> Creating a coroutine function

async def main():
    print("Coroutine function started")
    await asyncio.sleep(2)
    print("Coroutine function ended")

#-> 'async def' means that you are creating a func which is i/o bound and may paused and resumed later.

#main() #-->RuntimeWarning: coroutine 'main' was never awaited
#--> You can't run coroutine function like this.

asyncio.run(main())