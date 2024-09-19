import asyncio

async def access_resource (semaphore, resource_id):
    async with semaphore:
        # Simulate accessing a limited resource
        print (f" Accessing resource {resource_id}")
        await asyncio.sleep(1) # Simulate work with the resource
        print (f" Releasing resource {resource_id}")

async def main():
    semaphore = asyncio.Semaphore (2) # Allow 2 concurrent accesses
    await asyncio.gather (*(access_resource (semaphore, i) for i in range(5)))

asyncio.run(main())