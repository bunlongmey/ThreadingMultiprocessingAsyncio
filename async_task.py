# import asyncio

# async def async_write_to_file(filename, data, duration):
#     pass

# async def run_async_tasks():
#     pass

import aiofiles
import asyncio

async def write_to_file(filename, data):
    async with aiofiles.open(filename, 'w') as f:
        for num in data:
            await f.write(f"{num}\n")
    print(f"{filename} written with {len(data)} prime numbers.")

async def async_write(prime_chunks):
    tasks = []
    for i, chunk in enumerate(prime_chunks):
        filename = f"primes_chunk_{i}.txt"
        tasks.append(write_to_file(filename, chunk))
    await asyncio.gather(*tasks)

async def run_async_tasks(primes):
    # Break the primes list into chunks and write them asynchronously
    prime_chunks = [primes[i:i + 10000] for i in range(0, len(primes), 10000)]
    await async_write(prime_chunks)

# If you want to test this script independently, use the following:
if __name__ == "__main__":
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  # Example primes for testing
    asyncio.run(run_async_tasks(prime_numbers))
