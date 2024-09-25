# import random

# def generate_numbers_file(filename, num_numbers, min_value, max_value):
#     """Generates a file with random numbers."""
#     with open(filename, "w") as f:
#         for _ in range(num_numbers):
#             number = random.randint(min_value, max_value)
#             f.write(f"{number}\n")
#     print(f"File '{filename}' with {num_numbers} random numbers generated.")


import random

def generate_numbers(filename="numbers.txt", count=100000):
    with open(filename, 'w') as f:
        for _ in range(count):
            f.write(f"{random.randint(10**5, 10**8)}\n")
    print(f"{filename} generated with {count} random numbers.")

if __name__ == "__main__":
    generate_numbers()
