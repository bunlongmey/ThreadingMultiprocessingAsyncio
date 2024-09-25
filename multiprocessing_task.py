# import multiprocessing

# def is_prime(n):
#   pass

# def check_prime_chunk(numbers):
#   pass

# def find_primes_in_range(numbers, chunk_size):
#   pass
import multiprocessing
import requests

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def process_chunk(numbers):
    return [num for num in numbers if is_prime(num)]

def download_file(url, filename="numbers.txt"):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

def multiprocessing_task(url):
    download_file(url)
    with open('numbers.txt', 'r') as f:
        data = list(map(int, f.readlines()))
    
    num_cores = multiprocessing.cpu_count()
    chunk_size = len(data) // num_cores
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    with multiprocessing.Pool(processes=num_cores) as pool:
        results = pool.map(process_chunk, chunks)

    primes = [num for sublist in results for num in sublist]
    print(f"Found {len(primes)} prime numbers.")
    return primes

if __name__ == "__main__":
    url = "https://github.com/user/repo/raw/main/numbers.txt"  # Replace with actual URL
    multiprocessing_task(url)
