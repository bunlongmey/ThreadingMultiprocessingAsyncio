import multiprocessing_task
import threading_task
import async_task
import generate_numbers

def main():
    # Step 1: Generate numbers file
    print("Generating numbers.txt file...")
    generate_numbers.generate_numbers("numbers.txt", 10000)


    # Step 2: Read numbers from file
    with open("numbers.txt", "r") as f:
        numbers = [int(line.strip()) for line in f.readlines()]

    # Step 3: Run multiprocessing task to find primes
    print("Running multiprocessing task...")
    primes = multiprocessing_task.multiprocessing_task(numbers)
    print(f"Prime numbers found: {primes}")

    # Step 4: Run threading task to simulate I/O
    print("Running threading I/O tasks...")
    threading_task.run_io_tasks()

    # Step 5: Run async tasks
    print("Running async I/O tasks...")
    import asyncio
    asyncio.run(async_task.run_async_tasks())

if __name__ == "__main__":
    main()
