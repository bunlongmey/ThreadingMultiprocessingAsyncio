# import threading
# import time

# def simulate_io_task(file_name, duration):
#   pass

# def run_io_tasks():
#   pass

import threading
import requests

def download_chunk(url, start, end, chunk_num):
    response = requests.get(url)
    chunk_data = response.content.splitlines()[start:end]
    print(f"Downloaded chunk {chunk_num} with {len(chunk_data)} lines")
    return chunk_data

def threading_task(url):
    threads = []
    chunk_size = 25000  # Example chunk size
    for i in range(0, 100000, chunk_size):
        t = threading.Thread(target=download_chunk, args=(url, i, i + chunk_size, i//chunk_size + 1))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    url = "https://github.com/user/repo/raw/main/numbers.txt"  # Replace with actual URL
    threading_task(url)
